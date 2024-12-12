# Sahasya---Mental-Health-Assistant

## Overview

This project is a web-based application designed to help users with mental health support. It includes:
- A **Chatbot** that provides real-time responses using pre-trained models.
- A **Prediction System** to assess mental health based on specific user inputs.
- A user authentication system with secure database management.

The project uses **Flask** as the backend framework, a SQLite database for storing user data, and pre-trained models for predictions.

---

## Features

- **Chatbot**: A conversational assistant trained to provide basic support and responses.
- **Prediction Models**: Machine learning models to predict mental health levels for:
  - **Working Professionals** (`Sahasya_model_1_Decision.pkl`)
  - **Students** (`Sahasya_model_2_SVM.pkl`)
- **User Management**: Login, registration, and session handling using Flask-SQLAlchemy.
- **Interactive UI**: HTML, CSS, and JavaScript for user-friendly web pages.
- **Secure Authentication**: Password hashing for secure logins.

---
### Deployment
The project is deployed using **Render**. The deployment uses:
- **Procfile**: Defines the app's start command using `gunicorn`.
- **Dynamic Path Handling**: Ensures portability for models and the database across environments.

---

### Technologies Used
- **Backend**: Flask, Flask-SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: TensorFlow, Scikit-learn
- **Database**: SQLite
- **Deployment Platform**: Render

---

### Authors
- **Keshav** - Developer and Maintainer


