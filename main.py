# pylint: disable=wrong-import-order
import dependencies
from flask import Blueprint
#from . import db

try:
    main = Blueprint('main', __name__)
    print ('success - main-py import blueprint is working')

except:
    print ('oops - main-py is bust')

@main.route('/')
def index():
    return 'Index2'

@main.route('/profile')
def profile():
    return 'Profile'

@main.route('/aboutme')
def aboutme():
    return 'Aboutme'