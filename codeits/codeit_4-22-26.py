import sqlite3

conn = sqlite3.connect('codeit.db')
cursor = conn.cursor()

input_tablecreation = input("what is the name of the table you want to add ")


cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {input_tablecreation} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL)
""")
conn.commit()
print(f"table {input_tablecreation} has been created")

def get_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    return tables

# get tables here
tables = get_tables()
print('All tables in our database')
for table in tables:
    # table = [name, rows, etc...]
    #           0      1 ... len(table)-1
    print(table[0])

conn.close()