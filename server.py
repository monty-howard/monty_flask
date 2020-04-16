from flask import Flask, url_for, redirect
import sys
import os

print('Starting')
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return redirect(url_for('monty'))


@app.route('/monty')
def monty():
    return redirect(url_for('static', filename='index.html'))


@app.route('/update')
def update():
    # run 'git pull' to get any updates
    stream = os.popen('git pull')
    o = stream.read()
    return str(o), 200


if '--local' in sys.argv:
    app.run(host='127.0.0.1', port=80)
else:
    app.run(host='0.0.0.0', port=80)
