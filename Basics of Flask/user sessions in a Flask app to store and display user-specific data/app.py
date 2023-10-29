from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
#app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

@app.route('/home', methods=['POST'])
def home():
    session['username'] = request.form['username']
    username = session['username']
    return f'Hello, {username}! </br> <p>Welcome to the Flask Session Example </p><a href="/logout">Logout</a>'


@app.route('/', methods=['GET', 'POST'])
def login():
    return '''
    <form method="POST" action="/home">
        <p>Enter your username:</p>
        <input type="text" name="username">
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
