from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), nullable=False, unique=True)
    summarizatioavailable = db.Column(db.String(20))
    accountsummary = db.Column(db.String(255))
    summarytext = db.Column(db.String(255))
