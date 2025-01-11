# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/quiz'),
    KeyboardButton('/reply_webapp'),
    KeyboardButton('/inline_webapp'),
    KeyboardButton('/registration'))


submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(KeyboardButton('да'), KeyboardButton('нет'))

# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()