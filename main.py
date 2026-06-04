from mysql_client import get_genres, search_movies_by_title, search_movies_by_genre, search_movies_by_genre_and_year
from mongo_client import save_search_query, get_popular_queries
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
    get_pagination_action,
    show_popular_queries
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


def choose_genre() -> tuple[int, str] | None:
    genres = get_genres()
    show_genres(genres)

    genre_id = get_genre_id()

    if not genre_id.isdigit():
        show_message("Genre number must be an integer.")
        return None

    genre_id = int(genre_id)

    genres_by_id = {
        genre["category_id"]: genre["name"]
        for genre in genres
    }

    if genre_id not in genres_by_id:
        show_message("Unknown genre number.")
        return None

    return genre_id, genres_by_id[genre_id]


def main() -> None:
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            title = get_movie_title()

            if not title:
                show_message("Title cannot be empty.")
                continue

            save_search_query(search_type="title", query=title)

            show_paginated_movies(search_movies_by_title, title)

        elif choice == "2":
            genres = get_genres()
            show_genres(genres)

        elif choice == "3":

            genre = choose_genre()

            if genre is None:
                continue

            genre_id, genre_name = genre

            save_search_query(

                search_type="genre",

                query=genre_name,

            )

            show_paginated_movies(search_movies_by_genre, genre_id)

        elif choice == "4":

            genre = choose_genre()

            if genre is None:
                continue
            genre_id, genre_name = genre
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

            save_search_query(
                search_type="genre_and_year",
                query=f"{genre_name} | {start_year}-{end_year}"
            )

            show_paginated_movies(search_movies_by_genre_and_year, genre_id, start_year, end_year)

        elif choice == "5":
            queries = get_popular_queries()
            show_popular_queries(queries)

        elif choice == "0":
            show_message("Goodbye!")
            break

        else:
            show_message("Unknown option. Try again.")


if __name__ == "__main__":
    main()
