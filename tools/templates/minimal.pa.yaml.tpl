# ---------------------------------------------------------------------------
# Slate — minimal proof of concept. Eight icons, four controls' worth of ideas.
#
# Paste this first. If these eight icons render, the technique works on your
# tenant and the full browser (src/slate-icon-browser.pa.yaml) will too.
#
# Icon artwork: Google Material Design Icons, Apache License 2.0. See NOTICE.md.
# ---------------------------------------------------------------------------
Screens:
  scrSlateMinimal:
    Properties:
      Fill: =RGBA(255, 255, 255, 1)
      OnVisible: |
        =ClearCollect(
            colSlateIcons,
            Table(
{{ICON_ROWS}}
            )
        );
    Children:
      - lblSlateMinimalTitle:
          Control: Label
          Properties:
            X: =40
            Y: =32
            Width: =700
            Height: =32
            Text: ="Slate — inline SVG icons, no media files"
            Size: =16
            FontWeight: =FontWeight.Semibold

      - galSlateMinimal:
          Control: Gallery
          Variant: BrowseLayout_Vertical_TwoTextOneImage_VariantA_ver5.0
          Properties:
            X: =40
            Y: =88
            Width: =720
            Height: =180
            Layout: =Layout.Vertical
            WrapCount: =8
            TemplateSize: =120
            TemplatePadding: =0
            Items: =colSlateIcons
          Children:
            - imgSlateMinimalIcon:
                Control: Image
                Properties:
                  Width: =48
                  Height: =48
                  X: =(Parent.TemplateWidth - Self.Width) / 2
                  Y: =16
                  ImagePosition: =ImagePosition.Fit
                  Image: |
                    ="data:image/svg+xml;utf8," & EncodeUrl(
                        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 24 24"" fill=""#1F3864""><path d=""" &
                        ThisItem.Path & """/></svg>"
                    )

            - lblSlateMinimalName:
                Control: Label
                Properties:
                  X: =4
                  Y: =72
                  Width: =Parent.TemplateWidth - 8
                  Height: =36
                  Text: =ThisItem.Name
                  Size: =8
                  Align: =Align.Center
                  Wrap: =true

      # A single icon with no collection at all — the path data lives inline.
      # This is the pattern to reach for on a one-off button or header.
      - imgSlateInline:
          Control: Image
          Properties:
            X: =40
            Y: =300
            Width: =64
            Height: =64
            ImagePosition: =ImagePosition.Fit
            Image: |
              ="data:image/svg+xml;utf8," & EncodeUrl(
                  "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 24 24"" fill=""#A4262C""><path d=""M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z""/></svg>"
              )

      - lblSlateInlineNote:
          Control: Label
          Properties:
            X: =120
            Y: =300
            Width: =640
            Height: =64
            Text: |
              ="No collection needed for a one-off: the path data sits directly in the Image property. Change the fill hex to recolour it — the same glyph, any colour, zero extra assets."
            Size: =10
            Color: =RGBA(96, 94, 92, 1)
            VerticalAlign: =VerticalAlign.Middle
            Wrap: =true
