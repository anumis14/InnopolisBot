"""���� 40.1. ���������� Telegram

���������� ��������� ����� ��� ����������� ��������� - insert.
�� ����� �� ����� add, �� �������� ��������� ������ �� � ������ ����, � ������� ���������, �������� �� �� ����� ��������� ���.
� ���� ���, �� ������� ��������� ������ ����, � ��������� ������ ������ ��� ���������� ���������� ������.
"""

kb5 = ReplyKeyboardMarkup()

kb5.add(
   button1, button2, button3, button4, button5, button6
)
kb5.row(
   button1, button2, button3, button4, button5, button6
)

kb5.row(button4, button2)
kb5.add(button3, button2)
kb5.insert(button1)
kb5.insert(button6)
kb5.insert(KeyboardButton('9'))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
   await message.reply("������!", reply_markup=kb9)


"""����� ������ �������� ����� ������������ ����������, ��������� �������� ����������. 
������� ������������ ������ ����� ������� �, ���� ����� �� ��������� ��� �� �����. 
��� ����, ����� � ������������ � ������� ���������� �������� ������, ����� ��������� ��� ReplyKeboardRemove:
"""

keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



bot.py

from keyboards import kb5, ReplyKeyboardRemove

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
   await message.reply("������� ����������", reply_markup=ReplyKeyboardRemove())


"""
������ �������� � ������ �����������.
��� ����� ������ ����������, ������� ��������� ��� ������ ������ ������ �����.
����� ���������� ������������� � ��� ������, ���������� ��������� ��� ������-�� ��������.
�� ���� ����� ������������ ����� ������ X, ������� Y�.
� ��� Y ����� �������� ������ ��� ������, ��� ��� ��� ��� �� �������������� ���� API.
���������� ��������, ��� ����� ��������� � ������������� �������� callback_data:"""

keyboards.py

