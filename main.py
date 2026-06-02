from mysql_client import get_genres, search_movies_by_title
from ui import (
    get_menu_choice,
    get_movie_title,
    show_genres,
    show_menu,
    show_message,
    show_movies,
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

        elif choice == "0":
            show_message("Goodbye!")
            break

        else:
            show_message("Unknown option. Try again.")


if __name__ == "__main__":
    main()
