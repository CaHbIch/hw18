from flask_restx import Resource, Namespace

from implemented import movies_dao

genre_ns = Namespace('genres')


@genre_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movies_dao.all_genre_movie(), 200


@genre_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_genre(pk), 200
