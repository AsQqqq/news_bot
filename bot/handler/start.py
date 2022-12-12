from start_bot.import_bot import (
    dp,
    bot,
    ADMIN,
    CONTROL_TABLE,
    scheduler,
    SAFI_REJOICES,
    GERALD_REJOICES
)
from text import text
from aiogram import types
from datetime import timedelta, datetime
import time
from keyboard import (
    manu_keyboard,
    sub_news_keyboard,
    sports_subscription,
    videogame_subscription,
    bot_subscription,
    world_subscription,
    manu_keyboard_admins,
    user_keyboard_admins,
    keyboard_for_exiting_the_state_machine,
    edit_storyteller,
    keyboard_edit_bots,
    sports_subscription_not,
    videogame_subscription_not,
    bot_subscription_not,
    world_subscription_not,
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from handler.message_delete import message_delete

async def start_bot(message: types.Message):
    try:
        await message.delete()
    except:
        pass
    user_id = message.from_user.id
    global message_storyteller_exists, msg_start_stick, msg_start
    if not CONTROL_TABLE.user_exists(user_id):  
        CONTROL_TABLE.add_user(user_id)
        storyteller_user = "NotFound"
        CONTROL_TABLE.update_storyteller_user(user_id, storyteller_user)
    else:
        if CONTROL_TABLE.select_status(user_id) == False:
            await CONTROL_TABLE.update_status(user_id, True)
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller == "NotFound":
        message_storyteller_exists = await message.answer(text=text.select_message_personality, reply_markup=edit_storyteller)
    elif storyteller == "Safi":
        text_user = text.text_start_bot_text_user(storyteller)
        if ADMIN != user_id:
            msg_start_stick = await bot.send_sticker(message.from_user.id, SAFI_REJOICES)
            msg_start = await message.answer(text_user, reply_markup=manu_keyboard)
        elif ADMIN == user_id:
            msg_start_stick = await bot.send_sticker(message.from_user.id, SAFI_REJOICES)
            try:
                msg_start = await message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)
            except:
                msg_start = await bot.send_message(message.from_user.id, text.start_bot_text_admin, reply_markup=manu_keyboard_admins)
    elif storyteller == "Gerald":
        text_user = text.text_start_bot_text_user(storyteller)
        if ADMIN != user_id:
            msg_start_stick = await bot.send_sticker(message.from_user.id, GERALD_REJOICES)
            msg_start = await message.answer(text_user, reply_markup=manu_keyboard)
        elif ADMIN == user_id:
            msg_start_stick = await bot.send_sticker(message.from_user.id, GERALD_REJOICES)
            try:
                msg_start = await message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)
            except:
                msg_start = await bot.send_message(message.from_user.id, text.start_bot_text_admin, reply_markup=manu_keyboard_admins)
    else:
        print("ERROR: message in /start")


async def back_for_menu(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.message_back_from_user_menu
    if storyteller != "NotFound":    
        if user_id == ADMIN:
            await message.answer(text_user ,reply_markup=user_keyboard_admins)
        else:
            await message.answer(text_user ,reply_markup=manu_keyboard)
    else:
        await message.answer(text=text.message_error_storyteller)

@dp.callback_query_handler(text="storyteller_safi")
async def edit_name(call: types.CallbackQuery):
    await call.answer()
    global storyteller
    user_id = call.from_user.id
    storyteller_user = "Safi"
    CONTROL_TABLE.update_storyteller_user(user_id, storyteller_user)
    date_5 = datetime.now() + timedelta(seconds=5)
    message_safi = await call.message.answer("Выбрана Safi")
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.text_start_bot_text_user(storyteller)
    if ADMIN != user_id:
        await bot.send_sticker(call.from_user.id, SAFI_REJOICES)
        await call.message.answer(text_user, reply_markup=manu_keyboard)
    elif ADMIN == user_id:
        await bot.send_sticker(call.from_user.id, SAFI_REJOICES)
        await call.message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)

