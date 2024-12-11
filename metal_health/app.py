from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import joblib
import pandas as pd
import json
import sys
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

sys.path.insert(0, r"C:\Users\DELL\Desktop\Complete ai\Final_Projectv1\Project\Chatbot_Final")  # Ensure this line is correctly placed
from app1new import chatbot_response 

app = Flask(__name__)
app.secret_key = "1234"  # Set a secret key for session management

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Load models (adjust paths as necessary)
working_model = joblib.load(r"C:\Users\DELL\Desktop\Complete ai\Final_Projectv1\Project\metal_health\models\Sahasya_model_1_Decision.pkl")
student_model = joblib.load(r"C:\Users\DELL\Desktop\Complete ai\Final_Projectv1\Project\metal_health\models\Sahasya_model_2_SVM.pkl")

# Route to login page (login_page.html)
@app.route('/')
def login():
    return render_template('login_page.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})

@app.route('/login', methods=['POST'])
def login_submit():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Retrieve the user from the database
    user = User.query.filter_by(email=email).first()
    
    # Check if user exists and password matches
    if user and check_password_hash(user.password, password):
        session['user'] = user.email
        session['name'] = user.name
        session['age'] = user.age
        session['gender'] = user.gender
        session['profession'] = 'Working Professional'  # Example field
        return redirect(url_for('about'))
    else:
        flash("Invalid email or password", "error")
        return render_template('login_page.html')

# Route to home page (index.html)
@app.route('/home')
def home():
    if 'user' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('homepagenew1.html')


# Route to register page (register.html)
@app.route('/register')
def register():
    return render_template('register.html')

# Route to handle registration submission
@app.route('/register', methods=['POST'])
def register_submit():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')  # Capture confirm password

    # Check if password and confirm password match
    if password != confirm_password:
        flash("Passwords do not match", "error")
        return render_template('register.html')

    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash("Email is already registered", "error")
        return render_template('register.html')

    # Hash the password and create a new user
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(name=name, age=age, gender=gender, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash("Registration successful! Please login.", "success")
    return redirect(url_for('login'))

# Route to start assessment (frontpage.html)
@app.route('/start')
def start():
    return render_template('frontpage.html')

# Route to quiz introduction (quiz_intro.html)
@app.route('/quiz_intro')
def quiz_intro():
    return render_template('quiz_intro.html')

# Route to select category (student or working professional)
@app.route('/category', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        category = request.form.get('category')
        session['category'] = category
        # Redirect to the appropriate questionnaire page
        if category == 'student':
            return redirect(url_for('s_analysis'))
        else:
            return redirect(url_for('wp_analysis'))
    return render_template('category.html')

# Route for student questionnaire
@app.route('/s_analysis', methods=['GET', 'POST'])
def s_analysis():
    if request.method == 'POST':
        answers_json = request.form.get('answers')
        answers = json.loads(answers_json)  # Convert JSON string back to a Python list

        input_data = pd.DataFrame([answers])
        prediction = student_model.predict(input_data)  # Use student_model for prediction

        session['prediction'] = int(prediction[0])
        return redirect(url_for('result'))
    return render_template('s_analysis.html')

# Route for working professional questionnaire
@app.route('/wp_analysis', methods=['GET', 'POST'])
def wp_analysis():
    if request.method == 'POST':
        answers_json = request.form.get('answers')
        answers = json.loads(answers_json)  # Convert JSON string back to a Python list

        input_data = pd.DataFrame([answers])
        prediction = working_model.predict(input_data)  # Use working_model for prediction

        session['prediction'] = int(prediction[0])
        return redirect(url_for('working_result'))
    return render_template('wp_analysis.html')

# Mapping dictionary for prediction labels
PREDICTION_LABELS = {
    1: "No Depression",
    2: "Minimal Depression",
    3: "Moderate Depression",
    4: "Severe Depression"
}

WPPREDICTION_LABELS = {
    0: "High",
    1: "Low",
    2: "Medium",
}


# Route to display the student prediction result
@app.route('/result')
def result():
    prediction = session.get('prediction', 'No result')
    prediction_text = PREDICTION_LABELS.get(prediction, "Unknown")  # Get the text label
    return render_template('result.html', prediction=prediction_text)

# Route to display the working professional prediction result
@app.route('/working_result')
def working_result():
    prediction = session.get('prediction', 'No result')
    prediction_text = WPPREDICTION_LABELS.get(prediction, "Unknown")  # Get the text label
    return render_template('workingresult.html', prediction=prediction_text)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
