from app.dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def get_one(self, uid):
        director = self.session.query(Director).get(uid)
        return director
