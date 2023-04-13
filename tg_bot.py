import logging
import os
from dotenv import load_dotenv

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from QuestionsAnswerBot import answer_message


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


def answer(update: Update, context: CallbackContext) -> None:
    message_text = answer_message(
        update.message.text,
        os.getenv("PROJECT_ID"),
        os.getenv("SESSION_ID")
    )

    update.message.reply_text(message_text)


def main() -> None:
    load_dotenv()

    updater = Updater(os.getenv("TG_BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, answer))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
