from flask import request
from flask_restx import Resource, Namespace
from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')
movies_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query
        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if year:
            movies = movies.filter(Movie.year == year)
        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        if genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)
        movies = movies.all()
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
        db.session.add(movie)
        db.session.commit()
        return 'Фильм успешно обновлен', 200

    def delete(self, mid: int):
        movie = Movie.query.get(mid)
        if not movie:
            return 'Извините, такого фильма нету', 204
        db.session.delete(movie)
        db.session.commit()
        return 'Фильм удален', 200
