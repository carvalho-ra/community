from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config["SECRET_KEY"] = "028d82684689544411b57f7562dd2b41"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

from app import routes
