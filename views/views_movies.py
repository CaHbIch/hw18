from flask_restx import Resource, Namespace

from implemented import movies_dao

movies_ns = Namespace('movies')

@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movies_dao.get_alL_movies(), 200

    def post(self):
        return f'Фильм добавлен', movies_dao.add_movies(),200

@movies_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_movie(pk), 200

    def put(self, pk):
        return f"Фильм обновлен", movies_dao.update_movie(pk), 200

    def delete(self, pk):
        return f"Фильм удален", movies_dao.delete_movie(pk), 200