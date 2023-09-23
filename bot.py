import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types

BOT_TOKENS = [
    "6337536275:AAFZ2PAb0lni9xZlHPIiloWpqarFZ8L4bjY",
    "6253669210:AAGiUM6kodf9CPuIEXnCpkJ6geJRuwpRQhw",
]

MESSAGE = "Sorry, {first_name} for the inconvenience! Global maintenance is in progress... 🪲\nTry again later..\n~ Team AOC (DEVS)"

logging.basicConfig(level=logging.INFO)

async def send_message(bot: Bot, user_id: int, message: str):
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except types.BotBlocked:
        logging.info(f"User {user_id} has blocked the bot")
    except Exception as e:
        logging.error(e)

async def main():
    for token in BOT_TOKENS:
        bot = Bot(token=token)
        dp = Dispatcher(bot)

        @dp.message_handler()
        async def message_handler(message: types.Message):
            await send_message(bot, message.chat.id, MESSAGE)

        dp.register_message_handler(message_handler)
        await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
