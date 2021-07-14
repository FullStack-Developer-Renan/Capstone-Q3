from flask import Flask
from environs import Env
from app.configs import api, commands, database, migration, jwt


def create_app() -> Flask:
    env = Env()
    env.read_env

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")

    database.init_app(app)
    migration.init_app(app)
    commands.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    return app
