# https://t.me/Innocrs_bot
# Я пытался сделать на вебхуке, но так и не смог исправить ошибку 502, ngrok ни в какую не работал


import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM")
dp = Dispatcher(bot)


def create_table():
   conn = sqlite3.connect('users.db')
   cur = conn.cursor()
   cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               username TEXT,
               message TEXT);
               """)
   conn.commit()
   cur.close()
   conn.close()


@dp.message_handler(text='база')
async def echo(message: types.Message):
   conn = sqlite3.connect('users.db')
   cur = conn.cursor()
   user = cur.execute(f"""SELECT * FROM users WHERE userid = {message.chat.id}""").fetchone()
   if not user:
       data = (message.chat.id, message.chat.username)
       cur.execute("""INSERT INTO users(userid, username) VALUES (?,?)""", data)
       conn.commit()
       conn.close()
       await message.answer('Вы добавлены в базу данных')
   else:
       id, username = user[0], user[1]
       await message.answer(f'Вы уже есть в базе данных. Ваш id = {id}, username = {username}')



# @dp.message_handler(commands="start")
# async def cmd_start(msg: types.Message):
#     await msg.reply("Привет, я бот!")
#
#
# @dp.message_handler(commands="help")
# async def cmd_start(msg: types.Message):
#     await msg.reply("Привет, это бот. Для запуска напишите /start")
#
#
# @dp.message_handler()
# async def echo_message(msg : types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#

if __name__ == '__main__':
   create_table()
   executor.start_polling(dp, skip_updates=True)