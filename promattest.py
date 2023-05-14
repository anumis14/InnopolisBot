
import logging
import os

from config import BOT_TOKEN
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def user_start(message: types.Message):
   await message.reply('Привет, я бот, в скором времени функционал будет пополняться. Напиши команду /about, чтобы узнать обо мне больше информации')


@dp.message_handler(commands='about')
async def user_start(message: types.Message):
   await message.reply('На данный момент я лишь могу рассказать информации о себе и всё. В скором времени здесь будет больше классных функций!')

@dp.message_handler()
async def echo(message : types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)