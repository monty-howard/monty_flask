from flask import Flask, url_for, redirect, render_template
import sys
import os

print('Starting')
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/thingstodo')
def thingstodo():
    return render_template("thingstodo.html")


@app.route('/monty')
def monty():
    return redirect(url_for('static', filename='index.html'))


@app.route('/update')
def update():
    # run 'git pull' to get any updates
    stream = os.popen("""echo Running 'git pull'
    git pull""")
    o = stream.read()
    return f"UPDATE result: {o}", 200


if '--local' in sys.argv:
    app.run(host='127.0.0.1', port=80)
else:
    app.run(host='0.0.0.0', port=80)
