from flask import Flask, render_template 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foo/<name>')
def foo(name):
    return render_template('index1.html', to=name)

@app.route('/whereami')
def whereami():
    return 'Ghana!'

def bolden(func):
    def wrap():
        bold = func()
        return f'<b>{bold}<b>'
    return wrap

@app.route('/greeting/<name>/<int:age>')

def greeting(name, age):
    return f'<p>Hello, {age} year old {name} </p>'


if __name__ == ('__main__'):
   app.run(debug=True, host='0.0.0.0')

