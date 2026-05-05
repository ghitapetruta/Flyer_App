"""
app.py — Generator Flyer & Etichete (Metalcom)

UI bold & corporate cu landing page și navigare prin sidebar.

Rulare:
    pip install -r requirements.txt
    streamlit run app.py
"""
import streamlit as st


# ══════════════════════════════════════════════════════════════
# CONFIGURAȚIE PAGINĂ
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Generator Flyer & Etichete · Metalcom",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ══════════════════════════════════════════════════════════════
# PALETĂ BRAND METALCOM
# ══════════════════════════════════════════════════════════════
BRAND = {
    "red":        "#A11319",
    "red_dark":   "#7A0E13",
    "red_light":  "#D43A40",
    "grey":       "#565757",
    "grey_dark":  "#1C1C1C",
    "grey_light": "#F4F4F2",
    "border":     "#E5E2DD",
}


# ══════════════════════════════════════════════════════════════
# CSS GLOBAL — STIL BOLD & CORPORATE
# ══════════════════════════════════════════════════════════════
GLOBAL_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');

/* ── Global ── */
html, body, [class*="css"] {{
    font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}}

/* Reset padding-uri Streamlit */
.main .block-container {{
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}}

/* Ascund header-ul default Streamlit */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    height: 0;
}}

/* Butoane primary - roșu corporate */
.stButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"] {{
    background: {BRAND['red']} !important;
    color: white !important;
    border: none !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    padding: 12px 24px !important;
    border-radius: 4px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(161, 19, 25, 0.25) !important;
}}
.stButton > button[kind="primary"]:hover,
.stDownloadButton > button[kind="primary"]:hover {{
    background: {BRAND['red_dark']} !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 14px rgba(161, 19, 25, 0.4) !important;
}}

/* Butoane secondary */
.stButton > button:not([kind="primary"]),
.stDownloadButton > button:not([kind="primary"]) {{
    background: white !important;
    color: {BRAND['grey_dark']} !important;
    border: 1.5px solid {BRAND['border']} !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
    border-radius: 4px !important;
    padding: 10px 20px !important;
    transition: all 0.2s ease !important;
}}
.stButton > button:not([kind="primary"]):hover,
.stDownloadButton > button:not([kind="primary"]):hover {{
    border-color: {BRAND['red']} !important;
    color: {BRAND['red']} !important;
}}

/* Tab-uri — accent roșu cu underline gros */
.stTabs [data-baseweb="tab-list"] {{
    gap: 8px;
    border-bottom: 2px solid {BRAND['border']};
    padding-bottom: 0;
}}
.stTabs [data-baseweb="tab"] {{
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
    color: {BRAND['grey']} !important;
    padding: 12px 20px !important;
    border-radius: 4px 4px 0 0 !important;
    background: transparent !important;
    border-bottom: 3px solid transparent !important;
    transition: all 0.2s ease !important;
}}
.stTabs [data-baseweb="tab"]:hover {{
    color: {BRAND['red']} !important;
    background: {BRAND['grey_light']} !important;
}}
.stTabs [aria-selected="true"] {{
    color: {BRAND['red']} !important;
    border-bottom: 3px solid {BRAND['red']} !important;
    background: transparent !important;
}}

/* Headings cu accent vertical roșu */
h1 {{
    color: {BRAND['grey_dark']} !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
    font-size: 2.2rem !important;
}}
h2, h3 {{
    color: {BRAND['grey_dark']} !important;
    font-weight: 700 !important;
}}

/* Carduri pentru metrice */
[data-testid="stMetric"] {{
    background: white;
    border: 1px solid {BRAND['border']};
    border-left: 4px solid {BRAND['red']};
    padding: 16px 20px;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}}
[data-testid="stMetricLabel"] {{
    font-weight: 600 !important;
    color: {BRAND['grey']} !important;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    font-size: 12px !important;
}}
[data-testid="stMetricValue"] {{
    color: {BRAND['grey_dark']} !important;
    font-weight: 800 !important;
}}

