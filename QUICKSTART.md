# ⚡ Quick Start Guide

## 🚀 In 5 Minuten starten!

### Schritt 1: Modell kopieren
```bash
# Kopiere deine best_model.h5 Datei hierher
# Von: C:\Users\admin\Downloads\Weather\Weather3\results\best_model.h5
# Nach: [Dieses Verzeichnis]\best_model.h5
```

### Schritt 2: Virtual Environment erstellen

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Schritt 3: Dependencies installieren
```bash
pip install -r requirements.txt
```

Dies kann 5-10 Minuten dauern (TensorFlow ist groß).

### Schritt 4: App starten
```bash
python app.py
```

### Schritt 5: Im Browser öffnen
```
http://localhost:5000
```

## ✅ Das war's! Deine App läuft!

---

## 🌐 Online Deployment (Optional)

### Render (Empfohlen - Kostenlos)

1. Gehe zu [render.com](https://render.com)
2. Erstelle einen Account
3. "New" → "Web Service"
4. Verbinde dein GitHub Repository
5. Render erkennt automatisch Python/Flask
6. Klicke "Create Web Service"
7. Warte 5-10 Minuten
8. Deine App ist online! 🎉

**Wichtig für Render:**
- Stelle sicher, dass `best_model.h5` im Repository ist (oder in Git LFS)
- Füge gunicorn hinzu: `pip install gunicorn` und zur requirements.txt

### Railway (Alternative)

1. Gehe zu [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Repository auswählen
4. Railway deployed automatisch
5. Fertig!

### Heroku

1. Erstelle Heroku Account
2. Installiere Heroku CLI
3. Im Projektordner:
```bash
heroku login
heroku create dein-app-name
git push heroku main
```

---

## 🔧 Troubleshooting

### Problem: "Model file not found"
**Fix:** Kopiere `best_model.h5` ins Hauptverzeichnis

### Problem: TensorFlow Installation Error
**Fix (Windows):**
```bash
pip install tensorflow-cpu==2.15.0
```

**Fix (macOS M1/M2):**
```bash
pip install tensorflow-macos==2.15.0
```

### Problem: Port bereits belegt
**Fix:** Ändere Port in app.py auf 8000 oder 3000

### Problem: Zu langsam
**Fix:** 
- Nutze kleinere Bilder (< 1MB)
- Für Production: GPU-Version von TensorFlow

---

## 📝 Projekt-Checkliste

- [ ] `best_model.h5` kopiert
- [ ] Virtual Environment erstellt
- [ ] Dependencies installiert
- [ ] App läuft lokal
- [ ] Im Browser getestet
- [ ] Bilder erfolgreich klassifiziert
- [ ] (Optional) Online deployed

---

## 🎯 Features Testen

1. **Drag & Drop**: Ziehe ein Bild ins Upload-Feld
2. **Klick Upload**: Klicke zum Durchsuchen
3. **Klassifizierung**: Klicke "Classify Weather"
4. **Ergebnisse**: Sieh Vorhersage + Wahrscheinlichkeiten
5. **Neues Bild**: Klicke "Analyze Another Image"

---

## 📞 Hilfe benötigt?

1. Überprüfe die Konsole auf Fehlermeldungen
2. Lies README.md für Details
3. Stelle sicher alle Dateien vorhanden sind:
   - app.py ✓
   - best_model.h5 ✓
   - templates/index.html ✓
   - static/css/style.css ✓
   - static/js/script.js ✓
   - requirements.txt ✓

---

**Viel Erfolg! 🚀**
