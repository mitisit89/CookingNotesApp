from flask import Blueprint, render_template

post = Blueprint('post', __name__, template_folder='templates')


@post.route('/')
def index():
    return render_template('post.html')


@post.route('/create')
def create():
    pass


@post.route('/edit/<str>')
def edit():
    pass