/* Inputs cu accent roșu la focus */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {{
    border-radius: 4px !important;
    border: 1.5px solid {BRAND['border']} !important;
    transition: border-color 0.15s ease !important;
}}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {{
    border-color: {BRAND['red']} !important;
    box-shadow: 0 0 0 2px rgba(161, 19, 25, 0.1) !important;
}}

/* Selectbox & radio */
.stSelectbox > div > div {{
    border-radius: 4px !important;
}}

/* File uploader — bold border */
[data-testid="stFileUploader"] section {{
    border: 2px dashed {BRAND['border']} !important;
    background: {BRAND['grey_light']} !important;
    border-radius: 6px !important;
    transition: border-color 0.2s ease !important;
}}
[data-testid="stFileUploader"] section:hover {{
    border-color: {BRAND['red']} !important;
}}

/* Alerts/Info — accent corporate */
[data-testid="stAlert"] {{
    border-radius: 6px !important;
    border-left-width: 4px !important;
}}

/* Expander */
.streamlit-expanderHeader {{
    background: {BRAND['grey_light']} !important;
    border-radius: 4px !important;
    font-weight: 600 !important;
}}

/* Divider mai subtil */
hr {{
    border-color: {BRAND['border']} !important;
    margin: 1.5rem 0 !important;
}}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {BRAND['grey_dark']} 0%, #2A2A2A 100%);
}}
[data-testid="stSidebar"] * {{
    color: white !important;
}}
[data-testid="stSidebar"] .stRadio label {{
    background: rgba(255,255,255,0.05);
    padding: 12px 16px !important;
    border-radius: 6px;
    margin-bottom: 6px !important;
    border-left: 3px solid transparent;
    transition: all 0.2s ease;
    font-weight: 600 !important;
    letter-spacing: 0.3px;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: rgba(255,255,255,0.1) !important;
    border-left-color: {BRAND['red_light']};
}}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"] input:checked + div {{
    background: {BRAND['red']} !important;
}}

/* Buton din sidebar - alb pe fundal închis */
[data-testid="stSidebar"] .stButton > button {{
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1.5px solid rgba(255,255,255,0.2) !important;
    font-weight: 600 !important;
}}
[data-testid="stSidebar"] .stButton > button:hover {{
    background: {BRAND['red']} !important;
    border-color: {BRAND['red']} !important;
    color: white !important;
}}

[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.15) !important;
}}

/* ── HERO BANNER (header pe modul) ── */
.brand-hero {{
    background: linear-gradient(135deg, {BRAND['red']} 0%, {BRAND['red_dark']} 100%);
    color: white;
    padding: 32px 40px;
    border-radius: 8px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(161, 19, 25, 0.2);
}}
.brand-hero::before {{
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 200px;
    height: 100%;
    background: rgba(255,255,255,0.05);
    transform: skewX(-20deg) translateX(50px);
}}
.brand-hero-cat {{
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0.85;
    margin-bottom: 8px;
}}
.brand-hero-title {{
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.1;
    margin-bottom: 8px;
    color: white !important;
}}
.brand-hero-subtitle {{
    font-size: 15px;
    opacity: 0.9;
    font-weight: 400;
}}

/* ── LANDING PAGE ── */
.landing-container {{
    text-align: center;
    padding: 40px 0;
}}
.landing-hero {{
    margin-bottom: 60px;
}}
.landing-brand {{
    color: {BRAND['red']};
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 16px;
}}
.landing-title {{
    font-size: 56px !important;
    font-weight: 900 !important;
    color: {BRAND['grey_dark']} !important;
    letter-spacing: -1.5px !important;
    line-height: 1.05 !important;
    margin-bottom: 20px !important;
}}
.landing-title > span {{
    color: {BRAND['grey_dark']} !important;
}}
.landing-title span span {{
    color: {BRAND['red']} !important;
}}
.landing-subtitle {{
    font-size: 19px;
    color: {BRAND['grey']};
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.5;
    font-weight: 400;
}}

.module-card {{
    background: white;
    border: 2px solid {BRAND['border']};
    border-radius: 12px;
    padding: 40px 32px;
    text-align: left;
    height: 100%;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}}
