# Power Apps Innovation Master File

**Owner:** Justin Hilliard, HCT (Human Capital & Training), USBP HQ
**Solution prefix:** `usbpmsd`
**Audience:** Internal LLM build agent (Wolfkrow / Roundtable) and human developers
**Version:** 1.0, 2026-09-03

---

## 0. How to use this file

This file is a build catalog. Each entry is self-contained and follows the same structure so an LLM agent can be pointed at a single entry and produce a working implementation.

Entry structure:

- **What it is** (one paragraph)
- **Why it matters** (the operational payoff)
- **Constraints check** (does it fit the environment below)
- **Data model** (lists, tables, columns)
- **Build steps** (ordered, concrete)
- **Key formulas** (Power Fx, ready to paste and adapt)
- **Flows** (if any, described as trigger, actions, outputs)
- **Gotchas**
- **Done when** (acceptance criteria)

### 0.1 Environment constraints (hard rules)

The build agent MUST honor these for every entry:

| Rule | Detail |
|---|---|
| Tenant | CBP GCC (Government Community Cloud). Assume connector availability lags commercial. |
| PCF | NOT available. No code components. Every visual must be built from standard controls, HTML text, Image (SVG data URI), and components. |
| Licensing | Default to standard connectors only (SharePoint, Office 365 Users, Office 365 Outlook, OneDrive, Teams, Approvals). Dataverse is allowed only where the entry explicitly says so and the target app already has a premium justification. |
| Environment | Single Prod environment. No dev/test. Every entry must be safe to deploy dark (feature flag) and must not break existing screens on publish. |
| ALM | Build inside a Dataverse solution under prefix `usbpmsd` even when the data source is SharePoint. Solutions do not trigger premium licensing; Dataverse tables as a data source do. |
| Source control | No GitHub in the CBP environment. Export solutions to OneDrive on a schedule (see entry 19). |
| Naming | Office is always referred to as HCT (Human Capital & Training). |
| Theming | All new screens and components consume the existing multi-brand theme architecture (CBP, OFO, USBP, AMO, light and dark). Never hardcode colors. |
| Harness | Follow the Power Apps Principal Engineer harness v2.1: log architectural decisions to the decision log, log shortcuts to the debt register. |

### 0.2 Shared conventions

**Global theme record.** Every app has `gblTheme` set in `App.OnStart` or `App.Formulas`:

```
// App.Formulas
gblTheme = LookUp(colThemes, Brand = gblBrand && Mode = gblMode);
```

`gblTheme` exposes at minimum: `Primary, PrimaryText, Surface, SurfaceAlt, Border, Success, Warning, Danger, Info, FontFamily, Radius`.

**Global context record.** UI state lives in one record so screens and components can share it:

```
Set(gblUI, {
    activeModal: Blank(),
    toastQueue: [],
    busy: false,
    lastAction: Blank(),
    selectedRecordId: Blank()
});
```

Update with `Set(gblUI, Patch(gblUI, {busy: true}))` so unrelated properties survive.

**Named formulas over OnStart.** Prefer `App.Formulas` for anything derivable. Reserve `OnStart` for loads that must run once.

**Collections prefix:** `col`. **Global variables:** `gbl`. **Context variables:** `loc`. **Components:** `cmp`. **Screens:** `scr`.

**Every Patch goes through one wrapper pattern** (see entry 41 and 42, which depend on this):

```
// Instead of raw Patch(Source, Record, Changes)
// use the CRUD wrapper pattern:
Set(gblCrud, {source: "Enrollments", op: "Update", id: ThisItem.ID, before: ThisItem});
Patch(Enrollments, ThisItem, {Status: "Cancelled"});
Set(gblCrud, Patch(gblCrud, {after: LookUp(Enrollments, ID = ThisItem.ID), result: "OK"}));
Select(btnLogCrud); // hidden button that writes the audit row
```

### 0.3 Deployment safety pattern (applies to every entry)

1. Add a row to the `FeatureFlags` list (entry 13) named after the entry, `Enabled = false`.
2. Wrap new screen entry points and new UI in `Visible: fxFlag("EntryName")`.
3. Publish.
4. Flip the flag for the developer account only, verify in Prod.
5. Flip for a pilot group, then everyone.

```
// App.Formulas
fxFlag = ... // see entry 13 for the definition
```

---

## Part A. Controls and elements

### 1. HTML text control as a rendering engine

**What it is.** The HTML text control renders inline SVG. Any visual that can be described as SVG (sparklines, gauges, heatmaps, Gantt bars, org charts, progress rings) can be generated from a `Concat()` over a collection and dropped into the control. This replaces most PCF use cases.

**Why it matters.** PCF is unavailable. This is the single most important unlock in the catalog; entries 2, 20, 27, 36 all depend on it.

**Constraints check.** Fully standard. No connectors involved.

**Data model.** None. Input is any collection.

**Build steps.**

1. Insert an HTML text control `htmChart`. Set `AutoHeight = false`, fixed `Width` and `Height`.
2. Build the SVG string in a named formula or a `With()` block.
3. Set `htmChart.HtmlText` to the string.
4. Wrap in a component (entry 4 pattern) with input properties `Data`, `Width`, `Height`, `Color`.

**Key formulas.**

Sparkline from a table of numbers:

```
With(
    {
        pts: ForAll(Sequence(CountRows(colSeries)),
            With({v: Last(FirstN(colSeries, Value)).Value},
                {x: (Value - 1) * (Parent.Width / (CountRows(colSeries) - 1)),
                 y: Parent.Height - (v / Max(colSeries, Value)) * Parent.Height}
            )
        )
    },
    "<svg xmlns='http://www.w3.org/2000/svg' width='" & Parent.Width & "' height='" & Parent.Height & "'>" &
    "<polyline fill='none' stroke='" & gblTheme.Primary & "' stroke-width='2' points='" &
    Concat(pts, x & "," & y, " ") &
    "'/></svg>"
)
```

Progress ring:

```
With({r: 40, c: 2 * Pi() * 40, pct: locPercent},
    "<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'>" &
    "<circle cx='50' cy='50' r='" & r & "' fill='none' stroke='" & gblTheme.Border & "' stroke-width='8'/>" &
    "<circle cx='50' cy='50' r='" & r & "' fill='none' stroke='" & gblTheme.Primary & "' stroke-width='8' " &
    "stroke-dasharray='" & c & "' stroke-dashoffset='" & c * (1 - pct) & "' transform='rotate(-90 50 50)'/>" &
    "<text x='50' y='56' text-anchor='middle' font-size='18' fill='" & gblTheme.PrimaryText & "'>" & Round(pct * 100, 0) & "%</text>" &
    "</svg>"
)
```

**Gotchas.**
- The HTML text control sanitizes some attributes. `onclick` and `<script>` are stripped. No interactivity inside the SVG; put clickable regions as transparent buttons over the control.
- Use single quotes inside the SVG so the Power Fx string can use double quotes.
- Very large SVG strings (thousands of elements) slow rendering. Aggregate first.
- Colors must come from `gblTheme`.

**Done when.** A component `cmpSparkline` accepts a table and renders correctly in light and dark for all four brands.

---

### 2. SVG-in-Image control

**What it is.** The Image control accepts a data URI. `"data:image/svg+xml;utf8," & EncodeUrl(svg)` makes it a vector renderer. Best for icons, badges, and anything that must scale crisply or be used in a gallery where HTML text is heavy.

**Why it matters.** Image control is lighter than HTML text in galleries with many rows, supports `ImagePosition`, and can be used as a button's icon.

**Constraints check.** Fully standard.

**Build steps.**

1. Create a named formula per icon in `App.Formulas`, parameterized by color via `Substitute`.
2. Set `Image.Image` to the data URI.

**Key formulas.**

```
// App.Formulas
svgCheck = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path fill='COLOR' d='M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z'/></svg>";

fxIcon(svg: Text, color: Text): Text = "data:image/svg+xml;utf8," & EncodeUrl(Substitute(svg, "COLOR", color));

// Usage
Image: fxIcon(svgCheck, gblTheme.Success)
```

QR code: generate server-side via a Flow that calls no external service. Simpler alternative that stays in-tenant: build a QR matrix with a Flow using a known algorithm is heavy; instead, for classroom check-in (entry 31), encode a short numeric code as a large barcode-style SVG, or use the Barcode Reader control on the student side scanning a printed QR generated once by an HCT admin from an approved internal tool. Record the choice in the decision log.

