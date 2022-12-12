from aiogram import types
from start_bot.import_bot import bot

async def message_delete(message: types.Message):
    try:
        await message.delete()
    except:
        print(f"ERROR: message delete failed. {message}")