.module-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 6px;
    background: {BRAND['red']};
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}}
.module-card:hover {{
    border-color: {BRAND['red']};
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(161, 19, 25, 0.15);
}}
.module-card:hover::before {{
    transform: scaleX(1);
}}
.module-icon {{
    font-size: 48px;
    margin-bottom: 20px;
    display: block;
}}
.module-card-title {{
    font-size: 28px;
    font-weight: 800;
    color: {BRAND['grey_dark']};
    margin-bottom: 12px;
    letter-spacing: -0.3px;
}}
.module-card-desc {{
    font-size: 15px;
    color: {BRAND['grey']};
    line-height: 1.6;
    margin-bottom: 24px;
}}
.module-features {{
    list-style: none;
    padding: 0;
    margin: 0 0 28px 0;
}}
.module-features li {{
    color: {BRAND['grey_dark']};
    font-size: 14px;
    padding: 6px 0 6px 28px;
    position: relative;
    line-height: 1.4;
}}
.module-features li::before {{
    content: '▶';
    position: absolute;
    left: 0;
    color: {BRAND['red']};
    font-size: 10px;
    top: 10px;
}}
.module-output {{
    display: inline-block;
    background: {BRAND['grey_light']};
    color: {BRAND['grey_dark']};
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-right: 6px;
    margin-bottom: 6px;
}}
.module-output.red {{
    background: {BRAND['red']};
    color: white;
}}

/* Footer corporate */
.app-footer {{
    text-align: center;
    color: {BRAND['grey']};
    font-size: 12px;
    padding: 20px 0;
    border-top: 1px solid {BRAND['border']};
    margin-top: 40px;
    letter-spacing: 0.5px;
}}
.app-footer .brand {{
    color: {BRAND['red']};
    font-weight: 700;
}}

/* Data editor styling */
[data-testid="stDataEditor"] {{
    border: 1px solid {BRAND['border']};
    border-radius: 6px;
    overflow: hidden;
}}

/* Spinner colorat brand */
.stSpinner > div > div {{
    border-top-color: {BRAND['red']} !important;
}}

/* Color picker */
[data-testid="stColorPickerBlock"] > div {{
    border: 1.5px solid {BRAND['border']} !important;
    border-radius: 4px !important;
}}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# SESSION STATE — MOD CURENT
# ══════════════════════════════════════════════════════════════
if "app_mode" not in st.session_state:
    st.session_state.app_mode = "landing"  # landing | flyer | labels


def go_to(mode: str):
    """Setează modul curent (folosit de butoanele din landing)."""
    st.session_state.app_mode = mode


# ══════════════════════════════════════════════════════════════
# SIDEBAR — NAVIGARE
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    # Brand header
    st.markdown(f"""
    <div style="text-align: center; padding: 20px 0 24px 0; border-bottom: 1px solid rgba(255,255,255,0.15); margin-bottom: 24px;">
        <div style="font-size: 11px; letter-spacing: 4px; opacity: 0.7; margin-bottom: 8px;">METALCOM</div>
        <div style="font-size: 22px; font-weight: 800; letter-spacing: -0.5px;">PRINT TOOLS</div>
        <div style="width: 40px; height: 3px; background: {BRAND['red']}; margin: 12px auto 0;"></div>
    </div>
    """, unsafe_allow_html=True)

    # Navigare
    st.markdown("##### MOD DE LUCRU")

    if st.session_state.app_mode == "landing":
        st.markdown(
            f"""<div style="padding: 16px; background: rgba(255,255,255,0.05); border-radius: 6px;
            border-left: 3px solid {BRAND['red']}; font-size: 13px; line-height: 1.5;">
            👋 Bun venit! Alege un instrument din pagina principală.
            </div>""",
            unsafe_allow_html=True
        )
    else:
        # Selector activ
        current_label = "📄 Flyer" if st.session_state.app_mode == "flyer" else "🏷️ Etichete"
        new_choice = st.radio(
            "Selectează instrument:",
            options=["📄 Flyer", "🏷️ Etichete"],
            index=0 if st.session_state.app_mode == "flyer" else 1,
            label_visibility="collapsed",
            key="sidebar_mode_selector",
        )
        if new_choice == "📄 Flyer" and st.session_state.app_mode != "flyer":
            st.session_state.app_mode = "flyer"
            st.rerun()
        elif new_choice == "🏷️ Etichete" and st.session_state.app_mode != "labels":
            st.session_state.app_mode = "labels"
            st.rerun()

        st.divider()
        if st.button("⬅ Înapoi la dashboard", use_container_width=True):
            st.session_state.app_mode = "landing"
            st.rerun()

    st.divider()

    # Informații contextuale
    if st.session_state.app_mode == "flyer":
        st.markdown("""
        ##### 📄 GENERATOR FLYER

        Broșuri A4 cu produse, imagini, prețuri, badge-uri.

        **Output:** HTML + PPTX
        """)
    elif st.session_state.app_mode == "labels":
        st.markdown("""
        ##### 🏷️ GENERATOR ETICHETE

        Coli adezive A4 cu cod, denumire și preț.

        **Output:** HTML
        """)
    else:
        st.markdown("""
        ##### ℹ️ DESPRE

        Instrumente interne de print pentru generarea materialelor de produs.
        """)

    st.divider()
    st.caption("v2.0 · Streamlit")


