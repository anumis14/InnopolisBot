import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = "5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM"

WEBHOOK_HOST = "https://7678-178-176-167-185.ngrok-free.app"
WEBHOOK_PATH = ""
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = "http://127.0.0.1:4040"
WEBAPP_PORT = 3001


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
   await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
   logging.warning('Shutting down..')
   await bot.delete_webhook()
   logging.warning('Bye!')

##############################################
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   return SendMessage(message.chat.id, 'Вы обратились к справке бота')


if __name__ == '__main__':
   start_webhook(
       dispatcher=dp,
       webhook_path=WEBHOOK_PATH,
       on_startup=on_startup,
       on_shutdown=on_shutdown,
       skip_updates=True,
       host=WEBAPP_HOST,
       port=WEBAPP_PORT,
   )
