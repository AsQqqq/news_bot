from start_bot.import_bot import (
    dp,
    bot,
    ADMIN,
    CONTROL_TABLE,
    scheduler,
    SAFI_REJOICES
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
    user_keyboard_admins,
    keyboard_for_exiting_the_state_machine
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

async def start_bot(message: types.Message):
    user_id = message.from_user.id
    if not CONTROL_TABLE.user_exists(user_id):
        CONTROL_TABLE.add_user(user_id)
    else:
        if CONTROL_TABLE.select_status(user_id) == False:
            await CONTROL_TABLE.update_status(user_id, True)
        else:
            pass
    if ADMIN != user_id:
        await bot.send_sticker(message.from_user.id, SAFI_REJOICES)
        await message.answer(text.start_bot_text_user, reply_markup=manu_keyboard)
    elif ADMIN == user_id:
        await bot.send_sticker(message.from_user.id, SAFI_REJOICES)
        await message.answer(text.start_bot_text_admin, reply_markup=manu_keyboard_admins)

#everyone, news
editors_control = "everyone"

#машина состояний
class message_everyone(StatesGroup):
    mailing_list_name = State()
    mailing_list_description = State()
    mailing_list_img = State()
    mailing_list_sub = State()
async def message_everyone_add(message: types.Message):
  if message.from_user.id == ADMIN:
    await message.reply(text=text.message_everyone_text_state_add, reply_markup=keyboard_for_exiting_the_state_machine)
    await message_everyone.mailing_list_name.set()
  else:
    await message.answer(text=text.error_message)
#ловим название
async def name_message_everyone_bot(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['mailing_list_name'] = message.text
  await message_everyone.next()
  await message.answer(text=text.message_everyone_text_state_name)
#ловим описание
async def description_message_everyone_bot(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['mailing_list_description'] = message.text
  await message_everyone.next()
  await message.answer(text=text.message_everyone_text_state_photo)

async def photo_message_everyone_bot(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['mailing_list_img'] = message.photo[0].file_id
	await message.answer(text=text.message_everyone_text_state_sub)
	await message_everyone.next()

#ловим подпись
async def dev_message_everyone_bot(message: types.Message, state: FSMContext):
    global data_global_everyone
    async with state.proxy() as data:
        data['mailing_list_sub'] = message.text
    await message.answer(text=text.message_everyone_text_state_send, reply_markup=manu_keyboard_admins)
    data_global_everyone = await state.get_data()
    await check_error(message)
    await state.finish()

async def check_error(message: types.Message):
    global editors_control
    editors_control = "everyone"
    mailing_list_name = str(data_global_everyone.get("mailing_list_name"))
    mailing_list_img = data_global_everyone.get("mailing_list_img")
    mailing_list_description = str(data_global_everyone.get("mailing_list_description"))
    mailing_list_sub = str(data_global_everyone.get("mailing_list_sub"))
    await bot.send_photo(message.from_user.id, mailing_list_img, f'{mailing_list_name}\n{mailing_list_description}\n{mailing_list_sub}',\
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
  if message.from_user.id == ADMIN:
    await message.reply(text=text.message_news_text_state_add, reply_markup=keyboard_for_exiting_the_state_machine)
    await message_news.news_list_name.set()
  else:
    await message.answer(text=text.error_message)
#ловим название
async def name_news_everyone_bot(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['news_list_name'] = message.text
  await message_news.next()
  await message.answer(text=text.message_news_text_state_name)
#ловим описание
async def description_message_news_bot(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['news_list_description'] = message.text
  await message_news.next()
  await message.answer(text=text.message_news_text_state_sub)
#ловим подпись
async def dev_message_news_bot(message: types.Message, state: FSMContext):
    global data_global_news
    async with state.proxy() as data:
        data['news_list_sub'] = message.text
        data['news_list_img'] = "https://www.ampersand.net/wp-content/uploads/2018/06/quotationew.jpg"
    await message.answer(text=text.message_news_text_state_send, reply_markup=manu_keyboard_admins)
    data_global_news = await state.get_data()
    await check_error_file(message)
    await state.finish()


async def check_error_file(message: types.Message):
    global editors_control
    editors_control = "news"
    news_list_name = str(data_global_news.get("news_list_name"))
    news_list_img = str(data_global_news.get("news_list_img"))
    news_list_description = str(data_global_news.get("news_list_description"))
    news_list_sub = str(data_global_news.get("news_list_sub"))
    await bot.send_photo(message.from_user.id, news_list_img, f'{news_list_name}\n{news_list_description}\n{news_list_sub}',\
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
    await call.message.answer(text.edit_mailing_list_name_text)
    await call.answer()
    await update_user_name.mailing_list_name.set()
async def finish_state_name_update(message: types.Message, state: FSMContext):
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
    await call.message.answer(text.edit_mailing_list_description_text)
    await call.answer()
    await update_user_description.mailing_list_description.set()
async def finish_state_description_update(message: types.Message, state: FSMContext):
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
    await call.message.answer(text.edit_mailing_list_sub_text)
    await call.answer()
    await update_user_sub.mailing_list_sub.set()
async def finish_state_sub_update(message: types.Message, state: FSMContext):
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
async def delete_error(call: types.CallbackQuery):
    global data_global_everyone, data_global_news
    data_global_everyone = None
    data_global_news = None
    await call.message.answer(text.delete_mailing_list_text)

#отправка рассылки
@dp.callback_query_handler(text='send_mailing_list_')
async def news_bot_run(message: types.Message):
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

    dp.register_message_handler(message_everyone_add, text='Сделать рассылку', state=None)
    dp.register_message_handler(name_message_everyone_bot, state=message_everyone.mailing_list_name)
    dp.register_message_handler(description_message_everyone_bot, state=message_everyone.mailing_list_description)
    dp.register_message_handler(photo_message_everyone_bot, content_types=['photo'], state=message_everyone.mailing_list_img)
    dp.register_message_handler(dev_message_everyone_bot, state=message_everyone.mailing_list_sub)

    dp.register_message_handler(finish_state_name_update, state=update_user_name.mailing_list_name)
    dp.register_message_handler(finish_state_description_update, state=update_user_description.mailing_list_description)
    dp.register_message_handler(finish_state_sub_update, state=update_user_sub.mailing_list_sub)


    dp.register_message_handler(message_news_add, text='Обьявить новость', state=None)
    dp.register_message_handler(name_news_everyone_bot, state=message_news.news_list_name)
    dp.register_message_handler(description_message_news_bot, state=message_news.news_list_description)
    dp.register_message_handler(dev_message_news_bot, state=message_news.news_list_sub)
