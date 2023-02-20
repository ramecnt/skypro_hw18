from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie_model import MovieSchema
from app.implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movie_schemas = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        if director:
            movie_director = movie_service.get_by_director(director)
            return movie_schema.dump(movie_director), 200

        elif genre:
            movie_genre = movie_service.get_by_genre(genre)
            return movie_schema.dump(movie_genre), 200

        elif year:
            movie_year = movie_service.get_by_year(year)
            return movie_schema.dump(movie_year), 200

        all_movies = movie_service.get_all_movies()
        return movie_schemas.dump(all_movies), 200

    def post(self):
        request_json = request.json
        movie_service.create(request_json)
        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        movie = movie_service.get_one(uid)
        if movie is None:
            return '', 404
        return movie_schema.dump(movie), 200

    def put(self, uid):
        request_json = request.json
        request_json['id'] = uid
        movie_service.update(request_json)
        return "", 204

    def delete(self, uid):
        movie_service.delete(uid)
        return "", 204
