# The complete Power Apps spinner collection

Every set in one document: 63 loading spinners as Power Fx formulas for the Image control, including the determinate percent guidance and per set practice notes. Shared setup: paste a formula into an Image control's `Image` property, set `ImagePosition` to `ImagePosition.Fit`, keep the control square (the linear, shimmer, and typographic ones also suit wide controls), bind `Visible` to your loading flag, and swap `c` for your theme accent as a hex string (for example `varTheme.Accent`).

# The core seven

Each spinner is a self-contained animated SVG delivered through the Image control. Paste a formula into an Image control's `Image` property. No PCF, no timers, no media files.

### Setup
- Add an Image control, set `Image` to one of the formulas below.
- Set `ImagePosition` to `ImagePosition.Fit` and make the control square (for example 48 x 48 or 96 x 96). The SVG scales cleanly to any size.
- Leave the control's fill transparent so the spinner sits on whatever surface is behind it.
- To bind to your theme, swap the `c` value for your theme accent, for example `{c: varTheme.Accent}`. The color must be a hex string such as `"#005EA2"`.
- Drive `Visible` with your loading flag, for example `Visible: varIsLoading`. The animation restarts each time the control becomes visible.
- All animations are SMIL (`animate` and `animateTransform`), which the Image control renders in the browser, Windows, and mobile players.

### Orbit

Three moons on three rings, each at its own speed and direction. Reads as work happening at several layers.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='40' fill='none' stroke='" & c & "' stroke-opacity='0.12'/>" &
        "<circle cx='50' cy='50' r='27' fill='none' stroke='" & c & "' stroke-opacity='0.12'/>" &
        "<circle cx='50' cy='50' r='14' fill='none' stroke='" & c & "' stroke-opacity='0.12'/>" &
        "<circle cx='50' cy='50' r='5' fill='" & c & "'/>" &
        "<g><circle cx='50' cy='36' r='3.5' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='1.1s' repeatCount='indefinite'/></g>" &
        "<g><circle cx='50' cy='23' r='3' fill='" & c & "' opacity='0.7'/><animateTransform attributeName='transform' type='rotate' from='120 50 50' to='-240 50 50' dur='1.9s' repeatCount='indefinite'/></g>" &
        "<g><circle cx='50' cy='10' r='2.5' fill='" & c & "' opacity='0.45'/><animateTransform attributeName='transform' type='rotate' from='240 50 50' to='600 50 50' dur='3.1s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Halo

A gradient arc that grows and shrinks while it spins. The closest to a native indeterminate ring, with more life in it.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><linearGradient id='haloGrad' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='" & c & "'/><stop offset='1' stop-color='" & c & "' stop-opacity='0.15'/></linearGradient></defs>" &
        "<circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-opacity='0.1' stroke-width='6'/>" &
        "<g><circle cx='50' cy='50' r='38' fill='none' stroke='url(#haloGrad)' stroke-width='6' stroke-linecap='round' stroke-dasharray='60 179'><animate attributeName='stroke-dasharray' values='24 215;150 89;24 215' dur='1.6s' repeatCount='indefinite'/></circle><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='1.1s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Matrix

Nine tiles lit by a diagonal wave. Calm and square, suits dense data screens and grid-heavy apps.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<rect x='13' y='13' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0s' repeatCount='indefinite'/></rect>" &
        "<rect x='40' y='13' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.175s' repeatCount='indefinite'/></rect>" &
        "<rect x='67' y='13' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.35s' repeatCount='indefinite'/></rect>" &
        "<rect x='13' y='40' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.175s' repeatCount='indefinite'/></rect>" &
        "<rect x='40' y='40' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.35s' repeatCount='indefinite'/></rect>" &
        "<rect x='67' y='40' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.525s' repeatCount='indefinite'/></rect>" &
        "<rect x='13' y='67' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.35s' repeatCount='indefinite'/></rect>" &
        "<rect x='40' y='67' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.525s' repeatCount='indefinite'/></rect>" &
        "<rect x='67' y='67' width='20' height='20' rx='4' fill='" & c & "'><animate attributeName='opacity' values='0.15;1;0.15' dur='1.4s' begin='-0.7s' repeatCount='indefinite'/></rect>" &
        "</svg>"
    )
)
```

### Pulse

Five bars breathing from their centers with staggered timing. Good for anything that feels like processing or syncing.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<rect x='18' y='35' width='8' height='30' rx='4' fill='" & c & "'><animate attributeName='y' values='38;20;38' dur='1s' begin='-0s' repeatCount='indefinite'/><animate attributeName='height' values='24;60;24' dur='1s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;1;0.5' dur='1s' begin='-0s' repeatCount='indefinite'/></rect>" &
        "<rect x='32' y='35' width='8' height='30' rx='4' fill='" & c & "'><animate attributeName='y' values='38;20;38' dur='1s' begin='-0.12s' repeatCount='indefinite'/><animate attributeName='height' values='24;60;24' dur='1s' begin='-0.12s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;1;0.5' dur='1s' begin='-0.12s' repeatCount='indefinite'/></rect>" &
        "<rect x='46' y='35' width='8' height='30' rx='4' fill='" & c & "'><animate attributeName='y' values='38;20;38' dur='1s' begin='-0.24s' repeatCount='indefinite'/><animate attributeName='height' values='24;60;24' dur='1s' begin='-0.24s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;1;0.5' dur='1s' begin='-0.24s' repeatCount='indefinite'/></rect>" &
        "<rect x='60' y='35' width='8' height='30' rx='4' fill='" & c & "'><animate attributeName='y' values='38;20;38' dur='1s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='height' values='24;60;24' dur='1s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;1;0.5' dur='1s' begin='-0.36s' repeatCount='indefinite'/></rect>" &
        "<rect x='74' y='35' width='8' height='30' rx='4' fill='" & c & "'><animate attributeName='y' values='38;20;38' dur='1s' begin='-0.48s' repeatCount='indefinite'/><animate attributeName='height' values='24;60;24' dur='1s' begin='-0.48s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;1;0.5' dur='1s' begin='-0.48s' repeatCount='indefinite'/></rect>" &
        "</svg>"
    )
)
```

### Gyro

Two counter-rotating arc pairs around a pulsing core. Mechanical and precise, feels like instruments.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g><circle cx='50' cy='50' r='40' fill='none' stroke='" & c & "' stroke-width='5' stroke-linecap='round' stroke-dasharray='50 75.65 50 75.65'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='1.4s' repeatCount='indefinite'/></g>" &
        "<g><circle cx='50' cy='50' r='27' fill='none' stroke='" & c & "' stroke-opacity='0.6' stroke-width='5' stroke-linecap='round' stroke-dasharray='35 49.8 35 49.8'/><animateTransform attributeName='transform' type='rotate' from='360 50 50' to='0 50 50' dur='1s' repeatCount='indefinite'/></g>" &
        "<circle cx='50' cy='50' r='5' fill='" & c & "'><animate attributeName='r' values='4;7;4' dur='1s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Lattice

A runner traces a hexagon while a smaller one turns slowly inside. Distinctive without being loud.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M88 50 L69 82.9 L31 82.9 L12 50 L31 17.1 L69 17.1 Z' fill='none' stroke='" & c & "' stroke-opacity='0.12' stroke-width='3' stroke-linejoin='round'/>" &
        "<path d='M88 50 L69 82.9 L31 82.9 L12 50 L31 17.1 L69 17.1 Z' fill='none' stroke='" & c & "' stroke-width='3' stroke-linecap='round' stroke-linejoin='round' stroke-dasharray='60 168'><animate attributeName='stroke-dashoffset' values='0;-228' dur='1.6s' repeatCount='indefinite'/></path>" &
        "<g><path d='M69 50 L59.5 66.5 L40.5 66.5 L31 50 L40.5 33.5 L59.5 33.5 Z' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-opacity='0.5' stroke-width='2' stroke-linejoin='round'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='6s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Sonar

Rings expand and fade from a steady center. Quiet, patient, works well for searches and long waits.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='6' fill='none' stroke='" & c & "'><animate attributeName='r' values='6;44' dur='2.1s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.9;0' dur='2.1s' begin='-0s' repeatCount='indefinite'/><animate attributeName='stroke-width' values='4;1' dur='2.1s' begin='-0s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='6' fill='none' stroke='" & c & "'><animate attributeName='r' values='6;44' dur='2.1s' begin='-0.7s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.9;0' dur='2.1s' begin='-0.7s' repeatCount='indefinite'/><animate attributeName='stroke-width' values='4;1' dur='2.1s' begin='-0.7s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='6' fill='none' stroke='" & c & "'><animate attributeName='r' values='6;44' dur='2.1s' begin='-1.4s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.9;0' dur='2.1s' begin='-1.4s' repeatCount='indefinite'/><animate attributeName='stroke-width' values='4;1' dur='2.1s' begin='-1.4s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='6' fill='" & c & "'><animate attributeName='r' values='5;7;5' dur='2.1s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Notes

- The SVG uses single quotes throughout so the Power Fx string never needs a doubled quote.
- `EncodeUrl` handles the `#` in the hex color and the `<` `>` in the markup, which is what makes the data URI safe.
- Sizes, durations, and opacities are plain attributes in the strings, so you can tune speed by editing `dur` values without touching anything else.
- If you want a two-tone spinner, add a second name to the `With` record (for example `{c: "#005EA2", d: "#FFBE2E"}`) and reference `d` on the elements you want to recolor.


# Five more

Second set, same delivery as the first: each spinner is one animated SVG string for an Image control's `Image` property. Set `ImagePosition` to `ImagePosition.Fit`, keep the control square, drive `Visible` with your loading flag, and swap `c` for your theme accent (a hex string such as `"#005EA2"` or `varTheme.Accent`).

### Helix

Two strands of dots weave a rotating double helix. Depth comes from size and opacity trading places as each dot crosses.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='20' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0s' repeatCount='indefinite'/></circle>" &
        "<circle cx='30' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/></circle>" &
        "<circle cx='40' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/></circle>" &
        "<circle cx='60' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/></circle>" &
        "<circle cx='70' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/></circle>" &
        "<circle cx='80' cy='32' r='3.6' fill='" & c & "'><animate attributeName='cy' values='32;68;32' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/><animate attributeName='r' values='3.6;2.2;3.6' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.35;1' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/></circle>" &
        "<circle cx='20' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0s' repeatCount='indefinite'/></circle>" &
        "<circle cx='30' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.18s' repeatCount='indefinite'/></circle>" &
        "<circle cx='40' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.36s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.54s' repeatCount='indefinite'/></circle>" &
        "<circle cx='60' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.72s' repeatCount='indefinite'/></circle>" &
        "<circle cx='70' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.9s' repeatCount='indefinite'/></circle>" &
        "<circle cx='80' cy='68' r='2.2' fill='" & c & "'><animate attributeName='cy' values='68;32;68' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/><animate attributeName='r' values='2.2;3.6;2.2' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-1.08s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Loop

