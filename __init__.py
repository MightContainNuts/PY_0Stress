import dependencies
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return 'welcome to the base'

@app.route('/index')
def index():
    return render_template('index.html')