import logging
import os
from dotenv import load_dotenv
from google.cloud import dialogflow

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def answer(update: Update, context: CallbackContext) -> None:
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(os.getenv("PROJECT_ID"), os.getenv("SESSION_ID"))
    print(f"Session path: {session}\n")

    for text in [update.message.text]:
        text_input = dialogflow.TextInput(text=text, language_code="ru-RU")

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
        update.message.reply_text(response.query_result.fulfillment_text)


def main() -> None:
    updater = Updater(os.getenv("TG_BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, answer))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
