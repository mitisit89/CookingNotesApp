from flask import render_template, request
from app import app
from app.models import Posts


@app.route('/', methods=['GET'])
def index():
    q = request.args.get('q')
    if q:
        posts = Posts.query.filter(Posts.title.contains(q) | Posts.body.contains(q)).all()
    else:
        posts = Posts.query.all()
    return render_template('index.html', posts=posts)
