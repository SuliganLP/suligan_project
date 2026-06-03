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
    get_end_year,
    get_pagination_action
)

PAGE_SIZE = 10


def show_paginated_movies(search_function, *args) -> None:
    offset = 0

    while True:
        movies = search_function(*args, offset=offset)

        if not movies:
            if offset == 0:
                show_message("No movies found.")
                break

            show_message("No more movies.")
            offset -= PAGE_SIZE
            continue

        page_number = offset // PAGE_SIZE + 1
        show_message(f"\nPage {page_number}")
        show_movies(movies)

        action = get_pagination_action()

        if action == "n":
            offset += PAGE_SIZE

        elif action == "p":
            if offset == 0:
                show_message("You are already on the first page.")
                continue

            offset -= PAGE_SIZE

        elif action == "q":
            break

        else:
            show_message("Unknown command. Use 'N/n', 'P/p' or 'Q/q'.")


def choose_genre_id() -> int | None:
    genres = get_genres()
    show_genres(genres)

    genre_id = get_genre_id()

    if not genre_id.isdigit():
        show_message("Genre number must be an integer.")
        return None

    genre_id = int(genre_id)

    valid_genre_ids = {genre["category_id"] for genre in genres}

    if genre_id not in valid_genre_ids:
        show_message("Unknown genre number.")
        return None

    return genre_id


def main() -> None:
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            title = get_movie_title()

            if not title:
                show_message("Title cannot be empty.")
                continue

            show_paginated_movies(search_movies_by_title,title)

        elif choice == "2":
            genres = get_genres()
            show_genres(genres)

        elif choice == "3":
            genre_id = choose_genre_id()

            if genre_id is None:
                continue

            show_paginated_movies(search_movies_by_genre, genre_id)

        elif choice == "4":
            genre_id = choose_genre_id()

            if genre_id is None:
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

            show_paginated_movies(search_movies_by_genre_and_year,genre_id, start_year, end_year)

        elif choice == "0":
            show_message("Goodbye!")
            break

        else:
            show_message("Unknown option. Try again.")


if __name__ == "__main__":
    main()
