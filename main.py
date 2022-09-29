# pylint: disable=wrong-import-order
import dependencies
from flask import Blueprint, render_template
from __init__ import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'

@main.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')