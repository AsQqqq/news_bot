from start_bot.import_bot import dp
import logging
from aiogram.utils import executor
from handler import (
    start
)
from database import database

start.reg_handler(dp)

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    database.table_create_user()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)