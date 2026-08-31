#!/usr/bin/env python3
"""
Slate — build Material Design icon path data into pastable Power Apps YAML.

Fetches the official Material Design Icons SVGs, reduces each one to a single
`d` path string, and emits:

    data/icons.<style>.json          machine-readable icon table
    src/slate-icon-browser.pa.yaml   full pastable screen (gallery browser)
    src/slate-minimal.pa.yaml        8-icon proof-of-concept screen
    src/slate-app-formulas.fx        App.Formulas named formulas + UDFs

Usage:
    python3 tools/build_slate.py                 # filled style, all defaults
    python3 tools/build_slate.py --style outlined
    python3 tools/build_slate.py --offline       # rebuild YAML from cached JSON
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = "https://raw.githubusercontent.com/marella/material-design-icons/main/svg/{style}/{name}.svg"
STYLES = ["filled", "outlined", "round", "sharp", "two-tone"]

# ---------------------------------------------------------------- fetch/parse

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "slate-build"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8")


ELEMENT = re.compile(r"<(path|circle|rect|ellipse|polygon|polyline|line|g)\b([^>]*)/?>")
ATTR = re.compile(r'(\w[\w-]*)="([^"]*)"')


def num(v):
    """Trim a float to the shortest form that still round-trips visually."""
    f = float(v)
    return f"{f:g}"


def circle_to_d(a):
    """<circle> as two half-arcs. Same fill and winding, so it can be merged
    into a sibling path's `d` without changing the render."""
    cx, cy, r = float(a["cx"]), float(a["cy"]), float(a["r"])
    return (f"M{num(cx - r)} {num(cy)}"
            f"a{num(r)} {num(r)} 0 1 0 {num(2 * r)} 0"
            f"a{num(r)} {num(r)} 0 1 0 {num(-2 * r)} 0z")


def rect_to_d(a):
    x, y = float(a.get("x", 0)), float(a.get("y", 0))
    w, h = float(a["width"]), float(a["height"])
    if float(a.get("rx", 0)) or float(a.get("ry", 0)):
        raise ValueError("rounded <rect> not supported")
    return f"M{num(x)} {num(y)}h{num(w)}v{num(h)}h{num(-w)}z"


def normalize_start(d, first):
    """Make a path safe to append after another as an extra subpath.

    Material's optimised paths usually open with a *relative* `m`. On its own
    that is measured from the origin, but appended after another subpath it is
    measured from that subpath's end point -- which silently shifts the whole
    glyph. Prefixing `M0 0` resets the current point to the origin, so the
    relative moveto lands exactly where it did standalone. The zero-length
    subpath at the origin adds no fill.
    """
    if first or not d[:1].islower():
        return d
    return "M0 0" + d


def svg_to_d(svg):
    """Reduce an SVG to a single `d` string, or raise if it cannot be.

    Material's filled set is almost entirely single-path, but a handful of
    glyphs (priority_high, policy, category) mix a <path> with a <circle> or
    <rect>. Those all share one fill and the default nonzero fill-rule, so the
    shapes merge losslessly into one `d` as separate subpaths -- which keeps
    the Power Fx template a single <path> element for every icon in the set.
    """
    parts = []
    for tag, attr_text in ELEMENT.findall(svg):
        a = dict(ATTR.findall(attr_text))
        if a.get("fill") == "none":
            continue                      # the 24x24 transparent spacer
        if "opacity" in attr_text:
            raise ValueError("uses opacity (two-tone style)")
        if tag == "path":
            parts.append(normalize_start(a["d"].strip(), first=not parts))
        elif tag == "circle":
            parts.append(circle_to_d(a))
        elif tag == "rect":
            parts.append(rect_to_d(a))
        elif tag == "g":
            continue                      # plain grouping, no transform
        else:
            raise ValueError(f"unsupported <{tag}> geometry")
    if not parts:
        raise ValueError("no drawable geometry")
    if "transform=" in svg:
        raise ValueError("uses a transform")
    return " ".join(parts)


def load_manifest(path):
    entries = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            name = parts[0]
            entries.append({
                "name": name,
                "cat": parts[1] if len(parts) > 1 else "Misc",
                "tags": parts[2] if len(parts) > 2 else "",
            })
    return entries


