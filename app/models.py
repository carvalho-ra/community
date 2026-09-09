from app import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    profile_img = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='author', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')

    def count_posts(self):
        return len(self.posts)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    created_at = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
