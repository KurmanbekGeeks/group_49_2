# quiz.py
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Далее', callback_data='button1')

    keyboard.add(button)

    question = 'RM or Barcelona'

    answer = ['RM', 'Barcelona', 'Оба']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])