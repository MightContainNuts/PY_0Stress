# pylint: disable=wrong-import-order
import dependencies
from flask import Flask, Blueprint
from __init__ import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index2'

@main.route('/profile')
def profile():
    return 'Profile'