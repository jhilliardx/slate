# How Slate works

## The mechanism

Power Apps' `Image` property accepts a URL, a media resource, or a **data URI**.
Only the data URI can be produced by a formula, and that is the entire opening.

```powerapps
"data:image/svg+xml;utf8," & EncodeUrl(
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 24 24"" fill=""#1F3864""><path d=""M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z""/></svg>"
)
```

Everything after that is detail — but each of these details is the difference
between an icon and a blank box.

### `;utf8,` — exactly this

`data:image/svg+xml;utf8,` works. `data:image/svg+xml;charset=utf-8,` and a bare
`data:image/svg+xml,` do not, reliably. This is a Power Apps quirk, not an SVG or
RFC 2397 one, and it is the single most common reason a copied-from-the-internet
snippet renders nothing.

### The `xmlns` is mandatory

```
xmlns="http://www.w3.org/2000/svg"
```

Browsers will infer the SVG namespace from context in an `<img>`. The Power Apps
image host will not. Omit it and you get a blank box with no error anywhere.

### `EncodeUrl` is not optional

A hex colour contains `#`. In a URI, `#` starts the fragment — so
`fill="#1F3864"` silently truncates the URI at the `#` and the renderer receives
half an SVG. `EncodeUrl` percent-encodes it to `%23` along with the angle brackets,
quotes, and spaces.

### Six-digit hex only

`RGBAToHex(RGBA(31, 56, 100, 1))` returns `#1F3864FF` — eight digits plus alpha.
The Power Apps SVG renderer does not accept the eight-digit form and falls back to
black, which looks like "my theme binding isn't working" rather than a format
error. Always:

```powerapps
Left(RGBAToHex(SomeColor), 7)
```

Control opacity with the `Image` control's own properties, not the SVG alpha.

### `ImagePosition.Fit`

The generated SVG has a `viewBox` but no `width` or `height`, so it inherits the
size of its host. Set `ImagePosition: ImagePosition.Fit` and the same single
definition renders crisply at 16px and at 64px.

---

## Why a single `<path>`

Slate stores exactly one `d` string per icon, so the wrapper formula is a fixed
template with one variable. Most Material glyphs are already a single path; the
handful that mix a `<path>` with a `<circle>` or `<rect>` are merged at build
time, because all of them share one fill and the default nonzero fill rule.

There is a trap here worth knowing about if you ever do this by hand.

Material's optimised paths usually **open with a relative `m` moveto**:

```
m21.67 18.17-5.3-5.3h-.99...
```

On its own, an initial relative moveto is measured from the origin. Appended after
another subpath, it is measured from **that subpath's end point** — so the second
glyph silently slides across the canvas. Concatenating `d` strings is not safe by
default.

The fix is to reset the current point before each appended subpath:

```
M0 0m21.67 18.17-5.3-5.3h-.99...
```

`M0 0` opens a zero-length subpath at the origin, which contributes no fill, and
the relative moveto then lands exactly where it did standalone.

`tools/verify_slate.py` renders every generated icon and diffs it against the
upstream SVG pixel-for-pixel. That check is what caught this in the first place.

---

## Patterns

### One-off icon, no collection

For a single icon on a header or button, skip the table entirely:

```powerapps
"data:image/svg+xml;utf8," & EncodeUrl(
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 24 24"" fill=""#A4262C""><path d=""M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z""/></svg>"
)
```

### Theme-bound

```powerapps
Slate_Icon("settings", Left(RGBAToHex(AppTheme.Primary), 7))
```

or, without UDFs:

```powerapps
"data:image/svg+xml;utf8," & EncodeUrl(
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 24 24"" fill=""" &
    Left(RGBAToHex(AppTheme.Primary), 7) &
    """><path d=""" & LookUp(SlateIcons, Name = "settings").Path & """/></svg>"
)
```

### State-driven glyph and colour

Because the icon is an expression, both the shape and the colour can react:

```powerapps
Slate_Icon(
    Switch(ThisItem.Status,
        "Approved", "check_circle",
        "Rejected", "cancel",
        "pending"),
    Switch(ThisItem.Status,
        "Approved", RGBA(16, 124, 16, 1),
        "Rejected", RGBA(164, 38, 44, 1),
        RGBA(96, 94, 92, 1))
)
```

This is the part that media files cannot do. One glyph definition covers every
state and every colour, and there is no asset to keep in sync.

### Pressed / hover feedback on an icon button

```powerapps
Slate_Icon("save", If(Self.Pressed, RGBA(255,255,255,1), SlateDefaultColor))
```

### Without user-defined functions

The `Slate_*` functions need the **User-defined functions** toggle
(Settings → Updates → New), which some tenants — GCC and GCC High especially —
do not have yet. The `SlateIcons` **named formula** is generally available and
works on its own; use the inline `LookUp` form above. Everything Slate does is
possible without UDFs; they are ergonomics, not the mechanism.

---

## Performance notes

- **Put the table in `App.Formulas`, not `App.OnStart`.** Named formulas are lazy
  and cached: the icon table is not materialised until an icon is actually drawn,
  and never costs anything at app launch. A 150-row `ClearCollect` in `OnStart` is
  pure added startup latency on every session.
- **Named formulas are immutable**, so no screen can `Clear()` your icon set by
  accident.
- **The URI is rebuilt on each render.** That is cheap — string concatenation and
  a percent-encode — but if you have a gallery of thousands of rows, consider
  hoisting the constant part or precomputing URIs into a collection once.
- **Curate the set.** 150 icons is about 45 KB of formula text in the app
  document, which is negligible. Importing all 2,000+ Material icons would not be.
  Add what you use.

---

## Other styles

`build_slate.py --style` accepts `filled` (default), `outlined`, `round`, and
`sharp`. `two-tone` is rejected by the generator because it relies on `opacity`,
which cannot be collapsed into a single path without changing the render.
