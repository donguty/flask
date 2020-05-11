from app import app

from flask import Blueprint,render_template

page = Blueprint('page',__name__)

@page.route('/')
@page.route('/index')
def index():
    return render_template('index.html')