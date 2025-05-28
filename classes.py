# -------- #
# PYDANTIC MODELLE (Definieren die Datenstruktur für API-Dokumentation und Validierung)
# -------- #
from pydantic import BaseModel
from typing import Optional 
from datetime import date

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    release_year: int
    editor: str
    page_count: int
    price: float
    in_stock: bool

class Ebook(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    release_year: int
    editor: str
    page_count: int
    price: float

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    producer: str
    release_year: int
    price: float
    in_stock: bool

class Americano(BaseModel):
    id: Optional[int] = None
    price: float
    order_date: date

class Apple_Spritzer(BaseModel):
    id: Optional[int] = None
    price: float
    order_date: date

class Latte(BaseModel):
    id: Optional[int] = None
    price: float
    order_date: date

class Lemonade(BaseModel):
    id: Optional[int] = None
    price: float
    order_date: date

class Stock(BaseModel):
    cow_milk: int
    oat_milk: int
    coffee_beans: int
    lemonade: int
    apple_spritzer: int
    water: int

class StockAdjust(BaseModel):
    cow_milk: int = 0
    oat_milk: int = 0
    coffee_beans: int = 0
    lemonade: int = 0
    apple_spritzer: int = 0
    water: int = 0