def build_icons(entries, style, workers=12):
    def one(e):
        try:
            raw = fetch(SOURCE.format(style=style, name=e["name"]))
            return dict(e, d=svg_to_d(raw), src=raw)
        except Exception as exc:              # noqa: BLE001 - report and skip
            print(f"  skip {e['name']}: {exc}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=workers) as pool:
        icons = [i for i in pool.map(one, entries) if i]
    icons.sort(key=lambda i: (i["cat"], i["name"]))
    return icons


# ------------------------------------------------------------------ Power Fx

def fx_str(s):
    """Power Fx string literal — double any embedded double quote."""
    return '"' + s.replace('"', '""') + '"'


def title(name):
    return name.replace("_", " ").title()


def icon_rows(icons, indent):
    pad = " " * indent
    rows = []
    for i in icons:
        rows.append(
            f'{pad}{{ Name: {fx_str(i["name"])}, '
            f'Title: {fx_str(title(i["name"]))}, '
            f'Cat: {fx_str(i["cat"])}, '
            f'Tags: {fx_str(i["tags"])}, '
            f'Path: {fx_str(i["d"])} }}'
        )
    return ",\n".join(rows)


# ------------------------------------------------------------ template fillers

def render(template_path, **subs):
    with open(template_path, encoding="utf-8") as fh:
        text = fh.read()
    for key, val in subs.items():
        text = text.replace("{{" + key + "}}", val)
    if "{{" in text:
        leftover = re.findall(r"\{\{(\w+)\}\}", text)
        raise SystemExit(f"unfilled placeholders in {template_path}: {leftover}")
    return text


# ------------------------------------------------------ clipboard dialect

# Power Apps Studio accepts two YAML shapes and which one your build takes
# depends on the release wave your tenant is on:
#
#   1. Source format  - a top-level `Screens:` map, controls named without a
#      version. This is what `pac canvas`/Dataverse Git integration writes and
#      what current Studio pastes when you paste a whole screen.
#   2. Clipboard format - a bare list of controls, each pinned to an exact
#      control version. This is what Studio *emits* when you copy a control,
#      and it is the shape older builds will accept.
#
# Rather than make the reader guess, we generate both from one template. The
# versions below are the ones Studio has emitted since the 2023 wave; if your
# tenant differs, copy any control of that type out of your own app and match
# the number.
CONTROL_VERSIONS = {
    "Screen": "Screen@1.0.0",
    "Rectangle": "Rectangle@2.3.0",
    "Label": "Label@2.5.1",
    "Image": "Image@2.2.3",
    "Gallery": "Gallery@2.15.0",
    "GroupContainer": "GroupContainer@1.3.0",
    "HtmlViewer": "HtmlViewer@2.1.0",
    "Classic/TextInput": "Classic/TextInput@2.3.2",
    "Classic/DropDown": "Classic/DropDown@2.3.1",
    "Classic/Button": "Classic/Button@2.2.0",
    "Classic/ComboBox": "Classic/ComboBox@2.4.0",
}

CLIPBOARD_HEADER = """\
# ---------------------------------------------------------------------------
# {title}
# CLIPBOARD DIALECT - a flat list of controls, pinned to explicit control
# versions. Use this if Studio refuses the `Screens:` form.
#
#   1. Add a blank screen and rename it to {screen}.
#   2. Select the canvas and paste this file.
#   3. Open that screen's OnVisible and paste {onvisible} .
#
# If a paste fails with an unrecognised control, it is almost always the
# @version: copy the same control type out of your own app and match it.
# ---------------------------------------------------------------------------
"""


def dedent_block(lines, amount):
    out = []
    for ln in lines:
        if not ln.strip():
            out.append("")
        else:
            if ln[:amount].strip():
                raise ValueError(f"cannot dedent {amount} from: {ln!r}")
            out.append(ln[amount:])
    return out


def split_screen_yaml(text):
    """Return (screen_name, onvisible_fx, children_lines) from source format."""
    lines = text.split("\n")
    name = None
    for ln in lines:
        m = re.match(r"^  (\w[\w\d_]*):\s*$", ln)
        if m:
            name = m.group(1)
            break
    if not name:
        raise SystemExit("could not find screen name in template output")

    # OnVisible block: `      OnVisible: |` then everything indented deeper.
    onvis, children = [], []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "OnVisible: |":
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" " * 8)):
                onvis.append(lines[i])
                i += 1
            continue
        if lines[i].rstrip() == "    Children:":
            i += 1
            children = lines[i:]
            break
        i += 1

    while onvis and not onvis[-1].strip():
        onvis.pop()
    while children and not children[-1].strip():
        children.pop()

    return name, "\n".join(dedent_block(onvis, 8)), dedent_block(children, 6)


