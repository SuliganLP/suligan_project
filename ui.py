def show_menu() -> None:
    print("\nMovie Search")
    print("1. Search movies by title")
    print("2. Show genres")
    print("3. Search movies by genre")
    print("4. Search movies by genre and release year")
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
        movie_info = (
            f"{movie['title']} | "
            f"Rating: {movie['rating']} | "
            f"Year: {movie['release_year']}"
        )

        if "category" in movie:
            movie_info += f" | Genre: {movie['category']}"

        print(movie_info)


def show_genres(genres: list[dict]) -> None:
    if not genres:
        print("No genres found.")
        return

    print("\nGenres:")
    for genre in genres:
        print(f"{genre['category_id']}. {genre['name']}")


def get_genre_id() -> str:
    return input("Enter genre number: ").strip()


def get_start_year() -> str:
    return input("Enter start year: ").strip()


def get_end_year() -> str:
    return input("Enter end year: ").strip()
