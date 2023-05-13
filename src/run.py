
from loguru import logger
from src.constants import keybords
from src.filters import IsAdmin
from src.bot import bot
import emoji


class Bot:
    def __init__(self, telebot):
        self.bot = telebot

        # add mustom filters
        self.bot.add_custom_filter(IsAdmin())

        # register handlers
        self.handlers()

        # run bot
        logger.info("Bot is runing..")
        self.bot.infinity_polling()

    def handlers(self):
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, "you are admin of this group")

        @self.bot.message_handler(func=lambda _: True)
        def echo(message):
            self.send_message(
                message.chat.id,
                message.text,
                reply_markup=keybords.main)

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        if emojize:
            text = emoji.emojize(text, use_aliases=True)
        self.bot.send_message(chat_id, text, reply_markup=reply_markup)


if __name__ == "__main__":
    logger.info("Bot Started...")
    nashenas_bot = Bot(telebot=bot)
    nashenas_bot.run()

