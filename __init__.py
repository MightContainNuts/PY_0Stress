import dependencies
from flask import Flask

app = Flask(__name__)

@app.route('/')
def base():
    return 'welcome to the base'

@app.route('/index')
def index():
    return 'welcome to the index'