A comet with a fading tail rides an infinity path. The figure eight makes the wait feel continuous instead of circular.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M50 50 C62 30 88 30 88 50 C88 70 62 70 50 50 C38 30 12 30 12 50 C12 70 38 70 50 50 Z' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='3'/>" &
        "<circle r='4.2' fill='" & c & "'><animateMotion dur='2.2s' repeatCount='indefinite' path='M50 50 C62 30 88 30 88 50 C88 70 62 70 50 50 C38 30 12 30 12 50 C12 70 38 70 50 50 Z'/></circle>" &
        "<circle r='3' fill='" & c & "' opacity='0.55'><animateMotion dur='2.2s' begin='-2.08s' repeatCount='indefinite' path='M50 50 C62 30 88 30 88 50 C88 70 62 70 50 50 C38 30 12 30 12 50 C12 70 38 70 50 50 Z'/></circle>" &
        "<circle r='2' fill='" & c & "' opacity='0.3'><animateMotion dur='2.2s' begin='-1.96s' repeatCount='indefinite' path='M50 50 C62 30 88 30 88 50 C88 70 62 70 50 50 C38 30 12 30 12 50 C12 70 38 70 50 50 Z'/></circle>" &
        "</svg>"
    )
)
```

### Cradle

A Newton's cradle with eased swings and a proper handoff. The three middle balls hold still while momentum passes through.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='16' y1='18' x2='84' y2='18' stroke='" & c & "' stroke-width='3' stroke-linecap='round'/>" &
        "<g><line x1='28' y1='18' x2='28' y2='56' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/><circle cx='28' cy='62' r='5.5' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='26 28 18;0 28 18;0 28 18;0 28 18;26 28 18' keyTimes='0;0.25;0.5;0.75;1' calcMode='spline' keySplines='.55 0 .9 .6;.5 0 .5 1;.5 0 .5 1;.1 .4 .45 1' dur='1.6s' repeatCount='indefinite'/></g>" &
        "<line x1='39' y1='18' x2='39' y2='56' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/><circle cx='39' cy='62' r='5.5' fill='" & c & "'/>" &
        "<line x1='50' y1='18' x2='50' y2='56' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/><circle cx='50' cy='62' r='5.5' fill='" & c & "'/>" &
        "<line x1='61' y1='18' x2='61' y2='56' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/><circle cx='61' cy='62' r='5.5' fill='" & c & "'/>" &
        "<g><line x1='72' y1='18' x2='72' y2='56' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/><circle cx='72' cy='62' r='5.5' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 72 18;0 72 18;-26 72 18;0 72 18;0 72 18' keyTimes='0;0.25;0.5;0.75;1' calcMode='spline' keySplines='.5 0 .5 1;.1 .4 .45 1;.55 0 .9 .6;.5 0 .5 1' dur='1.6s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Sweep

A radar needle circles the scope and two contacts flash exactly as it passes them. The sync sells it.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='40' fill='none' stroke='" & c & "' stroke-opacity='0.18' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='27' fill='none' stroke='" & c & "' stroke-opacity='0.12'/>" &
        "<circle cx='50' cy='50' r='14' fill='none' stroke='" & c & "' stroke-opacity='0.12'/>" &
        "<line x1='10' y1='50' x2='90' y2='50' stroke='" & c & "' stroke-opacity='0.08'/>" &
        "<line x1='50' y1='10' x2='50' y2='90' stroke='" & c & "' stroke-opacity='0.08'/>" &
        "<g><path d='M50 50 L24.3 19.4 A40 40 0 0 1 50 10 Z' fill='" & c & "' fill-opacity='0.12'/><path d='M50 50 L39.65 11.4 A40 40 0 0 1 50 10 Z' fill='" & c & "' fill-opacity='0.22'/><line x1='50' y1='50' x2='50' y2='10' stroke='" & c & "' stroke-width='2.5' stroke-linecap='round'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='2s' repeatCount='indefinite'/></g>" &
        "<circle cx='50' cy='50' r='3' fill='" & c & "'/>" &
        "<circle cx='79.4' cy='67' r='3' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;1;1;0' keyTimes='0;0.03;0.2;0.6' dur='2s' begin='0.667s' repeatCount='indefinite'/></circle>" &
        "<circle cx='20.5' cy='55.2' r='3' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;1;1;0' keyTimes='0;0.03;0.2;0.6' dur='2s' begin='1.444s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Shapeshift

One solid form melts from circle to square to diamond and back while a ghost outline follows a beat behind.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path fill='none' stroke='" & c & "' stroke-opacity='0.25' stroke-width='2' d='M50 8 C73 8 92 27 92 50 C92 73 73 92 50 92 C27 92 8 73 8 50 C8 27 27 8 50 8 Z'><animate attributeName='d' values='M50 8 C73 8 92 27 92 50 C92 73 73 92 50 92 C27 92 8 73 8 50 C8 27 27 8 50 8 Z;M14 14 C38 14 62 14 86 14 C86 38 86 62 86 86 C62 86 38 86 14 86 C14 62 14 38 14 14 Z;M14 14 C38 14 62 14 86 14 C86 38 86 62 86 86 C62 86 38 86 14 86 C14 62 14 38 14 14 Z;M50 6 C64.7 21.3 79.3 35.3 94 50 C79.3 64.7 64.7 79.3 50 94 C35.3 79.3 20.7 64.7 6 50 C20.7 35.3 35.3 21.3 50 6 Z;M50 6 C64.7 21.3 79.3 35.3 94 50 C79.3 64.7 64.7 79.3 50 94 C35.3 79.3 20.7 64.7 6 50 C20.7 35.3 35.3 21.3 50 6 Z;M50 8 C73 8 92 27 92 50 C92 73 73 92 50 92 C27 92 8 73 8 50 C8 27 27 8 50 8 Z;M50 8 C73 8 92 27 92 50 C92 73 73 92 50 92 C27 92 8 73 8 50 C8 27 27 8 50 8 Z' keyTimes='0;0.15;0.33;0.48;0.66;0.81;1' calcMode='spline' keySplines='.6 0 .2 1;.5 0 .5 1;.6 0 .2 1;.5 0 .5 1;.6 0 .2 1;.5 0 .5 1' dur='3.2s' begin='-0.25s' repeatCount='indefinite'/></path>" &
        "<path fill='" & c & "' d='M50 15 C69.3 15 85 30.7 85 50 C85 69.3 69.3 85 50 85 C30.7 85 15 69.3 15 50 C15 30.7 30.7 15 50 15 Z'><animate attributeName='d' values='M50 15 C69.3 15 85 30.7 85 50 C85 69.3 69.3 85 50 85 C30.7 85 15 69.3 15 50 C15 30.7 30.7 15 50 15 Z;M20 20 C40 20 60 20 80 20 C80 40 80 60 80 80 C60 80 40 80 20 80 C20 60 20 40 20 20 Z;M20 20 C40 20 60 20 80 20 C80 40 80 60 80 80 C60 80 40 80 20 80 C20 60 20 40 20 20 Z;M50 12 C62.7 25.3 75.3 37.3 88 50 C75.3 62.7 62.7 75.3 50 88 C37.3 75.3 24.7 62.7 12 50 C24.7 37.3 37.3 25.3 50 12 Z;M50 12 C62.7 25.3 75.3 37.3 88 50 C75.3 62.7 62.7 75.3 50 88 C37.3 75.3 24.7 62.7 12 50 C24.7 37.3 37.3 25.3 50 12 Z;M50 15 C69.3 15 85 30.7 85 50 C85 69.3 69.3 85 50 85 C30.7 85 15 69.3 15 50 C15 30.7 30.7 15 50 15 Z;M50 15 C69.3 15 85 30.7 85 50 C85 69.3 69.3 85 50 85 C30.7 85 15 69.3 15 50 C15 30.7 30.7 15 50 15 Z' keyTimes='0;0.15;0.33;0.48;0.66;0.81;1' calcMode='spline' keySplines='.6 0 .2 1;.5 0 .5 1;.6 0 .2 1;.5 0 .5 1;.6 0 .2 1;.5 0 .5 1' dur='3.2s' repeatCount='indefinite'/></path>" &
        "</svg>"
    )
)
```

### Notes

- Loop uses `animateMotion`, and Cradle and Shapeshift use `calcMode='spline'` easing. Both are SMIL features the Image control renders in the browser, Windows, and mobile players.
- Cradle's two swing animations share one 1.6s clock with a handoff at the halfway point, so the loop is seamless.
- Sweep's contact dots use `begin` offsets of 0.667s and 1.444s against the 2s needle rotation, which is what keeps the flashes under the needle. If you change the rotation `dur`, scale those offsets by the same factor.
- Shapeshift morphs between three paths built from the same four cubic segments, which is the requirement for the `d` attribute to animate.


# Replicas and the percent ring

Three originals built after the referenced designs (the SteelKiwi dots loader, the 3D orbit preloader, and the gooey loader), plus a determinate ring that shows a real percentage. Same delivery as before: paste into an Image control's `Image` property, `ImagePosition.Fit`, square control.

### Cascade

After the DotsLoaderView pattern: dots sweep across a baseline, swelling mid flight, while a dash chases them along the line.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='10' y1='70' x2='90' y2='70' stroke='" & c & "' stroke-opacity='0.15' stroke-width='2'/>" &
        "<line x1='10' y1='70' x2='90' y2='70' stroke='" & c & "' stroke-width='2.5' stroke-linecap='round' stroke-dasharray='16 64'><animate attributeName='stroke-dashoffset' values='80;-80' dur='1.8s' repeatCount='indefinite'/></line>" &
        "<circle cx='8' cy='58' r='2' fill='" & c & "'><animate attributeName='cx' values='8;50;92' dur='1.8s' begin='-0s' repeatCount='indefinite'/><animate attributeName='cy' values='62;46;62' dur='1.8s' begin='-0s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.3 0 .6 1;.4 0 .7 1'/><animate attributeName='r' values='2;4.6;2' dur='1.8s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;0' dur='1.8s' begin='-0s' repeatCount='indefinite'/></circle>" &
        "<circle cx='8' cy='58' r='2' fill='" & c & "'><animate attributeName='cx' values='8;50;92' dur='1.8s' begin='-0.22s' repeatCount='indefinite'/><animate attributeName='cy' values='62;46;62' dur='1.8s' begin='-0.22s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.3 0 .6 1;.4 0 .7 1'/><animate attributeName='r' values='2;4.6;2' dur='1.8s' begin='-0.22s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;0' dur='1.8s' begin='-0.22s' repeatCount='indefinite'/></circle>" &
        "<circle cx='8' cy='58' r='2' fill='" & c & "'><animate attributeName='cx' values='8;50;92' dur='1.8s' begin='-0.44s' repeatCount='indefinite'/><animate attributeName='cy' values='62;46;62' dur='1.8s' begin='-0.44s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.3 0 .6 1;.4 0 .7 1'/><animate attributeName='r' values='2;4.6;2' dur='1.8s' begin='-0.44s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;0' dur='1.8s' begin='-0.44s' repeatCount='indefinite'/></circle>" &
        "<circle cx='8' cy='58' r='2' fill='" & c & "'><animate attributeName='cx' values='8;50;92' dur='1.8s' begin='-0.66s' repeatCount='indefinite'/><animate attributeName='cy' values='62;46;62' dur='1.8s' begin='-0.66s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.3 0 .6 1;.4 0 .7 1'/><animate attributeName='r' values='2;4.6;2' dur='1.8s' begin='-0.66s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;0' dur='1.8s' begin='-0.66s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Orbit 3D

After the 3D spinner preloader: satellites circle a shaded sphere on a tilted orbit, shrinking and dimming behind it, while the whole plane wobbles.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><radialGradient id='sph3d' cx='0.35' cy='0.3' r='0.95'><stop offset='0' stop-color='" & c & "' stop-opacity='0.45'/><stop offset='1' stop-color='" & c & "'/></radialGradient></defs>" &
        "<g><ellipse cx='50' cy='50' rx='38' ry='17' fill='none' stroke='" & c & "' stroke-opacity='0.18' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='12' fill='url(#sph3d)'/>" &
        "<circle r='3.5' fill='" & c & "'><animateMotion dur='2.4s' begin='-0s' repeatCount='indefinite' path='M88 50 A38 17 0 1 1 12 50 A38 17 0 1 1 88 50'/><animate attributeName='r' values='3.5;4.9;3.5;2.2;3.5' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.7;1;0.7;0.3;0.7' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-0s' repeatCount='indefinite'/></circle>" &
        "<circle r='3.5' fill='" & c & "'><animateMotion dur='2.4s' begin='-0.8s' repeatCount='indefinite' path='M88 50 A38 17 0 1 1 12 50 A38 17 0 1 1 88 50'/><animate attributeName='r' values='3.5;4.9;3.5;2.2;3.5' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-0.8s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.7;1;0.7;0.3;0.7' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-0.8s' repeatCount='indefinite'/></circle>" &
        "<circle r='3.5' fill='" & c & "'><animateMotion dur='2.4s' begin='-1.6s' repeatCount='indefinite' path='M88 50 A38 17 0 1 1 12 50 A38 17 0 1 1 88 50'/><animate attributeName='r' values='3.5;4.9;3.5;2.2;3.5' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-1.6s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.7;1;0.7;0.3;0.7' keyTimes='0;0.25;0.5;0.75;1' dur='2.4s' begin='-1.6s' repeatCount='indefinite'/></circle>" &
        "<animateTransform attributeName='transform' type='rotate' values='-8 50 50;8 50 50;-8 50 50' dur='7s' calcMode='spline' keySplines='.45 0 .55 1;.45 0 .55 1' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Gooey

