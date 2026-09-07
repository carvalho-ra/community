from main import app, database
from models import User, Post


with app.app_context():
    database.create_all()
