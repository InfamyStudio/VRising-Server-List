from flask import Flask, render_template
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = b'&k;5fdRJSj%V4E8W:ysBYXF39A)a&RS[?hQ48R'

promotedservers = [
    {
    'name': 'Server 1',
    'settings': 'Full loot',
    'dateposted': '1/1/2020'
},
    {
    'name': 'Server 2',
    'settings': 'Full loot',
    'dateposted': '1/3/2020'
},
    {
    'name': 'Server 3',
    'settings': 'PvE',
    'dateposted': '1/3/2022'
}
]

@app.route('/')
def index():
    return render_template('serverlisthome.html', promotedservers=promotedservers)

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/info')
def about():
    return render_template('info.html')

@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')

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
def serverlist():
    return render_template('serverlist.html')

@app.route('/topservers')
def topservers():
    return render_template('topservers.html')

@app.route('/newservers')
def newservers():
    return render_template('newservers.html')

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def error401(e):
    return render_template('401.html'), 401

@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500