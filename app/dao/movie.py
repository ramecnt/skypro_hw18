from app.dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_one(self, uid):
        movie = self.session.query(Movie).get(uid)
        return movie

    def get_by_director(self, director):
        movie = self.session.query(Movie).filter(Movie.director_id == director)
        return movie

    def get_by_genre(self, genre):
        movie = self.session.query(Movie).filter(Movie.genre_id == genre)
        return movie

    def get_by_year(self, year):
        movie = self.session.query(Movie).filter(Movie.year == year)
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, uid):
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