**Gotchas.**
- `EncodeUrl` is required; unencoded `#` in hex colors breaks the URI.
- Some GCC browsers cache the data URI aggressively. Append a harmless comment with a version number to bust it.

**Done when.** A `fxIcon` library of at least 20 icons exists in the theme component library (entry 37).

---

### 3. Timeline scrubber from a slider

**What it is.** A Slider whose value maps to a date, with a gallery filtered live to that date or a window around it. Feels like scrubbing video across the training calendar.

**Why it matters.** Organizers looking at a quarter want to "drag through time" rather than click month arrows.

**Constraints check.** Standard. Filtering happens on a local collection to avoid delegation issues.

**Data model.** Uses existing `TrainingEvents` list (Title, StartDate, EndDate, TrainingType, Sector, Station, InstructorEmail, RoomId, Capacity, Status).

**Build steps.**

1. Load the visible quarter into `colEvents` on screen visible.
2. Insert `sldTime` with `Min = 0`, `Max = DateDiff(locRangeStart, locRangeEnd, TimeUnit.Days)`.
3. Add label showing `DateAdd(locRangeStart, sldTime.Value, TimeUnit.Days)`.
4. Gallery `Items` filters `colEvents` to the window.

**Key formulas.**

```
// Screen.OnVisible
UpdateContext({locRangeStart: Date(Year(Today()), Month(Today()) - 1, 1)});
UpdateContext({locRangeEnd: DateAdd(locRangeStart, 90, TimeUnit.Days)});
ClearCollect(colEvents, Filter(TrainingEvents, StartDate >= locRangeStart && StartDate <= locRangeEnd));

// galEvents.Items
With({d: DateAdd(locRangeStart, sldTime.Value, TimeUnit.Days)},
    Filter(colEvents, StartDate <= DateAdd(d, 3, TimeUnit.Days) && EndDate >= DateAdd(d, -3, TimeUnit.Days))
)
```

Optional: draw tick marks with an HTML text sparkline showing event density per day under the slider (entry 20 pattern).

**Gotchas.** Slider `OnChange` fires continuously; keep the gallery bound to a collection, not a data source.

**Done when.** Dragging the slider updates the gallery with no visible lag on a 300-event quarter.

---

### 4. Component-based modal system

**What it is.** One reusable `cmpModal` component with input properties (Title, Body, ConfirmLabel, CancelLabel, Kind) and an output behavior property `OnConfirm`. Opened by setting `gblUI.activeModal`. Replaces the "forty hidden groups" pattern.

**Why it matters.** Every screen gets consistent dialogs, and adding a new confirmation is one line.

**Build steps.**

1. Create component `cmpModal`. Set `Width = App.Width`, `Height = App.Height`.
2. Input properties: `Config` (record: `{title, body, confirmLabel, cancelLabel, kind}`), `IsOpen` (boolean).
3. Behavior properties: `OnConfirm`, `OnCancel`.
4. Inside: full-screen semi-transparent rectangle, centered container, labels, two buttons.
5. Place one instance per screen, `IsOpen: !IsBlank(gblUI.activeModal)`, `Config: gblUI.activeModal`.

**Key formulas.**

```
// Open from anywhere
Set(gblUI, Patch(gblUI, {activeModal: {
    title: "Cancel enrollment?",
    body: "This frees the seat for the waitlist.",
    confirmLabel: "Cancel enrollment",
    cancelLabel: "Keep it",
    kind: "danger",
    action: "CancelEnrollment",
    payload: {id: ThisItem.ID}
}}));

// cmpModal confirm button OnSelect
Self.OnConfirm();
Set(gblUI, Patch(gblUI, {activeModal: Blank()}));

// Screen instance OnConfirm
Switch(gblUI.activeModal.action,
    "CancelEnrollment", Select(btnCancelEnrollment),
    "DeleteEvent", Select(btnDeleteEvent)
);
```

**Gotchas.** Components cannot reference screen controls; dispatch via hidden buttons on the screen as shown.

**Done when.** No screen has more than one modal instance, and all confirmations route through `gblUI.activeModal`.

---

### 5. Toast notifications

**What it is.** A `cmpToast` component that displays a queue of messages from `gblUI.toastQueue`, sliding in from the bottom right and auto-dismissing.

**Why it matters.** `Notify()` is visually inconsistent with the theme and cannot be styled.

**Build steps.**

1. Component with a gallery bound to `gblUI.toastQueue` (records: `{id, text, kind, createdAt}`).
2. A Timer (`Duration = 500`, `Repeat = true`, `AutoStart = true`) that removes toasts older than 5 seconds.
3. Row `Y` animates via a second short timer or by binding `Y` to `Timer.Value` on creation.

**Key formulas.**

```
// App.Formulas
fxToast(text: Text, kind: Text): Void = {
    Set(gblUI, Patch(gblUI, {toastQueue: Table(gblUI.toastQueue, {id: GUID(), text: text, kind: kind, createdAt: Now()})}))
};

// Timer OnTimerEnd
Set(gblUI, Patch(gblUI, {toastQueue: Filter(gblUI.toastQueue, DateDiff(createdAt, Now(), TimeUnit.Seconds) < 5)}));
```

Note: user-defined functions with `Void` return require the corresponding preview feature enabled in the app settings. If unavailable in GCC, implement `fxToast` as a hidden button `btnToast` with `OnSelect` reading `gblToastArg`.

**Gotchas.** Table + Patch on a global record every 500 ms is fine; keep the queue under 10 rows.

**Done when.** Toasts stack, auto-dismiss, and use `gblTheme` colors per kind.

---

### 6. Keyboard shortcuts

**What it is.** A hidden TextInput that always holds focus (re-focused via `Reset()` after any action). Its `OnChange` reads the last typed character and dispatches an action, then clears itself.

**Why it matters.** Schedulers who process dozens of events a day want `N` for new event, `J`/`K` to move selection, `/` to search.

**Build steps.**

1. Insert `txtKeys`, position off-screen (`X = -500`), `Width = 1`.
2. On screen `OnVisible`: `Reset(txtKeys)` (Reset moves focus if `Default` is blank; alternatively use `SetFocus(txtKeys)`).
3. `txtKeys.OnChange`: read `Right(Self.Text, 1)`, dispatch, then `Reset(Self)`.
4. Every button's `OnSelect` ends with `SetFocus(txtKeys)`.

**Key formulas.**

```
// txtKeys.OnChange
With({k: Lower(Right(Self.Text, 1))},
    Switch(k,
        "n", Navigate(scrNewEvent),
        "j", Set(gblUI, Patch(gblUI, {selectedIndex: Min(gblUI.selectedIndex + 1, CountRows(galEvents.AllItems))})),
        "k", Set(gblUI, Patch(gblUI, {selectedIndex: Max(gblUI.selectedIndex - 1, 1)})),
        "/", SetFocus(txtSearch)
    )
);
Reset(Self)
```

**Gotchas.**
- Only works while the hidden input has focus. Show a subtle "keyboard mode" indicator when it does.
- Do not capture keys when a real text input is focused.
- Log the pattern in the debt register: it is a workaround, not a platform feature.

**Done when.** `N`, `J`, `K`, `/` work on the calendar screen and the indicator reflects focus state.

---

### 7. Skeleton loaders

**What it is.** Placeholder rectangles in the shape of the content, with a shimmer driven by a Timer, shown while `gblUI.busy` is true.

**Build steps.**

1. Component `cmpSkeleton` with input `Rows`, `RowHeight`.
2. Gallery of `Sequence(Rows)` rendering two rectangles per row (title and body).
3. Timer `Duration = 1200`, `Repeat = true`. Fill of rectangles interpolates between `SurfaceAlt` and `Border` based on `Timer.Value`.

**Key formulas.**

```
// Rectangle.Fill
ColorFade(gblTheme.SurfaceAlt, 0.15 * Sin(tmrShimmer.Value / 1200 * 2 * Pi()))
```

**Done when.** Every list screen shows skeletons instead of a spinner during initial load.

---

### 8. Command palette

**What it is.** A single search box that searches screens, records, and actions from one unified collection. Opened by `/` (entry 6) or a header button.

**Build steps.**

1. Build `colCommands` in `App.OnStart` from three sources: static screens/actions, recent events, and people.
2. Component `cmpPalette` with a TextInput and a gallery filtered on `StartsWith` across `label` and `keywords`.
3. Each row has `kind` (`screen`, `record`, `action`) and a `target`.

