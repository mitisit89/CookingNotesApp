from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import CreatePostForm
from app.models import Posts, db
import re
from time import time
post = Blueprint('post', __name__, template_folder='templates')


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower() + '-' + str(int(time()))


@post.route('/<slug>')
def index(slug):
    post = Posts.query.filter(Posts.slug == slug).first()
    return render_template('post.html', post=post)


@login_required
@post.route('/create', methods=['GET', 'POST'])
def create():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = Posts(title=form.title.data, body=form.body.data, slug=slugify(form.title.data), author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)


@post.route('/edit/<str>')
def edit():
    pass
