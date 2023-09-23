import os
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import ChatAction
import time

BOT_TOKENS = [
    "6253669210:AAGiUM6kodf9CPuIEXnCpkJ6geJRuwpRQhw",
    "6337536275:AAFZ2PAb0lni9xZlHPIiloWpqarFZ8L4bjY",
]


def start_command(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    # Show typing animation
    context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    time.sleep(2)  # Simulate loading time

    context.bot.send_message(
        chat_id=user_id,
        text=f"Sorry, {first_name} for the inconvenience! Global maintenance is in progress... 🪲\nTry again later..\n~ Team AOC (DEVS)",
    )

    # Send the image along with the message
    context.bot.send_chat_action(chat_id=user_id, action=ChatAction.UPLOAD_PHOTO)
    time.sleep(2)  # Simulate loading time
    context.bot.send_photo(
        chat_id=user_id,
        photo=open("/home/admin/notice/New_Noticebot/image.jpeg", "rb"),
    )

    context.user_data["last_command"] = "start"


def main():
    for token in BOT_TOKENS:
        bot = telegram.Bot(token=token)
        updater = Updater(bot.token, use_context=True)
        dispatcher = updater.dispatcher

        # Add the start command handler to all bots
        dispatcher.add_handler(CommandHandler("start", start_command))

        updater.start_polling()
        updater.idle()


if __name__ == "__main__":
    main()