@dp.callback_query_handler(text="storyteller_gerald")
async def edit_name(call: types.CallbackQuery):
    await call.answer()
    global storyteller
    user_id = call.from_user.id
    storyteller_user = "Gerald"
    CONTROL_TABLE.update_storyteller_user(user_id, storyteller_user)
    date_5 = datetime.now() + timedelta(seconds=5)
    message_gerald = await call.message.answer("Выбран Gerald")
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.text_start_bot_text_user(storyteller)
    if ADMIN != user_id:
        await bot.send_sticker(call.from_user.id, GERALD_REJOICES)
        await call.message.answer(text_user, reply_markup=manu_keyboard)
    elif ADMIN == user_id:
        await bot.send_sticker(call.from_user.id, GERALD_REJOICES)
        await call.message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)

async def edit_bots(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.text_edit_bot_text(storyteller)
    if storyteller != "NotFound":    
        await message.answer(text_user ,reply_markup=keyboard_edit_bots)
    else:
        await message.answer(text=text.message_error_storyteller)

async def edit_storyteller_for_bot(message: types.Message):
    await message.delete()
    global message_storyteller_exists
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.select_message_personality
    if storyteller != "NotFound":    
        message_storyteller_exists = await message.answer(text_user ,reply_markup=edit_storyteller)
    else:
        await message.answer(text=text.message_error_storyteller)


#everyone, news
editors_control = "everyone"

#машина состояний
class message_everyone(StatesGroup):
    mailing_list_name = State()
    mailing_list_description = State()
    mailing_list_img = State()
    mailing_list_sub = State()

async def message_everyone_add(message: types.Message):
    global msg_state
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller != "NotFound":
        if message.from_user.id == ADMIN:
            msg_state = await message.answer(text=text.message_everyone_text_state_add, reply_markup=keyboard_for_exiting_the_state_machine)
            await message_everyone.mailing_list_name.set()
        else:
            await message.answer(text=text.error_message)
    else:
        await message.answer(text=text.message_error_storyteller)
#ловим название
async def name_message_everyone_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    async with state.proxy() as data:
        data['mailing_list_name'] = message.text
    await message_everyone.next()
    msg_state = await message.answer(text=text.message_everyone_text_state_name, reply_markup=keyboard_for_exiting_the_state_machine)
#ловим описание
async def description_message_everyone_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    async with state.proxy() as data:
        data['mailing_list_description'] = message.text
    await message_everyone.next()
    msg_state = await message.answer(text=text.message_everyone_text_state_photo, reply_markup=keyboard_for_exiting_the_state_machine)

async def photo_message_everyone_bot(message: types.Message, state: FSMContext):
    global msg_state
    try:
        user_id = message.from_user.id
        msg_state_id = msg_state.message_id
        await bot.delete_message(user_id, msg_state_id)
    except:
        pass
    await message.delete()
    if message.photo:
        async with state.proxy() as data:
            data['mailing_list_img'] = message.photo[0].file_id
        msg_state = await message.answer(text=text.message_everyone_text_state_sub, reply_markup=keyboard_for_exiting_the_state_machine)
        await message_everyone.next()
    else:
        await message.answer(text=text.message_error_storyteller)
#ловим подпись
async def dev_message_everyone_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    global data_global_everyone
    async with state.proxy() as data:
        data['mailing_list_sub'] = message.text
    msg_state = await message.answer(text=text.message_everyone_text_state_send, reply_markup=manu_keyboard_admins)
    data_global_everyone = await state.get_data()
    await check_error(message)
    await state.finish()

async def check_error(message: types.Message):
    global editors_control, msg_state
    try:
        user_id = message.from_user.id
        msg_state_id = msg_state.message_id
        await bot.delete_message(user_id, msg_state_id)
    except:
        pass
    editors_control = "everyone"
    mailing_list_name = str(data_global_everyone.get("mailing_list_name"))
    mailing_list_img = data_global_everyone.get("mailing_list_img")
    mailing_list_description = str(data_global_everyone.get("mailing_list_description"))
    mailing_list_sub = str(data_global_everyone.get("mailing_list_sub"))
    msg_state = await bot.send_photo(message.from_user.id, mailing_list_img, f'{mailing_list_name}\n{mailing_list_description}\n{mailing_list_sub}',\
        reply_markup=InlineKeyboardMarkup(resize_keyboard=True)\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_name}", callback_data=f"name handler_"))\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_description}", callback_data=f"description handler_"))\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_sub}", callback_data=f"sub handler_"))\
            .add(InlineKeyboardButton(f"{text.delete_mailing_list}", callback_data=f"delete_mailing_list_"))\
            .insert(InlineKeyboardButton(f"{text.send_mailing_list}", callback_data="send_mailing_list_")))

