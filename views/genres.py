from flask_restx import Resource, Namespace
from models import Genre, GenreSchema
from setup_db import db

genres_ns = Namespace('genres')
genres_schema = GenreSchema()


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return genres_schema.dump(genres, many=True), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = Genre.query.get(gid)
        return genres_schema.dump(genre), 200
