from aiogram import executor
import logging
from config import bot, Admins, dp
from handlers import (commands, echo, quiz, webapp, FSM_registration, store_fsm,
                      send_products,delete_products)
from buttons import start
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бок включен!', reply_markup=start)

    await main_db.create_db()


commands.register_handlers(dp)
quiz.register_handlers(dp)
webapp.register_handlers(dp)

FSM_registration.register_handlers_fsm_reg(dp)
store_fsm.register_handlers_store(dp)

send_products.register_handlers(dp)
delete_products.register_handlers(dp)

echo.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)