**Key formulas.**

```
// App.OnStart
ClearCollect(colCommands,
    {kind: "screen", label: "Calendar", keywords: "month quarter day", target: "scrCalendar"},
    {kind: "screen", label: "New event", keywords: "create schedule", target: "scrNewEvent"},
    {kind: "action", label: "Sync now", keywords: "refresh reload", target: "Sync"}
);
Collect(colCommands, ForAll(FirstN(Sort(TrainingEvents, StartDate, SortOrder.Descending), 50),
    {kind: "record", label: Title, keywords: TrainingType & " " & Station, target: Text(ID)}
));

// Palette row OnSelect
Switch(ThisItem.kind,
    "screen", Navigate(Switch(ThisItem.target, "scrCalendar", scrCalendar, "scrNewEvent", scrNewEvent)),
    "record", Set(gblUI, Patch(gblUI, {selectedRecordId: Value(ThisItem.target)})); Navigate(scrEventDetail),
    "action", Select(btnSync)
)
```

**Gotchas.** `Navigate` cannot take a screen name as text; the `Switch` mapping is required.

**Done when.** Typing "fire" surfaces the firearms training type and the next three firearms events.

---

### 9. Kanban with pick-up and place

**What it is.** Two-tap drag substitute. Tap a card to pick it up (stored in `gblUI.carried`), tap a column to place it. The carried card renders as a floating ghost that follows the last known pointer position updated by a short Timer sampling a transparent full-screen slider pair (X and Y). Simpler variant: ghost pins to the top of the target column on hover-less devices.

**Build steps.**

1. Horizontal gallery of columns (statuses). Inside each, vertical gallery of cards.
2. Card `OnSelect`: `Set(gblUI, Patch(gblUI, {carried: ThisItem}))`.
3. Column header or empty space `OnSelect`: Patch the carried record's status, clear `carried`.
4. Ghost: an image/label group `Visible: !IsBlank(gblUI.carried)`, positioned at the top of the screen (simple) or following pointer (advanced, using two transparent sliders as coordinate readers).

**Key formulas.**

```
// Column drop zone OnSelect
If(!IsBlank(gblUI.carried),
    Set(gblCrud, {source: "TrainingEvents", op: "Update", id: gblUI.carried.ID, before: gblUI.carried});
    Patch(TrainingEvents, gblUI.carried, {Status: ThisItem.StatusName});
    Set(gblCrud, Patch(gblCrud, {after: LookUp(TrainingEvents, ID = gblUI.carried.ID), result: "OK"}));
    Select(btnLogCrud);
    Set(gblUI, Patch(gblUI, {carried: Blank()}));
    fxToast("Moved to " & ThisItem.StatusName, "success")
)
```

**Done when.** Status changes require exactly two taps and log a CRUD row (entry 42).

---

### 10. Undo stack

**What it is.** Every Patch pushes the prior record and source name onto `colUndo`. An Undo button pops the last entry and re-patches the original values.

**Build steps.**

1. In the CRUD wrapper (0.2), after a successful Patch, `Collect(colUndo, {source, id, before, at: Now()})`.
2. Undo button: take `Last(colUndo)`, Patch the `before` record back, remove from the stack, log a CRUD row with `op = "Undo"`.

**Key formulas.**

```
// btnUndo.OnSelect
With({u: Last(colUndo)},
    Switch(u.source,
        "TrainingEvents", Patch(TrainingEvents, LookUp(TrainingEvents, ID = u.id), u.before),
        "Enrollments", Patch(Enrollments, LookUp(Enrollments, ID = u.id), u.before)
    );
    Remove(colUndo, u);
    fxToast("Undone", "info")
)
```

**Gotchas.** `before` is a record of the list's schema; restore only writable columns. Build a `fxWritable(record)` named formula per source that drops `ID, Created, Modified, Author, Editor`.

**Done when.** Ten consecutive undos restore state correctly and each is logged.

---

## Part B. Data and architecture

### 11. SharePoint list as a rules engine

**What it is.** A `Rules` list holding validation and business rules as data. The app evaluates them at runtime against the record being edited. Changing a rule is editing a list row, not republishing an app.

**Why it matters.** Single Prod environment means every republish is a risk. Moving logic to data removes most of the reasons to republish.

**Data model.** `Rules` list:

| Column | Type | Notes |
|---|---|---|
| Title | Text | Rule name |
| Scope | Choice | Which entity: Event, Enrollment, Instructor |
| Field | Text | Column name evaluated |
| Operator | Choice | eq, ne, gt, lt, ge, le, contains, blank, notblank, regex |
| Value | Text | Comparison value |
| Message | Text | Shown when rule fails |
| Severity | Choice | Block, Warn |
| Enabled | Yes/No | |
| Sector | Text | Optional scope narrowing, blank = all |
| SortOrder | Number | Evaluation order |

**Build steps.**

1. Load enabled rules for the current sector into `colRules` on app start.
2. Write `fxEval(rule, record)` that returns true when the rule PASSES.
3. Before save, compute `colViolations = Filter(colRules, !fxEval(ThisRule, locRecord))`.
4. Block save if any `Severity = "Block"`; show warnings otherwise.

**Key formulas.**

```
// Evaluate one rule against a record (record is converted to a text value by field name)
// Because Power Fx cannot index a record by a dynamic column name, use a field map:
fxFieldValue(rec: Record, field: Text): Text =
    Switch(field,
        "Capacity", Text(rec.Capacity),
        "StartDate", Text(rec.StartDate, "yyyy-mm-dd"),
        "EndDate", Text(rec.EndDate, "yyyy-mm-dd"),
        "TrainingType", rec.TrainingType,
        "InstructorEmail", rec.InstructorEmail,
        ""
    );

// Violations
ClearCollect(colViolations,
    Filter(colRules,
        !With({v: fxFieldValue(locRecord, Field)},
            Switch(Operator,
                "eq", v = Value,
                "ne", v <> Value,
                "gt", Value(v) > Value(Value),
                "lt", Value(v) < Value(Value),
                "ge", Value(v) >= Value(Value),
                "le", Value(v) <= Value(Value),
                "contains", Value in v,
                "blank", IsBlank(v),
                "notblank", !IsBlank(v),
                "regex", IsMatch(v, Value),
                true
            )
        )
    )
);
```

**Gotchas.** The field map must be maintained when columns are added; add it to the harness checklist. Cross-field rules (EndDate > StartDate) need a computed pseudo-field in the map (e.g., `"DurationDays"`).

**Done when.** An HCT admin can add "Capacity must be at least 4" without a developer.

---

### 12. Config-driven screens

**What it is.** A `ScreenConfig` list defining which fields appear on a form, their labels, order, required flag, and control type. One form component renders whatever the config says. Sectors get different forms from the same app.

**Data model.** `ScreenConfig`: Title (screen key), Field, Label, ControlType (text, number, date, choice, person), Required, SortOrder, Visible, Sector, HelpText.

**Build steps.**

1. Gallery `galForm` bound to `Filter(colScreenConfig, Title = "EventForm" && Visible)`, sorted by `SortOrder`.
2. Inside the row, one control of each type, only one visible based on `ControlType`.
3. Collect edits into `colFormValues` (`{field, value}`) on each control's `OnChange`.
4. On save, build the Patch record from `colFormValues` via a field map (same technique as entry 11).

**Key formulas.**

```
// Row: text input Visible
ThisItem.ControlType = "text"

// Row: text input OnChange
If(IsBlank(LookUp(colFormValues, field = ThisItem.Field)),
    Collect(colFormValues, {field: ThisItem.Field, value: Self.Text}),
    Patch(colFormValues, LookUp(colFormValues, field = ThisItem.Field), {value: Self.Text})
)

// Save
Patch(TrainingEvents, Defaults(TrainingEvents), {
    Title: LookUp(colFormValues, field = "Title").value,
    Capacity: Value(LookUp(colFormValues, field = "Capacity").value),
    TrainingType: LookUp(colFormValues, field = "TrainingType").value
})
```

**Gotchas.** Galleries reset control state on scroll; keep `Default` bound to `colFormValues` so values persist.

**Done when.** Reordering two fields in the list reorders them in the app without a publish.

---

### 13. Feature flags list

**What it is.** A `FeatureFlags` list with per-flag, per-user, per-sector enablement. `fxFlag("Name")` returns true when the current user should see the feature.

