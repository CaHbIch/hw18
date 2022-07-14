# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.data_movies_DAO import MoviesDAO
from setup_db import db

movies_dao = MoviesDAO(db.session)