After the gooey loader: three satellites orbit a core through a goo filter, so the blobs stretch, kiss, and split like liquid.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><filter id='goo' x='-40%' y='-40%' width='180%' height='180%'><feGaussianBlur in='SourceGraphic' stdDeviation='6' result='b'/><feColorMatrix in='b' type='matrix' values='1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 20 -9'/></filter></defs>" &
        "<g filter='url(#goo)'>" &
        "<circle cx='50' cy='50' r='11' fill='" & c & "'/>" &
        "<g><circle cx='71' cy='50' r='7' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='1.8s' repeatCount='indefinite'/></g>" &
        "<g><circle cx='31' cy='50' r='5.5' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' from='360 50 50' to='0 50 50' dur='2.6s' repeatCount='indefinite'/></g>" &
        "<g><circle cx='50' cy='27' r='4.5' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='3.4s' repeatCount='indefinite'/></g>" &
        "</g>" &
        "</svg>"
    )
)
```

### Percent

A determinate ring driven by a progress variable, with the number in the middle. This one reports real progress instead of implying it.

```
With(
    {c: "#005EA2", p: varLoadPct},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='42' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='8'/>" &
        "<circle cx='50' cy='50' r='42' fill='none' stroke='" & c & "' stroke-width='8' stroke-linecap='round' stroke-dasharray='" & Text(Round(2.639 * p, 0)) & " 300' transform='rotate(-90 50 50)'/>" &
        "<text x='50' y='58' text-anchor='middle' font-family='Segoe UI, sans-serif' font-size='22' font-weight='600' fill='" & c & "'>" & Text(Round(p, 0)) & "%</text>" &
        "</svg>"
    )
)
```

### Making the percentage accurate

Power Apps has no progress events. A single call like one `ClearCollect` from one source is atomic: it gives you nothing until it finishes, so no formula can report true byte-level progress inside it. Accurate percent therefore means one of these patterns:

1. Step pipeline. Break the load into N known steps and update a variable after each one, weighting steps by how long they typically take:
```
Set(varLoadPct, 0);
ClearCollect(colAgents, ...);   Set(varLoadPct, 40);
ClearCollect(colCourses, ...);  Set(varLoadPct, 70);
ClearCollect(colSlots, ...);    Set(varLoadPct, 95);
Set(varReady, true);            Set(varLoadPct, 100)
```
The steps must run sequentially for the numbers to mean anything. If you use `Concurrent`, have each branch set its own flag (`Set(varDoneA, true)`) and compute the percent from how many flags are true.

2. Paged or batched loads. When you pull a large table in pages (the usual way past the 2,000 row limit), you know the total up front from a count query, so the percent is exact: `varLoadPct = CountRows(colData) / varTotal * 100`, updated after each page inside the loop.

3. Smoothing. The ring jumps between step values. Add a Timer (Duration 50, Repeat true, running while loading) with `OnTimerEnd: Set(varShownPct, varShownPct + (varLoadPct - varShownPct) * 0.2)` and bind the ring to `varShownPct`. The displayed number glides to each real value instead of snapping.

Honesty note: a percent driven only by a timer with no connection to the actual work is decoration. If the work cannot be broken into measurable steps, use one of the indeterminate spinners instead of an invented number.

Text crispness note: SVG text scales with the control, which can soften at small sizes. If you want a sharper number, drop the `text` element from the SVG and overlay a Label with `Text: Round(varLoadPct, 0) & "%"` centered on the Image control.

Performance note: Gooey uses an SVG filter (`feGaussianBlur` plus `feColorMatrix`), which is heavier than plain shape animation. It renders fine in the browser and desktop players; sanity check it on your oldest field devices before shipping it broadly.


# Marksmanship

Range iconography built as loaders for firearms training apps. Same delivery as the other sets: paste into an Image control's `Image` property, `ImagePosition.Fit`, square control, `c` swapped for your theme accent.

### Zero

Impacts walk onto a bullseye one by one and hold as a group before the target is pasted clean. A zeroing sequence as a loop.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='42' fill='none' stroke='" & c & "' stroke-opacity='0.2' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='32' fill='none' stroke='" & c & "' stroke-opacity='0.2' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='22' fill='none' stroke='" & c & "' stroke-opacity='0.2' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='12' fill='none' stroke='" & c & "' stroke-opacity='0.2' stroke-width='1.5'/>" &
        "<line x1='50' y1='4' x2='50' y2='12' stroke='" & c & "' stroke-opacity='0.35' stroke-width='1.5'/>" &
        "<line x1='50' y1='88' x2='50' y2='96' stroke='" & c & "' stroke-opacity='0.35' stroke-width='1.5'/>" &
        "<line x1='4' y1='50' x2='12' y2='50' stroke='" & c & "' stroke-opacity='0.35' stroke-width='1.5'/>" &
        "<line x1='88' y1='50' x2='96' y2='50' stroke='" & c & "' stroke-opacity='0.35' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='2.5' fill='" & c & "' fill-opacity='0.5'/>" &
        "<circle cx='54' cy='44' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.08;0.10;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.08;0.13;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='45' cy='53' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.18;0.20;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.18;0.23;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='57' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.28;0.30;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.28;0.33;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='57' cy='52' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.38;0.40;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.38;0.43;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='44' cy='46' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.48;0.50;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.48;0.53;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='51' cy='48' r='3.2' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.58;0.60;0.86;0.94;1' dur='3s' repeatCount='indefinite'/><animate attributeName='r' values='6;6;3.2;3.2' keyTimes='0;0.58;0.63;1' dur='3s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Reticle

A mil-dot reticle drifts, steadies, and settles on center, with a dot confirming the hold before it breaks again.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='44' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='2'/>" &
        "<g>" &
        "<circle cx='50' cy='50' r='30' fill='none' stroke='" & c & "' stroke-opacity='0.45' stroke-width='1.5'/>" &
        "<line x1='50' y1='14' x2='50' y2='42' stroke='" & c & "' stroke-width='2'/>" &
        "<line x1='50' y1='58' x2='50' y2='86' stroke='" & c & "' stroke-width='2'/>" &
        "<line x1='14' y1='50' x2='42' y2='50' stroke='" & c & "' stroke-width='2'/>" &
        "<line x1='58' y1='50' x2='86' y2='50' stroke='" & c & "' stroke-width='2'/>" &
        "<circle cx='50' cy='34' r='1.4' fill='" & c & "'/><circle cx='50' cy='66' r='1.4' fill='" & c & "'/>" &
        "<circle cx='34' cy='50' r='1.4' fill='" & c & "'/><circle cx='66' cy='50' r='1.4' fill='" & c & "'/>" &
        "<circle cx='50' cy='50' r='2.6' fill='" & c & "' opacity='0'><animate attributeName='opacity' values='0;0;1;1;0' keyTimes='0;0.72;0.76;0.9;1' dur='3.2s' repeatCount='indefinite'/></circle>" &
        "<animateTransform attributeName='transform' type='translate' values='0 0;-7 4;5 -6;-3 3;0 0;0 0' keyTimes='0;0.18;0.42;0.6;0.72;1' calcMode='spline' keySplines='.4 0 .6 1;.4 0 .6 1;.4 0 .6 1;.3 0 .4 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/>" &
        "</g>" &
        "</svg>"
    )
)
```

### Cylinder

Six chambers light in turn as the cylinder ratchets through a full rotation, then it empties and starts over.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='36' fill='none' stroke='" & c & "' stroke-width='3'/>" &
        "<g>" &
        "<circle cx='71.0' cy='50.0' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;1;1;0.15' keyTimes='0;0.04;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='60.5' cy='68.2' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.167;0.207;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='39.5' cy='68.2' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.333;0.373;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='29.0' cy='50.0' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.500;0.540;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='39.5' cy='31.8' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.667;0.707;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='60.5' cy='31.8' r='7' fill='" & c & "' fill-opacity='0.15' stroke='" & c & "' stroke-width='1.5'><animate attributeName='fill-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.833;0.873;0.96;1' dur='3.6s' repeatCount='indefinite'/></circle>" &
        "<animateTransform attributeName='transform' type='rotate' values='0 50 50;0 50 50;60 50 50;60 50 50;120 50 50;120 50 50;180 50 50;180 50 50;240 50 50;240 50 50;300 50 50;300 50 50;360 50 50' keyTimes='0;0.117;0.167;0.284;0.333;0.450;0.500;0.617;0.667;0.784;0.833;0.950;1' dur='3.6s' repeatCount='indefinite'/>" &
        "</g>" &
        "<circle cx='50' cy='50' r='4' fill='" & c & "'/>" &
        "</svg>"
    )
)
```

### Plates

A five plate rack falls left to right with a snap on each hit, then the whole rack resets at once.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='10' y1='74' x2='90' y2='74' stroke='" & c & "' stroke-width='3' stroke-linecap='round'/>" &
        "<g><line x1='20' y1='58' x2='20' y2='74' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='20' cy='52' r='6.2' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 20 74;0 20 74;-80 20 74;-80 20 74;0 20 74;0 20 74' keyTimes='0;0.10;0.16;0.88;0.94;1' calcMode='spline' keySplines='0 0 1 1;.5 0 1 .5;0 0 1 1;.3 0 .3 1;0 0 1 1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "<g><line x1='35' y1='58' x2='35' y2='74' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='35' cy='52' r='6.2' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 35 74;0 35 74;-80 35 74;-80 35 74;0 35 74;0 35 74' keyTimes='0;0.23;0.29;0.88;0.94;1' calcMode='spline' keySplines='0 0 1 1;.5 0 1 .5;0 0 1 1;.3 0 .3 1;0 0 1 1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "<g><line x1='50' y1='58' x2='50' y2='74' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='50' cy='52' r='6.2' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 50 74;0 50 74;-80 50 74;-80 50 74;0 50 74;0 50 74' keyTimes='0;0.36;0.42;0.88;0.94;1' calcMode='spline' keySplines='0 0 1 1;.5 0 1 .5;0 0 1 1;.3 0 .3 1;0 0 1 1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "<g><line x1='65' y1='58' x2='65' y2='74' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='65' cy='52' r='6.2' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 65 74;0 65 74;-80 65 74;-80 65 74;0 65 74;0 65 74' keyTimes='0;0.49;0.55;0.88;0.94;1' calcMode='spline' keySplines='0 0 1 1;.5 0 1 .5;0 0 1 1;.3 0 .3 1;0 0 1 1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "<g><line x1='80' y1='58' x2='80' y2='74' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='80' cy='52' r='6.2' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 80 74;0 80 74;-80 80 74;-80 80 74;0 80 74;0 80 74' keyTimes='0;0.62;0.68;0.88;0.94;1' calcMode='spline' keySplines='0 0 1 1;.5 0 1 .5;0 0 1 1;.3 0 .3 1;0 0 1 1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Par

A shot timer arc runs to par, the ring flashes like the beep, and the clock resets.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-opacity='0.12' stroke-width='7'/>" &
        "<line x1='50' y1='6' x2='50' y2='14' stroke='" & c & "' stroke-width='3' stroke-linecap='round'/>" &
        "<circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-width='7' stroke-linecap='round' transform='rotate(-90 50 50)'><animate attributeName='stroke-dasharray' values='0 239;239 0;239 0;0 239' keyTimes='0;0.68;0.97;1' dur='2.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-width='7' opacity='0'><animate attributeName='r' values='38;38;47' keyTimes='0;0.68;0.9' dur='2.6s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;0;0.5;0;0' keyTimes='0;0.68;0.71;0.9;1' dur='2.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='5' fill='" & c & "'><animate attributeName='r' values='5;5;7;5;5' keyTimes='0;0.68;0.71;0.78;1' dur='2.6s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Notes

- Zero, Reticle, Cylinder, and Plates run on a single shared clock per spinner (one `dur` with `keyTimes`), so the sequences stay in sync no matter when the control loads.
- Cylinder's ratchet is a stepped rotate: each sixth of the cycle dwells and then advances 60 degrees, and each chamber's fill is keyed to the same fractions.
- Plates pivots each plate group around its post base with a fast fall spline, which is what gives the hit its snap.
- Longer loops (3 to 3.6s) suit these because they tell a small story; if a screen usually loads in under a second, prefer one of the continuous spinners so users never see just a fragment.


# Marksmanship, set two

Ten more range and federal law enforcement themed loaders. Same delivery: Image control, `ImagePosition.Fit`, square control, `c` swapped for your theme accent.

### Slipstream

The round hangs in frame under a slight lens shake while the air streaks past it. Camera tracking a bullet in flight.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g>" &
        "<line x1='0' y1='26' x2='100' y2='26' stroke='" & c & "' stroke-opacity='0.3' stroke-width='2' stroke-linecap='round' stroke-dasharray='12 88'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.42s' repeatCount='indefinite'/></line>" &
        "<line x1='0' y1='36' x2='100' y2='36' stroke='" & c & "' stroke-opacity='0.5' stroke-width='2' stroke-linecap='round' stroke-dasharray='20 80'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.55s' repeatCount='indefinite'/></line>" &
        "<line x1='0' y1='46' x2='100' y2='46' stroke='" & c & "' stroke-opacity='0.25' stroke-width='2' stroke-linecap='round' stroke-dasharray='9 91'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.35s' repeatCount='indefinite'/></line>" &
        "<line x1='0' y1='58' x2='100' y2='58' stroke='" & c & "' stroke-opacity='0.45' stroke-width='2' stroke-linecap='round' stroke-dasharray='16 84'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.62s' repeatCount='indefinite'/></line>" &
        "<line x1='0' y1='68' x2='100' y2='68' stroke='" & c & "' stroke-opacity='0.35' stroke-width='2' stroke-linecap='round' stroke-dasharray='22 78'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.48s' repeatCount='indefinite'/></line>" &
        "<line x1='0' y1='76' x2='100' y2='76' stroke='" & c & "' stroke-opacity='0.25' stroke-width='2' stroke-linecap='round' stroke-dasharray='11 89'><animate attributeName='stroke-dashoffset' values='0;100' dur='0.38s' repeatCount='indefinite'/></line>" &
        "<rect x='26' y='43' width='5' height='14' rx='1.5' fill='" & c & "' opacity='0.75'/>" &
        "<path d='M31 43 L58 43 Q73 43.5 80 50 Q73 56.5 58 57 L31 57 Z' fill='" & c & "'/>" &
        "<line x1='52' y1='43' x2='52' y2='57' stroke='" & c & "' stroke-opacity='0.35' stroke-width='1.5'/>" &
        "<animateTransform attributeName='transform' type='translate' values='0 0;0.9 -0.7;-0.8 0.5;0.6 0.8;-0.7 -0.6;0 0' dur='0.3s' repeatCount='indefinite'/>" &
        "</g>" &
        "</svg>"
    )
)
```

### Brass

