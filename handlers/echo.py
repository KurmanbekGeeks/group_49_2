# echo.py
from aiogram import Dispatcher, types


# @dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)