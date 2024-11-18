import sqlite3


# Подключение к базе данных
connection = sqlite3.connect('delivery.db', check_same_thread=False)
# Python + SQL
sql = connection.cursor()


# Создаем таблицу пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, number TEXT UNIQUE);')
# Создаем таблицу продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products (pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, pr_count INTEGER, pr_photo TEXT);')
# Создаем таблицу корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, user_product TEXT, pr_amount INTEGER);')


## Методы для пользователя ##
# Регистрация
def register(tg_id, name, num):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);', (tg_id, name, num))
    # Фиксируем изменения
    connection.commit()


# Проверка user'а на наличие в БД
def check_user(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False
