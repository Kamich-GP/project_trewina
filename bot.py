import telebot
import buttons, database


# Создаем объект бота
bot = telebot.TeleBot('7864118054:AAFdpvfFsiOlzUtBAez5bNg-95NlVuuoOXs')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if database.check_user(user_id):
        bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!')
    else:
        bot.send_message(user_id, 'Привет! Давай начнем регистрацию!\nНапиши свое имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
# Получение имени
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправь свой номер!',
                     reply_markup=buttons.num_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_num, user_name)


# Получение номера
def get_num(message, user_name):
    user_id = message.from_user.id
    # Если отправил номер в виде номера
    if message.contact:
        user_num = message.contact.phone_number
        # Заносим пользователя в БД
        database.register(user_id, user_name, user_num)
        bot.send_message(user_id, 'Регистрация прошла успешно!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    # Если пользователь написал в виде текста
    else:
        bot.send_message(user_id, 'Отправьте контакт по кнопке или отправьте контакт через скрепку!')
        # Возврат на этап получения номера
        bot.register_next_step_handler(message, get_num, user_name)


bot.polling(non_stop=True)
