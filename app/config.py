import os

basedir = os.path.abspath(os.path.dirname(__file__))

PASSWORD ="postgres"
PUBLIC_IP_ADDRESS ="34.132.90.11:5432"
DBNAME ="postgres"

#'postgresql://postgres:postgres@postgresdb:5432/postgres'

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or \
        f"postgresql://postgres:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "mailhog"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 1025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['cywong@example.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es', 'zh']
