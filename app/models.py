from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    summarizationavailable = db.Column(db.String(500), nullable=False)
    accountsummary = db.Column(db.String(500), nullable=False)
