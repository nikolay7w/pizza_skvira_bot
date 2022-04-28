from aiogram import types, Dispatcher
from create_bot import dp, Bot


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text.lower() == 'Привіт':
        await message.answer('І тобі привіт')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
