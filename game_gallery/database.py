import sqlite3
DB_NAME = "bob's database of games"

def connect():
    return sqlite3.connect(DB_NAME)
def create_tables(name):
    con = connect()
    cursor = con.cursor()

    cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        platform TEXT NOT NULL,
                        description TEXT)
                   """)
    