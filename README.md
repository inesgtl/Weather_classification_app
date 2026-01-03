# 🌦️ Weather Classification AI Web App

An intelligent web application that classifies weather conditions from images using a Convolutional Neural Network (CNN) powered by TensorFlow.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-orange)
![Flask](https://img.shields.io/badge/Flask-3.0-black)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🤖 **AI-Powered**: Deep learning CNN model with high accuracy
- 🌈 **5 Weather Classes**: Hail, Lightning, Rain, Sandstorm, Snow
- 🎨 **Modern UI**: Beautiful weather-themed responsive interface
- ⚡ **Real-time**: Instant predictions with confidence scores
- 📊 **Detailed Analysis**: Probability breakdown for all classes
- 📱 **Mobile Friendly**: Fully responsive design

## 🎯 Demo

Try it live: [Weather Classifier](https://your-app-url.com) *(Coming soon)*

## 🖼️ Screenshots

*Add your screenshots here*

## 🛠️ Tech Stack

**Backend:**
- Flask 3.0 - Web framework
- TensorFlow 2.20 - Deep learning
- NumPy - Numerical computing
- Pillow - Image processing

**Frontend:**
- HTML5 / CSS3
- Vanilla JavaScript
- Weather-themed animations

**Model:**
- Custom CNN architecture
- 128x128 RGB input
- 5-class classification
- K-Fold cross-validation

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/weather-classification-app.git
cd weather-classification-app
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 📊 Model Architecture
```
Conv2D (32) → BatchNorm → MaxPool → Dropout
Conv2D (64) → BatchNorm → MaxPool → Dropout
Conv2D (128) → BatchNorm → MaxPool → Dropout
Conv2D (256) → BatchNorm → MaxPool → Dropout
Flatten
Dense (512) → BatchNorm → Dropout
Dense (256) → BatchNorm → Dropout
Dense (5) → Softmax
```

## 🌦️ Weather Classes

| Icon | Class | Description |
|------|-------|-------------|
| 🧊 | Hail | Frozen precipitation in ice pellets |
| ⚡ | Lightning | Electrical discharge during storms |
| 🌧️ | Rain | Water droplets falling from clouds |
| 🌪️ | Sandstorm | Strong winds carrying sand particles |
| ❄️ | Snow | Frozen water vapor as white flakes |

## 📁 Project Structure
```
weather-classification-app/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment config
├── exported_model/           # Model weights (NPZ format)
├── templates/                # HTML templates
├── static/                   # CSS, JS, assets
└── README.md                 # Documentation
```

## 🚀 Deployment

### Deploy on Render

1. Fork this repository
2. Create account on [Render](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Render auto-detects Python/Flask
6. Deploy! 🎉

### Deploy on Railway

1. Create account on [Railway](https://railway.app)
2. New Project → Deploy from GitHub
3. Select your repository
4. Railway handles the rest
5. Your app is live! 🚂

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes.

## 👨‍💻 Author

**INESS**  
IT Application Developer   
📍 Annaba, Algeria

[GitHub](https://github.com/inesgtl) • 
## 🙏 Acknowledgments

- Built as a portfolio project demonstrating full-stack ML deployment
- Showcases web development, machine learning, and deployment skills
- Part of my software development training 
---

⭐ Star this repo if you find it helpful!  
Made with ❤️ and ☕ in annaba 
