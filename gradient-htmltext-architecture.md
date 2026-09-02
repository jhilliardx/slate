# Motion-Reactive Gradient Text (Power Apps Canvas)

Architecture for an HtmlText control whose gradient shifts with device motion on mobile, with graceful desktop equivalents. Target: GCC canvas apps, no premium connectors, optional PCF upgrade path.

## Concept

The HTML Text control cannot execute JavaScript, so all reactivity lives in Power Fx. The `Acceleration` signal re-evaluates any formula that references it, which means an HtmlText string built from `Acceleration.X/Y` re-renders as the device tilts. Desktop lacks motion signals, so a Timer (or slider/window-size proxy) substitutes as the animation driver.

```
┌─────────────────────────────────────────────┐
│  Input Layer                                │
│  Mobile: Acceleration signal (X, Y, Z in g) │
│  Desktop: Timer.Value / Slider / App.Width  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  Signal Normalization (named formulas)      │
│  fxIsMobile, fxHue, fxAngle                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  Render Layer                               │
│  HtmlText: CSS linear-gradient +            │
│  background-clip:text, built as Fx string   │
└─────────────────────────────────────────────┘
```

## Components

| Component | Purpose | Notes |
|-----------|---------|-------|
| `htmlGradientText` | Renders the gradient text | HTML Text control, transparent fill |
| `tmrDrift` | Desktop animation driver | Duration 8000, Repeat true, AutoStart true |
| `sldHueProxy` (optional) | Pointer-like interaction on desktop | Transparent, stretched under the text |
| Named formulas (App.Formulas) | Signal normalization | Keeps HtmlText string readable |

## Named Formulas (App.Formulas)

```
fxIsMobile = !(Acceleration.X = 0 && Acceleration.Y = 0 && Acceleration.Z = 0);

fxAngle =
    If(fxIsMobile,
        Round(90 + Acceleration.X * 45, 0),
        Round(tmrDrift.Value / tmrDrift.Duration * 360, 0)
    );

fxHueA =
    If(fxIsMobile,
        Round(Mod(210 + Acceleration.Y * 80, 360), 0),
        Round(Mod(tmrDrift.Value / tmrDrift.Duration * 360, 360), 0)
    );

fxHueB = Round(Mod(fxHueA + 120, 360), 0);
```

Caveats:
- Named formulas referencing controls (tmrDrift) work but couple App.Formulas to screen controls. If that bothers you, use `With()` inside the HtmlText instead, or a global variable set by tmrDrift.OnTimerEnd is not needed since Value is read live.
- `fxIsMobile` uses "all axes are exactly zero" as the browser tell. On a real device at rest, Z reads about -1 g (gravity), so this is a reliable discriminator.

## HtmlText Property

```
"<div style='
  font-size:" & Text(Self.Height * 0.5) & "px;
  font-weight:800;
  font-family:Segoe UI, sans-serif;
  background:linear-gradient(" & Text(fxAngle) & "deg,
    hsl(" & Text(fxHueA) & " 85% 60%),
    hsl(" & Text(fxHueB) & " 85% 60%));
  -webkit-background-clip:text;
  background-clip:text;
  color:transparent;
  line-height:1.1;'>" &
  varDisplayText &
"</div>"
```

## Input Behaviors by Platform

| Driver | Platform | Feel | Effort |
|--------|----------|------|--------|
| `Acceleration.X/Y` | Mobile player | Tilt shifts angle + hue | Free |
| Timer drift | Desktop browser | Slow ambient hue cycle | 1 control |
| Transparent slider | Desktop | Drag-to-shift, closest to physical interaction | 1 control |
| `App.Width` | Desktop | Resize/snap shifts hue | Zero controls, gimmick tier |

Slider variant: replace the desktop branch of `fxHueA` with `sldHueProxy.Value` mapped 0-360.

## Tuning Constants

- `* 45` on angle: degrees of gradient rotation per g of tilt. Raise for twitchier response.
- `* 80` on hue: hue degrees per g. 80 gives a noticeable but not seasick shift across a comfortable tilt range.
- Base hues 210/330: blue-to-pink at rest. Change to taste.
- Timer 8000 ms: full hue rotation every 8 s on desktop.

## Known Limitations

1. Signal tick rate: HtmlText re-renders on Power Fx recalcs, not per frame. Motion response is steppy, not fluid.
2. `Acceleration` returns zeros in browser preview and desktop browsers, hence the fallback branch.
3. `background-clip:text` requires the `-webkit-` prefix in the Power Apps webview; include both prefixed and unprefixed.
4. HtmlText sanitizes some HTML; inline styles on a div are safe, script/iframe are stripped.
5. GCC consideration: none, this is all client-side and connector-free.

## PCF Upgrade Path (v2)

If the steppy rendering grates, a PCF control gives true parity:

- Listen to `devicemotion` (mobile) and `mousemove` (desktop) natively.
- Render via `requestAnimationFrame` with lerped hue values for per-frame smoothness.
- Expose input properties: `text`, `baseHueA`, `baseHueB`, `sensitivity`, `fallbackMode`.
- Expose output property: current hue, if other controls should react in sync.
- Standard control (no dataset), virtual control template for React if desired.
- GCC: confirm PCF component framework is enabled in the environment (`PowerApps component framework for canvas apps` setting), same as your existing PCF work.

## Build Checklist

- [ ] Add tmrDrift (Duration 8000, Repeat, AutoStart, Visible false)
- [ ] Add named formulas to App.Formulas
- [ ] Add htmlGradientText, paste HtmlText property, set varDisplayText
- [ ] Test in browser (should drift), test in mobile player (should tilt-shift)
- [ ] Tune sensitivity constants
- [ ] Optional: slider proxy variant
- [ ] Optional: spec out PCF v2 if smoothness matters
