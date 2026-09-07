from app import app, database
from app.models import User, Post


with app.app_context():
    database.create_all()
