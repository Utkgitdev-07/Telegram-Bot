import logging
from aiogram import Bot, Dispatcher, executor, types # aiogram is a library for Telegram Bot API
from dotenv import load_dotenv # python-dotenv is a library for loading environment variables from a .env file
import os

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # get the token from .env file

#configure logging
logging.basicConfig(level=logging.INFO) # logging level INFO  is used to log less important messages

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN) # create a bot object
dp = Dispatcher(bot) #  create a dispatcher object for the bot perform the actions  like sending messages, photos, etc.

@dp.message_handler(commands=['start', 'help'])  # this handler will be called when the user sends /start or /help command
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This will retrun echo
    """
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)