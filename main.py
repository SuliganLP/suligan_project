from mysql_client import get_genres, search_movies_by_title, search_movies_by_genre, search_movies_by_genre_and_year
from ui import (
    get_menu_choice,
    get_movie_title,
    show_genres,
    show_menu,
    show_message,
    show_movies,
    get_genre_id,
    get_start_year,
    get_end_year
)


def main() -> None:
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            title = get_movie_title()

            if not title:
                show_message("Title cannot be empty.")
                continue

            movies = search_movies_by_title(title)
            show_movies(movies)

        elif choice == "2":
            genres = get_genres()
            show_genres(genres)

        elif choice == "3":
            genres = get_genres()
            show_genres(genres)

            genre_id = get_genre_id()

            if not genre_id.isdigit():
                show_message("Genre number must be an integer.")
                continue

            genre_id = int(genre_id)

            if not 1 <= genre_id <= 16:
                show_message("Choose a genre number from 1 to 16.")
                continue

            movies = search_movies_by_genre(genre_id)
            show_movies(movies)

        elif choice == "4":
            genres = get_genres()
            show_genres(genres)

            genre_id = get_genre_id()

            if not genre_id.isdigit():
                show_message("Genre number must be an integer.")
                continue

            genre_id = int(genre_id)

            valid_genre_ids = {genre["category_id"] for genre in genres}

            if genre_id not in valid_genre_ids:
                show_message("Unknown genre number.")
                continue

            start_year = get_start_year()
            end_year = get_end_year()

            if not start_year.isdigit() or not end_year.isdigit():
                show_message("Years must be integers.")
                continue

            start_year = int(start_year)
            end_year = int(end_year)

            if start_year > end_year:
                show_message("Start year cannot be greater than end year.")
                continue

            movies = search_movies_by_genre_and_year(genre_id, start_year, end_year)
            show_movies(movies)

        elif choice == "0":
            show_message("Goodbye!")
            break

        else:
            show_message("Unknown option. Try again.")


if __name__ == "__main__":
    main()
