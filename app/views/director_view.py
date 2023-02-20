from flask_restx import Namespace, Resource

from app.implemented import director_service
from app.dao.model.director_model import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
director_schemas = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return director_schemas.dump(directors), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        director = director_service.get_one(uid)
        return director_schema.dump(director), 200
