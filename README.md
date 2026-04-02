
# 🔥 Project Title

**Hybrid Fire Detection System Using Sensors and Machine Learning with Real-Time Mobile Bot Alerts**

---

# 📘 README

## 📌 Overview

This project presents a **hybrid fire detection system** that combines **hardware sensors** with **machine learning (ML)** for accurate and reliable fire detection.

The system continuously monitors the environment using sensors (temperature/flame) and enhances detection using an ML model (image-based or pattern-based). When fire is detected, a **bot instantly sends an alert message to the user’s phone**, enabling quick response and improved safety.

---

## 🚀 Key Features

* 🔥 **Dual Detection System** – Combines sensor data + ML-based analysis
* 🧠 **Machine Learning Integration** – Improves accuracy and reduces false alarms
* 📡 **Real-Time Monitoring** – Continuous sensing and processing
* 📱 **Instant Mobile Alerts** – Bot sends notifications to phone (Telegram/WhatsApp)
* ⚡ **Fast Response System** – Immediate detection and alert
* 🔔 **Scalable Architecture** – Can be extended to drones, IoT networks

---

## 🧠 How It Works

1. **Sensor Monitoring**

   * Flame/temperature sensors continuously collect data

2. **ML Processing**

   * ML model analyzes data (or camera feed) to confirm fire
   * Helps reduce false positives from sensors

3. **Decision System**

   * If both sensor + ML indicate fire → trigger alert

4. **Alert System**

   * Bot sends real-time notification to user’s phone
   * Optional alarm/buzzer is activated

---

## 🛠️ Components Used

### 🔌 Hardware

* Microcontroller (ESP32 )
* Flame Sensor
* Temperature Sensor (DHT11)
* Camera Module 
* Buzzer 

### 💻 Software

* Python / Arduino IDE
* Machine Learning Model (e.g., YOLO / CNN)
* OpenCV (for image processing)
* Bot API (Telegram / WhatsApp)

---

## 🤖 Machine Learning Part

* Model trained to detect **fire patterns (flames/smoke)**
* Uses image/video input for validation
* Can be implemented using:

  * YOLO (real-time detection)
  * CNN (classification model)

### ML Workflow

1. Collect fire/non-fire dataset
2. Train model
3. Deploy model on device
4. Run real-time inference

---

## 📂 Project Structure

```bash id="0plj2d"
├── sensor_code.ino / main.py     # Sensor data processing  
├── ml_model/                     # Trained ML model  
├── inference.py                  # Real-time ML detection  
├── bot_integration.py            # Alert system  
├── dataset/                      # Training data  
└── README.md                     # Documentation  
```

---

## ⚙️ Installation & Setup

### 1. Hardware Setup

* Connect sensors to microcontroller
* Attach camera module (for ML detection)
* Ensure WiFi connectivity

### 2. Software Setup

```bash id="4p36pv"
pip install ultralytics opencv-python requests
```

---

## ▶️ Usage

1. Start the system
2. Sensors begin monitoring
3. ML model analyzes environment (image/data)
4. If fire is detected:

   * 📱 Alert message sent to phone
   * 🔔 Alarm triggered (optional)

---

## 📲 Example Alert

```id="6c7tjw"
🔥 Fire Detected!
Confidence: 92%
Sensor Status: HIGH TEMPERATURE
Action Required Immediately!
```

---

## 🔔 Future Improvements

* AI-based smoke + gas detection
* Cloud dashboard with live feed
* GPS-based alert system
* Integration with autonomous drones 
* Automatic fire suppression system

---

## 🎯 Applications

* Smart homes & buildings
* Industrial safety systems
* Warehouses & factories
* Forest fire detection
* Agriculture fields & drone monitoring
