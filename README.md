# Devman-support-api
Бот техподдержки с dialogflow


Рабочий пример тг: [бот](https://t.me/DevSupTHBot)

Рабочий пример вк: [сообщество](https://vk.com/public219788185)


## Как установить

Python3 должен быть установлен. Далее загрузите ряд зависимостей с помощью pip (pip3):

    pip install -r requirements.txt

Далее создайте бота в тг. Сделать это можно у [BotFather](https://t.me/BotFather).

Создайте проект в [GoogleCloud](https://console.cloud.google.com/).
Создайте агента в [DialogFlow](https://dialogflow.cloud.google.com/) и привяжите его к GoogleCloud проекту.

Создайте сообщество в вк. Разрешите писать сообщение ботам. Дальше нажмите "Разрешить сообщения" на вкладке сообщества. Напишите сообщение в сообщество.

Рядом с программой создайте файл .env. Его содержимое должно быть похожим на это:

    TG_BOT_TOKEN=60864792:AAGvyNeBsE76vbf7svbVBwsdvf8sv
    QUESTIONS_FILE_PATH=questions.json
    PROJECT_ID=test-rjv7
    VK_GROUP_TOKEN=vk1.a.gLGusdbvuVYDBNIds5v67usdsBZNICMsdcv


TG_BOT_TOKEN - токен бота тг, полученный у [BotFather](https://t.me/BotFather).

QUESTIONS_FILE_PATH - путь до файла с тестовыми вопросами. По умолчанию - questions.json (файл из репозитория)

PROJECT_ID - id GoogleCloud проекта.

VK_GROUP_TOKEN - токен бота вк.


Запустите файл командой `python3 create_intent.py`. Он загрузит в dialogflow тестовые данные.
Запустите файл тг бота командой `python3 tg_bot.py`
Запустите файл вк бота командой `python3 vk_bot.py`


## Пример успешного запуска

![screen](https://github.com/MatveyKD/Devman-support-api/blob/main/Images/WorkingExample.gif)
![screenvk](https://github.com/MatveyKD/Devman-support-api/blob/main/Images/WorkingExampleVK.gif)
