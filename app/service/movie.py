from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self):
        return self.dao.get_all_movies()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_director(self, director):
        return self.dao.get_by_director(director)

    def get_by_genre(self, genre):
        return self.dao.get_by_genre(genre)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def update(self, data):
        uid = data.get('id')
        movie = self.get_one(uid)

        movie.id = data.get("id")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, uid):
        return self.dao.delete(uid)

    def create(self, data):
        return self.dao.create(data)
