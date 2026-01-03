// DOM Elements
const uploadBox = document.getElementById('uploadBox');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const imagePreview = document.getElementById('imagePreview');
const changeImage = document.getElementById('changeImage');
const predictBtn = document.getElementById('predictBtn');
const loading = document.getElementById('loading');
const results = document.getElementById('results');
const error = document.getElementById('error');
const errorMessage = document.getElementById('errorMessage');
const dismissError = document.getElementById('dismissError');
const tryAgain = document.getElementById('tryAgain');
const weatherEmoji = document.getElementById('weatherEmoji');
const weatherClass = document.getElementById('weatherClass');
const confidenceValue = document.getElementById('confidenceValue');
const weatherDescription = document.getElementById('weatherDescription');
const probabilityBars = document.getElementById('probabilityBars');

let selectedFile = null;

// Event Listeners
uploadBox.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', (e) => {
    handleFile(e.target.files[0]);
});

// Drag and Drop
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('dragover');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragover');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        handleFile(file);
    } else {
        showError('Please drop a valid image file');
    }
});

changeImage.addEventListener('click', () => {
    resetUI();
    fileInput.click();
});

predictBtn.addEventListener('click', predictWeather);

dismissError.addEventListener('click', () => {
    error.style.display = 'none';
    resetUI();
});

tryAgain.addEventListener('click', () => {
    results.style.display = 'none';
    resetUI();
});

// Functions
function handleFile(file) {
    if (!file) return;
    
    if (!file.type.startsWith('image/')) {
        showError('Please select a valid image file');
        return;
    }

    selectedFile = file;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        uploadBox.style.display = 'none';
        previewSection.style.display = 'block';
    };
    reader.readAsDataURL(file);
}

function resetUI() {
    selectedFile = null;
    fileInput.value = '';
    uploadBox.style.display = 'block';
    previewSection.style.display = 'none';
    loading.style.display = 'none';
    results.style.display = 'none';
    error.style.display = 'none';
}

function showError(message) {
    errorMessage.textContent = message;
    error.style.display = 'block';
    loading.style.display = 'none';
}

async function predictWeather() {
    if (!selectedFile) return;

    // Hide everything and show loading
    previewSection.style.display = 'none';
    results.style.display = 'none';
    error.style.display = 'none';
    loading.style.display = 'block';

    // Create FormData
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Prediction failed');
        }

        const data = await response.json();
        displayResults(data);

    } catch (err) {
        console.error('Error:', err);
        showError(err.message || 'Failed to classify weather. Please try again.');
    }
}

function displayResults(data) {
    loading.style.display = 'none';
    results.style.display = 'block';

    // Display main prediction
    weatherEmoji.textContent = data.emoji;
    weatherClass.textContent = data.predicted_class;
    confidenceValue.textContent = `${data.confidence.toFixed(2)}%`;
    weatherDescription.textContent = data.description;

    // Apply weather-specific styling to prediction card
    const predictionCard = document.querySelector('.prediction-card');
    predictionCard.className = 'prediction-card ' + data.predicted_class;

    // Display all probabilities
    probabilityBars.innerHTML = '';
    
    // Sort probabilities in descending order
    const sortedProbs = Object.entries(data.all_probabilities)
        .sort((a, b) => b[1] - a[1]);

    sortedProbs.forEach(([className, probability]) => {
        const barElement = document.createElement('div');
        barElement.className = 'probability-bar';
        
        const isTopPrediction = className === data.predicted_class;
        
        // Weather emojis for each class
        const classEmojis = {
            'hail': '🧊',
            'lightning': '⚡',
            'rain': '🌧️',
            'sandstorm': '🌪️',
            'snow': '❄️'
        };
        
        barElement.innerHTML = `
            <div class="probability-label">
                <span class="probability-label-name">
                    ${classEmojis[className]} ${className.charAt(0).toUpperCase() + className.slice(1)}
                    ${isTopPrediction ? '✓' : ''}
                </span>
                <span class="probability-label-value">${probability.toFixed(1)}%</span>
            </div>
            <div class="probability-bar-bg">
                <div class="probability-bar-fill" style="width: 0%"></div>
            </div>
        `;
        
        probabilityBars.appendChild(barElement);
        
        // Animate the bar
        setTimeout(() => {
            const fillBar = barElement.querySelector('.probability-bar-fill');
            fillBar.style.width = `${probability}%`;
        }, 100);
    });

    // Smooth scroll to results
    results.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Initialize
console.log('🌦️ Weather Classification App - Ready!');