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

SELECT_FILMS_BY_GENRE = """
SELECT
    f.film_id,
    f.title,
    f.rating,
    f.release_year,
    c.name AS category
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.category_id = %s
ORDER BY f.film_id
LIMIT 10 OFFSET %s
"""

SELECT_FILMS_BY_GENRE_AND_YEAR = """
SELECT
    f.film_id,
    f.title,
    f.rating,
    f.release_year,
    c.name AS category
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.category_id = %s
  AND f.release_year BETWEEN %s AND %s
ORDER BY f.film_id
LIMIT 10 OFFSET %s
"""

SELECT_RELEASE_YEAR_RANGE = """
SELECT
    MIN(release_year) AS min_year,
    MAX(release_year) AS max_year
FROM film
WHERE release_year IS NOT NULL
"""
