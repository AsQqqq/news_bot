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

manu_keyboard_admins = ReplyKeyboardMarkup(resize_keyboard = True)\
    .add(
    KeyboardButton(
        text=text.create_ads
        )
    )\
    .insert(
    KeyboardButton(
        text=text.create_warning
        )
    )\
    .add(
    KeyboardButton(
        text=text.create_update
        )
    )\
    .insert(
    KeyboardButton(
        text=text.other_admins_button
        )
    )

user_keyboard_admins = ReplyKeyboardMarkup(resize_keyboard = True)\
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
    )\
    .insert(
    KeyboardButton(
        text=text.back
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