from google.cloud import dialogflow


def answer_message(message_text, project_id, session_id):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print(f"Session path: {session}\n")

    text_input = dialogflow.TextInput(text=message_text, language_code="ru-RU")

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input
        }
    )
    return response.query_result.fulfillment_text
