from google.cloud import dialogflow
from dotenv import load_dotenv
import json
import os


load_dotenv()


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={
            "parent": parent,
            "intent": intent
        }
    )

    print("Intent created: {}".format(response))


if __name__ == "__main__":
    data = {}
    with open("questions.json", "r", encoding="UTF-8") as read_file:
        data = json.load(read_file)

    for question in data:
        create_intent(
            project_id=os.getenv("PROJECT_ID"),
            display_name=question,
            training_phrases_parts=data[question]["questions"],
            message_texts=[data[question]["answer"]]
        )
