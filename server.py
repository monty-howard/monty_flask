from flask import Flask, url_for, redirect
import sys

print('Starting')
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return redirect(url_for('monty'))


@app.route('/monty')
def monty():
    return redirect(url_for('static', filename='index.html'))


if '--local' in sys.argv:
    app.run(host='127.0.0.1', port=80)
else:
    app.run(host='0.0.0.0', port=80)
