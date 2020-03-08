from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from forms import PostForm
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
    form = PostForm()
    if form.validate_on_submit():
        new_post = Posts(title=form.title.data, body=form.body.data, slug=slugify(form.title.data), author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)


@login_required
@post.route('/<slug>/edit/', methods=['GET', 'POST'])
def edit(slug):
    post_for_edit = Posts.query.filter(Posts.slug == slug).first()
    if request.method == 'POST':
        edited_post = PostForm(formdata=request.form, obj=post_for_edit)
        edited_post.populate_obj(post_for_edit)
        db.session.commit()
        return redirect(url_for('post.index', slug=post_for_edit.slug))
    else:
        form = PostForm(obj=post_for_edit)
        return render_template('edit_post.html', form=form, post=post_for_edit)
