from flask import request
from flask_restx import Resource, Namespace
from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')
movies_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query.all()
        return movies_schema.dump(movies, many=True), 200

    def post(self):
        data = request.json
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        return 'Фильм добавлен в базу', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        return 'get', 200

    def put(self, mid: int):
        return 'put', 200

    def patch(self, mid: int):
        return 'patch', 200

    def delete(self, mid: int):
        return 'delete', 200
