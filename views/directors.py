from flask_restx import Resource, Namespace
from models import Director, DirectorSchema

director_ns = Namespace('directors')
directors_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dump(directors, many=True), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = Director.query.get(did)
        return directors_schema.dump(director), 200
