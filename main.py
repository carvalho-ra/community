from app import app, database
from app.models import User, Post


with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