**Data model.** `FeatureFlags`: Title (flag name), Enabled (Yes/No), Users (multi-line text, semicolon-separated emails, blank = all), Sectors (text, blank = all), Notes.

**Key formulas.**

```
// App.OnStart
ClearCollect(colFlags, Filter(FeatureFlags, Enabled));
Set(gblUserEmail, Lower(User().Email));

// App.Formulas
fxFlag(name: Text): Boolean =
    With({f: LookUp(colFlags, Title = name)},
        !IsBlank(f) &&
        (IsBlank(f.Users) || Lower(gblUserEmail) in Lower(f.Users)) &&
        (IsBlank(f.Sectors) || gblUserSector in f.Sectors)
    );
```

**Done when.** Every entry in this file is gated by its own flag on first deployment.

---

### 14. Shadow tables for time travel

**What it is.** A Flow copies every changed record to a `History` list with a snapshot of all columns as JSON plus the change metadata. Enables audit, diff, and "what did this look like last Tuesday."

**Data model.** `History`: Title (source list name), RecordId (number), Snapshot (multi-line text, JSON), ChangedBy (text), ChangedAt (date/time), Version (number).

**Flow.** `HIST-<ListName>`: Trigger "When an item is created or modified" on the source list. Actions: Compose JSON of trigger body, Create item in `History`. One Flow per tracked list.

**App side.** A history panel on the record detail screen lists versions and shows a field-level diff between any two using `ParseJSON`.

```
// Diff two snapshots for a known field set
With({a: ParseJSON(locSnapA), b: ParseJSON(locSnapB)},
    Filter(
        Table(
            {field: "Title", before: Text(a.Title), after: Text(b.Title)},
            {field: "Capacity", before: Text(a.Capacity), after: Text(b.Capacity)},
            {field: "StartDate", before: Text(a.StartDate), after: Text(b.StartDate)}
        ),
        before <> after
    )
)
```

**Gotchas.** Flow runs count against the tenant. For high-churn lists, batch: trigger every 15 minutes, filter Modified > last run.

**Done when.** Any record can be restored to any prior version from the app (via entry 10 mechanics).

---

### 15. Optimistic UI

**What it is.** Update the local collection first, Patch in the background, roll back if the Patch fails.

**Key formulas.**

```
// Cancel enrollment, optimistic
With({original: ThisItem},
    Patch(colEnrollments, ThisItem, {Status: "Cancelled"});
    IfError(
        Patch(Enrollments, LookUp(Enrollments, ID = original.ID), {Status: "Cancelled"}),
        Patch(colEnrollments, LookUp(colEnrollments, ID = original.ID), original);
        fxToast("Could not cancel. Reverted.", "danger"),
        fxToast("Cancelled", "success")
    )
)
```

**Gotchas.** Requires `IfError` (Formula-level error management) enabled in app settings.

**Done when.** All list-row actions feel instantaneous on a throttled connection.

---

### 16. Delta sync

**What it is.** Store the last sync timestamp in the app; pull only records modified after it and merge into the local collection.

**Key formulas.**

```
// btnSync.OnSelect
With({since: Coalesce(gblLastSync, DateAdd(Now(), -365, TimeUnit.Days))},
    ClearCollect(colDelta, Filter(TrainingEvents, Modified > since));
    ForAll(colDelta As d,
        If(IsBlank(LookUp(colEvents, ID = d.ID)),
            Collect(colEvents, d),
            Patch(colEvents, LookUp(colEvents, ID = d.ID), d)
        )
    );
    Set(gblLastSync, Now());
    SaveData(colEvents, "events");
    SaveData(Table({v: gblLastSync}), "lastSync")
)
```

**Gotchas.** `Modified > since` is delegable on SharePoint date columns. Deletions are not captured; use a soft-delete `IsDeleted` column and filter locally.

**Done when.** A 5,000-row list loads in under two seconds after first sync.

---

### 17. Server-side conflict enforcement on SharePoint

**What it is.** An instant (button-triggered) Flow that receives the record ID and the `Modified` timestamp the app last saw, checks the current `Modified`, and only writes if they match. Returns `OK` or `CONFLICT` with the current record.

**Flow.** `TRACS-SafeWrite`: Trigger PowerApps (V2) with inputs `ListName, RecordId, ExpectedModified, ChangesJson`. Actions: Get item, Condition `Modified == ExpectedModified`, if yes Update item from parsed JSON and respond `{status: "OK"}`, else respond `{status: "CONFLICT", current: item}`.

**App side.**

```
With({r: 'TRACS-SafeWrite'.Run("TrainingEvents", Text(ThisItem.ID), Text(ThisItem.Modified), JSON({Capacity: locNewCapacity}))},
    If(r.status = "OK",
        fxToast("Saved", "success"),
        Set(gblUI, Patch(gblUI, {activeModal: {title: "Someone else changed this", body: "Reload and try again.", confirmLabel: "Reload", kind: "warning", action: "Reload"}}))
    )
)
```

**Gotchas.** Timestamp precision: compare as ISO strings truncated to seconds on both sides.

**Done when.** Two schedulers editing the same event cannot silently overwrite each other.

---

### 18. Semantic version stamped in the app

**Data model.** `AppVersions`: Title (app name), Version (text, semver), PublishedAt, Notes, IsCurrent (Yes/No).

**App side.** Set `gblAppVersion = "1.4.2"` as a named formula. Footer label shows it. On start, compare with `LookUp(AppVersions, Title = "TRACS" && IsCurrent).Version` and toast if the user is on a stale cached version.

**Done when.** Every support ticket template asks for the version shown in the footer.

---

### 19. Pipeline-lite ALM without pipelines

**What it is.** A scheduled Flow exports the managed and unmanaged solution to a versioned OneDrive folder along with a manifest.

**Flow.** `ALM-Export`: Recurrence (weekly, plus manual trigger). Actions: Dataverse "Perform an unbound action" `ExportSolution` (requires Dataverse connector, which is available for solution operations without premium licensing of end users; verify in GCC), Create file in OneDrive `/Solutions/<name>/<yyyy-MM-dd>/<name>_<version>.zip`, Create file manifest JSON with version, date, exporter, notes from `AppVersions`.

**Gotchas.** If the unbound action is unavailable in GCC, fall back to a documented manual export checklist stored in the same folder. Record in the decision log.

**Done when.** Any prior weekly version can be re-imported.

---

## Part C. Scheduling and TRACS-specific

### 20. Conflict heatmap

**What it is.** Month grid where each day's cell color intensity equals booking density (events, seats, or instructor load). Built with the HTML text SVG engine.

**Build steps.**

1. Aggregate `colEvents` per day into `colDayLoad` (`{day, count, seats}`).
2. Render a 7-column grid of `<rect>` with `fill-opacity` proportional to count / max.
3. Overlay transparent buttons for click handling, or make the whole grid a legend and keep interaction in the existing calendar.

**Key formulas.**

```
ClearCollect(colDayLoad,
    AddColumns(
        GroupBy(AddColumns(colEvents, day, DateValue(StartDate)), day, grp),
        count, CountRows(grp),
        seats, Sum(grp, Capacity)
    )
);

// SVG cell loop (28 to 31 cells)
Concat(colDayLoad,
    "<rect x='" & (Weekday(day) - 1) * 40 & "' y='" & (RoundDown((Day(day) + Weekday(Date(Year(day), Month(day), 1)) - 2) / 7, 0)) * 40 & "' " &
    "width='38' height='38' rx='4' fill='" & gblTheme.Primary & "' fill-opacity='" & count / Max(colDayLoad, count) & "'/>"
)
```

**Done when.** Organizers can identify the three busiest days of a month at a glance.

---

### 21. Slot suggester

**What it is.** Given instructor, room, and student list, compute the earliest window of length N hours where everyone is free, within business hours, over the next 30 days.

**Build steps.**

1. Collect all busy intervals for participants from `TrainingEvents` (and optionally Outlook free/busy via the Office 365 Outlook connector `FindMeetingTimes`, standard).
2. Generate candidate slots with `Sequence` (days × hourly starts).
3. Filter candidates with no overlap.

**Key formulas.**

