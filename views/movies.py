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
        movie = Movie.query.get(mid)
        if not movie:
            return 'Извините, такого фильма нету', 204
        return movies_schema.dump(movie), 200

    def put(self, mid: int):
        movie = Movie.query.get(mid)
        new_data = request.json
        movie.id = new_data.get('id')
        movie.title = new_data.get('title')
        movie.description = new_data.get('description')
        movie.trailer = new_data.get('trailer')
        movie.year = new_data.get('year')
        movie.rating = new_data.get('rating')
        movie.genre_id = new_data.get('genre_id')
        movie.director_id = new_data.get('director_id')
        return 'Фильм успешно обновлен', 200

    def delete(self, mid: int):
        return 'delete', 200
