from dotenv import load_dotenv, find_dotenv
import os

import datetime

load_dotenv(find_dotenv(".env"))

user = os.getenv("POSTGRES_USER")
database = os.getenv("POSTGRES_DB")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRE_PORT", 5432)

mail_username = os.getenv("MAIL_USERNAME")
mail_password = os.getenv("MAIL_PASSWORD")

secret_key = os.getenv("SECRET_KEY")


class Config:
    # Secret key
    SECRET_KEY = secret_key
    # Database
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}" # PostgreSQL
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db" # Sqlite3
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    LABEL_DEFAULT_LOCALE = 'en'
    # Timezone
    LABEL_DEFAULT_TIMEZONE = 'Asia/Tashkent'
    # Email 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = mail_username
    MAIL_PASSWORD = mail_password
    # Language
    LANGUAGES = ['en', 'es', 'ru']
    # Cache
    CACHE_TYPE = 'simple'
    # Redirects
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///flask-test.db"
    WTF_CSRF_ENABLED = False


config = Config()
test_config = TestConfig()