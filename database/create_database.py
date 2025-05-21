import sqlite3
import csv


##### geht nur, solange die api in der main nicht läuft

# Verbindung zur Datenbank herstellen (erstellt 'buecher.db' automatisch, falls nicht vorhanden)
conn = sqlite3.connect('database/books.db')
cursor = conn.cursor()

# Tabelle 'buch' erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        release_year INTEGER,
        editor TEXT,
        page_count INTEGER,
        price FLOAT,
        in_stock BOOLEAN
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebook (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        release_year INTEGER,
        editor TEXT,
        page_count INTEGER,
        price FLOAT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie (
        id INTEGER PRIMARY KEY,
        title TEXT,
        producer TEXT,
        release_year INTEGER,
        price FLOAT
        in_stock BOOLEAN
    )
''')

conn.commit()
conn.close()
print("Datenbank und Tabellen wurden erstellt!")


### csv hab ich über dbeaver importiert :)