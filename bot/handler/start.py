from start_bot.import_bot import (
    dp,
    bot,
    ADMIN,
    CONTROL_TABLE,
    scheduler
)
from text import text
from aiogram import types
from datetime import timedelta, datetime
from keyboard import (
    manu_keyboard,
    sub_news_keyboard,
    sports_subscription,
    videogame_subscription,
    bot_subscription,
    world_subscription,
    manu_keyboard_admins,
    user_keyboard_admins
)

async def start_bot(message: types.Message):
    user_id = message.from_user.id
    if not CONTROL_TABLE.user_exists(user_id):
        CONTROL_TABLE.add_user(user_id)
    
    if ADMIN != user_id:
        await message.answer(text.start_bot_text_user, reply_markup=manu_keyboard)
    elif ADMIN == user_id:
        await message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)



async def choose_news_sub(message: types.Message):
    await message.answer(text.choose_news_subscription_text, reply_markup=sub_news_keyboard)

async def live_game(message: types.Message):
    await message.answer(text.live_game_text, reply_markup=sports_subscription)

async def video_game(message: types.Message):
    await message.answer(text.video_game_text, reply_markup=videogame_subscription)

async def bot_news(message: types.Message):
    await message.answer(text.bot_news_text, reply_markup=bot_subscription)

async def world_new(message: types.Message):
    await message.answer(text.world_news_text, reply_markup=world_subscription)

#CANSAL
@dp.callback_query_handler(text='not_sub_news')
async def help_command_inline(call: types.CallbackQuery):
    await call.message.answer(text=text.cansel_text, reply_markup=sub_news_keyboard)


#SUBSCRIPTION
@dp.callback_query_handler(text='sports_sub')
async def help_command_inline(call: types.CallbackQuery):
    user_id = call.from_user.id
    sub = "livegames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await call.message.answer(text=text.subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await call.message.answer(text=text.unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='videogame_sub')
async def help_command_inline(call: types.CallbackQuery):
    user_id = call.from_user.id
    sub = "videogames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await call.message.answer(text=text.subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await call.message.answer(text=text.unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='bot_sub')
async def help_command_inline(call: types.CallbackQuery):
    user_id = call.from_user.id
    sub = "bot"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await call.message.answer(text=text.subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await call.message.answer(text=text.unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='world_sub')
async def help_command_inline(call: types.CallbackQuery):
    user_id = call.from_user.id
    sub = "world"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await call.message.answer(text=text.subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await call.message.answer(text=text.unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

async def other_keyboard(message: types.Message):
    user_id = message.from_user.id
    if ADMIN == user_id:
        await message.answer(text.open_other_keyboard, reply_markup=user_keyboard_admins)

async def back_main_keyboard(message: types.Message):
    user_id = message.from_user.id
    if ADMIN == user_id:
        await message.answer(text.back_open_kbd, reply_markup=manu_keyboard_admins)

def reg_handler(dp):
    dp.register_message_handler(start_bot, commands="start")
    dp.register_message_handler(choose_news_sub, text="Выбрать новостную подписку")
    dp.register_message_handler(other_keyboard, text="Другая клавиатура")
    dp.register_message_handler(back_main_keyboard, text="Назад")
    dp.register_message_handler(live_game, text="Спорт")
    dp.register_message_handler(video_game, text="Видеоигры")
    dp.register_message_handler(bot_news, text="Бот")
    dp.register_message_handler(world_new, text="Мировые")