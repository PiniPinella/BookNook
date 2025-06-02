#### standard libs
from fastapi import FastAPI, HTTPException
#from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel
from typing import List

#### routing
from book_CRUD.book_functions import book_router  # Import der Router
from book_CRUD.ebook_functions import ebook_router
from book_CRUD.movie_functions import movie_router

from coffee_CRUD.americano_functions import americano_router
from coffee_CRUD.apple_spritzer_functions import apple_spritzer_router
from coffee_CRUD.latte_functions import latte_router
from coffee_CRUD.lemonade_functions import lemonade_router
from coffee_CRUD.stock_functions import stock_router
from statistic_CRUD.statistic_functions import statistic_router

#### fetching own functions and classes
from helper_functions import get_book_connection, get_coffee_connection#, row_to_book
from classes import Book, Ebook, Movie

from book_CRUD.book_functions import get_all_books
#from ebook_functions import
#from movie_functions import 



#------------ FastAPI app initialisation
app = FastAPI()

# connecting to function files

app.include_router(book_router)
app.include_router(ebook_router)
app.include_router(movie_router)
app.include_router(americano_router)
app.include_router(apple_spritzer_router)
app.include_router(latte_router)
app.include_router(lemonade_router)
app.include_router(stock_router)
app.include_router(statistic_router)

######## bash
# uvicorn main:app --reload
# http://localhost:8000/docs