import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://digger:123456asc@192.168.36.68/digger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123456'