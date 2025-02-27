import os
from datetime import timedelta

import flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from sqlalchemy.engine.create import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

"""
サーバーの設定
"""
load_dotenv(dotenv_path=".env")

app = flask.Flask(__name__)

app.config["JSON_SORT_KEYS"] = False
app.config["JSON_AS_ASCII"] = False
app.config["ENABLE_AUTH"] = True

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "sceret")
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_LEEWAY"] = 0
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=60 * 60 * 24 * 30)
app.config["JWT_NOT_BEFORE_DELTA"] = timedelta(seconds=0)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
app.config["JWT_CSRF_CHECK_FORM"] = False
app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_COOKIE_SAMESITE"] = "None"

CORS(
    app,
    resources={
        "*": {"origins": ["http://localhost:3000", "https://dreamtree.pages.dev"]}
    },
    supports_credentials=True,
)
jwt = JWTManager(app)


"""
データベースの設定
"""

user = os.environ.get("POSTGRES_USER", "postgres")
password = os.environ.get("POSTGRES_PASSWORD", "postgres")
host = os.environ.get("POSTGRES_HOST", "database")
port = os.environ.get("POSTGRES_PORT", "5432")
db_name = os.environ.get("POSTGRES_DB", "database")

url: str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"

# engineの設定
engine = create_engine(url=url, pool_recycle=10, echo=False)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


def get_db_session() -> scoped_session:
    return session()  # type: ignore


def get_db_engine():
    return engine
