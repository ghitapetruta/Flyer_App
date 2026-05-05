"""
labels_engine.py — motor de generare etichete A4 cu buton »Descarcă PDF« încorporat.

Bazat pe scripturile generate_labels.py / generate_labels_3col.py, dar generalizat:
- Layout flexibil: orice combinație cols × rows
- Dimensiuni parametrizabile (margini, gap-uri, înălțime etichetă)
- Logo opțional (bytes -> embed base64)
- Output HTML auto-conține butoane "Descarcă PDF" și "Tipărește"

Folosit de aplicația Streamlit (label_ui.py).
"""
from __future__ import annotations
import base64
from typing import Optional


# ══════════════════════════════════════════════════════════════
# DEFAULTS
# ══════════════════════════════════════════════════════════════
DEFAULT_LABEL_CONFIG = {
    "cols": 2,                  # număr coloane
    "rows": 8,                  # număr rânduri
    "label_height_mm": 31,      # înălțime etichetă (mm)
    "page_margin_mm": 8,        # margini A4 (mm)
    "gap_h_mm": 4,              # spațiu orizontal între etichete
    "gap_v_mm": 2,              # spațiu vertical între etichete
    "moneda": "Lei",            # text afișat după preț
    "tva_text": "TVA Inclus",   # text mic sub preț
    "color_red": "#C8102E",     # culoarea pentru prețul redus / badge reducere
}


# ══════════════════════════════════════════════════════════════
# FORMATARE
# ══════════════════════════════════════════════════════════════
def fmt_price(v) -> str:
    """Formatează un număr ca preț cu 2 zecimale."""
    if v is None or v == "":
        return ""
    try:
        num = float(v)
    except (ValueError, TypeError):
        return str(v)
    if num == int(num):
        return f"{int(num)}.00"
    return f"{num:.2f}"


def fmt_reducere(v) -> str:
    """Formatează reducerea ca procent."""
    if v is None or v == "":
        return ""
    try:
        num = float(v)
    except (ValueError, TypeError):
        return ""
    return f"{int(num)}%" if num == int(num) else f"{num:.1f}%"


def prepare_labels(products: list[dict]) -> list[dict]:
    """Adaugă câmpurile pre-formatate pentru afișare."""
    labels = []
    for p in products:
        pret = p.get("pret")
        pret_redus = p.get("pret_redus")
        labels.append({
            "cod": str(p.get("cod", "")).strip(),
            "denumire": str(p.get("denumire", "")).strip(),
            "um": str(p.get("um", "buc")).strip() or "buc",
            "pret": pret,
            "pret_fmt": fmt_price(pret),
            "reducere": p.get("reducere"),
            "reducere_fmt": fmt_reducere(p.get("reducere")),
            "pret_redus": pret_redus,
            "pret_redus_fmt": fmt_price(pret_redus),
            "are_reducere": (
                pret_redus is not None
                and str(pret_redus).strip() != ""
                and pret is not None
                and str(pret).strip() != ""
            ),
        })
    return labels


def chunk_pages(labels: list[dict], per_page: int) -> list[list]:
    """Împarte etichetele pe pagini. Ultima pagină se completează cu None."""
    pages = []
    for i in range(0, len(labels), per_page):
        page = labels[i:i + per_page]
        while len(page) < per_page:
            page.append(None)
        pages.append(page)
    return pages


# ══════════════════════════════════════════════════════════════
# IMAGE HELPER
# ══════════════════════════════════════════════════════════════
def logo_to_b64(img_bytes: Optional[bytes]) -> str:
    """Convertește bytes -> string base64 pentru embed în CSS."""
    if not img_bytes:
        return ""
    try:
        return base64.b64encode(img_bytes).decode("ascii")
    except Exception:
        return ""