def to_clipboard(text, title):
    name, onvis, children = split_screen_yaml(text)

    def version(m):
        ctrl = m.group(2).strip()
        if ctrl not in CONTROL_VERSIONS:
            raise SystemExit(f"no pinned version for control type {ctrl!r}")
        return f"{m.group(1)}Control: {CONTROL_VERSIONS[ctrl]}"

    body = re.sub(r"^(\s*)Control:\s*([\w/]+)\s*$", version,
                  "\n".join(children), flags=re.M)
    header = CLIPBOARD_HEADER.format(
        title=title, screen=name,
        onvisible=f"src/{name}-onvisible.fx")
    return name, header + body + "\n", "=" + onvis.lstrip("=") + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default="filled", choices=STYLES)
    ap.add_argument("--manifest", default=os.path.join(ROOT, "tools", "icons.txt"))
    ap.add_argument("--offline", action="store_true",
                    help="skip download, rebuild from data/icons.<style>.json")
    args = ap.parse_args()

    data_file = os.path.join(ROOT, "data", f"icons.{args.style}.json")

    if args.offline:
        with open(data_file, encoding="utf-8") as fh:
            icons = json.load(fh)["icons"]
        print(f"loaded {len(icons)} icons from cache")
    else:
        entries = load_manifest(args.manifest)
        print(f"fetching {len(entries)} '{args.style}' icons ...")
        icons = build_icons(entries, args.style)
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        with open(data_file, "w", encoding="utf-8") as fh:
            json.dump({
                "style": args.style,
                "source": SOURCE.format(style=args.style, name="<name>"),
                "license": "Apache-2.0 (Google Material Design Icons)",
                "count": len(icons),
                "icons": icons,
            }, fh, indent=2)
        print(f"wrote {data_file} ({len(icons)} icons)")

    tpl = os.path.join(ROOT, "tools", "templates")
    cats = sorted({i["cat"] for i in icons})
    out = {
        "src/slate-icon-browser.pa.yaml": render(
            os.path.join(tpl, "icon-browser.pa.yaml.tpl"),
            ICON_ROWS=icon_rows(icons, 12),
            COUNT=str(len(icons)),
            STYLE=args.style,
            CATEGORIES=", ".join(fx_str(c) for c in cats),
        ),
        "src/slate-minimal.pa.yaml": render(
            os.path.join(tpl, "minimal.pa.yaml.tpl"),
            ICON_ROWS=icon_rows(
                [i for i in icons if i["name"] in (
                    "home", "search", "person", "settings", "description",
                    "check_circle", "warning", "shield")], 12),
        ),
        "src/slate-app-formulas.fx": render(
            os.path.join(tpl, "app-formulas.fx.tpl"),
            ICON_ROWS=icon_rows(icons, 8),
            COUNT=str(len(icons)),
            STYLE=args.style,
        ),
    }
    for rel, title in (("src/slate-icon-browser.pa.yaml", "Slate icon browser"),
                       ("src/slate-minimal.pa.yaml", "Slate minimal proof of concept")):
        screen, clip, onvis = to_clipboard(out[rel], title)
        out[rel.replace(".pa.yaml", ".clipboard.yaml")] = clip
        out[f"src/{screen}-onvisible.fx"] = onvis

    for rel, text in out.items():
        dest = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {rel} ({len(text):,} bytes)")


if __name__ == "__main__":
    main()
