from app.dao.model.genre_model import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres

    def get_one(self, uid):
        genre = self.session.query(Genre).get(uid)
        return genre
