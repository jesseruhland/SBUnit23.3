from models import User, Post, db, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name="Alan", last_name="Alda")
joel = User(first_name="Joel", last_name="Burton")
jane = User(first_name="Jane", last_name="Smith")

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Commit--otherwise, this never gets saved!
db.session.commit()

post1 = Post(title="Post 1", content="This is the content of Post 1.", user_id=1)
post2 = Post(title="Post 2", content="This is the content of Post 2.", user_id=2)
post3 = Post(title="Post 3", content="This is the content of Post 3.", user_id=3)
post4 = Post(title="Post 4", content="This is the content of Post 4.", user_id=1)
post5 = Post(title="Post 5", content="This is the content of Post 5.", user_id=1)
post6 = Post(title="Post 6", content="This is the content of Post 6.", user_id=2)
post7 = Post(title="Post 7", content="This is the content of Post 7.", user_id=2)

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(post5)
db.session.add(post6)
db.session.add(post7)

db.session.commit()

tag1 = Tag(name="Tag One Name")
tag2 = Tag(name="Tag Two Name")
tag3 = Tag(name="Tag Three Name")
tag4 = Tag(name="Tag Four Name")
tag5 = Tag(name="Tag Five Name")

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.add(tag4)
db.session.add(tag5)

db.session.commit()

pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=1, tag_id=2)
pt3 = PostTag(post_id=1, tag_id=3)
pt4 = PostTag(post_id=2, tag_id=4)
pt5 = PostTag(post_id=5, tag_id=1)
pt6 = PostTag(post_id=3, tag_id=5)

db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)
db.session.add(pt5)
db.session.add(pt6)

db.session.commit()