Casings eject on the same arc, tumble, take two bounces off the deck, and slide out of frame.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='8' y1='74' x2='92' y2='74' stroke='" & c & "' stroke-opacity='0.2' stroke-width='2'/>" &
        "<g opacity='0'><g><rect x='-6' y='-2.5' width='12' height='5' rx='1.8' fill='" & c & "'/><rect x='-7.6' y='-3.2' width='2.6' height='6.4' rx='1' fill='" & c & "' opacity='0.65'/><animateTransform attributeName='transform' type='rotate' values='0;560' dur='2.2s' begin='0s' repeatCount='indefinite'/></g><animateTransform attributeName='transform' type='translate' values='12 38;30 20;48 69;58 54;66 69;72 62;78 70;86 70' keyTimes='0;0.16;0.4;0.52;0.64;0.74;0.84;1' calcMode='spline' keySplines='.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;0 0 1 1' dur='2.2s' begin='0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;1;0' keyTimes='0;0.05;0.88;1' dur='2.2s' begin='0s' repeatCount='indefinite'/></g>" &
        "<g opacity='0'><g><rect x='-6' y='-2.5' width='12' height='5' rx='1.8' fill='" & c & "'/><rect x='-7.6' y='-3.2' width='2.6' height='6.4' rx='1' fill='" & c & "' opacity='0.65'/><animateTransform attributeName='transform' type='rotate' values='0;560' dur='2.2s' begin='-0.73s' repeatCount='indefinite'/></g><animateTransform attributeName='transform' type='translate' values='12 38;30 20;48 69;58 54;66 69;72 62;78 70;86 70' keyTimes='0;0.16;0.4;0.52;0.64;0.74;0.84;1' calcMode='spline' keySplines='.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;0 0 1 1' dur='2.2s' begin='-0.73s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;1;0' keyTimes='0;0.05;0.88;1' dur='2.2s' begin='-0.73s' repeatCount='indefinite'/></g>" &
        "<g opacity='0'><g><rect x='-6' y='-2.5' width='12' height='5' rx='1.8' fill='" & c & "'/><rect x='-7.6' y='-3.2' width='2.6' height='6.4' rx='1' fill='" & c & "' opacity='0.65'/><animateTransform attributeName='transform' type='rotate' values='0;560' dur='2.2s' begin='-1.47s' repeatCount='indefinite'/></g><animateTransform attributeName='transform' type='translate' values='12 38;30 20;48 69;58 54;66 69;72 62;78 70;86 70' keyTimes='0;0.16;0.4;0.52;0.64;0.74;0.84;1' calcMode='spline' keySplines='.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;.25 .6 .5 1;.5 0 .75 .4;0 0 1 1' dur='2.2s' begin='-1.47s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;1;1;0' keyTimes='0;0.05;0.88;1' dur='2.2s' begin='-1.47s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Muzzle

A barrel and front sight with smoke wisps curling up, spreading, and thinning after the shot.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<rect x='45' y='60' width='10' height='30' rx='2' fill='" & c & "'/>" &
        "<rect x='48.4' y='53' width='3.2' height='7' rx='1' fill='" & c & "'/>" &
        "<line x1='44' y1='60' x2='56' y2='60' stroke='" & c & "' stroke-width='2' stroke-linecap='round'/>" &
        "<circle cx='50' cy='54' r='2.5' fill='" & c & "' opacity='0'><animate attributeName='cy' values='54;38;25;14' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='0.0s' repeatCount='indefinite'/><animate attributeName='cx' values='50;47.5;52.5;49' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='0.0s' repeatCount='indefinite'/><animate attributeName='r' values='2.5;5.5;8;10.5' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='0.0s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;0.4;0.22;0' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='0.0s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='54' r='2.5' fill='" & c & "' opacity='0'><animate attributeName='cy' values='54;38;25;14' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-0.65s' repeatCount='indefinite'/><animate attributeName='cx' values='50;47.5;52.5;49' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-0.65s' repeatCount='indefinite'/><animate attributeName='r' values='2.5;5.5;8;10.5' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-0.65s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;0.4;0.22;0' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-0.65s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='54' r='2.5' fill='" & c & "' opacity='0'><animate attributeName='cy' values='54;38;25;14' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.3s' repeatCount='indefinite'/><animate attributeName='cx' values='50;47.5;52.5;49' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.3s' repeatCount='indefinite'/><animate attributeName='r' values='2.5;5.5;8;10.5' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.3s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;0.4;0.22;0' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.3s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='54' r='2.5' fill='" & c & "' opacity='0'><animate attributeName='cy' values='54;38;25;14' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.9500000000000002s' repeatCount='indefinite'/><animate attributeName='cx' values='50;47.5;52.5;49' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.9500000000000002s' repeatCount='indefinite'/><animate attributeName='r' values='2.5;5.5;8;10.5' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.9500000000000002s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.5;0.4;0.22;0' keyTimes='0;0.35;0.7;1' dur='2.6s' begin='-1.9500000000000002s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Turner

A turning target faces you, holds for the string, edges away, and comes back around. Straight off the qual line.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='50' y1='80' x2='50' y2='90' stroke='" & c & "' stroke-opacity='0.5' stroke-width='3'/>" &
        "<line x1='40' y1='90' x2='60' y2='90' stroke='" & c & "' stroke-opacity='0.5' stroke-width='3' stroke-linecap='round'/>" &
        "<g transform='translate(50 46)'><g>" &
        "<rect x='-21' y='-32' width='42' height='64' rx='3' fill='none' stroke='" & c & "' stroke-width='2.5'/>" &
        "<circle r='13' fill='none' stroke='" & c & "' stroke-opacity='0.55' stroke-width='2'/>" &
        "<circle r='5' fill='" & c & "' fill-opacity='0.55'/>" &
        "<animateTransform attributeName='transform' type='scale' values='1 1;1 1;0.045 1;0.045 1;1 1;1 1' keyTimes='0;0.4;0.5;0.62;0.72;1' calcMode='spline' keySplines='0 0 1 1;.6 0 .4 1;0 0 1 1;.6 0 .4 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/>" &
        "<animate attributeName='opacity' values='1;1;0.45;0.45;1;1' keyTimes='0;0.4;0.5;0.62;0.72;1' dur='3.2s' repeatCount='indefinite'/>" &
        "</g></g>" &
        "</svg>"
    )
)
```

### Steel

A dueling tree: paddles swing around the post top to bottom, then swing back home in the same order.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='50' y1='14' x2='50' y2='84' stroke='" & c & "' stroke-width='3.5' stroke-linecap='round'/>" &
        "<line x1='36' y1='88' x2='64' y2='88' stroke='" & c & "' stroke-width='3.5' stroke-linecap='round'/>" &
        "<g><line x1='50' y1='26' x2='61' y2='26' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='66.5' cy='26' r='6' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 50 26;0 50 26;180 50 26;180 50 26;360 50 26;360 50 26' keyTimes='0;0.06;0.14;0.56;0.64;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/></g>" &
        "<g><line x1='50' y1='40' x2='61' y2='40' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='66.5' cy='40' r='6' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 50 40;0 50 40;180 50 40;180 50 40;360 50 40;360 50 40' keyTimes='0;0.15;0.23;0.65;0.73;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/></g>" &
        "<g><line x1='50' y1='54' x2='61' y2='54' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='66.5' cy='54' r='6' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 50 54;0 50 54;180 50 54;180 50 54;360 50 54;360 50 54' keyTimes='0;0.24;0.32;0.74;0.82;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/></g>" &
        "<g><line x1='50' y1='68' x2='61' y2='68' stroke='" & c & "' stroke-opacity='0.6' stroke-width='2'/><circle cx='66.5' cy='68' r='6' fill='" & c & "'/><animateTransform attributeName='transform' type='rotate' values='0 50 68;0 50 68;180 50 68;180 50 68;360 50 68;360 50 68' keyTimes='0;0.33;0.41;0.83;0.91;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Rings

Scoring rings light up outward from the X ring in a steady radiating pulse. The quietest of the set.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='46' y1='50' x2='54' y2='50' stroke='" & c & "' stroke-width='1.5'/>" &
        "<line x1='50' y1='46' x2='50' y2='54' stroke='" & c & "' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='10' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-opacity='0.15'><animate attributeName='stroke-opacity' values='0.15;1;0.15' dur='1.7s' begin='-1.70s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='18' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-opacity='0.15'><animate attributeName='stroke-opacity' values='0.15;1;0.15' dur='1.7s' begin='-1.53s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='26' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-opacity='0.15'><animate attributeName='stroke-opacity' values='0.15;1;0.15' dur='1.7s' begin='-1.36s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='34' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-opacity='0.15'><animate attributeName='stroke-opacity' values='0.15;1;0.15' dur='1.7s' begin='-1.19s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='42' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-opacity='0.15'><animate attributeName='stroke-opacity' values='0.15;1;0.15' dur='1.7s' begin='-1.02s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Ladder

A holdover reticle: the bright bar steps down the BDC ladder rung by rung, then snaps back to zero.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='45' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='2'/>" &
        "<line x1='50' y1='10' x2='50' y2='90' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/>" &
        "<line x1='16' y1='28' x2='84' y2='28' stroke='" & c & "' stroke-width='2'/>" &
        "<line x1='39' y1='42' x2='61' y2='42' stroke='" & c & "' stroke-opacity='0.45' stroke-width='1.5'/>" &
        "<line x1='41' y1='52' x2='59' y2='52' stroke='" & c & "' stroke-opacity='0.45' stroke-width='1.5'/>" &
        "<line x1='43' y1='62' x2='57' y2='62' stroke='" & c & "' stroke-opacity='0.45' stroke-width='1.5'/>" &
        "<line x1='44.5' y1='72' x2='55.5' y2='72' stroke='" & c & "' stroke-opacity='0.45' stroke-width='1.5'/>" &
        "<g><line x1='36' y1='28' x2='64' y2='28' stroke='" & c & "' stroke-width='3.5' stroke-linecap='round'/><animateTransform attributeName='transform' type='translate' values='0 0;0 0;0 14;0 14;0 24;0 24;0 34;0 34;0 44;0 44;0 0' keyTimes='0;0.14;0.18;0.32;0.36;0.5;0.54;0.68;0.72;0.9;1' dur='3.4s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;1;1;1;1;1;1;1;1;1;0.3;1' keyTimes='0;0.14;0.18;0.32;0.36;0.5;0.54;0.68;0.72;0.9;0.95;1' dur='3.4s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Focus

The scope picture starts doubled and soft, pulls to a single sharp reticle, holds, and drifts back out of focus.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><filter id='foc' x='-20%' y='-20%' width='140%' height='140%'><feGaussianBlur stdDeviation='2.4'><animate attributeName='stdDeviation' values='2.4;0;0;2.4' keyTimes='0;0.35;0.7;1' dur='3s' repeatCount='indefinite'/></feGaussianBlur></filter></defs>" &
        "<circle cx='50' cy='50' r='43' fill='none' stroke='" & c & "' stroke-width='3'/>" &
        "<g filter='url(#foc)'>" &
        "<g opacity='0.35'><line x1='50' y1='16' x2='50' y2='84' stroke='" & c & "' stroke-width='1.5'/><line x1='16' y1='50' x2='84' y2='50' stroke='" & c & "' stroke-width='1.5'/><animateTransform attributeName='transform' type='translate' values='5 3;0 0;0 0;5 3' keyTimes='0;0.35;0.7;1' dur='3s' repeatCount='indefinite'/></g>" &
        "<line x1='50' y1='16' x2='50' y2='84' stroke='" & c & "' stroke-width='1.5'/>" &
        "<line x1='16' y1='50' x2='84' y2='50' stroke='" & c & "' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='16' fill='none' stroke='" & c & "' stroke-opacity='0.5' stroke-width='1.5'/>" &
        "<circle cx='50' cy='50' r='2.2' fill='" & c & "'/>" &
        "</g>" &
        "</svg>"
    )
)
```

### Shield

