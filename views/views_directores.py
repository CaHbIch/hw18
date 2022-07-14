from flask import request
from flask_restx import Resource, Namespace

from implemented import movies_dao

director_ns = Namespace('directors')


@director_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movies_dao.all_director_movie(), 200


@director_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_director(pk), 200
