# 🌦️ Weather Classification Web App

Ein Deep Learning basiertes Wetterklassifizierungssystem mit moderner Weboberfläche.

A Deep Learning-based weather classification system with a modern web interface.

## 🎯 Features

- **5 Wetterklassen**: Hail (🧊), Lightning (⚡), Rain (🌧️), Sandstorm (🌪️), Snow (❄️)
- **CNN-Modell**: Hochpräzises Convolutional Neural Network
- **Drag & Drop**: Benutzerfreundliche Bildupload-Funktion
- **Echtzeit-Vorhersagen**: Sofortige Klassifizierung
- **Vertrauenswerte**: Detaillierte Wahrscheinlichkeiten für alle Klassen
- **Responsive Design**: Funktioniert auf Desktop und Mobilgeräten

## 📁 Projektstruktur

```
weather-classification-app/
│
├── app.py                      # Flask Backend
├── requirements.txt            # Python Dependencies
├── best_model.h5              # Trained Model (YOU NEED TO ADD THIS!)
│
├── templates/
│   └── index.html             # Frontend HTML
│
└── static/
    ├── css/
    │   └── style.css          # Styling
    └── js/
        └── script.js          # JavaScript Logic
```

## 🚀 Installation & Setup

### 1. Voraussetzungen (Prerequisites)

- Python 3.8 oder höher
- pip (Python Package Manager)

### 2. Repository klonen oder herunterladen

```bash
# Falls du Git verwendest
git clone <your-repo-url>
cd weather-classification-app

# Oder einfach alle Dateien in einen Ordner kopieren
```

### 3. Modell hinzufügen (WICHTIG!)

**⚠️ KRITISCHER SCHRITT:**

Du musst deine trainierte `best_model.h5` Datei in das Hauptverzeichnis kopieren:

```
weather-classification-app/
├── app.py
├── best_model.h5  ← DIESE DATEI MUSS HIER SEIN!
└── ...
```

Die Datei sollte sich in deinem `results/` Ordner befinden:
```
C:\Users\admin\Downloads\Weather\Weather3\results\best_model.h5
```

### 4. Virtual Environment erstellen (empfohlen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 5. Dependencies installieren

```bash
pip install -r requirements.txt
```

**Hinweis:** Die Installation von TensorFlow kann einige Minuten dauern.

### 6. Anwendung starten

```bash
python app.py
```

Du solltest folgende Ausgabe sehen:

```
============================================================
🌦️  WEATHER CLASSIFICATION WEB APP
============================================================

✅ Model loaded successfully!
🚀 Server starting...
📱 Access the app at: http://localhost:5000

⚠️  Make sure 'best_model.h5' is in the same directory!
============================================================
```

### 7. Im Browser öffnen

Öffne deinen Browser und gehe zu:
```
http://localhost:5000
```

## 💻 Verwendung (Usage)

1. **Bild hochladen**: Ziehe ein Wetterbild in den Upload-Bereich oder klicke zum Durchsuchen
2. **Klassifizieren**: Klicke auf "Classify Weather"
3. **Ergebnisse ansehen**: Sieh die Vorhersage mit Vertrauenswert und allen Wahrscheinlichkeiten

## 🌐 Deployment Optionen

### Option 1: Lokale Entwicklung (bereits fertig!)

Die App läuft bereits lokal auf deinem Computer.

### Option 2: Deployment auf Render (Kostenlos)

