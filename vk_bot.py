from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import os
import random
from dotenv import load_dotenv
from google.cloud import dialogflow

load_dotenv()


def answer(event, vk_api):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(os.getenv("PROJECT_ID"), os.getenv("SESSION_ID"))
    print(f"Session path: {session}\n")

    text_input = dialogflow.TextInput(text=event.text, language_code="ru-RU")

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input
        }
    )

    print("=" * 20)
    print(f"Query text: {response.query_result.query_text}")
    print(
        "Detected intent: {} (confidence: {})\n".format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence,
        )
    )
    print(f"Fulfillment text: {response.query_result.fulfillment_text}\n")

    vk_api.messages.send(
        user_id=event.user_id,
        message=response.query_result.fulfillment_text,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    vk_session = vk_api.VkApi(token=os.environ["VK_GROUP_TOKEN"])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer(event, vk_api)
