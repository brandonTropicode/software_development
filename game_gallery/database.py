import sqlite3
DB_NAME = "bob's database of games"
TABLE_NAME = 'games'

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    con = connect()
    cursor = con.cursor()

    cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        platform TEXT NOT NULL,
                        description TEXT)
                   """)
    
    con.commit()
    con.close()

def add_game(name, genre, platform, description):
    con = connect()
    cursor = con.cursor()
    cursor.execute(f"""INSERT INTO {TABLE_NAME} (name, genre, platform, description) values (?,?,?,?)""", (name, genre, platform, description))

    con.commit()
    con.close()

if __name__ == "__main__":
    # create table here
    create_tables()
    # add a game to the database
    add_game("wildwest 1v1", "tps", "all", None)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
