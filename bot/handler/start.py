from start_bot.import_bot import (
    dp,
    bot,
    ADMIN,
    CONTROL_TABLE,
    scheduler
)

from aiogram import types
from datetime import timedelta, datetime

async def start_bot(message: types.Message):
    user_id = message.from_user.id
    if not CONTROL_TABLE.user_exists(user_id):
        CONTROL_TABLE.add_user(user_id)
    
    if ADMIN != user_id:
        await message.answer("hello user!")
    elif ADMIN == user_id:
        await message.answer("hello admin!")
    else:
        print("ERROR: 'start_bot' not user_id")

def reg_handler(dp):
    dp.register_message_handler(start_bot, commands="start")