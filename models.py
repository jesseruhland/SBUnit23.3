"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String, nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')

    posts = db.relationship('Post', backref="users", cascade="all, delete")

    def __repr__(self):
        """Show user info"""
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name}>"

class Post(db.Model):
    """Post"""
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))


    def __repr__(self):
        """Show user info"""
        p = self
        return f"<Post {p.id} {p.title} {p.created_at} {p.user_id}>"


    def date_stamp(self):
        stamp = self.created_at
        result = stamp.strftime("%B %-d, %Y at %-I:%M %p")
        return result