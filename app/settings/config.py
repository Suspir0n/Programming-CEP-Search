from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random
import string

db = SQLAlchemy()
ma = Marshmallow()

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))


def secret_key(app):
    app.config['SECRET_KEY'] = key


def config_db(app):
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db


def config_ma(app):
    ma.init_app(app)


