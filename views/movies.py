from flask_restx import Resource, Namespace
from models import Movie, MovieSchema

movie_ns = Namespace('movies')
movies_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query.all()
        return movies_schema.dump(movies, many=True), 200

    def post(self):
        return 'post', 201


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
