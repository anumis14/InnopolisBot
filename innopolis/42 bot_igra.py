import random
from random import randint
import re
import logging
import os
from keyboards import *
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
import random
import re
from config import BOT_TOKEN
from aiogram.types import BotCommandScopeDefault, BotCommand, BotCommandScopeChat, InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher import filters
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup



start_menu = InlineKeyboardMarkup(resize_keyboard=True)
button_start = InlineKeyboardButton('Начать', callback_data='startgame')
button_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
start_menu.add(button_start, button_cancel)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


def random_num():
    secret_number = random.randint(1, 10)
    return secret_number


@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer('Привет! Это игра угадай число!\nДля старта игры нажми на кнопку начать')

start_menu = InlineKeyboardMarkup(resize_keyboard=True)
button_start = InlineKeyboardButton('Начать', callback_data='startgame')
button_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
start_menu.add(button_start, button_cancel)




@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer('Привет! Это игра угадай число!\nДля старта игры нажми на кнопку начать', reply_markup=start_menu)

secret_number = None
attempts = None


@dp.callback_query_handler(Text(equals='cancel'))
async def end_game_command(call: types.CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(Text(equals='startgame'))
async def start_game_command(call:types.CallbackQuery):
    global secret_number, attempts
    attempts = 3
    secret_number = random_num()
    await call.message.answer('Я загадал число от 1 до 10\nПопробуй угадай его')
    await bot.answer_callback_query(call.id)
    await call.message.delete()
    print(secret_number)


dp.message_handler(regexp=re.compile(r'^\d+$'))
async def check_numbers(message:types.Message):
    global secret_number
    user_number = int(message.text)
    if user_number > secret_number:
        await message.reply(f'Секретное число меньше.\nКоличество попыток: {attempts}')
    elif user_number < secret_number:
        await message.reply(f'Секретное число больше.\nКоличество попыток: {attempts}')
    else:
        await message.reply('Вы угадали!\nНачать заново?', reply_markup=start_menu)
        secret_number = None

dp.message_handler(regexp=re.compile(r'^\d+$'))
async def check_numbers(message:types.Message):
   global secret_number, attempts
   user_number = int(message.text)
   # print(user_number)
   attempts -= 1
   if secret_number != None:
       if user_number > secret_number:
           await message.reply(f'Секретное число меньше.\nКоличество попыток: {attempts}')
       elif user_number < secret_number:
           await message.reply(f'Секретное число больше.\nКоличество попыток: {attempts}')
       else:
           await message.reply('Вы угадали!\nНачать заново?',reply_markup=start_menu)
           secret_number = None
           attempts = None


@dp.message_handler(regexp=re.compile(r'^\d+$'))
async def check_numbers(message:types.Message):
    global secret_number, attempts
    user_number = int(message.text)
    # print(user_number)
    attempts -= 1
    if secret_number != None:

        if user_number > secret_number:
            await message.reply(f'Секретное число меньше.\nКоличество попыток: {attempts}')
        elif user_number < secret_number:
            await message.reply(f'Секретное число больше.\nКоличество попыток: {attempts}')
        else:
            await message.reply('Вы угадали!\nНачать заново?', reply_markup=start_menu)
            secret_number = None
            attempts = None

    else:
        await message.reply('Для начала игры введите /start')
    if attempts < 1:
        await message.reply('Вы проиграли', reply_markup=start_menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
