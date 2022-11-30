from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from start_bot import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import control_user_table

CONTROL_TABLE = control_user_table()

ADMIN = int(config.ADMINS)
storage = MemoryStorage()
scheduler = AsyncIOScheduler()
scheduler.start()

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)