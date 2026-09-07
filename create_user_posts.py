from app import app, database
from app.models import User, Post

# with app.app_context():
#     user = User(username="Rodrigo", email="rodrigo@gmail.com", password="123456")
#     user2 = User(username="Felipe", email="felipe@gmail.com", password="234567")

#     database.session.add(user)
#     database.session.add(user2)

#     database.session.commit()

# with app.app_context():
#     post = Post(user_id=1, title='Primeiro post', body='Post text')
#     database.session.add(post)
#     database.session.commit()


with app.app_context():
    all_users = User.query.all()
    print(all_users)

# with app.app_context():
#     all_posts = Post.query.first()
#     print(all_posts.author.email)
#     print(all_posts.title)

# delete database
# # with app.app_context():
# #     database.drop_all()
