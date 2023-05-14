import logging
import os

from aiogram import Bot, types, executor, Dispatcher

TOKEN = os.environ.get('TOKEN')
API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message : types.Message):
    await message.reply("Привет, вы ввели одну из команд!")


@dp.message_handler()
async def echo(message : types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)