A shield draws itself, a scan line sweeps down it like a credential check, and the star lights to confirm.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M50 12 L78 21 L78 45 C78 65 66 77 50 86 C34 77 22 65 22 45 L22 21 Z' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='2.5'/>" &
        "<path d='M50 12 L78 21 L78 45 C78 65 66 77 50 86 C34 77 22 65 22 45 L22 21 Z' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-linejoin='round' pathLength='100' stroke-dasharray='100'><animate attributeName='stroke-dashoffset' values='100;0;0;100' keyTimes='0;0.38;0.9;1' dur='3.4s' repeatCount='indefinite'/></path>" &
        "<defs><clipPath id='shc'><path d='M50 12 L78 21 L78 45 C78 65 66 77 50 86 C34 77 22 65 22 45 L22 21 Z'/></clipPath></defs>" &
        "<line x1='22' y1='18' x2='78' y2='18' stroke='" & c & "' stroke-width='2' clip-path='url(#shc)' opacity='0'><animate attributeName='y1' values='16;16;84;84' keyTimes='0;0.4;0.82;1' dur='3.4s' repeatCount='indefinite'/><animate attributeName='y2' values='16;16;84;84' keyTimes='0;0.4;0.82;1' dur='3.4s' repeatCount='indefinite'/><animate attributeName='opacity' values='0;0;0.65;0.65;0;0' keyTimes='0;0.4;0.44;0.78;0.86;1' dur='3.4s' repeatCount='indefinite'/></line>" &
        "<polygon points='50.0 35.0 52.8 43.1 61.4 43.3 54.6 48.5 57.1 56.7 50.0 51.8 42.9 56.7 45.4 48.5 38.6 43.3 47.2 43.1' fill='" & c & "' fill-opacity='0.12'><animate attributeName='fill-opacity' values='0.12;0.12;0.7;0.12' keyTimes='0;0.62;0.82;1' dur='3.4s' repeatCount='indefinite'/></polygon>" &
        "</svg>"
    )
)
```

### Lanes

Overhead view of four lanes: carriers run targets downrange, hold at distance, and bring them back staggered.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='8' y1='88' x2='92' y2='88' stroke='" & c & "' stroke-width='3' stroke-linecap='round'/>" &
        "<line x1='8' y1='12' x2='92' y2='12' stroke='" & c & "' stroke-opacity='0.3' stroke-width='2' stroke-dasharray='4 4'/>" &
        "<line x1='20' y1='14' x2='20' y2='86' stroke='" & c & "' stroke-opacity='0.15' stroke-width='1.5' stroke-dasharray='3 5'/>" &
        "<g><rect x='16' y='76' width='8' height='8' rx='1.5' fill='none' stroke='" & c & "' stroke-width='2'/><circle cx='20' cy='80' r='1.8' fill='" & c & "'/><animateTransform attributeName='transform' type='translate' values='0 0;0 -58;0 -58;0 0;0 0' keyTimes='0;0.34;0.5;0.84;1' calcMode='spline' keySplines='.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='2.8s' begin='0.0s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.5;0.5;1;1' keyTimes='0;0.34;0.5;0.84;1' dur='2.8s' begin='0.0s' repeatCount='indefinite'/></g>" &
        "<line x1='40' y1='14' x2='40' y2='86' stroke='" & c & "' stroke-opacity='0.15' stroke-width='1.5' stroke-dasharray='3 5'/>" &
        "<g><rect x='36' y='76' width='8' height='8' rx='1.5' fill='none' stroke='" & c & "' stroke-width='2'/><circle cx='40' cy='80' r='1.8' fill='" & c & "'/><animateTransform attributeName='transform' type='translate' values='0 0;0 -58;0 -58;0 0;0 0' keyTimes='0;0.34;0.5;0.84;1' calcMode='spline' keySplines='.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='2.8s' begin='-0.7s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.5;0.5;1;1' keyTimes='0;0.34;0.5;0.84;1' dur='2.8s' begin='-0.7s' repeatCount='indefinite'/></g>" &
        "<line x1='60' y1='14' x2='60' y2='86' stroke='" & c & "' stroke-opacity='0.15' stroke-width='1.5' stroke-dasharray='3 5'/>" &
        "<g><rect x='56' y='76' width='8' height='8' rx='1.5' fill='none' stroke='" & c & "' stroke-width='2'/><circle cx='60' cy='80' r='1.8' fill='" & c & "'/><animateTransform attributeName='transform' type='translate' values='0 0;0 -58;0 -58;0 0;0 0' keyTimes='0;0.34;0.5;0.84;1' calcMode='spline' keySplines='.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='2.8s' begin='-1.4s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.5;0.5;1;1' keyTimes='0;0.34;0.5;0.84;1' dur='2.8s' begin='-1.4s' repeatCount='indefinite'/></g>" &
        "<line x1='80' y1='14' x2='80' y2='86' stroke='" & c & "' stroke-opacity='0.15' stroke-width='1.5' stroke-dasharray='3 5'/>" &
        "<g><rect x='76' y='76' width='8' height='8' rx='1.5' fill='none' stroke='" & c & "' stroke-width='2'/><circle cx='80' cy='80' r='1.8' fill='" & c & "'/><animateTransform attributeName='transform' type='translate' values='0 0;0 -58;0 -58;0 0;0 0' keyTimes='0;0.34;0.5;0.84;1' calcMode='spline' keySplines='.4 0 .3 1;0 0 1 1;.4 0 .3 1;0 0 1 1' dur='2.8s' begin='-2.0999999999999996s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.5;0.5;1;1' keyTimes='0;0.34;0.5;0.84;1' dur='2.8s' begin='-2.0999999999999996s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Notes

- Brass runs all three casings on one keyframed trajectory with staggered starts, so there is always brass in the air. The bounces are spline eased pairs (ease out going up, ease in coming down).
- Slipstream's shake is a fast 0.3s translate loop on the whole frame; lower the values if it reads too jittery at small sizes.
- Focus and the goo spinner are the two filter-based ones (Focus animates feGaussianBlur's stdDeviation). Both render in all players; test on older field devices.
- Shield uses pathLength='100' to normalize the dash math for the self drawing outline, and a clipPath so the scan line stays inside the shield.
- Turner does the scaleX squash inside a translated group, which is how you scale about center with SMIL's single transform per group.


# Rifling and Turner II

Two additions to the marksmanship sets. Rifling is the spinning round with a corkscrew trail; Turner II swaps the bullseye carrier for a law enforcement silhouette. Same delivery: Image control, `ImagePosition.Fit`, square control, `c` swapped for your theme accent.

### Rifling

The round spins in frame with a rifled twist while its wispy trail corkscrews behind it to a flicker at the muzzle. The stripes and the helix run the same direction.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><clipPath id='blt'><path d='M42 43 L24 43 Q13 43.5 7 50 Q13 56.5 24 57 L42 57 Z'/></clipPath></defs>" &
        "<path fill='none' stroke='" & c & "' stroke-opacity='0.1' stroke-width='6' stroke-linecap='round' d='M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0'><animate attributeName='d' values='M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0;M47.0 47.4 L48.7 47.4 L50.4 48.0 L52.1 48.9 L53.8 50.2 L55.5 51.7 L57.2 52.9 L58.9 53.8 L60.6 54.1 L62.3 53.7 L64.0 52.6 L65.7 50.9 L67.4 48.9 L69.1 47.0 L70.8 45.4 L72.5 44.5 L74.2 44.5 L75.9 45.5 L77.6 47.3 L79.3 49.7 L81.0 52.3 L82.7 54.7 L84.4 56.4 L86.1 57.1 L87.8 56.6 L89.5 55.0 L91.2 52.4 L92.9 49.2 L94.6 46.1 L96.3 43.4 L98.0 41.8;M47.0 50.0 L48.7 48.9 L50.4 47.8 L52.1 47.0 L53.8 46.6 L55.5 46.8 L57.2 47.6 L58.9 49.0 L60.6 50.6 L62.3 52.3 L64.0 53.7 L65.7 54.7 L67.4 54.8 L69.1 54.2 L70.8 52.7 L72.5 50.7 L74.2 48.4 L75.9 46.2 L77.6 44.5 L79.3 43.7 L81.0 43.9 L82.7 45.2 L84.4 47.4 L86.1 50.2 L87.8 53.1 L89.5 55.6 L91.2 57.3 L92.9 57.8 L94.6 57.1 L96.3 55.0 L98.0 52.0;M47.0 52.6 L48.7 52.6 L50.4 52.0 L52.1 51.1 L53.8 49.8 L55.5 48.3 L57.2 47.1 L58.9 46.2 L60.6 45.9 L62.3 46.3 L64.0 47.4 L65.7 49.1 L67.4 51.1 L69.1 53.0 L70.8 54.6 L72.5 55.5 L74.2 55.5 L75.9 54.5 L77.6 52.7 L79.3 50.3 L81.0 47.7 L82.7 45.3 L84.4 43.6 L86.1 42.9 L87.8 43.4 L89.5 45.0 L91.2 47.6 L92.9 50.8 L94.6 53.9 L96.3 56.6 L98.0 58.2;M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0' dur='0.8s' repeatCount='indefinite'/></path>" &
        "<path fill='none' stroke='" & c & "' stroke-opacity='0.45' stroke-width='2' stroke-linecap='round' d='M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0'><animate attributeName='d' values='M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0;M47.0 47.4 L48.7 47.4 L50.4 48.0 L52.1 48.9 L53.8 50.2 L55.5 51.7 L57.2 52.9 L58.9 53.8 L60.6 54.1 L62.3 53.7 L64.0 52.6 L65.7 50.9 L67.4 48.9 L69.1 47.0 L70.8 45.4 L72.5 44.5 L74.2 44.5 L75.9 45.5 L77.6 47.3 L79.3 49.7 L81.0 52.3 L82.7 54.7 L84.4 56.4 L86.1 57.1 L87.8 56.6 L89.5 55.0 L91.2 52.4 L92.9 49.2 L94.6 46.1 L96.3 43.4 L98.0 41.8;M47.0 50.0 L48.7 48.9 L50.4 47.8 L52.1 47.0 L53.8 46.6 L55.5 46.8 L57.2 47.6 L58.9 49.0 L60.6 50.6 L62.3 52.3 L64.0 53.7 L65.7 54.7 L67.4 54.8 L69.1 54.2 L70.8 52.7 L72.5 50.7 L74.2 48.4 L75.9 46.2 L77.6 44.5 L79.3 43.7 L81.0 43.9 L82.7 45.2 L84.4 47.4 L86.1 50.2 L87.8 53.1 L89.5 55.6 L91.2 57.3 L92.9 57.8 L94.6 57.1 L96.3 55.0 L98.0 52.0;M47.0 52.6 L48.7 52.6 L50.4 52.0 L52.1 51.1 L53.8 49.8 L55.5 48.3 L57.2 47.1 L58.9 46.2 L60.6 45.9 L62.3 46.3 L64.0 47.4 L65.7 49.1 L67.4 51.1 L69.1 53.0 L70.8 54.6 L72.5 55.5 L74.2 55.5 L75.9 54.5 L77.6 52.7 L79.3 50.3 L81.0 47.7 L82.7 45.3 L84.4 43.6 L86.1 42.9 L87.8 43.4 L89.5 45.0 L91.2 47.6 L92.9 50.8 L94.6 53.9 L96.3 56.6 L98.0 58.2;M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0' dur='0.8s' repeatCount='indefinite'/></path>" &
        "<path fill='none' stroke='" & c & "' stroke-opacity='0.3' stroke-width='2' stroke-linecap='round' d='M47.0 50.0 L48.7 48.9 L50.4 47.8 L52.1 47.0 L53.8 46.6 L55.5 46.8 L57.2 47.6 L58.9 49.0 L60.6 50.6 L62.3 52.3 L64.0 53.7 L65.7 54.7 L67.4 54.8 L69.1 54.2 L70.8 52.7 L72.5 50.7 L74.2 48.4 L75.9 46.2 L77.6 44.5 L79.3 43.7 L81.0 43.9 L82.7 45.2 L84.4 47.4 L86.1 50.2 L87.8 53.1 L89.5 55.6 L91.2 57.3 L92.9 57.8 L94.6 57.1 L96.3 55.0 L98.0 52.0'><animate attributeName='d' values='M47.0 50.0 L48.7 48.9 L50.4 47.8 L52.1 47.0 L53.8 46.6 L55.5 46.8 L57.2 47.6 L58.9 49.0 L60.6 50.6 L62.3 52.3 L64.0 53.7 L65.7 54.7 L67.4 54.8 L69.1 54.2 L70.8 52.7 L72.5 50.7 L74.2 48.4 L75.9 46.2 L77.6 44.5 L79.3 43.7 L81.0 43.9 L82.7 45.2 L84.4 47.4 L86.1 50.2 L87.8 53.1 L89.5 55.6 L91.2 57.3 L92.9 57.8 L94.6 57.1 L96.3 55.0 L98.0 52.0;M47.0 52.6 L48.7 52.6 L50.4 52.0 L52.1 51.1 L53.8 49.8 L55.5 48.3 L57.2 47.1 L58.9 46.2 L60.6 45.9 L62.3 46.3 L64.0 47.4 L65.7 49.1 L67.4 51.1 L69.1 53.0 L70.8 54.6 L72.5 55.5 L74.2 55.5 L75.9 54.5 L77.6 52.7 L79.3 50.3 L81.0 47.7 L82.7 45.3 L84.4 43.6 L86.1 42.9 L87.8 43.4 L89.5 45.0 L91.2 47.6 L92.9 50.8 L94.6 53.9 L96.3 56.6 L98.0 58.2;M47.0 50.0 L48.7 51.1 L50.4 52.2 L52.1 53.0 L53.8 53.4 L55.5 53.2 L57.2 52.4 L58.9 51.0 L60.6 49.4 L62.3 47.7 L64.0 46.3 L65.7 45.3 L67.4 45.2 L69.1 45.8 L70.8 47.3 L72.5 49.3 L74.2 51.6 L75.9 53.8 L77.6 55.5 L79.3 56.3 L81.0 56.1 L82.7 54.8 L84.4 52.6 L86.1 49.8 L87.8 46.9 L89.5 44.4 L91.2 42.7 L92.9 42.2 L94.6 42.9 L96.3 45.0 L98.0 48.0;M47.0 47.4 L48.7 47.4 L50.4 48.0 L52.1 48.9 L53.8 50.2 L55.5 51.7 L57.2 52.9 L58.9 53.8 L60.6 54.1 L62.3 53.7 L64.0 52.6 L65.7 50.9 L67.4 48.9 L69.1 47.0 L70.8 45.4 L72.5 44.5 L74.2 44.5 L75.9 45.5 L77.6 47.3 L79.3 49.7 L81.0 52.3 L82.7 54.7 L84.4 56.4 L86.1 57.1 L87.8 56.6 L89.5 55.0 L91.2 52.4 L92.9 49.2 L94.6 46.1 L96.3 43.4 L98.0 41.8;M47.0 50.0 L48.7 48.9 L50.4 47.8 L52.1 47.0 L53.8 46.6 L55.5 46.8 L57.2 47.6 L58.9 49.0 L60.6 50.6 L62.3 52.3 L64.0 53.7 L65.7 54.7 L67.4 54.8 L69.1 54.2 L70.8 52.7 L72.5 50.7 L74.2 48.4 L75.9 46.2 L77.6 44.5 L79.3 43.7 L81.0 43.9 L82.7 45.2 L84.4 47.4 L86.1 50.2 L87.8 53.1 L89.5 55.6 L91.2 57.3 L92.9 57.8 L94.6 57.1 L96.3 55.0 L98.0 52.0' dur='0.8s' repeatCount='indefinite'/></path>" &
        "<g><circle cx='95' cy='50' r='2.6' fill='" & c & "'><animate attributeName='opacity' values='0.9;0.3;0.8;0.2;0.9' dur='0.45s' repeatCount='indefinite'/></circle>" &
        "<circle cx='92' cy='45' r='1.4' fill='" & c & "'><animate attributeName='opacity' values='0.2;0.8;0.3;0.7;0.2' dur='0.38s' repeatCount='indefinite'/></circle>" &
        "<circle cx='92.5' cy='55' r='1.2' fill='" & c & "'><animate attributeName='opacity' values='0.6;0.2;0.9;0.3;0.6' dur='0.52s' repeatCount='indefinite'/></circle></g>" &
        "<rect x='42' y='42' width='5' height='16' rx='1.5' fill='" & c & "' opacity='0.75'/>" &
        "<path d='M42 43 L24 43 Q13 43.5 7 50 Q13 56.5 24 57 L42 57 Z' fill='" & c & "' fill-opacity='0.5'/>" &
        "<path d='M42 43 L24 43 Q13 43.5 7 50 Q13 56.5 24 57 L42 57 Z' fill='none' stroke='" & c & "' stroke-width='1.8'/>" &
        "<g clip-path='url(#blt)'><g>" &
        "<line x1='-8' y1='60' x2='6' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='-2' y1='60' x2='12' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='4' y1='60' x2='18' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='10' y1='60' x2='24' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='16' y1='60' x2='30' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='22' y1='60' x2='36' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='28' y1='60' x2='42' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='34' y1='60' x2='48' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='40' y1='60' x2='54' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='46' y1='60' x2='60' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<line x1='52' y1='60' x2='66' y2='40' stroke='" & c & "' stroke-width='2.2' stroke-opacity='0.85'/>" &
        "<animateTransform attributeName='transform' type='translate' values='0 0;6 0' dur='0.3s' repeatCount='indefinite'/>" &
        "</g></g>" &
        "</svg>"
    )
)
```

