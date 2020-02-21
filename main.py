from app import app, veiw
from admin import admin
from post import post
from authorization import authorization

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(authorization, url_perfix='/authorization')
app.register_blueprint(post, url_prefix='/post')

if __name__ == '__main__':
    app.run()
