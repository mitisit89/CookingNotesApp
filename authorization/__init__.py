from flask import Blueprint, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from app.models import Users
from .forms import LoginForm

authorization = Blueprint('authorization', __name__, template_folder='templates')


@authorization.route('/', methods=['GET', 'POST'])
def register():
    pass


@authorization.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()


@authorization.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