```
ClearCollect(colBusy,
    Filter(colEvents,
        InstructorEmail = locInstructor || RoomId = locRoom || locStudentEmails in AttendeeEmails
    )
);

ClearCollect(colCandidates,
    ForAll(Sequence(30) As d,
        ForAll(Sequence(9, 7) As h,   // 07:00 to 15:00 starts
            {start: DateAdd(DateAdd(Today(), d.Value, TimeUnit.Days), h.Value, TimeUnit.Hours)}
        )
    )
);

ClearCollect(colFree,
    Filter(AddColumns(colCandidates, end, DateAdd(start, locDurationHours, TimeUnit.Hours)),
        Weekday(start) in [2,3,4,5,6] &&
        IsEmpty(Filter(colBusy, StartDate < end && EndDate > start))
    )
);
// Suggest First(colFree)
```

**Gotchas.** `AttendeeEmails` must be a text column with semicolon-delimited emails for `in` to work. `FindMeetingTimes` is the better path for real calendars; use it when the connector is available in GCC.

**Done when.** "Suggest a time" returns a valid slot within one second for a 20-student class.

---

### 22. "Schedule like this one"

**What it is.** Clone a past event including invitees, materials, and room, shifting dates by an offset.

**Key formulas.**

```
// btnClone.OnSelect
With({src: ThisItem, offset: DateDiff(ThisItem.StartDate, locNewStart, TimeUnit.Days)},
    Set(gblCrud, {source: "TrainingEvents", op: "Create", before: Blank()});
    Set(gblNew, Patch(TrainingEvents, Defaults(TrainingEvents), {
        Title: src.Title,
        StartDate: DateAdd(src.StartDate, offset, TimeUnit.Days),
        EndDate: DateAdd(src.EndDate, offset, TimeUnit.Days),
        TrainingType: src.TrainingType, Sector: src.Sector, Station: src.Station,
        InstructorEmail: src.InstructorEmail, RoomId: src.RoomId, Capacity: src.Capacity,
        AttendeeEmails: src.AttendeeEmails, MaterialsUrl: src.MaterialsUrl, Status: "Draft"
    }));
    Set(gblCrud, Patch(gblCrud, {id: gblNew.ID, after: gblNew, result: "OK"}));
    Select(btnLogCrud);
    Navigate(scrEventDetail)
)
```

**Done when.** Cloning a class with 15 attendees takes one tap plus a date pick.

---

### 23. Readiness countdown per agent

**What it is.** A panel listing each agent's certifications with days until lapse, sorted ascending, and a "book next available" button that jumps to the slot suggester or the next scheduled class of that type.

**Data model.** `Certifications`: AgentEmail, TrainingType, CompletedOn, ValidDays. Derived `ExpiresOn = DateAdd(CompletedOn, ValidDays, Days)`.

**Key formulas.**

```
ClearCollect(colReadiness,
    Sort(
        AddColumns(Filter(Certifications, AgentEmail in colMyTeamEmails),
            expiresOn, DateAdd(CompletedOn, ValidDays, TimeUnit.Days),
            daysLeft, DateDiff(Today(), DateAdd(CompletedOn, ValidDays, TimeUnit.Days), TimeUnit.Days)
        ),
        daysLeft
    )
);

// Book next
Set(gblUI, Patch(gblUI, {selectedRecordId:
    First(Sort(Filter(colEvents, TrainingType = ThisItem.TrainingType && StartDate > Today() && Status = "Open"), StartDate)).ID
}));
Navigate(scrEventDetail)
```

**Done when.** A supervisor sees red/amber/green per agent and can book in two taps.

---

### 24. Supervisor bulk enroll

**Build steps.** Multi-select gallery (checkbox per row, selected rows in `colSelected`), pick a class, loop Patch.

```
ForAll(colSelected As a,
    Patch(Enrollments, Defaults(Enrollments), {
        EventId: locEvent.ID, AgentEmail: a.Email, EnrolledBy: gblUserEmail, Status: "Enrolled"
    })
);
Select(btnLogCrudBulk);   // logs one row per enrollment, op = "Create", batchId = GUID()
fxToast(CountRows(colSelected) & " enrolled", "success")
```

**Gotchas.** Check capacity before the loop; enforce server-side via entry 17 or a Flow that rejects over-capacity.

**Done when.** Enrolling 12 agents takes under five seconds and creates 12 Outlook invites (entry 25 Flow).

---

### 25. Waitlist with auto-promote

**Flow.** `TRACS-Waitlist`: Trigger on `Enrollments` modified where `Status = "Cancelled"`. Get first waitlisted enrollment for the same event ordered by Created, update to `Enrolled`, send Outlook invite to student and instructor, notify supervisor.

**App side.** Enrollment button reads live capacity and writes `Status = If(enrolled >= capacity, "Waitlisted", "Enrolled")`.

**Done when.** A cancellation fills the seat within one minute with no human action.

---

### 26. Capacity forecasting

**What it is.** Trend demand per training type over the last N quarters and project the next quarter with a simple linear fit.

**Key formulas.**

```
// colQuarterly: {trainingType, qIndex, demand}
ClearCollect(colForecast,
    ForAll(Distinct(colQuarterly, trainingType) As t,
        With({pts: Filter(colQuarterly, trainingType = t.Value), n: CountRows(Filter(colQuarterly, trainingType = t.Value))},
            With({
                sx: Sum(pts, qIndex), sy: Sum(pts, demand),
                sxy: Sum(pts, qIndex * demand), sxx: Sum(pts, qIndex * qIndex)
            },
            With({slope: (n * sxy - sx * sy) / (n * sxx - sx * sx)},
                {trainingType: t.Value, slope: slope, intercept: (sy - slope * sx) / n,
                 next: (sy - slope * sx) / n + slope * (Max(pts, qIndex) + 1)}
            ))
        )
    )
);
```

Render with entry 1 sparklines plus a dashed projection segment.

**Done when.** HCT can show projected seat demand per type for next quarter in one screen.

---

### 27. Print-ready roster

**Build steps.** HTML text control with a print stylesheet (table, header, signature lines). Export: Flow `TRACS-RosterPDF` receives the HTML, creates an `.html` file in OneDrive, uses OneDrive "Convert file" to PDF, returns the file content or a share link.

```
// HTML
"<html><body style='font-family:Arial'><h2>" & locEvent.Title & "</h2>" &
"<table border='1' cellpadding='6' style='border-collapse:collapse;width:100%'>" &
"<tr><th>Name</th><th>Station</th><th>Signature</th></tr>" &
Concat(colRoster, "<tr><td>" & DisplayName & "</td><td>" & Station & "</td><td>&nbsp;</td></tr>") &
"</table></body></html>"
```

**Done when.** A PDF roster downloads in under ten seconds.

---

### 28. Calendar subscription (ICS feed)

**Flow.** `TRACS-ICS`: Recurrence hourly. Get items from `TrainingEvents` (next 180 days), build an ICS string (`BEGIN:VCALENDAR` ... `END:VCALENDAR`, one `VEVENT` per row with `UID`, `DTSTART`, `DTEND`, `SUMMARY`, `LOCATION`), write `tracs.ics` to a SharePoint document library with read access for the audience. Users subscribe from Outlook using the file URL.

**Gotchas.** Dates must be UTC in `yyyyMMddTHHmmssZ` format. Generate one feed per sector if volume is high.

**Done when.** Outlook shows TRACS events without opening the app.

---

## Part D. Concepts and whole apps

### 29. Personal COP widget mode

**What it is.** The app detects that it is embedded (Teams or SharePoint web part) and collapses to a compact dashboard with three tiles: my next class, my team's readiness, exceptions needing me.

**Key formulas.**

```
// App.Formulas
fxIsEmbedded = !IsBlank(Param("hostClientType")) && Param("hostClientType") <> "web"
             || Param("mode") = "widget";

// Screen selection in App.OnStart
If(fxIsEmbedded, Navigate(scrWidget), Navigate(scrCalendar))
```

Pass `mode=widget` as a query parameter from the SharePoint web part.

**Done when.** The same app renders full in the browser and compact in Teams.

---

### 30. Offline-first field mode

**Build steps.**

1. On start, `LoadData(colEvents, "events", true)` then attempt delta sync (entry 16).
2. All writes go to `colOutbox` (`{source, op, id, changes, createdAt}`) when `Connection.Connected = false`.
3. A Timer checks connectivity every 30 seconds and drains `colOutbox` through the CRUD wrapper.

