# commands.py
from aiogram import Dispatcher, types
import os
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'images.jpeg')

    photo = open(photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это мем')


    # with open(photo_path, 'rb') as photo:
    #     await bot.send_photo(chat_id=message.from_user.id,
    #                          photo=photo,
    #                          caption='Это мем')
    #
    #     await message.answer_photo(photo=photo, caption='Мем')




def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])