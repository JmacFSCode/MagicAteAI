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
            calories INTEGER,
            protein REAL,
            carbs REAL,
            fat REAL
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
    print("MagicAte database initialized!")
