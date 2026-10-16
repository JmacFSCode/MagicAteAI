import sqlite3

DB_NAME = "magicate.db"

def get_connection():
    connection = sqlite3.connect(DB_NAME)
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant TEXT NOT NULL,
        item_name TEXT NOT NULL,
        category TEXT NOT NULL,
        calories INTEGER,
        protein REAL,
        carbs REAL,
        fat REAL,
        UNIQUE(restaurant, item_name)
        )
    """)

    connection.commit()
    connection.close()


def add_menu_item(restaurant, item_name, category, calories, protein, carbs, fat):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO menu_items
        (restaurant, item_name, category, calories, protein, carbs, fat)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (restaurant, item_name, category, calories, protein, carbs, fat))

    connection.commit()
    connection.close()


def get_menu(restaurant):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM menu_items
        WHERE restaurant = ?
    """, (restaurant,))

    menu_items = cursor.fetchall()

    connection.close()

    return menu_items


def populate_menu():
    menu_items = [
        ("Demo Restaurant", "Grilled Chicken", "Main", 180, 30, 0, 6),
        ("Demo Restaurant", "Brown Rice", "Side", 210, 5, 44, 2),
        ("Demo Restaurant", "Black Beans", "Side", 130, 8, 22, 2),
        ("Demo Restaurant", "Steamed Vegetables", "Side", 50, 3, 10, 0),
        ("Demo Restaurant", "Fresh Fruit", "Side", 80, 1, 20, 0),
        ("Demo Restaurant", "Water", "Drink", 0, 0, 0, 0)
    ]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT OR IGNORE INTO menu_items
        (restaurant, item_name, category, calories, protein, carbs, fat)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, menu_items)

    connection.commit()
    connection.close()



if __name__ == "__main__":
    create_table()

    populate_menu()

    menu = get_menu("Demo Restaurant")

    for item in menu:
        print(item)