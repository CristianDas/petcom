from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hola mundo'


@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/layout')

def layout():
    return render_template('layout.html')

@app.route('/Admin')

def layout():
    return render_template('Admin.html')


@app.route('/registrar')

def registrar():
    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(debug = True)


