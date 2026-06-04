from datetime import datetime, timezone

from pymongo import MongoClient

from settings import (
    MONGO_COLLECTION,
    MONGO_DATABASE,
    MONGO_URI,
)

client = MongoClient(MONGO_URI)
database = client[MONGO_DATABASE]
collection = database[MONGO_COLLECTION]


def save_search_query(
        search_type: str,
        query: str,
) -> None:
    collection.insert_one(
        {
            "search_type": search_type,
            "query": query,
            "created_at": datetime.now(timezone.utc),
        }
    )


def get_popular_queries() -> list[dict]:
    pipeline = [
        {
            "$group": {
                "_id": {
                    "search_type": "$search_type",
                    "query": "$query",
                },
                "count": {"$sum": 1},
            }
        },
        {
            "$sort": {
                "count": -1,
                "_id.query": 1,
            }
        },
        {
            "$limit": 5
        },
    ]

    return list(collection.aggregate(pipeline))
