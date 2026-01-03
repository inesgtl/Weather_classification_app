from flask import Flask, request, render_template, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from PIL import Image
import io
import json
import os

app = Flask(__name__)

# Configuration
IMG_SIZE = (128, 128)
CLASSES = ['hail', 'lightning', 'rain', 'sandstorm', 'snow']

# Emojis for each weather class
WEATHER_EMOJIS = {
    'hail': '🧊',
    'lightning': '⚡',
    'rain': '🌧️',
    'sandstorm': '🌪️',
    'snow': '❄️'
}

# Descriptions for each weather class
WEATHER_DESCRIPTIONS = {
    'hail': 'Hail - Frozen precipitation in the form of ice pellets',
    'lightning': 'Lightning - Electrical discharge during a thunderstorm',
    'rain': 'Rain - Water droplets falling from clouds',
    'sandstorm': 'Sandstorm - Strong winds carrying sand particles',
    'snow': 'Snow - Frozen water vapor falling as white flakes'
}

# Model path
MODEL_WEIGHTS_PATH = 'exported_model/model_weights.npz'
MODEL_H5_PATH = 'best_model.h5'

model = None

def create_cnn_model(input_shape=(128, 128, 3), num_classes=5):
    """
    Recreate the CNN model architecture
    This matches your training code
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', padding='same',
                     kernel_regularizer=keras.regularizers.l2(0.0001),
                     input_shape=input_shape),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        layers.Conv2D(64, (3, 3), activation='relu', padding='same',
                     kernel_regularizer=keras.regularizers.l2(0.0001)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        layers.Conv2D(128, (3, 3), activation='relu', padding='same',
                     kernel_regularizer=keras.regularizers.l2(0.0001)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.3),
        
        layers.Conv2D(256, (3, 3), activation='relu', padding='same',
                     kernel_regularizer=keras.regularizers.l2(0.0001)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.35),
        
        layers.Flatten(),
        
        layers.Dense(512, activation='relu',
                    kernel_regularizer=keras.regularizers.l2(0.0001)),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        layers.Dense(256, activation='relu',
                    kernel_regularizer=keras.regularizers.l2(0.0001)),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

def load_model_from_npz_fixed():
    """Load model from NPZ weights file - FIXED VERSION"""
    global model
    
    print("\n" + "="*60)
    print("LOADING MODEL FROM NPZ FORMAT (FIXED)")
    print("="*60)
    
    try:
        # Create model architecture
        print("\n1. Creating model architecture...")
        model = create_cnn_model(input_shape=(*IMG_SIZE, 3), num_classes=len(CLASSES))
        print("   ✓ Model architecture created")
        
        # Load weights
        print("\n2. Loading weights from NPZ...")
        if not os.path.exists(MODEL_WEIGHTS_PATH):
            raise FileNotFoundError(f"Weights file not found: {MODEL_WEIGHTS_PATH}")
        
        weights_data = np.load(MODEL_WEIGHTS_PATH, allow_pickle=True)
        print(f"   ✓ Loaded {len(weights_data.files)} weight arrays")
        
        # Debug: print all available keys
        print("\n3. Available weight keys in NPZ file:")
        for key in sorted(weights_data.files)[:10]:  # Show first 10
            print(f"   - {key}")
        if len(weights_data.files) > 10:
            print(f"   ... and {len(weights_data.files) - 10} more")
        
        # IMPROVED: Set weights by collecting all weights first
        print("\n4. Setting weights to model layers...")
        
        # Collect all weight arrays in order
        all_weights = []
        weight_keys = sorted(weights_data.files, key=lambda x: int(x.split('_')[1]))  # Sort by layer number
        
        for key in weight_keys:
            all_weights.append(weights_data[key])
        
        print(f"   ✓ Collected {len(all_weights)} weight arrays")
        
        # Set all weights at once
        model.set_weights(all_weights)
        print("   ✓ All weights successfully loaded!")
        
        print("\n" + "="*60)
        print("✅ MODEL LOADED SUCCESSFULLY FROM NPZ!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error loading from NPZ: {e}")
        import traceback
        traceback.print_exc()
        return False

def load_model_from_h5():
    """Load model from H5 file (fallback)"""
    global model
    
    print("\n" + "="*60)
    print("LOADING MODEL FROM H5 FORMAT")
    print("="*60)
    
    try:
        if not os.path.exists(MODEL_H5_PATH):
            raise FileNotFoundError(f"H5 file not found: {MODEL_H5_PATH}")
        
        print(f"\nLoading model from {MODEL_H5_PATH}...")
        model = keras.models.load_model(MODEL_H5_PATH)
        print("✅ Model loaded successfully from H5!")
        return True
        
    except Exception as e:
        print(f"❌ Error loading from H5: {e}")
        return False

def load_model():
    """Try to load model from available formats"""
    global model
    
    # Try NPZ first with fixed loader
    if os.path.exists(MODEL_WEIGHTS_PATH):
        print("Found NPZ weights file. Loading with fixed method...")
        if load_model_from_npz_fixed():
            return
    
    # Fallback to H5
    if os.path.exists(MODEL_H5_PATH):
        print("\nNPZ not found. Trying H5 format...")
        if load_model_from_h5():
            return
    
    # No model found
    print("\n" + "="*60)
    print("⚠️ WARNING: NO MODEL FILE FOUND!")
    print("="*60)
    print("\nPlease provide one of the following:")
    print(f"1. NPZ format: Run 'export_model_to_npz.py' and copy 'exported_model/' folder here")
    print(f"2. H5 format: Copy 'best_model.h5' to this directory")
    print("="*60)

def preprocess_image(image_bytes):
    """Preprocess image for the model"""
    try:
        # Load image from bytes
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize
        img = img.resize(IMG_SIZE)
        
        # Convert to numpy array and normalize
        img_array = np.array(img) / 255.0
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        return img_array
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        raise

def predict_weather(image_bytes):
    """Make prediction on the image"""
    if model is None:
        return None, "Model not loaded"
    
    try:
        # Preprocess image
        processed_img = preprocess_image(image_bytes)
        
        # Make prediction
        predictions = model.predict(processed_img, verbose=0)
        
        # Get probabilities for each class
        probabilities = predictions[0]
        
        # Get predicted class
        predicted_class_idx = np.argmax(probabilities)
        predicted_class = CLASSES[predicted_class_idx]
        confidence = float(probabilities[predicted_class_idx]) * 100
        
        # Create results dictionary
        results = {
            'predicted_class': predicted_class,
            'confidence': confidence,
            'emoji': WEATHER_EMOJIS[predicted_class],
            'description': WEATHER_DESCRIPTIONS[predicted_class],
            'all_probabilities': {
                CLASSES[i]: float(probabilities[i]) * 100 
                for i in range(len(CLASSES))
            }
        }
        
        return results, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        try:
            # Read image bytes
            image_bytes = file.read()
            
            # Make prediction
            results, error = predict_weather(image_bytes)
            
            if error:
                return jsonify({'error': error}), 500
            
            return jsonify(results)
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'model_format': 'npz' if os.path.exists(MODEL_WEIGHTS_PATH) else 'h5' if os.path.exists(MODEL_H5_PATH) else 'none'
    })

if __name__ == '__main__':
    # Load model on startup
    load_model()
    
    # Start application
    print("\n" + "="*60)
    print("🌦️  WEATHER CLASSIFICATION WEB APP (FIXED)")
    print("="*60)
    print("\n🚀 Server starting...")
    print("📱 Access the app at: http://localhost:5000")
    print("\n⚠️  Make sure you have either:")
    print("   - exported_model/ folder (NPZ format)")
    print("   - best_model.h5 file (H5 format)")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)