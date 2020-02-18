from flask import Flask
from app.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app.models import Users,Role,Posts