# ══════════════════════════════════════════════════════════════
# CSS DINAMIC
# ══════════════════════════════════════════════════════════════
def _scale_factor(cols: int) -> dict:
    """Returnează un set de dimensiuni adaptate la numărul de coloane.

    Mai multe coloane = etichete mai înguste = font-uri și padding-uri mai mici.
    """
    if cols <= 1:
        return {
            "denumire_pt": 13, "cod_pt": 12, "label_pt": 11,
            "pret_pt": 28, "pret_suffix_pt": 9,
            "pret_vechi_pt": 14, "reducere_pt": 12,
            "logo_w_mm": 22, "logo_h_mm": 11,
            "padding_v_mm": 2.5, "padding_h_mm": 3,
            "line_clamp": 2, "gap_mm": 6,
        }
    if cols == 2:
        return {
            "denumire_pt": 11, "cod_pt": 10, "label_pt": 10,
            "pret_pt": 22, "pret_suffix_pt": 8,
            "pret_vechi_pt": 12, "reducere_pt": 11,
            "logo_w_mm": 18, "logo_h_mm": 9,
            "padding_v_mm": 2, "padding_h_mm": 2.5,
            "line_clamp": 2, "gap_mm": 5,
        }
    if cols == 3:
        return {
            "denumire_pt": 8.5, "cod_pt": 10, "label_pt": 7,
            "pret_pt": 15, "pret_suffix_pt": 7.5,
            "pret_vechi_pt": 9, "reducere_pt": 7.5,
            "logo_w_mm": 11, "logo_h_mm": 6,
            "padding_v_mm": 1.5, "padding_h_mm": 2,
            "line_clamp": 2, "gap_mm": 2.5,
        }
    if cols == 4:
        return {
            "denumire_pt": 7.5, "cod_pt": 8.5, "label_pt": 6.5,
            "pret_pt": 12, "pret_suffix_pt": 6.5,
            "pret_vechi_pt": 8, "reducere_pt": 6.5,
            "logo_w_mm": 9, "logo_h_mm": 5,
            "padding_v_mm": 1.2, "padding_h_mm": 1.5,
            "line_clamp": 2, "gap_mm": 1.8,
        }
    # 5+ coloane
    return {
        "denumire_pt": 6.5, "cod_pt": 7.5, "label_pt": 5.5,
        "pret_pt": 10, "pret_suffix_pt": 5.5,
        "pret_vechi_pt": 7, "reducere_pt": 5.5,
        "logo_w_mm": 7, "logo_h_mm": 4,
        "padding_v_mm": 1, "padding_h_mm": 1.2,
        "line_clamp": 2, "gap_mm": 1.5,
    }


