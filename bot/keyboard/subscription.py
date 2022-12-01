from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from text import text

sports_subscription = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.subscribe, callback_data='sports_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

videogame_subscription = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.subscribe, callback_data='videogame_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

bot_subscription = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.subscribe, callback_data='bot_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

world_subscription = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.subscribe, callback_data='world_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))