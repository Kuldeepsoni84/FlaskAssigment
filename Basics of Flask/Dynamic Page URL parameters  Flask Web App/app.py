from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')
@app.route('/login', methods=['GET','POST'])
def login_success():
    uname=request.args.get('username')
    pwd=request.args.get('password')
    if pwd and uname:
        return render_template('home.html',username=uname)
    else:
        return ""


if __name__ == '__main__':
    app.run()
