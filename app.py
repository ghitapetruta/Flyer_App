"""
app.py — Aplicație Streamlit cu două funcționalități:

  • Generator Flyer  — flyere A4 cu produse (HTML + PPTX)
  • Generator Etichete — etichete A4 (cod, denumire, preț) — HTML

Rulare:
    pip install -r requirements.txt
    streamlit run app.py

Apoi se deschide automat în browser. Funcționează identic pe desktop și mobil.
"""
import streamlit as st


# ── CONFIGURAȚIE PAGINĂ ────────────────────────────────────────
st.set_page_config(
    page_title="Generator Flyer & Etichete",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── STIL CUSTOM GLOBAL ─────────────────────────────────────────
st.markdown("""
<style>
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .stButton > button {
        width: 100%;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .preview-box {
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        background: #fafafa;
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    h1 { color: #A11319; }

    /* Sidebar — selector mod */
    [data-testid="stSidebar"] .stRadio > label {
        font-weight: 600;
        font-size: 16px;
    }
    [data-testid="stSidebar"] .stRadio > div {
        gap: 12px;
    }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR — SELECTOR MOD ─────────────────────────────────────
with st.sidebar:
    st.markdown("### 🎯 Mod de lucru")
    mode = st.radio(
        "Alege ce vrei să generezi:",
        options=["📄 Flyer", "🏷️ Etichete"],
        index=0,
        label_visibility="collapsed",
    )

    st.divider()

    if mode == "📄 Flyer":
        st.markdown(
            "**Flyer A4** — broșuri cu produse, "
            "imagini, prețuri, badge-uri. Output: HTML + PPTX."
        )
    else:
        st.markdown(
            "**Etichete A4** — coli adezive cu cod, "
            "denumire, preț. Layout flexibil 1-5 coloane. Output: HTML."
        )

    st.divider()
    st.caption("💡 Construit pe Streamlit · funcționează pe desktop și mobil")


# ── ROUTER ─────────────────────────────────────────────────────
if mode == "📄 Flyer":
    from flyer_ui import render as render_flyer
    render_flyer()
else:
    from labels_ui import render as render_labels
    render_labels()


# ── FOOTER ─────────────────────────────────────────────────────
st.divider()
st.caption("💡 Generator Flyer & Etichete · Streamlit · ad-free, open-source")