```
// Drain
If(Connection.Connected && !IsEmpty(colOutbox),
    ForAll(colOutbox As o,
        Switch(o.source,
            "Enrollments", Patch(Enrollments, If(o.op = "Create", Defaults(Enrollments), LookUp(Enrollments, ID = o.id)), o.changes)
        )
    );
    Clear(colOutbox);
    SaveData(colOutbox, "outbox");
    fxToast("Synced offline changes", "success")
)
```

**Gotchas.** `SaveData` works on mobile and, for the web player, when the corresponding setting is enabled. Conflicts on replay should route through entry 17.

**Done when.** A station with no connectivity can record attendance and sync later.

---

### 31. Digital sign-in kiosk

**What it is.** Tablet at the classroom door. Student taps their name (or scans a badge/QR with the Barcode Reader control) and attendance is patched instantly.

**Build steps.** Kiosk screen with a large name gallery filtered to the current event's roster, Barcode Reader control mapping code to `AgentEmail`, and a big confirmation animation (entry 5 toast or full-screen check).

```
// Barcode OnScan
With({code: Last(Self.Barcodes).Value},
    With({a: LookUp(colRoster, BadgeCode = code)},
        If(IsBlank(a), fxToast("Not on roster", "danger"),
            Patch(Attendance, Defaults(Attendance), {EventId: locEvent.ID, AgentEmail: a.Email, CheckedInAt: Now()});
            fxToast("Welcome, " & a.DisplayName, "success")
        )
    )
)
```

**Done when.** Check-in completes in under three seconds per student.

---

### 32. Instructor evaluation loop

**Flow.** `TRACS-Eval`: Trigger when `TrainingEvents.Status` becomes `Completed`. Send a Microsoft Forms link (or an in-app survey screen link with `eventId` param) to attendees. A second Flow on form response writes to `Evaluations` (EventId, InstructorEmail, Score, Comment).

**App side.** Instructor profile shows rolling average via entry 1 sparkline; training type shows quality trend.

**Done when.** Every completed class produces a score within 48 hours.

---

### 33. Self-healing data

**Flow.** `TRACS-Health`: Nightly. Queries: enrollments with no matching event, events with `EndDate < StartDate`, duplicate enrollments (same agent, same event), events past date still `Open`. Writes each finding to `DataIssues` (Type, Source, RecordId, Detail, Status).

**App side.** Admin screen lists open issues with "Fix" actions that call the appropriate CRUD wrapper.

**Done when.** The nightly run produces zero unaddressed issues older than 7 days.

---

### 34. Onboarding app that builds itself

**Flow.** `HCT-Onboard`: Trigger on new row in `Agents`. Reads `OnboardingTemplate` list (Task, Owner role, DueOffsetDays, TrainingType if it requires a class), creates `Tasks` rows, and for training tasks creates a waitlist entry against the next open class of that type.

**Done when.** A new agent record generates a full task list and initial enrollments with no manual entry.

---

### 35. Exception inbox

**Flow pattern.** Every Flow in the solution has a `Scope` with a parallel "Configure run after: failed" branch that writes to `FlowFailures` (FlowName, RunId, Step, Error, Payload JSON, Status, RetryCount).

**App side.** Admin screen shows failures with a Retry button that re-invokes the Flow with the stored payload.

```
// Retry
Switch(ThisItem.FlowName,
    "TRACS-Waitlist", 'TRACS-Waitlist-Manual'.Run(ThisItem.Payload),
    "TRACS-RosterPDF", 'TRACS-RosterPDF'.Run(ThisItem.Payload)
);
Patch(FlowFailures, ThisItem, {Status: "Retried", RetryCount: ThisItem.RetryCount + 1})
```

**Done when.** No one emails screenshots of failed Flows.

---

### 36. Analytics without Power BI

**What it is.** A nightly Flow writes aggregated metrics to a `Metrics` list (Date, Metric, Dimension, Value). The app renders SVG charts (entry 1) from that list. No premium, no Power BI licensing conversation.

**Data model.** `Metrics`: Date, Metric (text: seats_booked, classes_held, fill_rate, cancellations), Dimension (text: sector or training type), Value (number).

**Done when.** HCT leadership dashboard loads from `Metrics` alone with no direct queries to transactional lists.

---

### 37. Themed component library as its own solution

**What it is.** The multi-brand theme system, `cmpModal`, `cmpToast`, `cmpSkeleton`, `cmpSparkline`, `cmpPalette`, and the `fxIcon` library packaged as a component library in its own solution `usbpmsd_ComponentLibrary`. Other USBP MSD apps import it.

**Build steps.**

1. Create a component library (not a canvas app) in the solution.
2. Move shared components; expose `Theme` as an input property on each instead of relying on `gblTheme` directly.
3. Version the library; consuming apps get an update prompt.

**Done when.** TRACS and the COP both consume the library and share one theme definition.

---

### 38. Copilot-adjacent assistant without Copilot

**What it is.** A text box that parses plain requests like "book Smith for firearms next week" using `IsMatch` and `Filter` against known names, training types, and relative date phrases.

**Key formulas.**

```
With({t: Lower(txtAsk.Text)},
    With({
        verb: If(IsMatch(t, "book|enroll|schedule"), "book", If(IsMatch(t, "cancel|drop"), "cancel", "find")),
        who: First(Filter(colAgents, Lower(LastName) in t)),
        type: First(Filter(colTrainingTypes, Lower(Name) in t || Lower(ShortName) in t)),
        when: If("next week" in t, DateAdd(Today(), 7 - Weekday(Today()) + 1, TimeUnit.Days),
              If("tomorrow" in t, DateAdd(Today(), 1, TimeUnit.Days), Today()))
    },
        Set(gblIntent, {verb: verb, who: who, type: type, when: when});
        Navigate(scrIntentConfirm)
    )
)
```

`scrIntentConfirm` shows the parsed intent and the matching class for one-tap confirmation.

**Done when.** Five common phrasings resolve correctly without a language model.

---

### 39. App usage telemetry

Superseded and expanded by entry 41 (User Action Log). Keep the `Metrics` rollup Flow from entry 36 reading from the action log.

---

### 40. Living help

**Data model.** `Help`: Title (screen key), Heading, Body (multi-line rich text), ImageUrl, SortOrder, Sector.

**App side.** Every screen has a `?` button opening a side panel bound to `Filter(colHelp, Title = App.ActiveScreen.Name)`. HCT edits help in SharePoint; the app renders it.

**Done when.** Help content changes never require a publish.

---

## Part E. Observability modules

### 41. User Action Log (complete in-app activity log per user)

**What it is.** A module that records every meaningful user action in the app: screen navigation, button and gallery selections, searches, filter changes, modal open/close, keyboard shortcuts, sync events, errors, and session start/end. Each row carries the user, session, screen, control, action, optional payload, timestamp, and app version. Writes are buffered locally and flushed in batches to keep the app fast. An admin screen replays any user's session as a timeline.

**Why it matters.** Support ("what did you click before it broke"), UX evidence ("nobody uses the quarter view"), adoption metrics for cost avoidance documentation, and security review ("who looked at what").

**Constraints check.** Standard connectors only. SharePoint list backend. No PCF.

**Data model.** `AppActionLog` list:

| Column | Type | Notes |
|---|---|---|
| Title | Text | Action name (e.g., `Navigate`, `Select`, `Search`, `Filter`, `ModalOpen`, `Shortcut`, `Sync`, `Error`, `SessionStart`, `SessionEnd`) |
| UserEmail | Text | Indexed |
| SessionId | Text | GUID per app launch, indexed |
| Screen | Text | `App.ActiveScreen.Name` at time of action |
| Control | Text | Control name |
| Target | Text | Screen navigated to, record ID, search term, etc. |
| Payload | Multi-line text | JSON of extra context, kept under 2 KB |
| ClientTs | Date/Time | `Now()` on device |
| Seq | Number | Monotonic per session |
| AppVersion | Text | From entry 18 |
| Host | Text | `Param("hostClientType")` or `web` |
| DurationMs | Number | Optional, for timed actions |

Indexes: UserEmail, SessionId, ClientTs. Set list to 5,000-row threshold awareness: create an index on `ClientTs` and archive monthly (see Flow below).

**Build steps.**

1. **Session start.** In `App.OnStart`:

```
Set(gblSession, {id: GUID(), startedAt: Now(), seq: 0});
Clear(colActionBuffer);
fxLog("SessionStart", "App", "", "");
```

2. **Logging function.** Add to `App.Formulas` (or a hidden `btnLog` reading `gblLogArg` if user-defined functions are unavailable):