### Turner II

The turning target, now carrying a law enforcement silhouette with center mass scoring rings. Faces, holds, edges away, returns.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='50' y1='80' x2='50' y2='90' stroke='" & c & "' stroke-opacity='0.5' stroke-width='3'/>" &
        "<line x1='40' y1='90' x2='60' y2='90' stroke='" & c & "' stroke-opacity='0.5' stroke-width='3' stroke-linecap='round'/>" &
        "<g transform='translate(50 46)'><g>" &
        "<rect x='-22' y='-33' width='44' height='66' rx='3' fill='none' stroke='" & c & "' stroke-width='2.5'/>" &
        "<circle cx='0' cy='-20.5' r='6.2' fill='" & c & "' fill-opacity='0.3' stroke='" & c & "' stroke-width='1.8'/>" &
        "<path d='M-14.5 33 L-14.5 1 C-14.5 -8.5 -9.5 -12.5 -3.8 -13.6 L3.8 -13.6 C9.5 -12.5 14.5 -8.5 14.5 1 L14.5 33 Z' fill='" & c & "' fill-opacity='0.3' stroke='" & c & "' stroke-width='1.8' stroke-linejoin='round'/>" &
        "<circle cx='0' cy='4' r='9' fill='none' stroke='" & c & "' stroke-width='1.6' stroke-opacity='0.8'/>" &
        "<circle cx='0' cy='4' r='3.4' fill='" & c & "' fill-opacity='0.85'/>" &
        "<animateTransform attributeName='transform' type='scale' values='1 1;1 1;0.045 1;0.045 1;1 1;1 1' keyTimes='0;0.4;0.5;0.62;0.72;1' calcMode='spline' keySplines='0 0 1 1;.6 0 .4 1;0 0 1 1;.6 0 .4 1;0 0 1 1' dur='3.2s' repeatCount='indefinite'/>" &
        "<animate attributeName='opacity' values='1;1;0.45;0.45;1;1' keyTimes='0;0.4;0.5;0.62;0.72;1' dur='3.2s' repeatCount='indefinite'/>" &
        "</g></g>" &
        "</svg>"
    )
)
```

### Notes

- Rifling's helix is a traveling sine wave: each strand's path `d` morphs through five phase keyframes per 0.8s, with the two strands 180 degrees apart and a wide low opacity wisp underneath for the smoke feel. The wave travels rearward, so the trail reads as streaming off the spinning round.
- The bullet's spin is a barber pole: diagonal stripes clipped to the body translate sideways on a 0.3s loop. Stripe travel and wave travel run the same direction so the spin reads as one motion.
- Rifling's Power Fx string is the longest in the collection because the wave keyframes carry 31 points each; it is still just one Image formula and costs nothing at runtime beyond normal SVG rendering.
- Turner II keeps Turner's exact turn cycle and swaps the art: head, rounded shoulder torso, and center mass rings drawn to the B-27 style proportions.


# The canon twenty five

The patterns the web has settled on: Material indeterminate indicators, the platform activity spinners, the SpinKit era classics, skeleton shimmer, and the softer consumer styles, all rebuilt as single SVG strings with Material easing where it belongs. Delivery as always: Image control, `ImagePosition.Fit`, square control (MD Linear and Shimmer also work in wide controls), `c` swapped for your theme accent.

### MD Circular

The Material indeterminate circular: the arc grows while it rotates, collapses from the tail, and never lands in the same place twice.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g><circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-width='7' stroke-linecap='round' stroke-dasharray='2 237'>" &
        "<animate attributeName='stroke-dasharray' values='2 237;130 107;2 237' keyTimes='0;0.5;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='1.4s' repeatCount='indefinite'/>" &
        "<animate attributeName='stroke-dashoffset' values='0;-50;-236' keyTimes='0;0.5;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='1.4s' repeatCount='indefinite'/>" &
        "</circle><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='2s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### MD Linear

The Material indeterminate linear: two bars chase across the track on offset clocks, one long, one short.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><clipPath id='mlc'><rect x='8' y='46' width='84' height='8' rx='4'/></clipPath></defs>" &
        "<rect x='8' y='47' width='84' height='6' rx='3' fill='" & c & "' opacity='0.15'/>" &
        "<g clip-path='url(#mlc)'>" &
        "<rect x='-25' y='47' width='25' height='6' rx='3' fill='" & c & "'><animate attributeName='x' values='-25;15;95' keyTimes='0;0.45;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='2s' repeatCount='indefinite'/><animate attributeName='width' values='25;55;30' keyTimes='0;0.45;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='2s' repeatCount='indefinite'/></rect>" &
        "<rect x='-35' y='47' width='35' height='6' rx='3' fill='" & c & "'><animate attributeName='x' values='-35;25;95' keyTimes='0;0.5;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='2s' begin='-1s' repeatCount='indefinite'/><animate attributeName='width' values='35;40;20' keyTimes='0;0.5;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1' dur='2s' begin='-1s' repeatCount='indefinite'/></rect>" &
        "</g>" &
        "</svg>"
    )
)
```

### Quad

Four arc segments in stepped opacities snap around a quarter turn at a time with Material easing. A single hue take on the quantum spinner.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g>" &
        "<path d='M52.5 14.1 A36 36 0 0 1 85.9 47.5' fill='none' stroke='" & c & "' stroke-opacity='1.00' stroke-width='7' stroke-linecap='round'/>" &
        "<path d='M85.9 52.5 A36 36 0 0 1 52.5 85.9' fill='none' stroke='" & c & "' stroke-opacity='0.76' stroke-width='7' stroke-linecap='round'/>" &
        "<path d='M47.5 85.9 A36 36 0 0 1 14.1 52.5' fill='none' stroke='" & c & "' stroke-opacity='0.52' stroke-width='7' stroke-linecap='round'/>" &
        "<path d='M14.1 47.5 A36 36 0 0 1 47.5 14.1' fill='none' stroke='" & c & "' stroke-opacity='0.28' stroke-width='7' stroke-linecap='round'/>" &
        "<animateTransform attributeName='transform' type='rotate' values='0 50 50;90 50 50;180 50 50;270 50 50;360 50 50' keyTimes='0;0.25;0.5;0.75;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1;.4 0 .2 1;.4 0 .2 1' dur='2.2s' repeatCount='indefinite'/>" &
        "</g>" &
        "</svg>"
    )
)
```

### Spokes

Twelve spokes fading in sequence. The activity indicator every platform understands at a glance.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<line x1='50.0' y1='34.0' x2='50.0' y2='19.0' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-1.000s' repeatCount='indefinite'/></line>" &
        "<line x1='58.0' y1='36.1' x2='65.5' y2='23.2' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.917s' repeatCount='indefinite'/></line>" &
        "<line x1='63.9' y1='42.0' x2='76.8' y2='34.5' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.833s' repeatCount='indefinite'/></line>" &
        "<line x1='66.0' y1='50.0' x2='81.0' y2='50.0' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.750s' repeatCount='indefinite'/></line>" &
        "<line x1='63.9' y1='58.0' x2='76.8' y2='65.5' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.667s' repeatCount='indefinite'/></line>" &
        "<line x1='58.0' y1='63.9' x2='65.5' y2='76.8' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.583s' repeatCount='indefinite'/></line>" &
        "<line x1='50.0' y1='66.0' x2='50.0' y2='81.0' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.500s' repeatCount='indefinite'/></line>" &
        "<line x1='42.0' y1='63.9' x2='34.5' y2='76.8' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.417s' repeatCount='indefinite'/></line>" &
        "<line x1='36.1' y1='58.0' x2='23.2' y2='65.5' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.333s' repeatCount='indefinite'/></line>" &
        "<line x1='34.0' y1='50.0' x2='19.0' y2='50.0' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.250s' repeatCount='indefinite'/></line>" &
        "<line x1='36.1' y1='42.0' x2='23.2' y2='34.5' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.167s' repeatCount='indefinite'/></line>" &
        "<line x1='42.0' y1='36.1' x2='34.5' y2='23.2' stroke='" & c & "' stroke-width='5' stroke-linecap='round' opacity='0.15'><animate attributeName='opacity' values='1;0.15' dur='1s' begin='-0.083s' repeatCount='indefinite'/></line>" &
        "</svg>"
    )
)
```

### Orbit Fade

A ring of dots with a brightness wave running around it, head sharp and tail long.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50.0' cy='17.0' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-1.100s' repeatCount='indefinite'/></circle>" &
        "<circle cx='66.5' cy='21.4' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-1.008s' repeatCount='indefinite'/></circle>" &
        "<circle cx='78.6' cy='33.5' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.917s' repeatCount='indefinite'/></circle>" &
        "<circle cx='83.0' cy='50.0' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.825s' repeatCount='indefinite'/></circle>" &
        "<circle cx='78.6' cy='66.5' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.733s' repeatCount='indefinite'/></circle>" &
        "<circle cx='66.5' cy='78.6' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.642s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50.0' cy='83.0' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.550s' repeatCount='indefinite'/></circle>" &
        "<circle cx='33.5' cy='78.6' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.458s' repeatCount='indefinite'/></circle>" &
        "<circle cx='21.4' cy='66.5' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.367s' repeatCount='indefinite'/></circle>" &
        "<circle cx='17.0' cy='50.0' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.275s' repeatCount='indefinite'/></circle>" &
        "<circle cx='21.4' cy='33.5' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.183s' repeatCount='indefinite'/></circle>" &
        "<circle cx='33.5' cy='21.4' r='4' fill='" & c & "' opacity='0.1'><animate attributeName='opacity' values='1;0.1;0.1' keyTimes='0;0.55;1' dur='1.1s' begin='-0.092s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Chase

Three dots chase around the ring, slowing into the curve and whipping out of it while they pulse in size.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g>" &
        "<circle cx='50.0' cy='20.0' r='5' fill='" & c & "'><animate attributeName='r' values='3.4;6;3.4' dur='1.3s' begin='-0.00s' repeatCount='indefinite'/></circle>" &
        "<circle cx='76.0' cy='65.0' r='5' fill='" & c & "'><animate attributeName='r' values='3.4;6;3.4' dur='1.3s' begin='-0.43s' repeatCount='indefinite'/></circle>" &
        "<circle cx='24.0' cy='65.0' r='5' fill='" & c & "'><animate attributeName='r' values='3.4;6;3.4' dur='1.3s' begin='-0.86s' repeatCount='indefinite'/></circle>" &
        "<animateTransform attributeName='transform' type='rotate' values='0 50 50;80 50 50;360 50 50' keyTimes='0;0.55;1' calcMode='spline' keySplines='.45 0 .75 .35;.25 .65 .55 1' dur='1.3s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Double Bounce

