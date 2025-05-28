from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
import sqlite3

# self made
from helper_functions import get_book_connection, get_coffee_connection

statistic_router = APIRouter(prefix="/statistic")

@statistic_router.get("/")
def get_statistic():
    """
    Returns total count and value of all in-stock books and movies.
    """
    try:
        conn = get_book_connection()
        cursor = conn.cursor()

        #books
        cursor.execute("SELECT COUNT(*), SUM(price) FROM book WHERE in_stock = 'true'")
        book_count, book_value = cursor.fetchone()

        # movies
        cursor.execute("SELECT COUNT(*), SUM(price) FROM movie WHERE in_stock = 'true'")
        movie_count, movie_value = cursor.fetchone()

        conn.close()

        # not null
        total_count = (book_count or 0) + (movie_count or 0)
        total_value = (book_value or 0) + (movie_value or 0)

        return {
            "total_items": total_count,
            "total_value ($)": round(total_value, 2),
            "details": {
                "books": {"count": book_count or 0, "value": round(book_value or 0, 2)},
                "movies": {"count": movie_count or 0, "value": round(movie_value or 0, 2)}
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Statistics could not be calculated: {str(e)}")