def build_css(cfg: dict, logo_b64: str = "") -> str:
    """Construiește CSS-ul complet pe baza configurației."""
    cols = int(cfg.get("cols", 2))
    rows = int(cfg.get("rows", 8))
    label_h = float(cfg.get("label_height_mm", 31))
    margin = float(cfg.get("page_margin_mm", 8))
    gap_h = float(cfg.get("gap_h_mm", 4))
    gap_v = float(cfg.get("gap_v_mm", 2))
    color_red = cfg.get("color_red", "#C8102E")

    s = _scale_factor(cols)
    page_w = 210 - 2 * margin
    page_h = 297 - 2 * margin
    col_pct = round(100 / cols, 2)

    return f"""
@page {{
  size: A4 portrait;
  margin: {margin}mm;
}}

* {{ box-sizing: border-box; }}

html, body {{
  margin: 0; padding: 0;
  font-family: Arial, Helvetica, sans-serif;
  color: #000;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

body {{ background: #888; padding: 24px 16px; }}

.page {{
  width: {page_w}mm;
  height: {page_h}mm;
  background: #fff;
  margin: 0 auto 24px;
  box-shadow: 0 4px 24px rgba(0,0,0,.25);
  display: flex;
  align-items: center;
  justify-content: center;
}}
.page + .page {{ page-break-before: always; }}

.grid {{
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}}
.grid td {{
  width: {col_pct}%;
  padding: {gap_v / 2}mm {gap_h / 2}mm;
  vertical-align: top;
}}
.grid tr:first-child td {{ padding-top: 0; }}
.grid tr:last-child td {{ padding-bottom: 0; }}
.grid td:first-child {{ padding-left: 0; }}
.grid td:last-child {{ padding-right: 0; }}

.label {{
  width: 100%;
  height: {label_h}mm;
  border: 0.3mm solid #000;
  padding: {s["padding_v_mm"]}mm {s["padding_h_mm"]}mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
}}
.label-empty {{
  border: none;
  height: {label_h}mm;
}}

.row-top {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1.5mm;
}}
.denumire {{
  font-size: {s["denumire_pt"]}pt;
  font-weight: bold;
  line-height: 1.1;
  text-transform: uppercase;
  flex: 1;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: {s["line_clamp"]};
  -webkit-box-orient: vertical;
}}

.logo {{
  flex-shrink: 0;
  width: {s["logo_w_mm"]}mm;
  height: {s["logo_h_mm"]}mm;
  {f'background-image: url("data:image/png;base64,{logo_b64}");' if logo_b64 else ""}
  background-repeat: no-repeat;
  background-position: right top;
  background-size: contain;
}}

.cod-line {{
  font-size: {s["cod_pt"]}pt;
  line-height: 1;
}}
.cod-line .cod-val {{ font-weight: bold; }}

.pret-line {{
  display: flex;
  align-items: baseline;
  gap: {s["gap_mm"]}mm;
  line-height: 1;
  flex-wrap: wrap;
}}
.pret-label {{ font-size: {s["label_pt"]}pt; }}
.pret-val {{
  font-size: {s["pret_pt"]}pt;
  font-weight: bold;
  line-height: 1;
}}
.pret-suffix {{
  font-size: {s["pret_suffix_pt"]}pt;
  line-height: 1.15;
}}

.pret-vechi {{
  font-size: {s["pret_vechi_pt"]}pt;
  text-decoration: line-through;
  color: #555;
}}
.reducere-badge {{
  font-size: {s["reducere_pt"]}pt;
  font-weight: bold;
  color: {color_red};
  background: #fff3f3;
  border: 0.3mm solid {color_red};
  padding: 0.5mm 1.5mm;
  border-radius: 1.2mm;
}}
.pret-redus-val {{
  font-size: {s["pret_pt"]}pt;
  font-weight: bold;
  color: {color_red};
  line-height: 1;
}}

/* ===== Bara de acțiuni (vizibilă doar pe ecran) ===== */
.action-bar {{
  position: fixed;
  top: 12px;
  right: 12px;
  z-index: 9999;
  display: flex;
  gap: 8px;
  align-items: center;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 8px 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  font-family: Arial, sans-serif;
}}
.action-btn {{
  color: #fff;
  border: none;
  padding: 8px 16px;
  font-size: 14px;
  font-weight: bold;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}}
.btn-pdf {{ background: {color_red}; }}
.btn-pdf:hover {{ filter: brightness(0.85); }}
.btn-print {{ background: #333; }}
.btn-print:hover {{ background: #000; }}
.action-btn:disabled {{ background: #999 !important; cursor: wait; }}
.action-info {{ font-size: 12px; color: #666; padding: 0 4px; }}

@media print {{
  body {{ background: none !important; padding: 0; }}
  .page {{ box-shadow: none; margin: 0 auto; }}
  .action-bar {{ display: none !important; }}
}}
"""


