from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel
from typing import List

######## bash
# uvicorn main:app --reload

# Initialisiere die FastAPI-App
app = FastAPI()

# -------- #
# PYDANTIC MODELLE (Definieren die Datenstruktur für API-Dokumentation und Validierung)
# -------- #

class Book(BaseModel):
    id: int
    title: str
    author: str
    release_year: int
    editor: str
    page_count: int
    price: float
    in_stock: bool

class Ebook(BaseModel):
    id: int
    title: str
    author: str
    release_year: int
    editor: str
    page_count: int
    price: float

class Movie(BaseModel):
    id: int
    title: str
    producer: str
    release_year: int
    price: float
    in_stock: bool


# -------- #
# HELPER-FUNKTIONEN
# -------- #

def get_db_connection():
    """Erstellt und gibt eine DB-Verbindung mit Dictionary-Rows zurück"""
    conn = sqlite3.connect("database/books.db")
    conn.row_factory = sqlite3.Row  # Ermöglicht zugriff via Spaltennamen (row["title"])
    return conn

def row_to_book(row) -> Book:
    """Wandelt eine DB-Zeile in ein Book-Objekt um"""
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

# -------- #
# API-ENDPOINTS
# -------- #

@app.get("/books", response_model=List[Book])
def get_all_books():
    """Gibt alle Bücher aus der Datenbank zurück"""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book")
        return [row_to_book(row) for row in cursor.fetchall()]
    finally:
        conn.close()  # Wird NACH return ausgeführt

@app.get("/books/{id}", response_model=Book)
def get_book(id: int):
    """Gibt ein spezifisches Buch anhand der ID zurück"""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book WHERE id = ?", (id,))  # Hier book_id verwenden
        book = cursor.fetchone()
        if not book:
            raise HTTPException(status_code=404, detail="Buch nicht gefunden")
        return row_to_book(book)
    finally:
        conn.close()