import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLITE
# MYSQL, POSTGRES, SQL SERVER
class Config:
    POSTS_PER_PAGE = 5
    SECRET_KEY = os.environ.get("SECRET_KEY") or "voce-nunca-adivinhara"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ["naoresponda.microblog@yahoo.com"]
    SERVER_NAME = "localhost:5000"
    MAIL_PORT = 8025
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    LANGUAGES = ["pt-BR", "en"]
    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
