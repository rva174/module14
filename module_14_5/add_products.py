import sqlite3


def add_products(db_name='database.db'):
    """Добавление продуктов в таблицу Products."""
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # Добавляем продукты в таблицу
        cursor.executemany('''
            INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
        ''', [
            ("Яблоко", "Свежие красные яблоки", 50),
            ("Банан", "Спелые бананы", 30),
            ("Апельсин", "Сочные апельсины", 60),
            ("Груша", "Сладкие груши", 70)
        ])

        connection.commit()  # Фиксация изменений
        print("Продукты успешно добавлены.")

    except sqlite3.Error as e:
        print(f"Ошибка при добавлении продуктов: {e}")  # Обработка ошибок
    finally:
        connection.close()


def get_all_products(db_name='database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


if __name__ == '__main__':
    add_products()  # Вызов функции для добавления продуктов

    # Проверим, были ли продукты добавлены
    products = get_all_products()
    print("Список продуктов:", products)  # Выводим список добавленных продуктов
