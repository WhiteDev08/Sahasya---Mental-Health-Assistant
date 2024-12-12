# Sahasya---Mental-Health-Assistant 🧠💬

## Overview 🌟

This project is a web-based application designed to help users with mental health support. It includes:
- A **Chatbot** 🤖 that provides real-time responses using pre-trained models.
- A **Prediction System** 📊 to assess mental health based on specific user inputs.
- A user authentication system with secure database management 🔒.

The project uses **Flask** as the backend framework, a SQLite database for storing user data, and pre-trained models for predictions.

---

## Features 🚀

- **Chatbot** 🤖: A conversational assistant trained to provide basic support and responses.
- **Prediction Models** 🔮: Machine learning models to predict mental health levels for:
  - **Working Professionals** 👨‍💻 (`Sahasya_model_1_Decision.pkl`)
  - **Students** 🎓 (`Sahasya_model_2_SVM.pkl`)
- **User Management** 🧑‍💼: Login, registration, and session handling using Flask-SQLAlchemy.
- **Interactive UI** 🖥️: HTML, CSS, and JavaScript for user-friendly web pages.
- **Secure Authentication** 🔐: Password hashing for secure logins.

---

### Deployment 🚢
The project is deployed using **Render**. The deployment uses:
- **Procfile** 📝: Defines the app's start command using `gunicorn`.
- **Dynamic Path Handling** 📂: Ensures portability for models and the database across environments.

---

### Technologies Used 🛠️
- **Backend**: Flask, Flask-SQLAlchemy 🐍
- **Frontend**: HTML, CSS, JavaScript 🎨
- **Machine Learning**: TensorFlow, Scikit-learn 🤖
- **Database**: SQLite 🗄️
- **Deployment Platform**: Render 🌐

---
# Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/WhiteDev08/Sahasya---Mental-Health-Assistant.git
   cd Sahasya---Mental-Health-Assistant

2.**Ensure the exact versions:**
- Use the **Python version** specified in `runtime.txt`.
- Install dependencies using the versions listed in `requirements.txt`.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4.**Run the application locally:**
  python app.py

---
## Disclaimer ⚠️

🚨 **Important Note**:
- This project has been tested to work **only on local machines** 🖥️ and may not function correctly on deployment platforms like Render 🌐 due to environment and version compatibility issues.
- Please ensure you strictly follow the versions specified in:
  - `runtime.txt` 📜 for Python version.
  - `requirements.txt` 📂 for dependency versions.
- If you encounter issues, verify your local environment matches the required configurations. 🔧
**THIS WAS BUILT ON PYTHON 3.10.0**
---
### Authors ✍️
- **Keshav** - Chatbot and Machine Learning  
- **Afreen Samiullah** - Web Development  
- **Boogitha Sivakumar** - Web Development  
- **Anirudh.S** - Chatbot and Machine Learning  
- **Bhargav Kamath** - Chatbot and Machine Learning  
- **Sruthi** - Web Development 