# ══════════════════════════════════════════════════════════════
# HTML BUILDER
# ══════════════════════════════════════════════════════════════
def _build_label(lbl: dict, moneda: str, tva_text: str) -> str:
    """Construiește HTML-ul pentru o singură etichetă."""
    if lbl is None:
        return '<div class="label-empty"></div>'

    # Linia preț (cu sau fără reducere)
    if lbl["are_reducere"]:
        pret_block = (
            f'<span class="pret-vechi">{lbl["pret_fmt"]}</span>'
            + (f'<span class="reducere-badge">-{lbl["reducere_fmt"]}</span>'
               if lbl["reducere_fmt"] else "")
            + f'<span class="pret-redus-val">{lbl["pret_redus_fmt"]}</span>'
            + f'<span class="pret-suffix">{moneda} {tva_text}<br>/ {lbl["um"]}</span>'
        )
    else:
        pret_block = (
            f'<span class="pret-label">Preț:</span>'
            f'<span class="pret-val">{lbl["pret_fmt"]}</span>'
            f'<span class="pret-suffix">{moneda} {tva_text}<br>/ {lbl["um"]}</span>'
        )

    return f'''<div class="label">
      <div class="row-top">
        <div class="denumire">{lbl["denumire"]}</div>
        <div class="logo"></div>
      </div>
      <div class="cod-line">
        <span>Cod:</span>
        <span class="cod-val">{lbl["cod"]}</span>
      </div>
      <div class="pret-line">{pret_block}</div>
    </div>'''


def _build_page(page_labels: list, cols: int, rows: int,
                moneda: str, tva_text: str) -> str:
    """Construiește HTML-ul pentru o pagină A4 de etichete."""
    rows_html = []
    for r in range(rows):
        cells = []
        for c in range(cols):
            idx = r * cols + c
            lbl = page_labels[idx] if idx < len(page_labels) else None
            cells.append(f'<td>{_build_label(lbl, moneda, tva_text)}</td>')
        rows_html.append('<tr>' + ''.join(cells) + '</tr>')

    return f'''<div class="page">
  <table class="grid">
    {chr(10).join(rows_html)}
  </table>
</div>'''


def generate_html(products: list[dict],
                  cfg: Optional[dict] = None,
                  logo_b64: str = "") -> str:
    """Generează HTML-ul complet pentru etichete.

    Args:
        products: listă de dict-uri cu chei: cod, denumire, um, pret, reducere, pret_redus
        cfg: dict cu setări (vezi DEFAULT_LABEL_CONFIG); valorile lipsă iau default
        logo_b64: string base64 al logo-ului (opțional)

    Returns:
        HTML complet ca string.
    """
    config = dict(DEFAULT_LABEL_CONFIG)
    if cfg:
        config.update(cfg)

    cols = int(config["cols"])
    rows = int(config["rows"])
    per_page = cols * rows
    moneda = config.get("moneda", "Lei")
    tva_text = config.get("tva_text", "TVA Inclus")

    labels = prepare_labels(products)
    pages = chunk_pages(labels, per_page)

    css = build_css(config, logo_b64=logo_b64)

    pages_html = "\n".join(
        _build_page(p, cols, rows, moneda, tva_text) for p in pages
    )

    total_pages = len(pages)
    total_labels = len(labels)

    return f'''<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<title>Etichete</title>
<style>
{css}
</style>
</head>
<body>

<div class="action-bar">
  <span class="action-info">{total_pages} pagina(e) · {total_labels} etichete</span>
  <button class="action-btn btn-pdf" onclick="descarcaPDF()">⬇ Descarcă PDF</button>
  <button class="action-btn btn-print" onclick="window.print()">🖨 Tipărește</button>
</div>

{pages_html}

<script>
function descarcaPDF() {{
  // Folosim print-ul nativ al browserului. Utilizatorul alege "Save as PDF"
  // ca destinație și bifează "Background graphics".
  alert(
    "În fereastra de print care urmează:\\n" +
    "• Destinație: »Save as PDF«\\n" +
    "• Bifează: »Background graphics«\\n\\n" +
    "Apasă OK pentru a continua."
  );
  window.print();
}}
</script>

</body>
</html>'''