#машина состояний
class message_news(StatesGroup):
    news_list_name = State()
    news_list_description = State()
    news_list_sub = State()
    news_list_img = State()
async def message_news_add(message: types.Message):
    global msg_state
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller != "NotFound":
        if message.from_user.id == ADMIN:
            msg_state = await message.answer(text=text.message_news_text_state_add, reply_markup=keyboard_for_exiting_the_state_machine)
            await message_news.news_list_name.set()
        else:
            await message.answer(text=text.error_message)
    else:
        await message.answer(text=text.message_error_storyteller)
#ловим название
async def name_news_everyone_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    async with state.proxy() as data:
        data['news_list_name'] = message.text
    await message_news.next()
    msg_state = await message.answer(text=text.message_news_text_state_name, reply_markup=keyboard_for_exiting_the_state_machine)
#ловим описание
async def description_message_news_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    async with state.proxy() as data:
        data['news_list_description'] = message.text
    await message_news.next()
    msg_state = await message.answer(text=text.message_news_text_state_sub, reply_markup=keyboard_for_exiting_the_state_machine)
#ловим подпись
async def dev_message_news_bot(message: types.Message, state: FSMContext):
    global msg_state
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    global data_global_news
    async with state.proxy() as data:
        data['news_list_sub'] = message.text
        data['news_list_img'] = "https://www.ampersand.net/wp-content/uploads/2018/06/quotationew.jpg"
    msg_state = await message.answer(text=text.message_news_text_state_send, reply_markup=manu_keyboard_admins)
    data_global_news = await state.get_data()
    await check_error_file(message)
    await state.finish()

async def check_error_file(message: types.Message):
    global editors_control, msg_state
    try:
        user_id = message.from_user.id
        msg_state_id = msg_state.message_id
        await bot.delete_message(user_id, msg_state_id)
    except:
        pass
    editors_control = "news"
    news_list_name = str(data_global_news.get("news_list_name"))
    news_list_img = str(data_global_news.get("news_list_img"))
    news_list_description = str(data_global_news.get("news_list_description"))
    news_list_sub = str(data_global_news.get("news_list_sub"))
    msg_state = await bot.send_photo(message.from_user.id, news_list_img, f'{news_list_name}\n{news_list_description}\n{news_list_sub}',\
        reply_markup=InlineKeyboardMarkup(resize_keyboard=True)\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_name}", callback_data=f"name {news_list_name}"))\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_description}", callback_data=f"description {news_list_description}"))\
            .add(InlineKeyboardButton(f"{text.edit_mailing_list_sub}", callback_data=f"sub {news_list_sub}"))\
            .add(InlineKeyboardButton(f"{text.delete_mailing_list}", callback_data=f"delete_mailing_list_"))\
            .insert(InlineKeyboardButton(f"{text.send_mailing_list}", callback_data="send_mailing_list_news_")))

#UPDATE STATE NAME
class update_user_name(StatesGroup):
    mailing_list_name = State()
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('name '))
async def edit_name(call: types.CallbackQuery):
    global msg_state
    user_id = call.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    msg_state = await call.message.answer(text.edit_mailing_list_name_text)
    await call.answer()
    await update_user_name.mailing_list_name.set()
async def finish_state_name_update(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    await message.delete()
    global data_global_everyone, data_global_news
    async with state.proxy() as edit_data:
        edit_data['mailing_list_name'] = message.text
    state_data = await state.get_data("mailing_list_name")
    new_name = str(state_data.get('mailing_list_name'))
    await state.finish()
    if editors_control == "everyone":
        data_global_news = None
        data_global_everyone.update({"mailing_list_name":f"{new_name}"})
        await check_error(message)
    elif editors_control == "news":
        data_global_everyone = None
        data_global_news.update({"news_list_name":f"{new_name}"})
        await check_error_file(message)
#UPDATE STATE NAME
class update_user_description(StatesGroup):
    mailing_list_description = State()
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('description '))
async def edit_description(call: types.CallbackQuery):
    global msg_state
    user_id = call.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    msg_state = await call.message.answer(text.edit_mailing_list_description_text)
    await call.answer()
    await update_user_description.mailing_list_description.set()