1. Erstelle einen Account auf [Render](https://render.com)

2. Erstelle eine `render.yaml` Datei:

```yaml
services:
  - type: web
    name: weather-classifier
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

3. Füge `gunicorn` zu `requirements.txt` hinzu:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

4. Pushe zu GitHub und verbinde mit Render

### Option 3: Deployment auf Railway (Kostenlos)

1. Account auf [Railway](https://railway.app) erstellen
2. "New Project" → "Deploy from GitHub"
3. Repository auswählen
4. Railway erkennt automatisch die Flask-App
5. Stelle sicher, dass `best_model.h5` im Repository ist

### Option 4: Deployment auf Google Cloud Platform

```bash
# Erstelle app.yaml
runtime: python311
entrypoint: gunicorn -b :$PORT app:app

# Deploy
gcloud app deploy
```

## 🔧 Technische Details

### Modell-Architektur
- **Typ**: Convolutional Neural Network (CNN)
- **Input**: 128x128 RGB Bilder
- **Layers**: 4 Conv2D + BatchNorm + MaxPooling + Dropout
- **Dense Layers**: 512 → 256 → 5 (Ausgabe)
- **Regularisierung**: L2 Regularization, Dropout
- **Training**: K-Fold Cross-Validation (5 folds)

### Backend (Flask)
- **Framework**: Flask 3.0.0
- **ML Framework**: TensorFlow 2.15.0
- **Bildverarbeitung**: Pillow (PIL)
- **API Endpoints**:
  - `GET /` - Hauptseite
  - `POST /predict` - Wettervorhersage
  - `GET /health` - Health Check

### Frontend
- **HTML5/CSS3** mit modernem, responsivem Design
- **Vanilla JavaScript** (keine zusätzlichen Frameworks)
- **Features**: Drag & Drop, Bildvorschau, animierte Ergebnisse

## 📊 Modell-Performance

Basierend auf deinem Training:

**Cross-Validation Ergebnisse:**
- Mean Accuracy: ~XX%
- Mean Precision: ~XX%
- Mean Recall: ~XX%

**Test Set Ergebnisse:**
- Test Accuracy: ~XX%
- Macro F1-Score: ~XX%

*(Die genauen Werte findest du in `results/results_summary.txt`)*

## 🐛 Fehlerbehebung (Troubleshooting)

### Problem: "Model file not found"

**Lösung:** Stelle sicher, dass `best_model.h5` im gleichen Verzeichnis wie `app.py` ist.

### Problem: TensorFlow Installation schlägt fehl

**Lösung für Windows:**
```bash
pip install tensorflow-cpu==2.15.0  # CPU-Only Version
```

**Lösung für macOS (M1/M2):**
```bash
pip install tensorflow-macos==2.15.0
pip install tensorflow-metal==1.1.0
```

### Problem: Port 5000 bereits in Verwendung

**Lösung:** Ändere den Port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # oder ein anderer Port
```

### Problem: Langsame Vorhersagen

**Lösung:** 
- Verwende kleinere Bilder (< 2MB)
- Bei vielen Anfragen: Verwende GPU-Version von TensorFlow
- Für Production: Implementiere Caching

## 📝 Anpassungen (Customization)

### Andere Bildgröße verwenden

In `app.py`:
```python
IMG_SIZE = (256, 256)  # Statt (128, 128)
```

**⚠️ Wichtig:** Dies muss mit der Trainingsgröße übereinstimmen!

### Neue Klassen hinzufügen

1. Modell mit neuen Klassen trainieren
2. In `app.py` aktualisieren:
```python
CLASSES = ['hail', 'lightning', 'rain', 'sandstorm', 'snow', 'fog', 'tornado']
```

### Design anpassen

Bearbeite `static/css/style.css` um Farben, Schriftarten, etc. zu ändern.

## 🎓 Nächste Schritte

Für dein Ausbildung bei Cosmoshop könnten folgende Erweiterungen interessant sein:

1. **User Authentication** (Login-System)
2. **Datenbank Integration** (PostgreSQL/MySQL)
3. **History Feature** (Vorhersage-Verlauf speichern)
4. **API-Only Mode** (RESTful API für mobile Apps)
5. **Batch Processing** (Mehrere Bilder auf einmal)
6. **Model Retraining Interface** (Modell mit neuen Daten trainieren)

## 📚 Ressourcen

- [Flask Dokumentation](https://flask.palletsprojects.com/)
- [TensorFlow Dokumentation](https://www.tensorflow.org/guide)
- [Deployment Best Practices](https://flask.palletsprojects.com/en/3.0.x/deploying/)

## 🤝 Support

Bei Fragen oder Problemen:
1. Überprüfe die Fehlermeldungen in der Konsole
2. Stelle sicher, dass alle Dependencies installiert sind
3. Verifiziere, dass `best_model.h5` vorhanden ist

## 📄 Lizenz

Dieses Projekt ist für Lern- und Portfolio-Zwecke erstellt.

---

**Viel Erfolg bei deiner Ausbildung bei Cosmoshop! 🚀**

Made with ❤️ for Weather Classification
