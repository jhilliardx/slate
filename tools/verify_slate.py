#!/usr/bin/env python3
"""
Slate — verify the generated artefacts before anyone pastes them.

Checks, in order:
  1. Both YAML dialects parse as YAML.
  2. Every Power Fx string literal in the emitted files is balanced.
  3. The SVG that the Power Fx will build is well-formed XML, for every icon.
  4. The data URI round-trips through EncodeUrl back to that same SVG.
  5. Every icon actually rasterises to non-empty artwork, and a contact sheet
     is written to docs/preview.png for eyeballing.
"""
import json
import os
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILL = "#1F3864"
fails = []


def check(label, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}{(' - ' + detail) if detail and not ok else ''}")
    if not ok:
        fails.append(label)


def svg_for(path, fill=FILL):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            f'fill="{fill}"><path d="{path}"/></svg>')


def encode_url(s):
    """Power Fx EncodeUrl: percent-encode everything outside A-Za-z0-9-_.~"""
    return urllib.parse.quote(s, safe="-_.~")


def main():
    icons = json.load(open(os.path.join(ROOT, "data", "icons.filled.json"),
                           encoding="utf-8"))["icons"]
    print(f"\n[1] YAML parses ({len(icons)} icons in set)")
    for rel in ("src/slate-icon-browser.pa.yaml", "src/slate-minimal.pa.yaml",
                "src/slate-icon-browser.clipboard.yaml",
                "src/slate-minimal.clipboard.yaml"):
        p = os.path.join(ROOT, rel)
        try:
            doc = yaml.safe_load(open(p, encoding="utf-8"))
            check(rel, doc is not None, "parsed to None")
        except Exception as exc:                              # noqa: BLE001
            check(rel, False, str(exc))

    print("\n[2] Power Fx string literals balanced")
    for rel in ("src/slate-icon-browser.pa.yaml", "src/slate-app-formulas.fx",
                "src/scrSlateIcons-onvisible.fx", "src/slate-minimal.pa.yaml"):
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        # Strip comments, then a literal is "..." with "" as the escape.
        body = re.sub(r"^\s*//.*$", "", text, flags=re.M)
        body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)
        body = re.sub(r"^\s*#.*$", "", body, flags=re.M)
        stripped = re.sub(r'""', "", body)
        check(f"{rel} ({stripped.count(chr(34))} quotes)",
              stripped.count('"') % 2 == 0, "odd number of quotes")

    print("\n[3] Generated SVG is well-formed XML")
    bad = [i["name"] for i in icons
           if not _xml_ok(svg_for(i["path"] if "path" in i else i["d"]))]
    check(f"{len(icons)} icons parse as XML", not bad, ", ".join(bad[:5]))

    print("\n[4] Data URI round-trips")
    rt = []
    for i in icons:
        raw = svg_for(i["d"])
        uri = "data:image/svg+xml;utf8," + encode_url(raw)
        if urllib.parse.unquote(uri.split(",", 1)[1]) != raw:
            rt.append(i["name"])
        if "#" in uri.split(",", 1)[1]:          # an unescaped # truncates the URI
            rt.append(i["name"] + " (bare #)")
    check(f"{len(icons)} URIs decode to the original SVG", not rt, ", ".join(rt[:5]))

    print("\n[5] Rasterises to real artwork")
    try:
        import cairosvg
    except ImportError:
        print("  SKIP  cairosvg not installed")
        return finish()

    from PIL import Image
    import io as _io
    blank = []
    for i in icons:
        png = cairosvg.svg2png(bytestring=svg_for(i["d"]).encode(), output_width=48,
                               output_height=48)
        im = Image.open(_io.BytesIO(png)).convert("RGBA")
        # count pixels that actually got painted
        painted = sum(c for v, c in enumerate(im.getchannel("A").histogram()) if v > 16)
        if painted < 20:
            blank.append(i["name"])
    check(f"{len(icons)} icons render non-empty", not blank, ", ".join(blank[:8]))

    print("\n[6] Merged path data matches the upstream artwork, pixel for pixel")
    drift = []
    for i in icons:
        if "src" not in i:
            continue
        a = _alpha(cairosvg, Image, _io, svg_for(i["d"]))
        b = _alpha(cairosvg, Image, _io, i["src"])
        diff = sum(1 for x, y in zip(a, b) if abs(x - y) > 40)
        if diff > len(a) * 0.005:          # >0.5% of pixels
            drift.append(f"{i['name']} ({diff}px)")
    check(f"{len(icons)} icons match their source SVG", not drift, ", ".join(drift[:8]))

    contact_sheet(icons)
    finish()


def _alpha(cairosvg, Image, _io, svg, size=96):
    """Alpha channel of a rendered SVG - shape only, ignoring fill colour."""
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=size,
                           output_height=size)
    return list(Image.open(_io.BytesIO(png)).convert("RGBA").getchannel("A").getdata())


def _xml_ok(s):
    try:
        ET.fromstring(s)
        return True
    except ET.ParseError:
        return False


def contact_sheet(icons, cols=15, cell=64):
    rows = (len(icons) + cols - 1) // cols
    w, h = cols * cell, rows * cell
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
             f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#ffffff"/>']
    for n, i in enumerate(icons):
        x, y = (n % cols) * cell, (n // cols) * cell
        s = (cell - 20) / 24
        parts.append(f'<g transform="translate({x + 10},{y + 10}) scale({s:.4f})" '
                     f'fill="{FILL}"><path d="{i["d"]}"/></g>')
    parts.append("</svg>")
    sheet = "".join(parts)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    open(os.path.join(ROOT, "docs", "preview.svg"), "w", encoding="utf-8").write(sheet)
    import cairosvg
    cairosvg.svg2png(bytestring=sheet.encode(),
                     write_to=os.path.join(ROOT, "docs", "preview.png"),
                     output_width=w * 2, output_height=h * 2)
    print(f"  wrote docs/preview.svg and docs/preview.png ({cols}x{rows} grid)")


def finish():
    print()
    if fails:
        print(f"{len(fails)} check(s) FAILED")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
