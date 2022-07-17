from flask import request
from flask_restx import Resource, Namespace

from implemented import movies_dao

movies_ns = Namespace('movies')


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        if director_id:
            return movies_dao.get_movie_by_director(director_id), 200
        if genre_id:
            return movies_dao.get_movie_by_genre(genre_id), 200
        if year:
            return movies_dao.get_movie_by_year(year), 200
        return movies_dao.get_alL_movies(), 200

    def post(self):
        add_movies = movies_dao.add_movies()
        return f'Фильм добавлен', add_movies, 200


@movies_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        one_movie = movies_dao.get_one_movie(pk)
        return one_movie, 200

    def put(self, pk):
        update_movie = movies_dao.update_movie(pk)
        return f"Фильм обновлен", update_movie, 200

    def delete(self, pk):
        delete_movie = movies_dao.delete_movie(pk)
        return f"Фильм удален", delete_movie, 200