```
fxLog(action: Text, control: Text, target: Text, payload: Text): Void = {
    Set(gblSession, Patch(gblSession, {seq: gblSession.seq + 1}));
    Collect(colActionBuffer, {
        Title: action,
        UserEmail: gblUserEmail,
        SessionId: gblSession.id,
        Screen: App.ActiveScreen.Name,
        Control: control,
        Target: target,
        Payload: payload,
        ClientTs: Now(),
        Seq: gblSession.seq,
        AppVersion: gblAppVersion,
        Host: Coalesce(Param("hostClientType"), "web")
    })
};
```

3. **Instrument navigation.** Wrap every `Navigate` in `fxNav`:

```
fxNav(target: Text): Void = {
    fxLog("Navigate", "", target, "");
    Switch(target,
        "scrCalendar", Navigate(scrCalendar),
        "scrEventDetail", Navigate(scrEventDetail),
        "scrNewEvent", Navigate(scrNewEvent),
        "scrAdmin", Navigate(scrAdmin)
    )
};
```

Also log on every `Screen.OnVisible`: `fxLog("ScreenVisible", "", Self.Name, "")`. This captures back-button and deep-link navigation that bypasses `fxNav`.

4. **Instrument selections.** Every button and gallery `OnSelect` begins with `fxLog("Select", Self.Name, <target or record id as text>, "")`. Enforce via the harness checklist. For galleries: `fxLog("Select", "galEvents", Text(ThisItem.ID), "")`.

5. **Instrument searches and filters.** Search box `OnChange` (debounced by a 600 ms Timer): `fxLog("Search", "txtSearch", Self.Text, "")`. Filter dropdowns: `fxLog("Filter", Self.Name, Self.Selected.Value, "")`.

6. **Instrument modals, shortcuts, sync, errors.** In `cmpModal` open/close, entry 6 dispatcher, entry 16 sync button, and every `IfError` failure branch: `fxLog("Error", <control>, <operation>, JSON(FirstError))`.

7. **Flush.** A Timer `tmrFlush` (`Duration = 15000`, `Repeat = true`) plus flush on `App.OnStart` completion and on navigation to any screen. Batch write with a single `Collect` to SharePoint (Power Apps batches this into parallel calls):

```
// tmrFlush.OnTimerEnd
If(!IsEmpty(colActionBuffer) && Connection.Connected,
    With({batch: colActionBuffer},
        Clear(colActionBuffer);
        IfError(
            Collect(AppActionLog, batch),
            Collect(colActionBuffer, batch)   // put back on failure
        )
    );
    SaveData(colActionBuffer, "actionBuffer")
)
```

8. **Session end.** There is no reliable app-close event. Approximate with: on every flush, also `SaveData`. On next `OnStart`, if `LoadData(colActionBuffer, "actionBuffer", true)` returns rows from a prior session, flush them and write `SessionEnd` for that prior session with `ClientTs` = last buffered timestamp.

9. **Retention Flow.** `LOG-Archive`: monthly, move rows older than 90 days to `AppActionLogArchive` (or a CSV in a document library), delete from the live list.

10. **Admin replay screen** `scrActionReplay`:
    - Dropdown of users (distinct from last 30 days), dropdown of sessions for that user.
    - Vertical gallery sorted by `Seq` showing time, screen, action, control, target.
    - A vertical SVG timeline (entry 1) with one tick per action, color by action type, and gaps proportional to time between actions.
    - "Jump to error" button that scrolls to the first `Error` row.
    - Summary tiles: session length, screens visited, actions per minute, errors.

```
// Sessions for user
ClearCollect(colSessions,
    Sort(
        AddColumns(
            GroupBy(Filter(AppActionLog, UserEmail = drpUser.Selected.Value), SessionId, grp),
            startedAt, Min(grp, ClientTs),
            endedAt, Max(grp, ClientTs),
            actions, CountRows(grp),
            errors, CountRows(Filter(grp, Title = "Error"))
        ),
        startedAt, SortOrder.Descending
    )
);

// Replay rows
ClearCollect(colReplay, Sort(Filter(AppActionLog, SessionId = drpSession.Selected.SessionId), Seq));
```

11. **Privacy and governance.** Log control names and record IDs, never PII payloads beyond what the record ID already implies. Do not log search text if it could contain names of agents in a sensitive context; log the term length instead if policy requires. Document the decision in the decision log. Gate the replay screen behind an `Admins` list check.

**Gotchas.**
- `App.ActiveScreen.Name` is correct at the time `fxLog` runs; when logging inside `fxNav`, it captures the origin screen, which is what you want.
- Delegation: `Filter(AppActionLog, UserEmail = x)` is delegable; `GroupBy` is not. Pull the user's last 30 days first (delegable date filter), then group locally. Cap at 2,000 rows via the data row limit setting.
- Do not put `fxLog` in `OnChange` of a slider or in any Timer-driven property; only in discrete user actions.
- If `Void` user-defined functions are not enabled in GCC, replace `fxLog(...)` with `Set(gblLogArg, {action, control, target, payload}); Select(btnLog)`.

**Done when.**
- Every screen, button, gallery, search, filter, modal, shortcut, sync, and error writes a row.
- A 20-minute session of ordinary use produces no perceptible slowdown.
- An admin can select any user, any session, and replay it as a timeline within five seconds.
- Metrics Flow (entry 36) computes daily active users, screens per session, and top actions from this list.

---

### 42. CRUD Audit Module (all record operations across all data sources)

**What it is.** A module that records every Create, Read (optional, see below), Update, Delete, Undo, and bulk operation the app performs against any data source, with before and after snapshots, the user who did it, the session and action that triggered it, and the outcome. Includes an admin screen that shows CRUD activity for each data source and for all sources combined, with filtering by user, source, operation, time range, and record ID, plus a field-level diff viewer.

**Why it matters.** Audit trail for HCT scheduling decisions, root cause for bad data, rollback source (feeds entries 10 and 14), and a single answer to "who changed this and when."

**Constraints check.** Standard connectors, SharePoint backend. Works alongside Dataverse sources (Dataverse auditing exists but this module gives a unified view across SharePoint and Dataverse).

**Data model.** `CrudAudit` list:

| Column | Type | Notes |
|---|---|---|
| Title | Text | Operation: `Create`, `Update`, `Delete`, `Undo`, `BulkCreate`, `BulkUpdate`, `Read` (optional) |
| Source | Text | Data source display name, indexed |
| RecordId | Text | Source record ID, indexed |
| UserEmail | Text | Indexed |
| SessionId | Text | Links to entry 41 |
| ActionSeq | Number | The `Seq` of the triggering user action in entry 41 |
| Screen | Text | |
| Before | Multi-line text | JSON snapshot before (blank for Create) |
| After | Multi-line text | JSON snapshot after (blank for Delete) |
| ChangedFields | Text | Comma-separated list of fields that differ |
| Result | Text | `OK` or `Error` |
| ErrorText | Text | |
| BatchId | Text | Groups bulk operations |
| ClientTs | Date/Time | |
| AppVersion | Text | |

**Build steps.**

1. **Source registry.** Named formula listing every data source the app touches, used for the admin dropdown and for writable-field maps:

```
// App.Formulas
tblSources = Table(
    {name: "TrainingEvents", kind: "SharePoint", writable: "Title,StartDate,EndDate,TrainingType,Sector,Station,InstructorEmail,RoomId,Capacity,AttendeeEmails,MaterialsUrl,Status"},
    {name: "Enrollments", kind: "SharePoint", writable: "EventId,AgentEmail,EnrolledBy,Status"},
    {name: "Attendance", kind: "SharePoint", writable: "EventId,AgentEmail,CheckedInAt"},
    {name: "Certifications", kind: "SharePoint", writable: "AgentEmail,TrainingType,CompletedOn,ValidDays"},
    {name: "Rules", kind: "SharePoint", writable: "Field,Operator,Value,Message,Severity,Enabled,Sector,SortOrder"}
);
```

2. **The wrapper.** All writes go through one of three patterns. The build agent must never emit a bare `Patch`, `Remove`, or `Collect` against a data source outside these.

Single write:

