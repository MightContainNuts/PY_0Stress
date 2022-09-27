import dependencies
from flask import Flask

app = Flask( __name__ )

app.route('/')
def base():
    return 'welcome to the index'

app.route('/index')
def base():
    return 'welcome to the index'