from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('������ ������!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


bot.py


@dp.message_handler(commands=['start'])
async def process_rm_command(message: types.Message):
   await message.reply("Inline", reply_markup=inline_kb1)



"""
�������� ������ �.. ������ �� ����������!
������? ���� � ���� ���� �������� �����������, �� �� ����� ��������, ��� �������� ���������� ���� CallbackQuery. 
��� ��� ������ ��� ��� � ����� �����������.

��������� ������ �������:"""

@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
   await bot.answer_callback_query(callback_query.id)
   await bot.send_message(callback_query.from_user.id, '������ ������ ������!')





"""
������� ����� ����� �������� �� ��� ������� - ��� ����� ���� ����� answerCallbackQuery.
� ������������ �������, ��� ����� ��������� ��������, � ���� ��� ����� �����������,
���� ���� �� �� ����������� ���������� ���-����.
����� ������� �������������, ����� ������� ����������� ������ � �������� ��.
��� ���� �� ����� �������� �� ������ ����� ��������� ������, ������������, 
��� ������ ���� ������, ������� ���� �� �� �����, ����� ������������ �������� ��, �� ����� �� �������� ��������. 
������������ �������� - ���� �������, �� ������� �� ��������.

�������� ��� ����������."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('������ ������!', callback_data='button1')
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('������ ������', callback_data='btn2'))

inline_btn_3 = InlineKeyboardButton('������ 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('������ 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('������ 5', callback_data='btn5')

inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)

inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline � ���� �� ����", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('������', url='https://www.yandex.ru'))


@dp.callback_query_handler(Text(startswith=('btn')))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
   code = callback_query.data[-1]
   if code.isdigit():
       code = int(code)
   if code == 2:
       await bot.answer_callback_query(callback_query.id, text='������ ������ ������')
   elif code == 5:
       await bot.answer_callback_query(
           callback_query.id,
           text='������ ������ � ������� 5.\n� ���� ����� ����� ���� ������ �� 200 ��������', show_alert=True)
   else:
       await bot.answer_callback_query(callback_query.id)
   await bot.send_message(callback_query.from_user.id, f'������ ������ ������! code={code}')


@dp.message_handler(commands=['start'])
async def process_command_2(message: types.Message):
   await message.reply("��������� ��� ��������� ������", reply_markup=inline_kb_full)



'''
�������� �� �������� �� �������, ����� �� �������� ��������:
�� ������ ���������� ���� InlineKeyboardMarkup, ���������,
��� ������ ������ ������ ���� �� ������ ���� (�������, ��� ��� �� ���������������� �� ����� row)
� ����� ��������� ���� ��� ������� ������ ����� ��������� ������, 
� ������� ��������� ������ ������ � ��������� callback_data
������ ���������� ��� ����� ������ � ��������� �� ������.
������� ������� add, ����� ����� row.
� ��� ��� ������ ���������� ����� ����, �� � ������ ������ ���������� ������� ������� ������, �� ������ ������ ���
����� ��������� ������, � ������� ��������� ��� �� callback_data, � ������ ���������.

��, ��� �� ������� � switch_inline_query, ����� ������������� ������������ ��� ������� ������: ������������ ��������� ������� ���,
� ��� ��������� ������ ����� ����� ���� 
(� ���� ����� ��������� ��������� �������� ����),

������ ����� ������ ����� ��������� ��, ��� �� �������. 
�������� ����� ��������� ������ ������,
����� ������ ����� ���������� ��� ������-���� �������, �� ���� ����� ������ �����, �� �� � ���������
��� ������������� switch_inline_query_current_chat ��������� ����� �� ��, ��� � � ���������� ������,
�� ��� ������ ����, � ���������� � �������

�� � ��������� �������� url - ��������� ������ �� ������� ������, ���� ������� � ����� ���������

��� ��� �������� ���������� row_width ����� ����, �� ������ ������������� ������������ ��������������.

####
���������� ������� �� ������ �� �������:
��� ������� ������ ����������� ��� ������ ������, ��� ��� �� �����, � ����� ���������� ��������� ������,
�����, ����� � �� callback_data. 

������� ��������� ������ ������ ����� ������� ������ ��� � ����� ������ ����������.
������ �� ������ �� ����� ����� ������ ��������� � callback_data,
������� ������ �������� ���������, ����� ��� � ������� ������ �:
���� 2, �� �������� �� ������ � �������� �������������� ���������. 

�������� text ��� ����� ������ �� ������.
�� ��������� �� ����� ������� ������ ���� � ��� �������� ����� ���� ������.
���� 5, �� �������� ��� ��, �� ��������� show_alert=True, ����� ������� �� �������� �������, ��� ����� �������� ������ � �������
� ���� ������ ������ �������� �� ������

� ������� �� ������� ������, ���������� ��������� �� � ���� ������,
� � ���������,� ������� ���� ����������.
������� �������� �� �������� ����� �������� ��� ��� ��� ���� ������:
URL � Callback.(���������� ��� Login- � Pay-������)

�������� ������ ���� 
'''

import logging

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN


# ������ ����
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# ��������� ��� ����
dp = Dispatcher(bot)
# �������� �����������, ����� �� ���������� ������ ���������
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
   buttons = [
       types.InlineKeyboardButton(text="Yandex", url="https://yandex.ru"),
       types.InlineKeyboardButton(text="��. ����� Telegram", url="tg://resolve?domain=telegram")
   ]
   keyboard = types.InlineKeyboardMarkup(row_width=1)
   keyboard.add(*buttons)
   await message.answer("������-������", reply_markup=keyboard)



if __name__ == "__main__":
   # ������ ����
   executor.start_polling(dp, skip_updates=True)




"""����� ������� ������-������ ��������� � ���� URL, �.�. �������. �������������� ������ ��������� HTTP(S) � tg:
"""

@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
   buttons = [
       types.InlineKeyboardButton(text="Yandex", url="https://yandex.ru"),
       types.InlineKeyboardButton(text="��. ����� Telegram", url="tg://resolve?domain=telegram")
   ]
   keyboard = types.InlineKeyboardMarkup(row_width=1)
   keyboard.add(*buttons)
   await message.answer("������-������", reply_markup=keyboard)


"""

� ������ ������ �� ������� ���������� ����� � ����������� ��� ��������( �� ������� ����� ������,
����� ��� �� ��������� �� ��������� ������)

���� ������ ��� ������ � ���, �� ������� row_width=1 (����� ����� �������������� �������� �� ��������� 3).


�������� ������
������ 1
�������� ���� � ����������� ��� �������� �������.

�������"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'TOKEN�'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)













