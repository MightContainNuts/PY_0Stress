# pylint: disable=wrong-import-order
import dependencies
from flask import Blueprint
#from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'

@main.route('/aboutme')
def aboutme():
    return 'Aboutme'

@main.route('/clog')
def clog():
    return 'Concept2 log'