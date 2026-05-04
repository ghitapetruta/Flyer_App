# 📄 Generator Flyer — Aplicație Streamlit

Aplicație web pentru generarea flyerelor în format **PDF**, **HTML** și **PPTX**, cu acces din browser pe orice device (desktop, mobil, tabletă).

---

## ✨ Ce poate face aplicația

- 🏢 Configurare antet (date firmă, logo, texte promoționale)
- 📦 Editare produse într-un tabel **+ import din Excel**
- 🎨 Personalizare completă (culori, fonturi, dimensiuni)
- 📝 Texte observații
- 🚀 Generare în **3 formate**:
  - **PDF** — gata de printat sau trimis prin email
  - **HTML** — pentru browser/preview
  - **PPTX** — importabil în Canva, PowerPoint, Google Slides
- 7 layout-uri diferite (1, 2, 3, 3a, 4, 5, 6 produse/pagină)

---

## 🚀 Pornire rapidă (LOCAL)

### 1. Instalare Python
- **Windows / Mac**: descarcă de la [python.org/downloads](https://www.python.org/downloads/) (versiunea 3.10 sau mai nouă)
- La instalare pe Windows: **bifează „Add Python to PATH"**

### 2. Instalare dependințe sistem (pentru WeasyPrint - generare PDF)

WeasyPrint are nevoie de câteva biblioteci sistem.

**Pe Windows:**
Instalează **GTK3 Runtime** de la [github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) (~30MB). E suficient.

**Pe Mac:**
```bash
brew install pango libffi
```

**Pe Linux (Ubuntu/Debian):**
```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libcairo2 libgdk-pixbuf2.0-0
```

> 💡 Dacă nu vrei să instalezi WeasyPrint, aplicația funcționează totuși — doar butonul "PDF" va apărea ca indisponibil. HTML și PPTX merg fără probleme.

### 3. Instalare biblioteci Python
Deschide **Terminal** (Mac) sau **cmd / PowerShell** (Windows) în folderul aplicației:

```bash
pip install -r requirements.txt
```

### 4. Pornire aplicație
```bash
streamlit run app.py
```

Se va deschide automat browserul la `http://localhost:8501`.

---

## 📱 Rulare pe mobil în aceeași rețea Wi-Fi

Când rulezi `streamlit run app.py`, în Terminal vei vedea:

```
You can now view your Streamlit app in your browser.
  Local URL:    http://localhost:8501
  Network URL:  http://192.168.1.42:8501
```

Pe telefon/tabletă (conectat la **același Wi-Fi**), deschide browserul la **Network URL**.

---

## ☁️ Deploy gratuit pe Streamlit Cloud (recomandat)

Pentru ca aplicația să fie accesibilă de oriunde, fără să rulezi nimic local:

1. **Cont GitHub** la [github.com](https://github.com)
2. Creează un repository nou și încarcă **5 fișiere**:
   - `app.py`
   - `flyer_engine.py`
   - `requirements.txt`
   - `packages.txt` *(important pentru WeasyPrint pe cloud)*
   - `README.md`
3. Mergi la [share.streamlit.io](https://share.streamlit.io) și loghează-te cu GitHub
4. Apasă **"New app"** → selectează repository-ul → **"Deploy"**
5. Aștepți 5-8 minute (instalează WeasyPrint și dependențele)
6. Primești URL public, ex: `https://flyer-metalcom.streamlit.app`

> ⚠️ **Important pentru deploy pe cloud:** fișierul `packages.txt` trebuie inclus în repository. El conține biblioteci sistem (Pango, Cairo, GDK-PixBuf, fonturi) necesare pentru WeasyPrint să genereze PDF-uri.

---

## 📋 Funcționalități detaliate

### 🏢 Tab Antet
- Numele firmei, telefonul, email-ul, website-urile
- Texte din header (titlu mare, texte promoționale)
- Footer legal
- Upload imagine antet (logo)

### 📦 Tab Produse
- **Editare nume coloane atribute** — schimbă "Adâncime/Înălțime/Finisaj" în orice (ex: "Culoare/Volum/Material")
- **Import Excel** — încarcă un fișier .xlsx cu produsele
- **Descărcare model Excel** — pentru a începe editarea în Excel offline
- **Tabel editabil** cu 15 coloane: Cod, Denumire, 3 atribute, Preț, Monedă, UM, Reducere, Preț redus, Badge, Imagine badge, Imagine, Text preț, Text bulină
- Adăugare/ștergere rânduri direct în tabel
- Upload multiplu de imagini

### 🎨 Tab Stil
- Color pickers pentru toate culorile
- Slidere pentru dimensiuni (titlu, preț, bulină, etc.)
- Selector de fonturi (Montserrat, Roboto, Arial, etc.)
- Reset la valorile implicite

### 📝 Tab Observații
- Editor pentru textele din footer (bullet points)

### 🚀 Tab Generează
- Selectare layout: 1, 2, 3, 3a, 4, 5 sau 6 produse/pagină
- Estimare număr pagini
- Buton mare **"Generează"**
- Preview flyer direct în pagină
- **3 butoane download:**
  - 📕 **PDF** — direct, gata de printat
  - 📄 **HTML** — pentru browser/editare
  - 📊 **PPTX** — pentru import în Canva

---

## 📥 Format Excel pentru import

Fișierul Excel trebuie să aibă pe primul rând **antetul** cu numele coloanelor și apoi rândurile cu produse.

**Coloane așteptate (în această ordine):**

| # | Nume coloană | Conținut |
|---|---|---|
| 1 | Cod | Cod produs |
| 2 | Denumire | Denumire produs |
| 3 | *Atribut 1* | ex: "Adâncime", valoare ex: "350mm" |
| 4 | *Atribut 2* | ex: "Înălțime", valoare ex: "89mm" |
| 5 | *Atribut 3* | ex: "Finisaj", valoare ex: "Alb" |
| 6 | Preț | Număr (fără simbol monedă) |
| 7 | Monedă | "LEI", "EUR", "$" etc. |
| 8 | UM | "buc", "kg", "m²" etc. |
| 9 | Reducere (%) | Număr (ex: 20) sau gol |
| 10 | Preț redus | Număr sau gol |
| 11 | Badge | Text pe casetă (ex: "ALB", "IP44") |
| 12 | Imagine badge | Nume fișier (ex: "ip44.png") |
| 13 | Imagine | Nume fișier (ex: "produs.jpg") |
| 14 | Text preț | Text mic sub preț (ex: "Preț cu TVA inclus") |
| 15 | Text bulină | Text custom în bulină (ex: "NOU", "-30%") |

> 💡 **Numele atributelor (coloanele 3, 4, 5)** sunt preluate automat din header-ul fișierului. Schimbă-le după nevoie.

> 💡 Pentru a începe rapid: în Tab Produse → secțiunea "Import/Export Excel" → apasă **"📥 Descarcă model_produse.xlsx"** pentru a primi un fișier exemplu.

---

## 🛠️ Probleme frecvente

| Problemă | Soluție |
|---|---|
| `streamlit: command not found` | Folosește `python -m streamlit run app.py` |
| `ModuleNotFoundError: pptx` | `pip install python-pptx` |
| `cannot load library 'libgobject-2.0-0'` | Instalează GTK3 Runtime (Windows) sau `apt install libpango-1.0-0` (Linux) |
| Pe Streamlit Cloud nu se generează PDF | Verifică că `packages.txt` e în repository |
| Aplicația se deschide dar e goală | Verifică că `flyer_engine.py` e în același folder cu `app.py` |
| Pe mobil nu se vede tot | Rotește telefonul în mod landscape |
| Imaginile nu apar în PDF | În browser, la print bifează **"Background graphics"** (sau folosește butonul PDF direct din app) |

---

## 📁 Structura fișierelor

```
📁 flyer-app/
├── app.py                  ← aplicația Streamlit
├── flyer_engine.py         ← motorul de generare HTML/PPTX/PDF
├── requirements.txt        ← dependințe Python
├── packages.txt            ← dependințe sistem (pentru Streamlit Cloud)
└── README.md               ← acest fișier
```

---

## 💡 Avantaje față de varianta cu Excel + script Python

- ✅ **Nu mai trebuie editat Excel pe disk** — totul în formular vizual (sau import dacă preferi Excel)
- ✅ **Color pickers** pentru culori (nu trebuie scrise coduri HEX manual)
- ✅ **Slidere** pentru dimensiuni cu preview imediat
- ✅ **Tabel editabil** cu validare automată (numere/text)
- ✅ **Preview HTML** direct în pagină, fără descărcare
- ✅ **PDF direct** dintr-un click (fără să mai treci prin browser)
- ✅ **Funcționează pe mobil** și tabletă, nu doar desktop
- ✅ **Deploy gratuit pe internet** — accesibil de oriunde
- ✅ **Import / Export Excel** — pentru utilizatori care preferă Excel pentru editare în masă