Two soft discs grow through each other in opposite phase. A classic that still reads calm and modern.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='6' fill='" & c & "' opacity='0.5'><animate attributeName='r' values='4;32;4' dur='2s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.55;0.12;0.55' dur='2s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='20' fill='" & c & "' opacity='0.3'><animate attributeName='r' values='32;4;32' dur='2s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.12;0.55;0.12' dur='2s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Ping

One crisp radar ping: a ring accelerates outward and dissolves while the center dot holds steady.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='7' fill='" & c & "'/>" &
        "<circle cx='50' cy='50' r='10' fill='none' stroke='" & c & "' stroke-width='3'><animate attributeName='r' values='9;38' dur='1.3s' calcMode='spline' keySplines='.1 .5 .3 1' repeatCount='indefinite'/><animate attributeName='opacity' values='0.8;0' dur='1.3s' calcMode='spline' keySplines='.1 .5 .3 1' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Ellipsis

The typing indicator: three dots hop and brighten left to right. Best for chat-like or conversational surfaces.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='34' cy='52' r='5.5' fill='" & c & "' opacity='0.25'><animate attributeName='opacity' values='0.25;1;0.25' dur='1.2s' begin='-1.20s' repeatCount='indefinite'/><animate attributeName='cy' values='52;46;52' keyTimes='0;0.3;0.6' dur='1.2s' begin='-1.20s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='52' r='5.5' fill='" & c & "' opacity='0.25'><animate attributeName='opacity' values='0.25;1;0.25' dur='1.2s' begin='-1.02s' repeatCount='indefinite'/><animate attributeName='cy' values='52;46;52' keyTimes='0;0.3;0.6' dur='1.2s' begin='-1.02s' repeatCount='indefinite'/></circle>" &
        "<circle cx='66' cy='52' r='5.5' fill='" & c & "' opacity='0.25'><animate attributeName='opacity' values='0.25;1;0.25' dur='1.2s' begin='-0.84s' repeatCount='indefinite'/><animate attributeName='cy' values='52;46;52' keyTimes='0;0.3;0.6' dur='1.2s' begin='-0.84s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Elastic

Three dots inflate with a visible overshoot and settle before shrinking. The overshoot is what makes it feel designed.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='30' cy='50' r='3.5' fill='" & c & "'><animate attributeName='r' values='3.5;7.4;6;6.5;3.5' keyTimes='0;0.3;0.45;0.55;1' dur='1.4s' begin='-0.00s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='3.5' fill='" & c & "'><animate attributeName='r' values='3.5;7.4;6;6.5;3.5' keyTimes='0;0.3;0.45;0.55;1' dur='1.4s' begin='-0.16s' repeatCount='indefinite'/></circle>" &
        "<circle cx='70' cy='50' r='3.5' fill='" & c & "'><animate attributeName='r' values='3.5;7.4;6;6.5;3.5' keyTimes='0;0.3;0.45;0.55;1' dur='1.4s' begin='-0.32s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Wave

Seven slim bars ride one smooth sine. Denser and softer than a bounce equalizer.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<rect x='17.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.00s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.00s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='27.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.10s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.10s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='37.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.20s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.20s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='47.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.30s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.30s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='57.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.40s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.40s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='67.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.50s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.50s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "<rect x='77.5' y='36' width='5' height='28' rx='2.5' fill='" & c & "'><animate attributeName='y' values='40;26;40' dur='1.1s' begin='-0.60s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/><animate attributeName='height' values='20;48;20' dur='1.1s' begin='-0.60s' repeatCount='indefinite' calcMode='spline' keyTimes='0;0.5;1' keySplines='.42 0 .58 1;.42 0 .58 1'/></rect>" &
        "</svg>"
    )
)
```

### Flip

One square flips on alternating axes with a dim at each turn, like a card showing its faces in order.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g transform='translate(50 50)'><g>" &
        "<rect x='-15' y='-15' width='30' height='30' rx='4' fill='" & c & "'><animate attributeName='fill-opacity' values='1;0.55;1;1;0.55;1;1' keyTimes='0;0.15;0.3;0.5;0.65;0.8;1' dur='2.4s' repeatCount='indefinite'/></rect>" &
        "<animateTransform attributeName='transform' type='scale' values='1 1;0 1;1 1;1 1;1 0;1 1;1 1' keyTimes='0;0.15;0.3;0.5;0.65;0.8;1' calcMode='spline' keySplines='.4 0 .2 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1;.4 0 .2 1;0 0 1 1' dur='2.4s' repeatCount='indefinite'/>" &
        "</g></g>" &
        "</svg>"
    )
)
```

### Folding

Four tiles vanish and refold clockwise, half a cycle apart, echoing the folding cube family.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g transform='translate(40.75 40.75)'><rect x='-8.6' y='-8.6' width='17.2' height='17.2' rx='2' fill='" & c & "'><animate attributeName='fill-opacity' values='1;1;0.5;0.5;1;1' keyTimes='0;0.02;0.12;0.52;0.62;1' dur='2.4s' repeatCount='indefinite'/></rect><animateTransform attributeName='transform' type='scale' values='1 1;1 1;0 0;0 0;1 1;1 1' keyTimes='0;0.02;0.12;0.52;0.62;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1;0 0 1 1' dur='2.4s' repeatCount='indefinite' additive='sum'/></g>" &
        "<g transform='translate(59.25 40.75)'><rect x='-8.6' y='-8.6' width='17.2' height='17.2' rx='2' fill='" & c & "'><animate attributeName='fill-opacity' values='1;1;0.5;0.5;1;1' keyTimes='0;0.13;0.23;0.63;0.73;1' dur='2.4s' repeatCount='indefinite'/></rect><animateTransform attributeName='transform' type='scale' values='1 1;1 1;0 0;0 0;1 1;1 1' keyTimes='0;0.13;0.23;0.63;0.73;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1;0 0 1 1' dur='2.4s' repeatCount='indefinite' additive='sum'/></g>" &
        "<g transform='translate(59.25 59.25)'><rect x='-8.6' y='-8.6' width='17.2' height='17.2' rx='2' fill='" & c & "'><animate attributeName='fill-opacity' values='1;1;0.5;0.5;1;1' keyTimes='0;0.24;0.34;0.74;0.84;1' dur='2.4s' repeatCount='indefinite'/></rect><animateTransform attributeName='transform' type='scale' values='1 1;1 1;0 0;0 0;1 1;1 1' keyTimes='0;0.24;0.34;0.74;0.84;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1;0 0 1 1' dur='2.4s' repeatCount='indefinite' additive='sum'/></g>" &
        "<g transform='translate(40.75 59.25)'><rect x='-8.6' y='-8.6' width='17.2' height='17.2' rx='2' fill='" & c & "'><animate attributeName='fill-opacity' values='1;1;0.5;0.5;1;1' keyTimes='0;0.35;0.45;0.85;0.95;1' dur='2.4s' repeatCount='indefinite'/></rect><animateTransform attributeName='transform' type='scale' values='1 1;1 1;0 0;0 0;1 1;1 1' keyTimes='0;0.35;0.45;0.85;0.95;1' calcMode='spline' keySplines='0 0 1 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1;0 0 1 1' dur='2.4s' repeatCount='indefinite' additive='sum'/></g>" &
        "</svg>"
    )
)
```

### Carousel

Page dots with the emphasis gliding along the row. Familiar from every onboarding flow ever shipped.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='26' cy='50' r='3' fill='" & c & "' opacity='0.35'><animate attributeName='r' values='3;5.6;3' dur='1.5s' begin='-1.50s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-1.50s' repeatCount='indefinite'/></circle>" &
        "<circle cx='38' cy='50' r='3' fill='" & c & "' opacity='0.35'><animate attributeName='r' values='3;5.6;3' dur='1.5s' begin='-1.20s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-1.20s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='3' fill='" & c & "' opacity='0.35'><animate attributeName='r' values='3;5.6;3' dur='1.5s' begin='-0.90s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.90s' repeatCount='indefinite'/></circle>" &
        "<circle cx='62' cy='50' r='3' fill='" & c & "' opacity='0.35'><animate attributeName='r' values='3;5.6;3' dur='1.5s' begin='-0.60s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.60s' repeatCount='indefinite'/></circle>" &
        "<circle cx='74' cy='50' r='3' fill='" & c & "' opacity='0.35'><animate attributeName='r' values='3;5.6;3' dur='1.5s' begin='-0.30s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.35;1;0.35' dur='1.5s' begin='-0.30s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Hourglass

An hourglass drains, flips with a snap, and drains again, with the fills swapping exactly as physics says they should.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g>" &
        "<path d='M32 20 L68 20 L54 50 L68 80 L32 80 L46 50 Z' fill='none' stroke='" & c & "' stroke-width='3' stroke-linejoin='round'/>" &
        "<path d='M38 26 L62 26 L50 47 Z' fill='" & c & "'><animate attributeName='fill-opacity' values='0.9;0.15;0.15;0.9;0.9' keyTimes='0;0.42;0.5;0.92;1' dur='2.6s' repeatCount='indefinite'/></path>" &
        "<path d='M50 53 L63 76 L37 76 Z' fill='" & c & "'><animate attributeName='fill-opacity' values='0.15;0.9;0.9;0.15;0.15' keyTimes='0;0.42;0.5;0.92;1' dur='2.6s' repeatCount='indefinite'/></path>" &
        "<animateTransform attributeName='transform' type='rotate' values='0 50 50;0 50 50;180 50 50;180 50 50;360 50 50' keyTimes='0;0.42;0.5;0.92;1' calcMode='spline' keySplines='0 0 1 1;.5 0 .3 1;0 0 1 1;.5 0 .3 1' dur='2.6s' repeatCount='indefinite'/>" &
        "</g>" &
        "</svg>"
    )
)
```

### Bounce

A ball falls with gravity, squashes on impact, and recovers, while its shadow breathes underneath. Animation principles 101.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<ellipse cx='50' cy='79' rx='8' ry='2.5' fill='" & c & "' opacity='0.2'><animate attributeName='rx' values='4;11;4' keyTimes='0;0.5;1' dur='0.95s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.08;0.3;0.08' keyTimes='0;0.5;1' dur='0.95s' repeatCount='indefinite'/></ellipse>" &
        "<ellipse cx='50' cy='30' rx='9' ry='9' fill='" & c & "'><animate attributeName='cy' values='28;67;71;67;28' keyTimes='0;0.46;0.5;0.54;1' calcMode='spline' keySplines='.33 0 .66 .33;0 0 1 1;0 0 1 1;.33 .66 .66 1' dur='0.95s' repeatCount='indefinite'/><animate attributeName='ry' values='9;9;5.5;9;9' keyTimes='0;0.46;0.5;0.54;1' dur='0.95s' repeatCount='indefinite'/><animate attributeName='rx' values='9;9;11.5;9;9' keyTimes='0;0.46;0.5;0.54;1' dur='0.95s' repeatCount='indefinite'/></ellipse>" &
        "</svg>"
    )
)
```

### Shimmer

Skeleton rows with a light band sweeping through. The pattern users now read as content on its way, not failure.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><linearGradient id='shg' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='" & c & "' stop-opacity='0'/><stop offset='0.5' stop-color='" & c & "' stop-opacity='0.45'/><stop offset='1' stop-color='" & c & "' stop-opacity='0'/></linearGradient>" &
        "<clipPath id='shk'><rect x='14' y='30' width='72' height='8' rx='4'/><rect x='14' y='46' width='56' height='8' rx='4'/><rect x='14' y='62' width='64' height='8' rx='4'/></clipPath></defs>" &
        "<rect x='14' y='30' width='72' height='8' rx='4' fill='" & c & "' opacity='0.15'/>" &
        "<rect x='14' y='46' width='56' height='8' rx='4' fill='" & c & "' opacity='0.15'/>" &
        "<rect x='14' y='62' width='64' height='8' rx='4' fill='" & c & "' opacity='0.15'/>" &
        "<g clip-path='url(#shk)'><rect x='0' y='26' width='26' height='50' fill='url(#shg)'><animate attributeName='x' values='-28;102' dur='1.5s' repeatCount='indefinite'/></rect></g>" &
        "</svg>"
    )
)
```

### Pie

A disc fills like a pie chart sweeping to full, then blinks clean and starts over. Reads as progress even when it is not.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='40' fill='none' stroke='" & c & "' stroke-opacity='0.12' stroke-width='4'/>" &
        "<circle cx='50' cy='50' r='20' fill='none' stroke='" & c & "' stroke-width='40' transform='rotate(-90 50 50)' stroke-dasharray='0.5 126'><animate attributeName='stroke-dasharray' values='0.5 126;125.7 0;125.7 0;0.5 126' keyTimes='0;0.5;0.88;1' dur='2.4s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.8;0.8;0.8;0;0.8' keyTimes='0;0.5;0.86;0.93;1' dur='2.4s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Segments

