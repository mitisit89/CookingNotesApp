from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import CreatePostForm
from app.models import Posts, db

post = Blueprint('post', __name__, template_folder='templates')


@post.route('/')
def index():
    return render_template('post.html')


@login_required
@post.route('/create', methods=['GET', 'POST'])
def create():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = Posts(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)


@post.route('/edit/<str>')
def edit():
    pass
