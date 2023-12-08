from flask import Flask
from flask_restx import Api

from config import Config
# from models import Review, Book
from setup_db import db
from views.movies import movie_ns
# from views.reviews import review_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    create_data(app, db)


def create_data(app, db):
    # with app.app_context():
    #     db.create_all()
    #
    #     with db.session.begin():
    #         db.session.add_all()
    pass


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)



