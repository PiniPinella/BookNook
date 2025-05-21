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


with open('books.csv', 'r') as f:
     reader = csv.reader(f)
     for row in reader:
         cursor.execute("""
 INSERT INTO book (id, title, author, release_year, editor, pages_count, price, in_stock)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['ID'],          # CSV-Spalte 'ID' → DB-Spalte 'id'
            row['Title'],       # CSV-Spalte 'Titel' → DB 'titel'
            row['Author'],
            row['Release Year'],
            row['Editor'],
            row['Page Count'],
            row['Price'],
            True if row['In Stock'].lower() == 'true' else False  # String zu Boolean
        ))
        
conn.commit()
conn.close()
print("Datenbank und Tabellen wurden erstellt!")

########### Datenbank füllen








# ToDos für später
# Für jedes Produkt (also Buch, EBook, Film) sollen folgende Aufrufe möglich sein:
# - Alle Einträge aufrufen
# - Eintrag aufrufen (bspw. Anhand einer ID)
# - Eintrag hinzufügen
# - Eintrag verändern
# - Eintrag entfernen