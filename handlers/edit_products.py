# edit_products.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db


class EditProducts(StatesGroup):
    for_field = State()
    for_new_photo = State()
    for_new_field = State()


async def start_send_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_all = InlineKeyboardButton('Вывести все товары:', callback_data='edit_products_all')
    button_one = InlineKeyboardButton('Вывести по одному:', callback_data='edit_products_one')
    keyboard.add(button_all, button_one)

    await message.answer('Выберите в каком виде хотите просмотреть товары:', reply_markup=keyboard)



async def send_all_products(call: types.CallbackQuery):
    products = main_db.fetch_all_products()

    if products:
        for product in products:
            caption = (f'Название - {product["name_product"]}\n'
                       f'Размер - {product["size"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Артикул - {product["product_id"]}\n'
                       f'Информация о товаре - {product["info_product"]}\n'
                       f'Цена - {product["price"]}\n')

            edit_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
            edit_button = InlineKeyboardButton('Редактировать', callback_data=f'edit_{product["product_id"]}')
            edit_keyboard.add(edit_button)

            await call.message.answer_photo(photo=product["photo"], caption=caption, reply_markup=edit_keyboard)

    else:
        await call.message.answer('База пустая! Товар нет!')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands='edit_store')
    dp.register_callback_query_handler(send_all_products, Text(equals='edit_products_all'))