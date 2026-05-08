import sqlite3

import os
DB_NAME = os.path.join(os.getenv("PERSISTENCE_MOUNT", "/data"), "reviews.db")

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            text TEXT,
            photo_id TEXT,
            rating INTEGER DEFAULT 0,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # На случай, если таблица уже была создана без поля rating
    try:
        cursor.execute("ALTER TABLE reviews ADD COLUMN rating INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()

def add_review(user_id, username, text, photo_id, rating=0):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reviews (user_id, username, text, photo_id, rating) VALUES (?, ?, ?, ?, ?)",
                   (user_id, username, text, photo_id, rating))
    review_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return review_id

def update_review_status(review_id, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE reviews SET status = ? WHERE id = ?", (status, review_id))
    conn.commit()
    conn.close()

def get_review(review_id):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # <- теперь можно обращаться по имени колонки
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE id = ?", (review_id,))
    review = cursor.fetchone()
    conn.close()
    return review  # sqlite3.Row или None