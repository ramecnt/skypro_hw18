from flask_restx import Namespace, Resource

from app.implemented import genre_service
from app.dao.model.genre_model import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genre_schemas.dump(genres), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        genre = genre_service.get_one(uid)
        return genre_schema.dump(genre), 200