```
// 1. stage
Set(gblCrud, {source: "Enrollments", op: "Update", id: Text(ThisItem.ID), before: JSON(ThisItem), batchId: ""});
// 2. write
IfError(
    Set(gblCrudResult, Patch(Enrollments, ThisItem, {Status: "Cancelled"})),
    Set(gblCrud, Patch(gblCrud, {after: "", result: "Error", error: FirstError.Message})),
    Set(gblCrud, Patch(gblCrud, {after: JSON(gblCrudResult), result: "OK", error: ""}))
);
// 3. log
Select(btnLogCrud);
```

Create:

```
Set(gblCrud, {source: "Enrollments", op: "Create", id: "", before: "", batchId: ""});
IfError(
    Set(gblCrudResult, Patch(Enrollments, Defaults(Enrollments), {EventId: locEvent.ID, AgentEmail: locAgent, Status: "Enrolled"})),
    Set(gblCrud, Patch(gblCrud, {result: "Error", error: FirstError.Message})),
    Set(gblCrud, Patch(gblCrud, {id: Text(gblCrudResult.ID), after: JSON(gblCrudResult), result: "OK", error: ""}))
);
Select(btnLogCrud);
```

Delete:

```
Set(gblCrud, {source: "Enrollments", op: "Delete", id: Text(ThisItem.ID), before: JSON(ThisItem), after: "", batchId: ""});
IfError(
    Remove(Enrollments, ThisItem),
    Set(gblCrud, Patch(gblCrud, {result: "Error", error: FirstError.Message})),
    Set(gblCrud, Patch(gblCrud, {result: "OK", error: ""}))
);
Select(btnLogCrud);
```

Bulk (entry 24): set `batchId: GUID()` once, then run the single-write pattern inside `ForAll`, calling `Select(btnLogCrud)` per row. `ForAll` cannot call `Select`; instead collect audit rows into `colCrudBuffer` directly inside the loop (see step 3) and flush after.

3. **The logger.** Hidden `btnLogCrud.OnSelect`:

```
With({
    b: If(IsBlank(gblCrud.before), Blank(), ParseJSON(gblCrud.before)),
    a: If(IsBlank(gblCrud.after), Blank(), ParseJSON(gblCrud.after)),
    fields: Split(LookUp(tblSources, name = gblCrud.source).writable, ",")
},
    Collect(colCrudBuffer, {
        Title: gblCrud.op,
        Source: gblCrud.source,
        RecordId: gblCrud.id,
        UserEmail: gblUserEmail,
        SessionId: gblSession.id,
        ActionSeq: gblSession.seq,
        Screen: App.ActiveScreen.Name,
        Before: gblCrud.before,
        After: gblCrud.after,
        ChangedFields: If(gblCrud.op = "Update" && !IsBlank(b) && !IsBlank(a),
            Concat(Filter(fields, fxJsonField(b, Value) <> fxJsonField(a, Value)), Value, ","),
            ""),
        Result: gblCrud.result,
        ErrorText: Coalesce(gblCrud.error, ""),
        BatchId: gblCrud.batchId,
        ClientTs: Now(),
        AppVersion: gblAppVersion
    })
);
// also feed the undo stack (entry 10)
If(gblCrud.result = "OK" && gblCrud.op in ["Update", "Delete"],
    Collect(colUndo, {source: gblCrud.source, id: Value(gblCrud.id), before: gblCrud.before, at: Now()})
);
```

`fxJsonField(obj, name)` reads a field from an untyped object by name. Power Fx cannot index untyped objects dynamically, so implement it as a `Switch` over the union of all writable field names across `tblSources` returning `Text(obj.FieldName)`. Generate this `Switch` from `tblSources` at build time and keep it in the harness as a generated artifact.

4. **Flush.** Reuse `tmrFlush` from entry 41; flush `colCrudBuffer` to `CrudAudit` with the same put-back-on-failure logic. Flush CRUD rows before action rows so the audit is never behind the activity log.

5. **Read logging (optional).** Log `Read` only for sensitive sources (e.g., `Certifications`) on record detail screen `OnVisible`: `Set(gblCrud, {source: "Certifications", op: "Read", id: Text(locRecord.ID), before: "", after: "", result: "OK"}); Select(btnLogCrud)`. Do not log gallery loads.

6. **Flow-side writes.** Every Flow that writes to a tracked list adds a "Create item" in `CrudAudit` with `UserEmail = "flow:<FlowName>"`, `SessionId = <run id>`, `Before` from the pre-update "Get item", `After` from the update response. This closes the gap where the app is not the writer.

7. **Admin screen `scrCrudAudit`.**

   - Filters: source dropdown (from `tblSources` plus "All"), operation multi-select, user, date range, record ID search, result (OK/Error).
   - Gallery: time, user, source, op, record ID, changed fields, result. Row color by op via `gblTheme`.
   - Detail panel: side-by-side Before/After with a field-level diff gallery:

```
ClearCollect(colDiff,
    With({b: ParseJSON(galAudit.Selected.Before), a: ParseJSON(galAudit.Selected.After),
          fields: Split(LookUp(tblSources, name = galAudit.Selected.Source).writable, ",")},
        Filter(
            AddColumns(fields, before, fxJsonField(b, Value), after, fxJsonField(a, Value)),
            before <> after
        )
    )
);
```

   - Per-source tab strip: tapping a source shows counts of Create/Update/Delete/Error for the selected range as SVG bars (entry 1).
   - "All sources" view: a stacked bar per day across sources.
   - Record history: entering a record ID shows every operation ever performed on it, oldest first, with a "Restore to this version" button that patches `Before` (or `After`) of the selected row back through the wrapper with `op = "Undo"`.
   - Export: button that calls Flow `AUDIT-Export` to produce a CSV in OneDrive for the filtered range.

8. **Retention.** `AUDIT-Archive` monthly: rows older than 365 days move to `CrudAuditArchive`. Never delete without archiving; note the retention decision in the decision log with the HCT records officer's input.

**Gotchas.**
- `JSON()` on a SharePoint record includes lookup and person columns as nested objects; that is fine for snapshots but `fxJsonField` should return `Text(obj.Field.Value)` for choice columns and `Text(obj.Field.Email)` for person columns.
- `JSON(ThisItem)` inside a gallery works; `JSON()` of a data source row fetched with `LookUp` also works. `JSON` requires the corresponding feature to be enabled in older apps.
- Snapshots on lists with large multi-line text fields can approach the 255-char limit if you accidentally use a single-line column. `Before` and `After` must be multi-line plain text.
- Delegation: filter `CrudAudit` by indexed columns first (Source, UserEmail, ClientTs), then apply non-delegable filters locally.
- If a screen shows both the action log and CRUD audit, join on `SessionId` and `ActionSeq` to show "the user clicked X, which caused these 12 writes."

**Done when.**
- Zero bare `Patch`/`Remove`/`Collect` calls against data sources remain in the app (verify with the harness lint step: search the app's YAML export for `Patch(` not preceded by `Set(gblCrud`).
- Every write from app or Flow appears in `CrudAudit` within 15 seconds.
- Admin can answer "who changed Capacity on event 4412 and what was it before" in under 30 seconds.
- Restoring a prior version works and itself produces an audit row with `op = "Undo"`.

---

## Part F. Build order recommendation

For TRACS, implement in this order so later entries can depend on earlier ones:

1. Entry 13 (feature flags), 18 (version stamp), 0.2 conventions
2. Entry 4 (modal), 5 (toast), 7 (skeleton) into the component library (37)
3. Entry 42 (CRUD audit) and 41 (action log), since every subsequent write should be wrapped from day one
4. Entry 16 (delta sync), 15 (optimistic UI), 10 (undo)
5. Entry 11 (rules), 12 (config screens), 40 (living help)
6. Entry 1, 2 (SVG engine and icons), then 20, 23, 26, 36 (visuals and analytics)
7. Entry 17 (safe write), 25 (waitlist), 24 (bulk enroll), 21, 22
8. Entry 27, 28, 31, 35, 33
9. Everything else as demand appears

## Part G. Harness additions

Add to the Power Apps Principal Engineer harness v2.1 checklist:

- [ ] Every data source write uses the CRUD wrapper (entry 42).
- [ ] Every `Navigate` uses `fxNav` (entry 41).
- [ ] Every `OnSelect` begins with `fxLog`.
- [ ] New UI is behind a feature flag (entry 13).
- [ ] No hardcoded colors; all from `gblTheme`.
- [ ] `tblSources` updated when a new data source is added, and the `fxJsonField` switch regenerated.
- [ ] Decision log entry for any entry marked with a GCC availability caveat (5, 15, 19, 21, 30).
