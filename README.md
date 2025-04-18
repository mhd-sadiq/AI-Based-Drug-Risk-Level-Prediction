# 🧠 AI-Based Drug Abuse Detection System

An AI-powered web application that predicts the **drug abuse risk level (Low or High)** based on behavioral and demographic data. This system is designed to support healthcare professionals by identifying individuals at high risk and enabling timely intervention and treatment.

## 📌 Project Overview

- **Objective:** Assess the current drug risk level of individuals who already use drugs.
- **Technology:** Machine Learning (Random Forest Classifier), Flask, Pandas, Scikit-learn.
- **Dataset:** National Survey on Drug Use and Health (NSDUH, 2015–2019) from [Kaggle](https://www.kaggle.com/).
- **Application:** Web-based prediction system for real-time drug risk assessment.

## 💡 Key Features

- Predicts whether a user is at **Low** or **High** risk of drug abuse.
- Interactive **Flask web application** for easy data input and real-time results.
- Uses behavioral and demographic features for prediction.
- Trained on a cleaned dataset of over **270,000 records**.
- Achieved **95% Accuracy**, **95% Precision**, and **94% F1-Score**.
- Provides **feature importance** to understand influential risk factors.

## 🧪 Machine Learning Model

- **Model Used:** Random Forest Classifier
- **Why Random Forest?**
  - Works well with both categorical and numerical data.
  - Handles imbalanced data better than many other models.
  - Offers feature importance for interpretability.
- **Training Split:** 80% training / 20% testing
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score

## 📊 Dataset Details

- **Source:** NSDUH Survey (via Kaggle)
- **Size:** 270,000+ records
- **Format:** CSV
- **Features:** Age, gender, education, mental health status, drug usage, etc.
- **Preprocessing:**
  - Handled missing values
  - Removed duplicates
  - One-hot encoded categorical variables
  - Scaled numerical values

## 🚀 Deployment

- **Framework:** Flask
- **Functionality:**
  - Simple web interface to enter user data
  - Real-time predictions displayed on submission
- **Example Use Case:**
  - A healthcare worker enters patient details and gets instant risk classification (Low/High)

## 🧱 Project Structure

├── static/ # Static files (CSS/JS/images) ├── templates/ # HTML templates (Flask) │ └── index.html # 
Main form UI ├── model/ # Trained ML model file (.pkl) ├── app.py # Flask app script ├──
requirements.txt # List of dependencies └── README.md # Project documentation


## ⚠️ Challenges

- The dataset includes **self-reported data**, which may introduce bias.
- **Imbalanced class distribution** required careful model tuning.
- Based on 2015–2019 data, so trends may not fully reflect current patterns.

## 🔮 Future Work

- Expand to real-time health monitoring platforms.
- Use more recent or live data for better accuracy.
- Add multi-class classification for drug types or severity stages.
- Integrate secure user authentication and data storage.

## 📚 Libraries Used

- `pandas`
- `scikit-learn`
- `matplotlib`
- `flask`
- `joblib`

## 📎 Acknowledgments

- Dataset: [NSDUH Dataset on Kaggle](https://www.kaggle.com/)
- Project developed as part of AI/ML curriculum at **Learn Logic AI**

---

## 🙏 Thank You

This project was created to assist in the **early identification and rehabilitation** of individuals struggling with substance abuse. Your feedback and suggestions are welcome!

> **Developed by:** Sadiq  
> **Institution:** Learn Logic AI  
> **Date:** April 5, 2025
