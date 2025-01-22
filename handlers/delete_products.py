# delete_products.py
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import main_db
from aiogram.types import InputMediaPhoto


async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)

    button_all = types.InlineKeyboardButton('Вывести все товары', callback_data='delete_all_products')
    button_one = types.InlineKeyboardButton('Вывести по одному', callback_data='delete_one_products')

    keyboard.add(button_all, button_one)

    await message.answer('Выберите как просмотреть товары:' , reply_markup=keyboard)


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

            keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
            delete_button = types.InlineKeyboardButton('Delete',
                                                       callback_data=f'delete_{product["product_id"]}')
            keyboard.add(delete_button)

            await call.message.answer_photo(photo=product["photo"], caption=caption, reply_markup=keyboard)

    else:
        await call.message.answer('База пуста! Товаров нет.')


async def delete_all_products(call: types.CallbackQuery):
    product_id = call.data.split('_')[1]

    main_db.delete_product(product_id)

    if call.message.photo:
        new_caption = 'Товар удален! Обновите список'

        photo_404 = open('media/images.png', 'rb')

        await call.message.edit_media(
            InputMediaPhoto(media=photo_404, caption=new_caption)
        )

    else:
        await call.message.edit_text('Товар удален! Обновите список')



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['delete_store'])
    dp.register_callback_query_handler(send_all_products, Text(equals='delete_all_products'))
    dp.register_callback_query_handler(delete_all_products, Text(startswith='delete_'))