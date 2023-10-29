# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy  # Example for SQLAlchemy
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Simulated user database (replace with a real database)
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}
db = SQLAlchemy(app)
#with app.app_context():
#db.create_all()
# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes

@app.route('/')
def home():
    return 'Welcome to the Flask app!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected_route'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': password}
            return redirect(url_for('login'))
        return "Username already exists"
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected_route():
    return f"This is a protected route. You are logged in as user: {current_user.id}"

if __name__ == '__main__':
    app.run()