Eight ring segments light clockwise until the circle completes, then clear together. Stepped progress without numbers.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M52.5 14.1 A36 36 0 0 1 73.6 22.8' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;1;1;0.15' keyTimes='0;0.04;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M77.2 26.4 A36 36 0 0 1 85.9 47.5' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.125;0.165;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M85.9 52.5 A36 36 0 0 1 77.2 73.6' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.250;0.290;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M73.6 77.2 A36 36 0 0 1 52.5 85.9' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.375;0.415;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M47.5 85.9 A36 36 0 0 1 26.4 77.2' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.500;0.540;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M22.8 73.6 A36 36 0 0 1 14.1 52.5' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.625;0.665;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M14.1 47.5 A36 36 0 0 1 22.8 26.4' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.750;0.790;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "<path d='M26.4 22.8 A36 36 0 0 1 47.5 14.1' fill='none' stroke='" & c & "' stroke-opacity='0.15' stroke-width='6' stroke-linecap='round'><animate attributeName='stroke-opacity' values='0.15;0.15;1;1;0.15' keyTimes='0;0.875;0.915;0.9;1' dur='2.4s' repeatCount='indefinite'/></path>" &
        "</svg>"
    )
)
```

### Blob

An organic blob rolls through shapes while slowly rotating. The friendly end of the spectrum, popular in consumer apps.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g><path d='M50 20.0 C66.6 20.0 75.0 36.2 75.0 50 C75.0 63.8 66.0 79.0 50 79.0 C34.0 79.0 17.0 68.2 17.0 50 C17.0 31.8 33.4 20.0 50 20.0 Z' fill='" & c & "' fill-opacity='0.8'><animate attributeName='d' values='M50 20.0 C66.6 20.0 75.0 36.2 75.0 50 C75.0 63.8 66.0 79.0 50 79.0 C34.0 79.0 17.0 68.2 17.0 50 C17.0 31.8 33.4 20.0 50 20.0 Z;M50 25.0 C63.8 25.0 81.0 32.9 81.0 50 C81.0 67.1 63.2 74.0 50 74.0 C36.8 74.0 21.0 66.0 21.0 50 C21.0 34.0 36.2 25.0 50 25.0 Z;M50 19.0 C67.1 19.0 77.0 35.1 77.0 50 C77.0 64.9 68.2 83.0 50 83.0 C31.8 83.0 25.0 63.8 25.0 50 C25.0 36.2 32.9 19.0 50 19.0 Z;M50 23.0 C64.9 23.0 83.0 31.8 83.0 50 C83.0 68.2 64.4 76.0 50 76.0 C35.6 76.0 19.0 67.1 19.0 50 C19.0 32.9 35.1 23.0 50 23.0 Z;M50 20.0 C66.6 20.0 75.0 36.2 75.0 50 C75.0 63.8 66.0 79.0 50 79.0 C34.0 79.0 17.0 68.2 17.0 50 C17.0 31.8 33.4 20.0 50 20.0 Z' keyTimes='0;0.25;0.5;0.75;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1' dur='3.2s' repeatCount='indefinite'/></path>" &
        "<animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='9s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Metronome

A pendulum bob swings along a faint guide arc with true ease at both ends. Steady, rhythmic, unhurried.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M31.2 63.3 A40 40 0 0 1 68.8 63.3' fill='none' stroke='" & c & "' stroke-opacity='0.18' stroke-width='2'/>" &
        "<g><line x1='50' y1='28' x2='50' y2='64' stroke='" & c & "' stroke-opacity='0.4' stroke-width='1.5'/><circle cx='50' cy='68' r='6' fill='" & c & "'/>" &
        "<animateTransform attributeName='transform' type='rotate' values='-28 50 28;28 50 28;-28 50 28' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.7s' repeatCount='indefinite'/></g>" &
        "<circle cx='50' cy='28' r='2.5' fill='" & c & "' fill-opacity='0.6'/>" &
        "</svg>"
    )
)
```

### Swap

Two unequal dots trade places with a snap, rest, and trade back. Minimal enough for tight corners of the UI.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<g><circle cx='38' cy='50' r='5.5' fill='" & c & "'/><circle cx='62' cy='50' r='3.8' fill='" & c & "' fill-opacity='0.55'/>" &
        "<animateTransform attributeName='transform' type='rotate' values='0 50 50;180 50 50;180 50 50;360 50 50;360 50 50' keyTimes='0;0.35;0.5;0.85;1' calcMode='spline' keySplines='.4 0 .2 1;0 0 1 1;.4 0 .2 1;0 0 1 1' dur='1.9s' repeatCount='indefinite'/></g>" &
        "</svg>"
    )
)
```

### Notch

Two segmented rings counter-rotate at constant speed. Quiet, technical, at home in admin consoles.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='38' fill='none' stroke='" & c & "' stroke-width='5' stroke-linecap='round' stroke-dasharray='26 13.8'><animateTransform attributeName='transform' type='rotate' from='0 50 50' to='360 50 50' dur='3.2s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='26' fill='none' stroke='" & c & "' stroke-opacity='0.4' stroke-width='5' stroke-linecap='round' stroke-dasharray='16 11.3'><animateTransform attributeName='transform' type='rotate' from='360 50 50' to='0 50 50' dur='4.2s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Trace

A vitals trace draws itself across the frame and runs off the end. A natural fit for monitoring dashboards.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<path d='M4 55 L26 55 L31 48 L36 55 L44 55 L49 28 L54 74 L59 55 L96 55' fill='none' stroke='" & c & "' stroke-opacity='0.12' stroke-width='2.5' stroke-linejoin='round'/>" &
        "<path d='M4 55 L26 55 L31 48 L36 55 L44 55 L49 28 L54 74 L59 55 L96 55' fill='none' stroke='" & c & "' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round' pathLength='100' stroke-dasharray='32 68'><animate attributeName='stroke-dashoffset' values='132;-68' dur='2.1s' repeatCount='indefinite'/></path>" &
        "</svg>"
    )
)
```

### Breathe

A disc and its halo inhale and exhale on a slow eased cycle. The gentlest possible way to say please wait.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<circle cx='50' cy='50' r='16' fill='none' stroke='" & c & "' stroke-width='2'><animate attributeName='r' values='16;27;16' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='2.6s' repeatCount='indefinite'/><animate attributeName='opacity' values='0.3;0;0.3' keyTimes='0;0.5;1' dur='2.6s' repeatCount='indefinite'/></circle>" &
        "<circle cx='50' cy='50' r='12' fill='" & c & "'><animate attributeName='r' values='12;19;12' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='2.6s' repeatCount='indefinite'/><animate attributeName='fill-opacity' values='0.45;0.9;0.45' keyTimes='0;0.5;1' dur='2.6s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

### Practice notes

- Material easing (cubic bezier .4 0 .2 1) is used on every spinner that starts and stops: MD Circular, MD Linear, Quad, Flip, Folding, Swap. Constant speed spinners (Notch, Spokes) stay linear on purpose; easing a constant rotation makes it look broken.
- Respect duration norms: continuous cycles between 1 and 2 seconds feel responsive; anything under 0.7s reads as anxious. The slow ones here (Breathe, Blob) are for calm full screen waits, not button-level activity.
- Best practice for choosing: skeleton Shimmer for content regions that will fill with layout, a small continuous spinner (MD Circular, Spokes, Notch) for actions, a determinate control (your Percent ring) whenever real progress exists. Avoid two different spinner styles visible at once.
- Delay showing any spinner about 300ms after the action; flashing one for a 100ms load makes the app feel slower than showing nothing.


# Typographic: Loading...

### Wave

The word rides a smooth sine, every letter a beat behind its neighbor.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<text x='13.1' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>L<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.00s' repeatCount='indefinite'/></text>" &
        "<text x='21.3' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>o<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.08s' repeatCount='indefinite'/></text>" &
        "<text x='29.5' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>a<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.16s' repeatCount='indefinite'/></text>" &
        "<text x='37.7' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>d<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.24s' repeatCount='indefinite'/></text>" &
        "<text x='45.9' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>i<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.32s' repeatCount='indefinite'/></text>" &
        "<text x='54.1' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>n<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.40s' repeatCount='indefinite'/></text>" &
        "<text x='62.3' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>g<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.48s' repeatCount='indefinite'/></text>" &
        "<text x='70.5' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>.<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.56s' repeatCount='indefinite'/></text>" &
        "<text x='78.7' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>.<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.64s' repeatCount='indefinite'/></text>" &
        "<text x='86.9' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "'>.<animateTransform attributeName='transform' type='translate' values='0 2;0 -3.5;0 2' keyTimes='0;0.5;1' calcMode='spline' keySplines='.42 0 .58 1;.42 0 .58 1' dur='1.1s' begin='-0.72s' repeatCount='indefinite'/></text>" &
        "</svg>"
    )
)
```

### Type

The word types on letter by letter while an underscore caret hops ahead, then blinks off the line.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<text x='13.1' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>L<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.050;0.060;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='21.3' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>o<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.105;0.115;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='29.5' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>a<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.160;0.170;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='37.7' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>d<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.215;0.225;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='45.9' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>i<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.270;0.280;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='54.1' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>n<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.325;0.335;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='62.3' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>g<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.380;0.390;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='70.5' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>.<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.435;0.445;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='78.7' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>.<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.490;0.500;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<text x='86.9' y='54' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='12.5' font-weight='600' fill='" & c & "' opacity='0'>.<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.545;0.555;0.82;0.9;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></text>" &
        "<rect x='9.5' y='56' width='7' height='2.4' rx='1.2' fill='" & c & "'><animate attributeName='x' values='9.5;17.7;25.9;34.1;42.3;50.5;58.7;66.9;75.1;83.3;91.5;9.5' keyTimes='0;0.105;0.160;0.215;0.270;0.325;0.380;0.435;0.490;0.545;0.66;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/><animate attributeName='opacity' values='1;0.1;1;0.1;1;0.1;1;1' keyTimes='0;0.68;0.72;0.76;0.8;0.84;0.88;1' calcMode='discrete' dur='3s' repeatCount='indefinite'/></rect>" &
        "</svg>"
    )
)
```

### Ants

Marching ants trace the letterforms while the fill breathes underneath.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<text x='50' y='55' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='15' font-weight='600' fill='" & c & "' fill-opacity='0.25'>Loading...<animate attributeName='fill-opacity' values='0.15;0.45;0.15' dur='2.4s' repeatCount='indefinite'/></text>" &
        "<text x='50' y='55' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='15' font-weight='600' fill='none' stroke='" & c & "' stroke-width='0.8' stroke-dasharray='3 3'>Loading...<animate attributeName='stroke-dashoffset' values='0;-24' dur='1.2s' repeatCount='indefinite'/></text>" &
        "</svg>"
    )
)
```

### Shine

A soft light band sweeps through the letters, the skeleton shimmer applied to type.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<defs><linearGradient id='tshg' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='" & c & "' stop-opacity='0'/><stop offset='0.5' stop-color='" & c & "' stop-opacity='0.9'/><stop offset='1' stop-color='" & c & "' stop-opacity='0'/></linearGradient>" &
        "<clipPath id='tclip'><text x='50' y='55' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='15' font-weight='600'>Loading...</text></clipPath></defs>" &
        "<text x='50' y='55' text-anchor='middle' font-family='Segoe UI, Arial, sans-serif' font-size='15' font-weight='600' fill='" & c & "' opacity='0.3'>Loading...</text>" &
        "<g clip-path='url(#tclip)'><rect x='0' y='38' width='26' height='24' fill='url(#tshg)'><animate attributeName='x' values='-28;102' dur='1.7s' repeatCount='indefinite'/></rect></g>" &
        "</svg>"
    )
)
```

### Dots

The word holds still and only the ellipsis works, typing over and over. The most restrained of the fifteen.

```
With(
    {c: "#005EA2"},
    "data:image/svg+xml;utf8, " & EncodeUrl(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>" &
        "<text x='68' y='54' text-anchor='end' font-family='Segoe UI, Arial, sans-serif' font-size='14' font-weight='600' fill='" & c & "'>Loading</text>" &
        "<circle cx='73.5' cy='52' r='2.1' fill='" & c & "' opacity='0.2'><animate attributeName='opacity' values='0.2;1;0.2' dur='1.2s' begin='-1.20s' repeatCount='indefinite'/></circle>" &
        "<circle cx='79.5' cy='52' r='2.1' fill='" & c & "' opacity='0.2'><animate attributeName='opacity' values='0.2;1;0.2' dur='1.2s' begin='-1.02s' repeatCount='indefinite'/></circle>" &
        "<circle cx='85.5' cy='52' r='2.1' fill='" & c & "' opacity='0.2'><animate attributeName='opacity' values='0.2;1;0.2' dur='1.2s' begin='-0.84s' repeatCount='indefinite'/></circle>" &
        "</svg>"
    )
)
```

These five want wide controls (about 3:1). The whole word ones (Ants, Shine, Dots) need only a string edit to change the phrasing; Wave and Type position each letter on fixed slots, so rewording means adjusting the x positions too.

