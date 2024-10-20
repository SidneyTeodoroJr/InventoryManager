import sqlite3

def get_db_connection():
    return sqlite3.connect('inventory.db')

def create_table():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_added TEXT NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()

def add_item_to_db(name, date_added, description):
    with get_db_connection() as conn:
        conn.execute('''
            INSERT INTO items (name, date_added, description)
            VALUES (?, ?, ?)
        ''', (name, date_added, description))
        conn.commit()

def get_items_from_db():
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT id, name, date_added, description FROM items')
        return [{'id': row[0], 'name': row[1], 'date_added': row[2], 'description': row[3]} for row in cursor.fetchall()]

def delete_item_from_db(item_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
        conn.commit()

def update_item_in_db(item_id, new_name, new_description):
    with get_db_connection() as conn:
        conn.execute('''
            UPDATE items 
            SET name = ?, description = ?
            WHERE id = ?
        ''', (new_name, new_description, item_id))
        conn.commit()

def delete_all_items_from_db():
    with get_db_connection() as conn:
        conn.execute('DELETE FROM items')
        conn.commit()