async def finish_state_description_update(message: types.Message, state: FSMContext):
    await message.delete()
    global data_global_everyone, data_global_news
    async with state.proxy() as edit_data:
        edit_data['mailing_list_description'] = message.text
    state_data = await state.get_data("mailing_list_description")
    new_description = str(state_data.get('mailing_list_description'))
    await state.finish()
    if editors_control == "everyone":
        data_global_news = None
        data_global_everyone.update({"mailing_list_description":f"{new_description}"})
        await check_error(message)
    elif editors_control == "news":
        data_global_everyone = None
        data_global_news.update({"news_list_description":f"{new_description}"})
        await check_error_file(message)
#UPDATE STATE NAME
class update_user_sub(StatesGroup):
    mailing_list_sub = State()
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('sub '))
async def edit_sub(call: types.CallbackQuery):
    global msg_state
    user_id = call.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    msg_state = await call.message.answer(text.edit_mailing_list_sub_text)
    await call.answer()
    await update_user_sub.mailing_list_sub.set()
async def finish_state_sub_update(message: types.Message, state: FSMContext):
    await message.delete()
    global data_global_everyone, data_global_news
    async with state.proxy() as edit_data:
        edit_data['mailing_list_sub'] = message.text
    state_data = await state.get_data("mailing_list_sub")
    new_sub = str(state_data.get('mailing_list_sub'))
    await state.finish()
    if editors_control == "everyone":
        data_global_news = None
        data_global_everyone.update({"mailing_list_sub":f"{new_sub}"})
        await check_error(message)
    elif editors_control == "news":
        data_global_everyone = None
        data_global_news.update({"news_list_sub":f"{new_sub}"})
        await check_error_file(message)

@dp.callback_query_handler(text='delete_mailing_list_')
async def delete_error(message: types.Message):

    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)

    global data_global_everyone, data_global_news
    data_global_everyone = None
    data_global_news = None
    msg = await message.answer(text.delete_mailing_list_text)
    date_15 = datetime.now() + timedelta(seconds=30)
    scheduler.add_job(message_delete, "date", run_date=date_15, kwargs={"message":msg}, id="delete_start_message")
    await start_bot(message)

#отправка рассылки
@dp.callback_query_handler(text='send_mailing_list_')
async def news_bot_run(message: types.Message):

    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)

    read = await CONTROL_TABLE.select_user_and_true_status()
    mailing_list_name = str(data_global_everyone.get("mailing_list_name"))
    mailing_list_img = str(data_global_everyone.get("mailing_list_img"))
    mailing_list_description = str(data_global_everyone.get("mailing_list_description"))
    mailing_list_sub = str(data_global_everyone.get("mailing_list_sub"))
    for row in read:
        try:
            await bot.send_photo(row[0], mailing_list_img, f'{mailing_list_name}\n{mailing_list_description}\n{mailing_list_sub}')
        except:
            await CONTROL_TABLE.update_status(row[0], False)

#отправка рассылки
@dp.callback_query_handler(text='send_mailing_list_news_')
async def news_bot_run(message: types.Message):

    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)

    read = await CONTROL_TABLE.select_user_and_true_status_and_sub_to_news_bot()
    news_list_name = str(data_global_news.get("news_list_name"))
    news_list_img = str(data_global_news.get("news_list_img"))
    news_list_description = str(data_global_news.get("news_list_description"))
    news_list_sub = str(data_global_news.get("news_list_sub"))
    for row in read:
        try:
            await bot.send_photo(row[0], news_list_img, f'{news_list_name}\n{news_list_description}\n{news_list_sub}')
        except:
            await CONTROL_TABLE.update_status(row[0], False)

#CANSAL
@dp.callback_query_handler(text='not_sub_news')
async def help_command_inline(message: types.Message):
    user_id = message.from_user.id
    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    message_text = text.text_cansel_text(storyteller)
    msg = await bot.send_message(user_id, text=message_text, reply_markup=sub_news_keyboard)

