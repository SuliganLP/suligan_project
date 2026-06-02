def show_menu() -> None:
    print("\nMovie Search")
    print("1. Search movies by title")
    print("2. Show genres")
    print("0. Exit")


def get_menu_choice() -> str:
    return input("Choose an option: ").strip()


def get_movie_title() -> str:
    return input("Enter movie title: ").strip()


def show_message(message: str) -> None:
    print(message)


def show_movies(movies: list[dict]) -> None:
    if not movies:
        print("No movies found.")
        return

    for movie in movies:
        print(
            f"{movie['title']} | "
            f"Rating: {movie['rating']} | "
            f"Year: {movie['release_year']}"
        )


def show_genres(genres: list[dict]) -> None:
    if not genres:
        print("No genres found.")
        return

    print("\nGenres:")
    for genre in genres:
        print(f"{genre['category_id']}. {genre['name']}")
