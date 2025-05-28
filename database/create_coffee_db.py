import sqlite3

conn = sqlite3.connect("database/coffee.db")
cursor = conn.cursor()
cursor.execute("""
  CREATE TABLE IF NOT EXISTS stock (
    cow_milk INTEGER,
    oat_milk INTEGER,
    coffee_beans INTEGER,
    lemonade_INTEGER,
    apple_spritzer INTEGER,
    water INTEGER
  )
""")
conn.commit()

# did the rest in dbeaver