async def choose_news_sub(message: types.Message):
    global choose_news_sub_message
    await message.delete()
    user_id = message.from_user.id
    subs = ("videogames", "livegames", "bot", "world")
    for row in subs:
        bool_sub = str(row) + " " + str(CONTROL_TABLE.exists_user_sub(row, user_id))
        if bool_sub == "videogames True":
            sub_videogames = True
        if bool_sub == "livegames True":
            sub_livegames = True
        if bool_sub == "bot True":
            sub_bot = True
        if bool_sub == "world True":
            sub_world = True
    subs_list = []
    try:
        if sub_videogames == True:
            game = "Видеоигры"
            subs_list.append(game)
    except:
        sub_videogames = False

    try:
        if sub_livegames == True:
            sport = "Спорт"
            subs_list.append(sport)
    except:
        sub_livegames = False

    try:
        if sub_bot == True:
            bots = "Бот"
            subs_list.append(bots)
    except:
        sub_bot = False

    try:
        if sub_world == True:
            world = "Мир"
            subs_list.append(world)
    except:
        sub_world = False
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if sub_videogames == False and sub_livegames == False and sub_bot == False and sub_world == False:
        if storyteller != "NotFound":
            choose_news_sub_message = await message.answer(text.choose_news_subscription_text, reply_markup=sub_news_keyboard)
        else:
            await message.answer(text=text.message_error_storyteller)
    elif sub_videogames == True and sub_livegames == True and sub_bot == True and sub_world == True:
        level = "2"
        text_news_ = text.choose_news_variant(subs_list, level, storyteller)
        if storyteller != "NotFound":
            choose_news_sub_message = await message.answer(text=text_news_, reply_markup=sub_news_keyboard)
        else:
            await message.answer(text=text.message_error_storyteller)
    else:
        level = "1"
        text_news_ = text.choose_news_variant(subs_list, level, storyteller)
        if storyteller != "NotFound":
            choose_news_sub_message = await bot.send_message(user_id, text=text_news_, reply_markup=sub_news_keyboard)
        else:
            await message.answer(text=text.message_error_storyteller)

async def live_game(message: types.Message):
    global choose_sub_message
    await message.delete()
    user_id = message.from_user.id

    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass

    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    sub = "livegames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.live_game_text, reply_markup=sports_subscription_not)
        else:
            await message.answer(text=text.message_error_storyteller)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.live_game_text, reply_markup=sports_subscription)
        else:
            await message.answer(text=text.message_error_storyteller)

async def video_game(message: types.Message):
    global choose_sub_message
    await message.delete()
    user_id = message.from_user.id

    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass

    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    text_user = text.text_video_game_text(storyteller)
    sub = "videogames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text=text_user, reply_markup=videogame_subscription_not)
        else:
            await message.answer(text=text.message_error_storyteller)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text=text_user, reply_markup=videogame_subscription)
        else:
            await message.answer(text=text.message_error_storyteller)


async def bot_news(message: types.Message):
    global choose_sub_message
    await message.delete()
    user_id = message.from_user.id

    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass

    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    sub = "bot"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.bot_news_text, reply_markup=bot_subscription)
        else:
            await message.answer(text=text.message_error_storyteller)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.bot_news_text, reply_markup=bot_subscription_not)
        else:
            await message.answer(text=text.message_error_storyteller)

async def world_new(message: types.Message):
    global choose_sub_message
    await message.delete()
    user_id = message.from_user.id

    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass

    sub = "world"
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)

    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.world_news_text, reply_markup=world_subscription)
        else:
            await message.answer(text=text.message_error_storyteller)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        if storyteller != "NotFound":
            choose_sub_message = await message.answer(text.world_news_text, reply_markup=world_subscription_not)
        else:
            await message.answer(text=text.message_error_storyteller)

#SUBSCRIPTION
@dp.callback_query_handler(text='sports_sub')
async def help_command_inline(message: types.Message):
    user_id = message.from_user.id
    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    subscribe_text = text.text_subscribe_text(storyteller)
    unsubscribe_text = text.text_unsubscribe_text(storyteller)
    sub = "livegames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await bot.send_message(user_id, text=subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await bot.send_message(user_id, text=unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='videogame_sub')