# ══════════════════════════════════════════════════════════════
# LANDING PAGE
# ══════════════════════════════════════════════════════════════
def render_landing():
    """Dashboard de pornire cu 2 carduri-instrument."""
    st.markdown(f"""
    <div class="landing-container">
        <div class="landing-hero">
            <div class="landing-brand">METALCOM · PRINT TOOLS</div>
            <h1 class="landing-title">Generator de <span>materiale</span><br>pentru produse</h1>
            <p class="landing-subtitle">
                Două instrumente într-o singură aplicație. Configurează, editează,
                și descarcă rapid materiale gata de printat sau publicat.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Cele 2 carduri-instrument
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
        <div class="module-card">
            <span class="module-icon">📄</span>
            <h3 class="module-card-title">Flyer</h3>
            <p class="module-card-desc">
                Broșuri A4 cu produse, imagini, badge-uri și prețuri.
                Personalizare completă a stilului și layout-ului.
            </p>
            <ul class="module-features">
                <li>7 layout-uri diferite (1-6 produse/pagină)</li>
                <li>3 atribute personalizabile per produs</li>
                <li>Import Excel + tabel editabil</li>
                <li>Imagini și badge-uri custom</li>
                <li>Editor de stil complet (culori, fonturi)</li>
            </ul>
            <div>
                <span class="module-output red">HTML</span>
                <span class="module-output red">PPTX</span>
                <span class="module-output">PDF (din browser)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
        if st.button("📄  Deschide Generator Flyer  →",
                     key="open_flyer", use_container_width=True, type="primary"):
            go_to("flyer")
            st.rerun()

    with col2:
        st.markdown(f"""
        <div class="module-card">
            <span class="module-icon">🏷️</span>
            <h3 class="module-card-title">Etichete</h3>
            <p class="module-card-desc">
                Coli adezive A4 cu etichete pentru produse: cod, denumire, preț.
                Layout flexibil pentru orice format de coală.
            </p>
            <ul class="module-features">
                <li>Layout flexibil 1-5 coloane × 1-12 rânduri</li>
                <li>Logo opțional pe fiecare etichetă</li>
                <li>Suport pentru reducere (preț tăiat + badge %)</li>
                <li>Import Excel + tabel editabil</li>
                <li>Validare automată că încap pe pagină</li>
            </ul>
            <div>
                <span class="module-output red">HTML</span>
                <span class="module-output">PDF (din browser)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
        if st.button("🏷️  Deschide Generator Etichete  →",
                     key="open_labels", use_container_width=True, type="primary"):
            go_to("labels")
            st.rerun()


# ══════════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════════
if st.session_state.app_mode == "landing":
    render_landing()
elif st.session_state.app_mode == "flyer":
    from flyer_ui import render as render_flyer
    render_flyer()
elif st.session_state.app_mode == "labels":
    from labels_ui import render as render_labels
    render_labels()


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="app-footer">
    <span class="brand">METALCOM</span> · Print Tools v2.0 · Construit cu Streamlit
</div>
""", unsafe_allow_html=True)
