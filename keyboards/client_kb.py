from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Режим роботи')
b2 = KeyboardButton('Розташування')
b3 = KeyboardButton('Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_client.add(b1).add(b2).insert(b3)
