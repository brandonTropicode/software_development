import sqlite3
DB_NAME = "menubase.db"


def connect():
    conn =  sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS menu(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price DECIMAL(10,2) NOT NULL,
                        category TEXT NOT NULL)
                   """)
    
    conn.commit()
    conn.close()

def add_item(name, description, price, category):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO menu (name, description, price, category) values (?,?,?,?)", (name, description, price, category))

    conn.commit()
    conn.close()

def get_item_by_id(id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM menu WHERE id = ?",(id,))
    item = cursor.fetchone()

    conn.close()
    return item
def get_menu():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM menu")
    entire_menu = cursor.fetchall()

    conn.close()
    return entire_menu 

def display_menu_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, description, price, category
        FROM menu
    """)

    items = cursor.fetchall()

    conn.close()

    print("\n" + "=" * 100)
    print(" " * 38 + "CRYSTAL CAVERNS MENU")
    print("=" * 100)

    if len(items) == 0:
        print("\nNo menu items found.\n")
        print("=" * 100)
        return

    print(f"{'ID':<5} {'Name':<20} {'Description':<35} {'Price':<12} {'Category':<15}")
    print("-" * 100)

    for item in items:
        item_id = item["id"]
        name = item["name"]
        description = item["description"]
        price = item["price"]
        category = item["category"]

        print(
            f"{item_id:<5} "
            f"{name:<20} "
            f"{description:<35} "
            f"${price:<11.2f} "
            f"{category:<15}"
        )

    print("=" * 100 + "\n")