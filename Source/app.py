from flask import Flask, render_template, request
app = Flask(__name__)
app.run(debug=True)
app.static_folder = 'static'
app.secret_key = b'&k;5fdRJSj%V4E8W:ysBYXF39A)a&RS[?hQ48R'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reset')
def reset():
    return render_template('password.html')

@app.route('/serverlist')
def reset():
    return render_template('serverlist.html')