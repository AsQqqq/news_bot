from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from start_bot import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import control_user_table

CONTROL_TABLE = control_user_table()

#safi stickers
SAFI_EMOTION = config.safi_emotion
SAFI_REJOICES = config.safi_rejoices
SAFI_SAD = config.safi_sad
SAFI_SMILING = config.safi_smiling
SAFI_NO_MOOD = config.safi_no_mood
#gerald stickers
GERALD_EMOTION = config.gerald_emotion
GERALD_REJOICES = config.gerald_rejoices
GERALD_ANGRY = config.gerald_angry
GERALD_SMILING = config.gerald_smiling

ADMIN = int(config.ADMINS)
storage = MemoryStorage()
scheduler = AsyncIOScheduler()
scheduler.start()

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)