from app import app,veiw
from admin import admin
app.register_blueprint(admin,url_prefix='/admin')
if __name__ == '__main__':
    app.run()
