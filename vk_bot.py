from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import os
import random
from dotenv import load_dotenv

from GetDFAnswer import get_answer


def answer(event, vk_api, project_id):
    DF_asnwer = get_answer(
        event.text,
        project_id,
        event.user_id
    )

    if not DF_asnwer.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=DF_asnwer.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()

    project_id = os.getenv("PROJECT_ID")

    vk_session = vk_api.VkApi(token=os.environ["VK_GROUP_TOKEN"])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer(
                event,
                vk_api,
                project_id
            )
