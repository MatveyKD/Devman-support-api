from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import os
import random
from dotenv import load_dotenv

from QuestionsAnswerBot import answer_message


def answer(event, vk_api):
    message_text = answer_message(
        event.text,
        os.getenv("PROJECT_ID"),
        os.getenv("SESSION_ID")
    )

    vk_api.messages.send(
        user_id=event.user_id,
        message=message_text,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    load_dotenv()
    vk_session = vk_api.VkApi(token=os.environ["VK_GROUP_TOKEN"])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer(event, vk_api)
