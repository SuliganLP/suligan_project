SELECT_FILMS_BY_TITLE = """
SELECT film_id, title, rating, release_year
FROM film
WHERE title LIKE %s
ORDER BY film_id
LIMIT 10 OFFSET %s
"""

SELECT_GENRES = """
SELECT category_id, name
FROM category
ORDER BY category_id
"""
