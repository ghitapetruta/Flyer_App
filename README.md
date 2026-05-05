# 📄 Generator Flyer & Etichete — Aplicație Streamlit

Aplicație web cu **două funcționalități**, accesibile din sidebar:

1. **📄 Generator Flyer** — flyere A4 cu produse, imagini, prețuri, badge-uri, layout-uri multiple. Output: HTML + PPTX.
2. **🏷️ Generator Etichete** — coli adezive A4 cu cod, denumire, preț. Layout flexibil 1-5 coloane. Output: HTML.

Ambele funcționează din browser, pe orice device (desktop, mobil, tabletă).

---

## ✨ Ce poate face aplicația

### 📄 Modul Flyer
- Configurare antet (date firmă, logo, texte promoționale)
- Editare produse într-un tabel **+ import din Excel**
- 3 atribute personalizabile pe produs (ex. Adâncime, Înălțime, Finisaj)
- Personalizare completă (culori, fonturi, dimensiuni)
- Imagini per produs + badge-uri custom (text și pictograme)
- 7 layout-uri (1, 2, 3, 3a, 4, 5, 6 produse/pagină)
- Output: **HTML** (cu buton pentru salvare PDF din browser) + **PPTX** (importabil în Canva)

### 🏷️ Modul Etichete
- Editare produse într-un tabel **+ import din Excel** + descărcare model
- Logo opțional pe fiecare etichetă
- Layout flexibil: **1-5 coloane × 1-12 rânduri** (până la 60 etichete/pagină)
- Dimensiuni configurabile (înălțime etichetă, margini, spațiu între)
- Suport pentru reducere (preț tăiat + badge procent + preț nou)
- Validare automată dacă etichetele încap pe pagină
- Output: **HTML** cu buton încorporat pentru salvare ca PDF

---

## 🚀 Pornire rapidă (LOCAL)

### 1. Instalare Python
- **Windows / Mac**: descarcă de la [python.org/downloads](https://www.python.org/downloads/) (versiunea 3.10 sau mai nouă)
- La instalare pe Windows: **bifează „Add Python to PATH"**

### 2. Instalare biblioteci Python
Deschide **Terminal** (Mac) sau **cmd / PowerShell** (Windows) în folderul aplicației:

```bash
pip install -r requirements.txt
```

### 3. Pornire aplicație
```bash
streamlit run app.py
```

Se va deschide automat browserul la `http://localhost:8501`. În sidebar-ul din stânga alegi **Flyer** sau **Etichete**.

---

## 📱 Rulare pe mobil în aceeași rețea Wi-Fi

Când rulezi `streamlit run app.py`, în terminal vei vedea:

```
You can now view your Streamlit app in your browser.
  Local URL:    http://localhost:8501
  Network URL:  http://192.168.1.42:8501
```

Pe telefon/tabletă (conectat la **același Wi-Fi**), deschide browserul la **Network URL**.

---

## ☁️ Deploy pe Streamlit Cloud (recomandat)

1. **Cont GitHub** la [github.com](https://github.com)
2. Creează un repository nou și încarcă **fișierele**:
   - `app.py` (router)
   - `flyer_ui.py` și `flyer_engine.py` (modul Flyer)
   - `labels_ui.py` și `labels_engine.py` (modul Etichete)
   - `requirements.txt`
   - `packages.txt`
   - `README.md`
3. Mergi la [share.streamlit.io](https://share.streamlit.io) și loghează-te cu GitHub
4. Apasă **"New app"** → selectează repository-ul → **"Deploy"**
5. Aștepți 2-3 minute (instalează dependințele)
6. Primești URL public, ex: `https://flyer-metalcom.streamlit.app`

---

## 📥 Format Excel pentru import

### Pentru Flyer
**15 coloane** (numele atributelor 3-5 sunt configurabile):

| # | Coloană | Conținut |
|---|---|---|
| 1 | Cod | Cod produs |
| 2 | Denumire | Denumire produs |
| 3-5 | *Atribute* | Ex: Adâncime, Înălțime, Finisaj |
| 6 | Preț | Număr |
| 7 | Monedă | "LEI", "EUR", etc. |
| 8 | UM | "buc", "kg", "m²" |
| 9 | Reducere (%) | Număr sau gol |
| 10 | Preț redus | Număr sau gol |
| 11 | Badge | Text pe casetă (ex: "ALB", "IP44") |
| 12 | Imagine badge | Nume fișier pictogramă |
| 13 | Imagine | Nume fișier produs |
| 14 | Text preț | Ex: "Preț cu TVA inclus" |
| 15 | Text bulină | Custom (ex: "NOU", "-30%") |

### Pentru Etichete
**6 coloane**:

| # | Coloană | Conținut |
|---|---|---|
| 1 | Cod | Cod produs |
| 2 | Denumire | Denumire produs |
| 3 | UM | "Buc", "kg" |
| 4 | Preț | Număr |
| 5 | Reducere (%) | Număr (opțional) |
| 6 | Preț redus | Număr (opțional) |

> 💡 Pentru fiecare modul, în Tab Produse poți descărca un fișier model gata-completat.

---

## 📁 Structura fișierelor

```
📁 flyer-app/
├── app.py                  ← router cu sidebar (Flyer / Etichete)
├── flyer_ui.py             ← UI Streamlit pentru Flyer
├── flyer_engine.py         ← motor generare HTML/PPTX flyer
├── labels_ui.py            ← UI Streamlit pentru Etichete
├── labels_engine.py        ← motor generare HTML etichete
├── requirements.txt        ← dependințe Python
├── packages.txt            ← dependințe sistem (gol — nu mai e nevoie)
└── README.md               ← acest fișier
```

---

## 💡 Cum obții PDF-ul

Aplicația nu generează direct PDF (am scos WeasyPrint din motive de portabilitate pe Streamlit Cloud). Workflow-ul recomandat:

1. Apasă **"🚀 Generează"** în tab-ul corespunzător
2. Apasă **"📄 Descarcă HTML"**
3. Deschide HTML-ul descărcat în browser
4. Apasă butonul roșu flotant **"⬇ Descarcă PDF"** (sau Ctrl+P)
5. În dialogul de print, alege **"Save as PDF"** și bifează **"Background graphics"**

Avantaj: PDF-ul are calitate maximă (fonturi vectoriale, fără pixelare) și include toate culorile, fundalurile, fonturile.

---

## 🛠️ Probleme frecvente

| Problemă | Soluție |
|---|---|
| `streamlit: command not found` | `python -m streamlit run app.py` |
| `ModuleNotFoundError: pptx` | `pip install python-pptx` |
| Pe mobil nu se vede tot | Rotește telefonul în mod landscape |
| PDF generat din browser nu are culori/fundaluri | La print bifează **"Background graphics"** |
| Sidebar-ul ascuns | Apasă pe săgeata `>>` din colțul stânga-sus |
