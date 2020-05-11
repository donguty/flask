from app import app

from flask import Blueprint,request,render_template

from .forms import LoginForm

page = Blueprint('page',__name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
@page.route('/index')
def index():
    return render_template('index.html', title = 'Index')

@page.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm(request.form)

    if request.method=='POST' and form.validate():
        print(form.username.data)
        print(form.password.data)
        print('Thanks for registering')

    return render_template('auth/login.html', title = 'Login', form=form)