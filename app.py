from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def dashboard():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in database.users_database and password == database.users_database[username]:
        return render_template('dashboard.html')
    


def bolden(func):
    def wrap():
        bold = func()
        return f'<b>{bold}<b>'
    return wrap

@app.route('/greeting/<name>/<int:age>')
def greeting(name, age):
    return f'<p>Hello, {age} year old {name} </p>'


if __name__ == "__main__":
   app.run(debug=True, port=5501)

