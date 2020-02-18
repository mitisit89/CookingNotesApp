
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.models import *
user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
security = Security(app, user_datastore)
from app.view import *