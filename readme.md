# 📚 BookNook - A Bookstore & Café API
*This was intended as a group project for 3-5 people (DataCraft School), 
but I had some free time and didn't understand much about APIs, so I used this as a learning-by-doing experience.*
 
A RESTful API for managing products in a bookstore (books, e-books, movies) and café orders, built with FastAPI and SQLite. This was supposed to be a german data school project for up to 5 people. But I had some free time and didn't understand much about APIs, so I used this as a learning-by-doing-chance.

## 📖 Features

- **Bookstore Management**:
  - CRUD operations for Books, E-Books, and Movies
  - Inventory tracking (in-stock status)
  
- **Café Management**:
  - Order tracking for drinks (Latte, Americano, etc.)
  - Backstock inventory management (coffee beans, milk, etc.)
  
- **Additional Features**:
  - Comprehensive change logging
  - Real-time inventory statistics
  - Automatic API documentation

## 🛠️ Technologies

- Python 3.9+
- FastAPI
- SQLite (separate databases for bookstore and café)
- Pydantic (data validation)
- Uvicorn (ASGI server)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api