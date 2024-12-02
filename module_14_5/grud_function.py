import sqlite3


def initiate_db(db_name='database.db'):
    """Инициализация базы данных и создание таблиц Users и Products, если они не существуют."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        # Создание таблицы Products, если она не существует
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
            )
        """)

        # Создание таблицы Users, если она не существует
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        """)

        conn.commit()


def add_user(username, email, age, db_name='database.db'):
    """Добавление нового пользователя в таблицу Users."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (username, email, age, balance)
            VALUES (?, ?, ?, ?)
        """, (username, email, age, 1000))  # Баланс по умолчанию 1000
        conn.commit()


def is_included(username, db_name='database.db'):
    """Проверка, существует ли пользователь в таблице Users."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Users WHERE username = ?
        """, (username,))
        result = cursor.fetchone()
        return result[0] > 0  # Возвращает True, если пользователь существует




# Пример использования функций
if __name__ == "__main__":
    initiate_db()  # Инициализируем базу данных
    add_user("john_doe", "john@example.com", 30)  # Добавляем пользователя
    print(is_included("john_doe"))  # Проверяем, существует ли пользовател