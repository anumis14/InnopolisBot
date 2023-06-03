import logging
import random
import re

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_menu = InlineKeyboardMarkup(resize_keyboard=True)
button_start = InlineKeyboardButton("Начать", callback_data="startgame")
button_cancel = InlineKeyboardButton("Отмена", callback_data="cancel")
start_menu.add(button_start, button_cancel)

secret_number = None
attempts = None


def random_num():
    secret_number = random.randint(1, 10)
    return secret_number

@dp.message_handler(commands=["start"])
async def start_command(message:types.Message):
    await message.answer("Привет! Для старта игры нажми начать", reply_markup=start_menu)

@dp.callback_query_handler(text="cancel")
async def end_game_command(call : CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text="startgame")
async def start_game_command(call : CallbackQuery):
    global secret_number, attempts
    attempts = 3
    secret_number = random_num()
    await call.message.answer("Я загадаю число от 1 до 10\nПопробуй угадать его")
    await bot.answer_callback_query(call.id)
    await call.message.delete()
    print(secret_number)

@dp.message_handler(regexp=re.compile(r'^\d+$'))
async def check_numbers(message : types.Message):
    global secret_number, attempts
    user_number = int(message.text)
    if attempts <= 0:
        await message.reply("У вас закончились попытки. Хотите испытать удачу заново?", reply_markup=start_menu)
    elif user_number > secret_number:
        attempts -= 1
        await message.reply(f"Секретное число меньше.\nКоличество попыток: {attempts}")
    elif user_number < secret_number:
        attempts -= 1
        await message.reply(f"Секретное число больше.\nКоличество попыток: {attempts}")
    else:
        await message.reply("Вы угадали число. Хотите начать заново?", reply_markup=start_menu)
        secret_number = None

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)