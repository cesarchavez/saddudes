from flask import Flask, render_template, url_for, request, redirect
from sad import combination

app = Flask(__name__)

@app.route('/')
def index():
    data = combination(12 )
    return render_template('index.html', len=len(data), data=data)

@app.route('/10')
def index10():
    data = combination(10)
    return render_template('index.html', len=len(data), data=data)

@app.route('/12')
def index12():
    data = combination(12)
    return render_template('index.html', len=len(data), data=data)

@app.route('/borrador')
def borrador():
    return render_template('borrador.html')

if __name__ == "__ main__":
    app.run(debug=True)