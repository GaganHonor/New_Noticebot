import aiogram
import asyncio

bot = aiogram.Bot(token="6253669210:AAGiUM6kodf9CPuIEXnCpkJ6geJRuwpRQhw")
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_command(message: aiogram.types.Message):
    """Send a text message on `/start`."""

    first_name = message.from_user.first_name
    await message.reply(
        f"Sorry, {first_name} for the inconvenience! Global maintenance is in progress... 🪲\nTry again later..\n~ Team AOC (DEVS)"
    )


if __name__ == "__main__":
    asyncio.run(dp.start_polling())
