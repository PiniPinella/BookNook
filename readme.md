# 📚 BookNook - A Bookstore & Café API
*Originally designed as a group project for 3–5 participants at DataCraft School,
I decided to tackle it solo during some free time. I didn’t know much about APIs back then,
so I turned it into a hands-on learning experience.*
 
This is a RESTful API for managing products in a bookstore (books, e-books, movies) and café orders, built with FastAPI and SQLite.

## 📖 Features

- **Bookstore Management**:
  - CRUD operations for Books, E-Books, and Movies
  - Inventory tracking (in-stock status)
  
- **Café Management**:
  - Order tracking for drinks (Latte, Americano, etc.)
  - Backstock inventory management (coffee beans, milk, etc.)
  
- **Additional Features**:
  - Comprehensive change logging
  - Real-time inventory statistics for Books and Movies
  - Automatic API documentation

## 🛠️ Technologies

- Python 3.9+
- FastAPI
- SQLite (separate databases for bookstore and café)
- Pydantic (data validation)
- Uvicorn (ASGI server)

## 🚀 Terminal-Installation

1. Clone the repository:
    git clone https://github.com/yourusername/bookstore-api.git
    cd bookstore-api

2. Install required libraries
    pip install -r requirements.txt

3. Run the API
    uvicorn main:app --reload


## 📊 Database Structure


erDiagram
    BUCH {
        int id PK
        string titel
        string autor
        int erscheinungsjahr
        float preis
        bool auf_lager
    }
    
    CAFE_BESTELLUNG {
        int id PK
        string produkttyp
        datetime bestelldatum
        float preis
    }
    
    AENDERUNGSLOG {
        datetime timestamp
        string operation
        string tabelle
        int eintrag_id
        string details
    }