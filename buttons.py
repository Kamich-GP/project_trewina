from telebot import types


# Кнопка для отправки номера
def num_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    num = types.KeyboardButton('Отправить номер📞', request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(num)

    return kb


# Кнопки главного меню
def main_menu(products):
    # Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем сами кнопки
    cart = types.InlineKeyboardButton(text='Корзина🛒', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}', callback_data=i[0]) for i in products]
    # Добавляем кнопки в пространство
    kb.add(*all_products)
    kb.row(cart)

    return kb
