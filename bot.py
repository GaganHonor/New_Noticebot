import asyncio
import os
import telegram
from telegram import Update
from telegram.ext import AsyncUpdater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import ChatAction
import time

BOT_TOKENS = [
    "6253669210:AAGiUM6kodf9CPuIEXnCpkJ6geJRuwpRQhw",
    "6337536275:AAFZ2PAb0lni9xZlHPIiloWpqarFZ8L4bjY",
]


async def start_command(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    # Show typing animation
    await context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(2)  # Simulate loading time

    await context.bot.send_message(
        chat_id=user_id,
        text=f"Sorry, {first_name} for the inconvenience! Global maintenance is in progress... 🪲\nTry again later..\n~ Team AOC (DEVS)",
    )


async def main():
    for token in BOT_TOKENS:
        updater = AsyncUpdater(token=token, use_context=True)
        dispatcher = updater.dispatcher

        # Add the start command handler to all bots
        dispatcher.add_handler(CommandHandler("start", start_command))

        await updater.start_polling()
        await updater.idle()


if __name__ == "__main__":
    asyncio.run(main())
