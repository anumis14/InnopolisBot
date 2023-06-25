BOT_TOKEN = "5750208451:AAF_2d9cBb-UlnG0zzyjEz2a32nMSSFxayI"
ADNINS = ["719450837"]

# import asyncio  # импортирование модуля asyncio, который позволяет использовать асинхронный код
# import json  # импортирование модуля json, который позволяет работать с JSON-данными
import logging  # импортирование модуля logging, который позволяет вести логирование

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


from aiogram import Bot, Dispatcher, executor, types  # импортирование основных классов из aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # импортирование класса хранилища состояний
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton  # импортирование классов кнопок

