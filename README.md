# 📄 Generator Flyer — Aplicație Streamlit

Aplicație web pentru generarea flyerelor în format HTML și PPTX, cu acces din browser pe orice device (desktop, mobil, tabletă).

---

## 🚀 Pornire rapidă (LOCAL)

### 1. Instalare Python
- **Windows / Mac**: descarcă de la [python.org/downloads](https://www.python.org/downloads/) (versiunea 3.10 sau mai nouă)
- La instalare pe Windows: **bifează „Add Python to PATH"**

### 2. Instalare dependințe
Deschide **Terminal** (Mac) sau **cmd / PowerShell** (Windows) în folderul aplicației și rulează:

```bash
pip install -r requirements.txt
```

Sau, dacă ai probleme cu `pip`, folosește:
```bash
python -m pip install -r requirements.txt
```

### 3. Pornire aplicație
```bash
streamlit run app.py
```

Se va deschide automat browserul la adresa `http://localhost:8501`.

> 💡 **Pentru oprire:** apasă `Ctrl+C` în Terminal.

---

## 📱 Rulare pe mobil în aceeași rețea Wi-Fi

Când rulezi `streamlit run app.py`, în Terminal vei vedea ceva de genul:

```
You can now view your Streamlit app in your browser.

  Local URL:    http://localhost:8501
  Network URL:  http://192.168.1.42:8501
```

Pe telefon/tabletă (conectat la **același Wi-Fi**), deschide browserul la **Network URL** și aplicația va funcționa direct, fără instalare.

---

## ☁️ Deploy gratuit pe Streamlit Cloud (recomandat)

Pentru ca aplicația să fie accesibilă de oriunde, fără să rulezi nimic local:

1. **Creează cont GitHub** (dacă nu ai) la [github.com](https://github.com)
2. Creează un repository nou și încarcă cele 3 fișiere:
   - `app.py`
   - `flyer_engine.py`
   - `requirements.txt`
3. Mergi la [share.streamlit.io](https://share.streamlit.io) și loghează-te cu GitHub
4. Apasă **"New app"** → selectează repository-ul → apasă **"Deploy"**
5. În câteva minute primești un URL public (ex: `https://flyer-metalcom.streamlit.app`)
6. Acel URL funcționează din **orice browser** — desktop, mobil, tabletă, oriunde în lume

---

## 📋 Funcționalități

### 🏢 Tab Antet
- Numele firmei, telefonul, email-ul, website-urile
- Texte din header (titlu mare, texte promoționale)
- Footer legal
- Upload imagine antet (logo)

### 📦 Tab Produse
- Tabel editabil cu toate produsele
- 15 coloane: Cod, Denumire, 3 atribute, Preț, Monedă, UM, Reducere, Preț redus, Badge, Imagine badge, Imagine, Text preț, Text bulină
- Adăugare/ștergere rânduri
- Upload multiplu de imagini (numele fișierelor trebuie să corespundă coloanelor "Imagine" și "Imagine badge")

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
- Buton mare **"Generează HTML + PPTX"**
- Preview flyer direct în pagină
- Download HTML (pentru export PDF din browser)
- Download PPTX (pentru import în Canva sau PowerPoint)

---

## 🛠️ Probleme frecvente

| Problemă | Soluție |
|---|---|
| `streamlit: command not found` | Folosește `python -m streamlit run app.py` |
| `ModuleNotFoundError: pptx` | `pip install python-pptx` |
| Aplicația se deschide dar e goală | Verifică că `flyer_engine.py` e în același folder cu `app.py` |
| Pe mobil nu se vede tot | Rotește telefonul în mod landscape, sau folosește pinch-to-zoom |
| Imaginile nu apar în PDF | În browser, la print bifează **"Background graphics"** |

---

## 📁 Structura fișierelor

```
📁 flyer-app/
├── app.py                  ← aplicația Streamlit
├── flyer_engine.py         ← motorul de generare HTML/PPTX
├── requirements.txt        ← dependințe Python
└── README.md               ← acest fișier
```

---

## 💡 Avantaje față de varianta cu Excel + script Python

- ✅ **Nu mai trebuie editat Excel** — totul în formular vizual
- ✅ **Color pickers** pentru culori (nu trebuie scrise coduri HEX manual)
- ✅ **Slidere** pentru dimensiuni cu preview imediat
- ✅ **Tabel editabil** cu validare automată (numere/text)
- ✅ **Preview HTML** direct în pagină, fără descărcare
- ✅ **Funcționează pe mobil** și tabletă, nu doar desktop
- ✅ **Deploy gratuit pe internet** — accesibil de oriunde

---

Pentru întrebări sau probleme, contactează administratorul.
