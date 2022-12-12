def text_start_bot_text_user(storyteller):
    if storyteller == "Safi":
        start_bot_text_user = f"Привет! Я {storyteller}, твоя виртуальная помощница"
    elif storyteller == "Gerald":
        start_bot_text_user = f"Привет! Я {storyteller}, твой виртуальный помощник"
    elif storyteller == "NotFound":
        start_bot_text_user = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started") 
    return start_bot_text_user


def text_video_game_text(storyteller):
    if storyteller == "Safi":
        video_game_text = "Новости из компьютерных игр. Я конечно девочка, но играла и в кс, например можно из новостей узнать последние новости по киберспорту"
    elif storyteller == "Gerald":
        video_game_text = "Новости из компьютерных игр"
    elif storyteller == "NotFound":
        video_game_text = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return video_game_text

def text_cansel_text(storyteller):
    if storyteller == "Safi":
        cansel_text = "Я отменила"
    elif storyteller == "Gerald":
        cansel_text = "Я отменил"
    elif storyteller == "NotFound":
        cansel_text = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return cansel_text

def text_subscribe_text(storyteller):
    if storyteller == "Safi":
        subscribel_text = "Я оформила подписку"
    elif storyteller == "Gerald":
        subscribel_text = "Я тебя подписал)"
    elif storyteller == "NotFound":
        subscribel_text = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return subscribel_text

def text_unsubscribe_text(storyteller):
    if storyteller == "Safi":
        unsubscribe_text = "Я отписалась"
    elif storyteller == "Gerald":
        unsubscribe_text = "Готово."
    elif storyteller == "NotFound":
        unsubscribe_text = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return unsubscribe_text


def text_edit_bot_text(storyteller):
    if storyteller == "Safi":
        edit_message_bot_text = "Это настройки бота! Тут можешь поставить колегу Gerald'а или изменить еще что нибудь"
    elif storyteller == "Gerald":
        edit_message_bot_text = "Это настройки данного бота. Здесь ты можешь выбрать к примеру Safi"
    elif storyteller == "NotFound":
        edit_message_bot_text = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return edit_message_bot_text

select_message_personality = "Выбери разкасчика"

start_bot_text_admin = "Господин! Я приветствую вас!"

choose_news_subscription = "Выбрать новостную подписку"
choose_news_subscription_text = "Выбери на что ты хочешь подписаться)"

def choose_news_variant(subs_list, level, storyteller):
    if storyteller == "Safi":
        if level == "1":
            text_in_news = f"Вы уже подписаны на {', '.join(subs_list)}, что добовляем? <3"
        elif level == "2":
            text_in_news = f"Вы уже подписаны на всё, вибери что хочешь убрать("
    elif storyteller == "Gerald":
        if level == "1":
            text_in_news = f"Вы уже подписаны на {', '.join(subs_list)}, что добовляем?"
        elif level == "2":
            text_in_news = f"Вы уже подписаны на всё, вибери что хочешь убрать"
    elif storyteller == "NotFound":
        text_in_news = f"ERROR: Stolyteller = {storyteller}"
    else:
        print("ERROR: Stolyteller not started")
    return text_in_news


live_game_button = "Спорт"
video_game_button = "Видеоигры"
bot_news_button = "Бот"
world_news_button = "Мировые"


live_game_text = "Новости спорта. К примеру футбол, волейбол и так далее"

bot_news_text = "Новости про бота, какие обновления вышли и так далее"
world_news_text = "Мировые новости. Что вообще происходит за границей монитора?"

bot_settings = "Настройки бота"
contact_the_author = "Связаться с автором"

unsubscribe = "Отписаться"
subscribe = "Подписаться"
cancel = "Отмена"

back = "Назад"

create_ads = "Сделать рассылку"
create_warning = "Обьявить новость"
create_update = "Обьявить об обновлении"
other_admins_button = "Другая клавиатура"

open_other_keyboard = "Другая клавиатура открыта!"
back_open_kbd = "Вы вернулись назад"

#keyboard for exiting the state machine 
kfetsm = "Отменить!"

edit_mailing_list_name = "Изменить имя"
edit_mailing_list_description = "Изменить описание"
edit_mailing_list_sub = "Изменить подпись"
delete_mailing_list = "Удалить"
send_mailing_list = "Отправить"

delete_mailing_list_text = "Запись была удалена"
edit_mailing_list_name_text = "Напиши новое название"
edit_mailing_list_description_text = "Напиши новое описание"
edit_mailing_list_sub_text = "Напиши новую подпись"

error_message = "Я не понимаю твои слова. Напиши /start или /help"

#message_everyone_text_state
message_everyone_text_state_add = "💻Напиши название рассылки"
message_everyone_text_state_name = "📓Напиши текст рассылки"
message_everyone_text_state_photo = "📝Приложи фото"
message_everyone_text_state_sub = "💜Укажите подпись создателя"
message_everyone_text_state_send = "☑️рассылка отправлена"

message_delete_state = "Действие было отменено!"

#message_news_text_state
message_news_text_state_add = "💻Напиши название новости"
message_news_text_state_name = "📓Напиши текст новости"
message_news_text_state_sub = "💜Укажите подпись создателя"
message_news_text_state_send = "☑️рассылка отправлена"

message_error_storyteller = "Сначало нужно выбрать разкасчика!"

keyboard_button_edit_storyteller = "Изменить разкасчика"
keyboard_button_edit_cell1 = "Ячейка №2"
keyboard_button_edit_cell2 = "Ячейка №3"
keyboard_button_edit_back = "Вернуться"

message_back_from_user_menu = "Вы вернулись в главное меню!"