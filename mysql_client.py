import pymysql
from pymysql.cursors import DictCursor
from settings import MYSQL_CONFIG
from sql_queries import SELECT_FILMS_BY_TITLE, SELECT_GENRES, SELECT_FILMS_BY_GENRE, SELECT_FILMS_BY_GENRE_AND_YEAR


def search_movies_by_title(title: str, offset: int = 0) -> list[dict]:
    with pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor) as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_FILMS_BY_TITLE, (f"%{title}%", offset))
            return cursor.fetchall()


def get_genres() -> list[dict]:
    with pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor) as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_GENRES)
            return cursor.fetchall()


def search_movies_by_genre(genre_id: int, offset: int = 0) -> list[dict]:
    with pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor) as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_FILMS_BY_GENRE,(genre_id, offset))
            return cursor.fetchall()


def search_movies_by_genre_and_year(
    genre_id: int,
    start_year: int,
    end_year: int,
    offset: int = 0
) -> list[dict]:
    with pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor) as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_FILMS_BY_GENRE_AND_YEAR, (genre_id, start_year, end_year, offset))
            return cursor.fetchall()