# GCC, GCC High, and DoD notes

Slate was built for sovereign-cloud tenants first. The design constraint that
shapes it: **assume no outbound internet at runtime, and assume you cannot get a
CDN allowlisted.**

## Why the usual icon approaches fail here

**External stylesheets and icon CDNs.** Anything that reaches
`fonts.googleapis.com`, `cdnjs`, `jsDelivr`, or an unpkg-style host is either
blocked by tenant DLP policy or simply unreachable from GCC High and DoD. Even
where it resolves today, it is a runtime dependency on the public internet inside
an accredited boundary, which is a finding waiting to happen.

**Media resources.** These work, but they are per-app assets. Every fork,
every copy for a new agency component, every solution re-import re-uploads them.
One colour per file means a status icon needs three uploads. And they inflate the
`.msapp`.

**Third-party icon components.** AppSource and PCF components carry procurement,
ATO, and tenant-approval overhead that is rarely worth it for icons.

## What Slate does instead

Path data is plain text stored in the app document. The `Image` property builds a
`data:` URI at render time. There is **no network call of any kind** — nothing to
allowlist, nothing to accredit, nothing to break when a boundary policy tightens.

The app behaves identically air-gapped as it does connected.

## Feature availability

GCC, GCC High, and DoD trail Commercial on Power Platform feature rollout, so
check these before you commit to a pattern:

| Feature | Slate's dependence |
| --- | --- |
| **Named formulas** (`App.Formulas`) | Recommended. Generally available and present on sovereign clouds. |
| **User-defined functions** (`Slate_Icon()`) | **Optional.** Preview-gated under Settings → Updates → New; often absent on GCC High. Every pattern has a non-UDF form — see `HOW-IT-WORKS.md`. |
| **Modern (Fluent) controls** | **Not used.** Slate's screens use classic controls only (`Classic/TextInput`, `Classic/DropDown`) precisely because modern control availability varies by cloud. |
| **YAML paste in Studio** | Required to paste the screens. If your build predates it, `data/icons.filled.json` and `src/slate-app-formulas.fx` still give you everything; build the screen by hand. |

## Control versions

The clipboard-dialect files pin control versions (`Control: Label@2.5.1`).
Sovereign clouds run behind Commercial on release waves, so your versions may
differ. If a paste fails on an unrecognised control:

1. In your own app, add a control of that type.
2. Copy it (<kbd>Ctrl</kbd>+<kbd>C</kbd>) and paste into a text editor.
3. Read the `@version` Studio emitted.
4. Update `CONTROL_VERSIONS` in `tools/build_slate.py` and regenerate, or just
   edit the YAML.

This is the single most likely paste failure, and it is a one-line fix.

## Solution and ALM behaviour

Because the icons are formula text rather than binary assets:

- They export and import with the solution with no media-resource fixups.
- They diff cleanly in source control (`pac canvas` / Dataverse Git integration).
- There are no broken media references after a copy or an environment migration.
- Nothing changes between DEV, TEST, and PROD — no per-environment asset URLs.

## Air-gapped build

`build_slate.py` needs internet only to fetch icons. Once `data/icons.filled.json`
exists, regenerate all Power Apps artefacts with no network at all:

```bash
python3 tools/build_slate.py --offline
```

Commit `data/icons.filled.json` and a disconnected environment can rebuild
everything from it.
