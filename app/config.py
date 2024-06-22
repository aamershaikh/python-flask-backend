import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/asdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
