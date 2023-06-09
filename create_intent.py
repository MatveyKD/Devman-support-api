from google.cloud import dialogflow
from dotenv import load_dotenv
import json
import os


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
    load_dotenv()

    data = {}
    with open(os.getenv("QUESTIONS_FILE_PATH", "questions.json"), "UTF-8") as file:
        data = json.load(file)

    for question_text, question_data in data.items():
        create_intent(
            project_id=os.getenv("PROJECT_ID"),
            display_name=question_text,
            training_phrases_parts=question_data["questions"],
            message_texts=question_data["answer"]
        )
