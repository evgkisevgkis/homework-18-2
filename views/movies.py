from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return 'get', 200

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
