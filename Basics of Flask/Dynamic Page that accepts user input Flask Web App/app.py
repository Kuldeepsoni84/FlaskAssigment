from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')
@app.route('/login', methods=['GET','POST'])
def login_success():
    uname=request.form.get('username')
    pwd=request.form.get('password')

    if pwd and uname:
        return render_template('home.html',uname=uname)
    else:
        return "Server Error"


if __name__ == '__main__':
    app.run()
