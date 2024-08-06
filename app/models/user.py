from flask_login import UserMixin
from flask_sqlalchemy.model import sa
from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(120), nullable=True)
    last_name = sa.Column(sa.String(120), nullable=True)
    username = sa.Column(sa.String(150), unique=True, nullable=False, index=True)
    email = sa.Column(sa.String(150), nullable=True)
    password = sa.Column(sa.String(150), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)

    def __repr__(self):
        return f"<User {self.username}>"

