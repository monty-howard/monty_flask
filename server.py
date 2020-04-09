from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "hello", 200

@app.route('/monty')
def monty():
    return redirect(url_for('static', filename='index.html'))

app.run(host='0.0.0.0', port=80)