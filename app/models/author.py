from flask_sqlalchemy.model import sa
from app import db


class About(db.Model):
    __tablename__ = "about"

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    birthday = sa.Column(sa.DateTime, nullable=False)
    website = sa.Column(sa.String(200), nullable=True)
    phone = sa.Column(sa.String(14), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    age = sa.Column(sa.Integer, nullable=False, default=0)
    degree = sa.Column(sa.String(7), nullable=True)
    email = sa.Column(sa.String(60), nullable=False)
    freelance = sa.Column(sa.String(60), nullable=True)
    is_active = sa.Column(sa.Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Stats(db.Model):
    __tablename__ = "stats"
    
    id = sa.Column(sa.Integer, primary_key=True)
    happy_clients = sa.Column(sa.Integer, nullable=False, default=0)
    projects = sa.Column(sa.Integer, nullable=False, default=0)
    hours_of_support = sa.Column(sa.Integer, nullable=False, default=0)
    hard_works = sa.Column(sa.Integer, nullable=False, default=0)   
    is_active = sa.Column(sa.Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return "Stats"
    

class Skils(db.Model):
    __tablename__ = "skils"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30), nullable=False)
    procent = sa.Column(sa.Integer, nullable=False, default=0) 
    is_active = sa.Column(sa.Boolean, nullable=False, default=True)
    
    def __repr__(self) -> str:
        return self.name
    

class Resume(db.Model):
    __tablename__ = "resume"

    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.String(120), nullable=False)
    summary = sa.Column(sa.Text, nullable=False)
    education = sa.Column(sa.Text, nullable=False)
    professional_experience = sa.Column(sa.Text, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return self.full_name
    

