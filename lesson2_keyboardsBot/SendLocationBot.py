import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить свою локацию', request_location=True))

@dp.message_handler(commands=['start'])
async def process_hi6_command(message: types.Message):
    await message.reply("Отправьте геолокацию", reply_markup=markup_request)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
