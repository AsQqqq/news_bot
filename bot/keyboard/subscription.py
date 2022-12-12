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


sports_subscription_not = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.unsubscribe, callback_data='sports_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

videogame_subscription_not = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.unsubscribe, callback_data='videogame_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

bot_subscription_not = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.unsubscribe, callback_data='bot_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))

world_subscription_not = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text=text.unsubscribe, callback_data='world_sub'))\
    .add(InlineKeyboardButton(text=text.cancel, callback_data='not_sub_news'))



edit_storyteller = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text="Safi", callback_data='storyteller_safi'))\
    .insert(InlineKeyboardButton(text="Gerald", callback_data='storyteller_gerald'))