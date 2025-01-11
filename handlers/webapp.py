# webapp.py
from aiogram import types, Dispatcher


async def reply_webapp(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    geeks_online = types.KeyboardButton('Geeks Online',
                                        web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = types.KeyboardButton('Youtube',
                                   web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    github = types.KeyboardButton('Github', web_app=types.WebAppInfo(url='https://github.com/'))

    netflix = types.KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/'))


    keyboard.add(geeks_online, youtube, github, netflix)

    await message.answer('Reply Кнопки: ', reply_markup=keyboard)


async def inline_webapp(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=4)

    spotify = types.InlineKeyboardButton('Spotify', web_app=types.WebAppInfo(url='https://open.spotify.com/'))

    jutsu = types.InlineKeyboardButton('Jutsu', web_app=types.WebAppInfo(url='https://www.jutsu.com/'))

    kinokrad = types.InlineKeyboardButton('Kinokrad', web_app=types.WebAppInfo(url='https://kinokrad.ac/'))

    os_kg = types.InlineKeyboardButton('OS KG', web_app=types.WebAppInfo(url='https://oc.kg/'))

    geeks_online = types.InlineKeyboardButton('Geeks Online', url='https://online.geeks.kg/')

    keyboard.add(spotify, jutsu, kinokrad, os_kg, geeks_online)

    await message.answer('Inline кнопки: ', reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])
    dp.register_message_handler(inline_webapp, commands=['inline_webapp'])