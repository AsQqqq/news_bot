from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from text import text

manu_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)\
    .add(
    KeyboardButton(
        text=text.choose_news_subscription
    )
    )\
    .insert(
    KeyboardButton(
        text=text.bot_settings
    )
    )\
    .add(
    KeyboardButton(
        text=text.contact_the_author
    )
    )

sub_news_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)\
    .add(
    KeyboardButton(
        text=text.live_game_button
    )
    )\
    .insert(
    KeyboardButton(
        text=text.video_game_button
    )
    )\
    .add(
    KeyboardButton(
        text=text.bot_news_button
    )
    )\
    .insert(
    KeyboardButton(
        text=text.world_news_button
    )
    )