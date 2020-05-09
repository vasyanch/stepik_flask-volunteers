import os

current_path = os.path.dirname(os.path.realpath(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('STEPIK_VOLUNTEERS_SECRET_KEY_API')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
