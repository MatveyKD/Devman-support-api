# Devman-support-api
Бот техподдержки с dialogflow

## Как установить

Python3 должен быть установлен. Далее загрузите ряд зависимостей с помощью pip (pip3):

    pip install -r requirements.txt

Далее создайте бота в тг. Сделать это можно у [BotFather](https://t.me/BotFather).

Создайте проект в [GoogleCloud](https://console.cloud.google.com/).
Создайте агента в [DialogFlow](https://dialogflow.cloud.google.com/) и привяжите его к GoogleCloud проекту.

Создайте сообщество в вк. Разрешите писать сообщение ботам. Дальше нажмите "Разрешить сообщения" на вкладке сообщества. Напишите сообщение в сообщество.

Рядом с программой создайте файл .env. Его содержимое должно быть похожим на это:

    TG_BOT_TOKEN=60864792:AAGvyNeBsE76vbf7svbVBwsdvf8sv
    PROJECT_ID=test-rjv7
    SESSION_ID=87645643
    VK_GROUP_TOKEN=vk1.a.gLGusdbvuVYDBNIds5v67usdsBZNICMsdcv


TG_BOT_TOKEN - токен бота тг, полученный у [BotFather](https://t.me/BotFather).

PROJECT_ID - id GoogleCloud проекта.

SESSION_ID - ваш id в тг. Получить можно у [бота](https://t.me/getmyid_bot)

VK_GROUP_TOKEN - токен бота вк.

## Пример успешного запуска

![screen](https://github.com/MatveyKD/Devman-support-api/blob/main/Images/WorkingExample.gif)
