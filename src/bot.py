import telebot
import os
from loguru import logger
from src.utils.io import write_json
from src.constants import keybords
import emoji


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(
            func=lambda message: True
            )(self.echo_all)

    def run(self):
        logger.info("Bot is runing..")
        self.bot.infinity_polling()

    def echo_all(self, message):
        write_json(message.json, "message.json")
        print(emoji.demojize(message.text))
        self.bot.send_message(
            message.chat.id,
            message.text,
            reply_markup=keybords.main,
            )


if __name__ == "__main__":
    logger.info("Bot Started...")
    bot = Bot()
    bot.run()
