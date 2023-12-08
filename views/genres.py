from flask_restx import Resource, Namespace

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return 'get', 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        return 'get', 200