async def help_command_inline(message: types.Message):
    user_id = message.from_user.id
    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    subscribe_text = text.text_subscribe_text(storyteller)
    unsubscribe_text = text.text_unsubscribe_text(storyteller)
    sub = "videogames"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await bot.send_message(user_id, text=subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await bot.send_message(user_id, text=unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='bot_sub')
async def help_command_inline(message: types.Message):
    user_id = message.from_user.id
    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    subscribe_text = text.text_subscribe_text(storyteller)
    unsubscribe_text = text.text_unsubscribe_text(storyteller)
    sub = "bot"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await bot.send_message(user_id, text=subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await bot.send_message(user_id, text=unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

#SUBSCRIPTION
@dp.callback_query_handler(text='world_sub')
async def help_command_inline(message: types.Message):
    user_id = message.from_user.id
    try:
        choose_sub_message_id = choose_sub_message.message_id
        await bot.delete_message(user_id, choose_sub_message_id)
    except:
        pass
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    subscribe_text = text.text_subscribe_text(storyteller)
    unsubscribe_text = text.text_unsubscribe_text(storyteller)
    sub = "world"
    if CONTROL_TABLE.exists_user_sub(sub, user_id) == False:
        await bot.send_message(user_id, text=subscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, True, user_id)
    elif CONTROL_TABLE.exists_user_sub(sub, user_id) == True:
        await bot.send_message(user_id, text=unsubscribe_text, reply_markup=sub_news_keyboard)
        await CONTROL_TABLE.add_user_sub(sub, False, user_id)

async def other_keyboard(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller != "NotFound":    
        user_id = message.from_user.id
        if ADMIN == user_id:
            msg = await message.answer(text.open_other_keyboard, reply_markup=user_keyboard_admins)
    else:
        await message.answer(text=text.message_error_storyteller)

async def back_main_keyboard(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller != "NotFound":
        user_id = message.from_user.id
        if ADMIN == user_id:
            await message.answer(text.back_open_kbd, reply_markup=manu_keyboard_admins)
    else:
        await message.answer(text=text.message_error_storyteller)

async def not_state(message: types.Message, state: FSMContext):
    await message.delete()
    user_id = message.from_user.id
    msg_state_id = msg_state.message_id
    await bot.delete_message(user_id, msg_state_id)
    storyteller = CONTROL_TABLE.select_storyteller_user(user_id)
    if storyteller != "NotFound":
        if user_id == ADMIN:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await message.answer(text=text.message_delete_state, reply_markup=manu_keyboard_admins)
        else:
            await message.answer('Я не понимаю твои слова. Напиши /start или /help')

    else:
        await message.answer(text=text.message_error_storyteller)

def reg_handler(dp):
    dp.register_message_handler(start_bot, commands="start")
    dp.register_message_handler(choose_news_sub, text=text.choose_news_subscription)
    dp.register_message_handler(edit_bots, text=text.bot_settings)
    dp.register_message_handler(back_for_menu, text=text.keyboard_button_edit_back)
    dp.register_message_handler(edit_storyteller_for_bot, text=text.keyboard_button_edit_storyteller)
    dp.register_message_handler(other_keyboard, text=text.other_admins_button)
    dp.register_message_handler(back_main_keyboard, text=text.back)
    dp.register_message_handler(live_game, text=text.live_game_button)
    dp.register_message_handler(video_game, text=text.video_game_button)
    dp.register_message_handler(bot_news, text=text.bot_news_button)
    dp.register_message_handler(world_new, text=text.world_news_button)
    dp.register_message_handler(not_state, Text(equals=text.kfetsm, ignore_case=True), state='*')
    dp.register_message_handler(message_everyone_add, text=text.create_ads, state=None)
    dp.register_message_handler(name_message_everyone_bot, state=message_everyone.mailing_list_name)
    dp.register_message_handler(description_message_everyone_bot, state=message_everyone.mailing_list_description)
    dp.register_message_handler(photo_message_everyone_bot, content_types=types.ContentTypes.ANY, state=message_everyone.mailing_list_img)
    dp.register_message_handler(dev_message_everyone_bot, state=message_everyone.mailing_list_sub)
    dp.register_message_handler(finish_state_name_update, state=update_user_name.mailing_list_name)
    dp.register_message_handler(finish_state_description_update, state=update_user_description.mailing_list_description)
    dp.register_message_handler(finish_state_sub_update, state=update_user_sub.mailing_list_sub)
    dp.register_message_handler(message_news_add, text=text.create_warning, state=None)
    dp.register_message_handler(name_news_everyone_bot, state=message_news.news_list_name)
    dp.register_message_handler(description_message_news_bot, state=message_news.news_list_description)
    dp.register_message_handler(dev_message_news_bot, state=message_news.news_list_sub)
