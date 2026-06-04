# Movie Search Application

Console application for searching movies from the Sakila MySQL database.

The application also stores search history in MongoDB and displays the five most popular search queries.

## Features

* Search movies by title
* Show available movie genres
* Search movies by genre
* Search movies by genre and release year range
* Show available minimum and maximum release years
* Display search results page by page
* Store search queries in MongoDB
* Show the five most popular search queries
* Handle database connection errors

## Technologies

* Python
* MySQL
* MongoDB
* PyMySQL
* PyMongo
* python-dotenv

## Project Structure

```text
.
├── main.py
├── mysql_client.py
├── mongo_client.py
├── sql_queries.py
├── settings.py
├── ui.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Environment Variables

Create a local `.env` file in the project root.

Use as a template:

```env
MYSQL_HOST=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DATABASE=sakila

MONGO_URI=
MONGO_DATABASE=
MONGO_COLLECTION=final_project_your_group_your_full_name
```

Do not commit the `.env` file because it contains credentials.

## Running the Application

Run:

```bash
python main.py
```

## Menu

```text
1. Search movies by title
2. Show genres
3. Search movies by genre
4. Search movies by genre and release year
5. Show popular queries
0. Exit
```

## Pagination

Search results are displayed in pages of 10 movies.

Available commands:

```text
N — next page
P — previous page
Q — return to the main menu
```

## MongoDB Search History

Every search query is saved in MongoDB with:

* search type
* query value
* creation time

The application can display the five most popular queries by frequency.

## Author

Alexander Suligan
