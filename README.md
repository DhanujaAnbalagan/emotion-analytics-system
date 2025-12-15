
# Real-Time Emotion Analytics System

A real-time facial emotion analytics system built using **DeepFace**, **OpenCV**, and **TensorFlow**, designed to perform live emotion inference from webcam input and log anonymized emotion statistics for analysis.

This project focuses on **system integration, real-time performance handling, and analytics logging**, rather than training a custom ML model.

---

## 🚀 Features

- Real-time webcam-based facial emotion inference
- Uses pretrained DeepFace emotion recognition model
- Smooth emotion confidence tracking with time-based throttling
- Modular architecture for maintainability
- Anonymized emotion analytics logging (`CSV`)
- Fully local execution (no cloud, no data upload)

---

## 🧠 System Architecture

Camera Feed
↓
Face Detection + Emotion Inference (DeepFace)
↓
Emotion Smoothing & Dominance Tracking
↓
Real-Time Visualization
↓
CSV Analytics Logging


---

## 🗂️ Project Structure


emotion-analytics-system/
│
├── camera.py # Webcam capture handling
├── emotion_engine.py # DeepFace emotion inference logic
├── tracker.py # Emotion smoothing & dominance logic
├── logger.py # CSV-based analytics logging
├── dashboard.py # Visualization utilities
├── main.py # Application entry point
├── requirements.txt
├── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository
bash
git clone https://github.com/DhanujaAnbalagan/emotion-analytics-system.git
cd emotion-analytics-system

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
pip install tf-keras

4. Run the system
python main.py


Press Q to exit the application.

📊 Output

Live emotion labels and confidence bars on webcam feed
Automatically generated emotion_log.csv containing:
Timestamp
Emotion probabilities
Dominant emotion per frame window

🛠️ Tech Stack

Python
OpenCV
DeepFace
TensorFlow
NumPy
Pandas

🚧 Future Enhancements

Multi-face emotion tracking

Emotion trend visualization dashboard

Web-based analytics interface

Configurable logging controls

API-based emotion analytics service

