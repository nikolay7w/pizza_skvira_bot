from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Слава Україні!!!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом через ЛС, напишіть йому: \nhttps://t.me/Pizza_Skvira_bot')

#@dp.message_handler(commands=['Режим_роботи'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 8:00 до 20:00   Сб-Вс с 10:00 до 18:00')

#@dp.message_handler(commands=['Розташування'])
async def pizza_adress_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вул. Степана Бандери')


async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, lambda message: 'Режим роботи' in message.text)
    dp.register_message_handler(pizza_adress_command, lambda message: 'Розташування' in message.text)
    dp.register_message_handler(pizza_menu_command, lambda message: 'Меню' in message.text)