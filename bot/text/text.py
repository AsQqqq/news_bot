name_assistant = "Safi"
assistant_gender = "ж"

if assistant_gender == "ж":
    start_bot_text_user = f"Привет! Я {name_assistant}, твоя виртуальная помощница"
else:
    start_bot_text_user = f"Привет! Я {name_assistant}, твой виртуальный помощник"
start_bot_text_admin = "Господин! Я приветствую вас!"

#BUTTON
choose_news_subscription = "Выбрать новостную подписку"
choose_news_subscription_text = "Выбери на что ты хочешь подписаться)"

live_game_button = "Спорт"
video_game_button = "Видеоигры"
bot_news_button = "Бот"
world_news_button = "Мировые"

live_game_text = "Новости спорта. К примеру футбол, волейбол и так далее"
if assistant_gender == "ж":
    video_game_text = "Новости из компьютерных игр. Я конечно девочка, но играла и в кс, например можно из новостей узнать последние новости по киберспорту"
else:
    video_game_text = "Новости из компьютерных игр"
bot_news_text = "Новости про бота, какие обновления вышли и так далее"
world_news_text = "Мировые новости. Что вообще происходит за границей монитора?"

bot_settings = "Настройки бота"
contact_the_author = "Связаться с автором"

if assistant_gender == "ж":
    cansel_text = "Я отменила"
else:
    cansel_text = "Я отменил"

if assistant_gender == "ж":
    subscribe_text = "Я оформила подписку"
else:
    subscribel_text = "Я тебя подписал)"

if assistant_gender == "ж":
    unsubscribe_text = "Я отписалась"
else:
    unsubscribe_text = "Готово."

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