# -------- #
# HELPER-FUNKTIONEN
# -------- #

import sqlite3
from classes import Book, Ebook, Movie, Americano, Apple_Spritzer, Latte, Lemonade, Stock

from datetime import datetime

def get_book_connection():
    """Creates and returns book db connection mit dict rows"""
    conn = sqlite3.connect("database/books.db")
    conn.row_factory = sqlite3.Row  # enables access via column name (row["title"])
    return conn

def get_coffee_connection():
    """Creates and returns coffee db connection mit dict rows"""
    conn = sqlite3.connect("database/coffee.db")
    conn.row_factory = sqlite3.Row 
    return conn

def row_to_book(row) -> Book:
    """Converts db rows to book object"""
    return Book(
        id=row["id"],
        title=row["title"],
        author=row["author"],
        release_year=row["release_year"],
        editor=row["editor"],
        page_count=row["page_count"],
        price=row["price"],
        in_stock=bool(row["in_stock"])
    )
def row_to_ebook(row) -> Ebook:
    """Converts db rows to ebook object"""
    return Ebook(
        id=row["id"],
        title=row["title"],
        author=row["author"],
        release_year=row["release_year"],
        editor=row["editor"],
        page_count=row["page_count"],
        price=row["price"],
    )

def row_to_movie(row) -> Movie:
    """Converts db rows to movie object"""
    return Movie(
        id=row["id"],
        title=row["title"],
        producer=row["producer"],
        release_year=row["release_year"],
        price=row["price"],
        in_stock=bool(row["in_stock"])
    )

def row_to_americano(row):
    """Converts database row (with datetime) to Pydantic model (date only)"""
    return Americano(
        id=row[0],
        price=row[1],
        order_date=datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").date()
    )

def row_to_apple_spritzer(row):
    """Converts database row (with datetime) to Pydantic model (date only)"""
    return Apple_Spritzer(
        id=row[0],
        price=row[1],
        order_date=datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").date()
    )

def row_to_latte(row):
    """Converts database row (with datetime) to Pydantic model (date only)"""
    return Latte(
        id=row[0],
        price=row[1],
        order_date=datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").date()
    )

def row_to_lemonade(row):
    """Converts database row (with datetime) to Pydantic model (date only)"""
    return Lemonade(
        id=row[0],
        price=row[1],
        order_date=datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").date()
    )

def row_to_stock(row):
    """Converts db row into stock object"""
    return Stock(
        cow_milk=row["cow_milk"],
        oat_milk=row["oat_milk"],
        coffee_beans=row["coffee_beans"],
        lemonade=row["lemonade"],
        apple_spritzer=row["apple_spritzer"],
        water=row["water"]
    )