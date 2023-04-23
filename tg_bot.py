import logging
import os
from dotenv import load_dotenv

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from GetDFAnswer import get_answer


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def answer(update: Update, context: CallbackContext) -> None:
    DF_answer = get_answer(
        update.message.text,
        context.bot_data["project_id"],
        update.message.chat_id
    )

    update.message.reply_text(DF_answer.fulfillment_text)


def main() -> None:
    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    project_id = os.getenv("PROJECT_ID")

    updater = Updater(os.getenv("TG_BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.bot_data["project_id"] = project_id

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, answer))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
