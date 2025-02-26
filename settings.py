import os

import flask
from dotenv import load_dotenv
from flask_cors import CORS
from sqlalchemy.engine.create import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from typing import cast

"""
サーバーの設定
"""

app = flask.Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['ENABLE_AUTH'] = True

"""
データベースの設定
"""

# 2023-01-11T00:00
date_time_format = '%Y-%m-%dT%H:%M'
date_format = '%Y-%m-%d'
manth_format = '%Y-%m'

# read dev.env file
load_dotenv(dotenv_path=".env")

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
db_name = os.environ.get("POSTGRES_DB")

url: str = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'

# engineの設定
engine = create_engine(url=url, pool_recycle=10, echo=True)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()


def get_db_session() -> scoped_session:
    return session()  # type: ignore


def get_db_engine():
    return engine


def get_db_base():
    return Base
