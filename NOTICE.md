# Notices and attribution

## Material Design Icons

The icon artwork distributed with this project — the SVG path data in
`data/icons.*.json` and every file generated from it under `src/` and `docs/` —
is from the **Google Material Design Icons** project and is licensed under the
**Apache License, Version 2.0**.

- Upstream: https://github.com/google/material-design-icons
- Retrieved via the flat mirror: https://github.com/marella/material-design-icons
- Licence: https://www.apache.org/licenses/LICENSE-2.0

```
Copyright Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

The path data has been mechanically transformed — spacer paths removed, and
`<circle>` and `<rect>` elements converted to equivalent path subpaths — so that
each glyph is a single `d` string. The rendered result is verified to match the
upstream artwork pixel-for-pixel by `tools/verify_slate.py`.

## Slate

Everything else in this repository — the generator, the validator, the Power Fx,
the YAML structure, and the documentation — is licensed under the MIT License.
See `LICENSE`.

## Trademarks

Power Apps, Power Fx, and Power Platform are trademarks of Microsoft Corporation.
Material Design is a trademark of Google LLC. This project is an independent work
and is not affiliated with, endorsed by, or sponsored by either company.
