from flask import render_template
from app import app
from app.models import Posts


@app.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


def search():
    pass
