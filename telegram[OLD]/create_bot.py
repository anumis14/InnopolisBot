from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5454897047:AAFhOIOAOj2yCTjmluB_Jnb-ZSeOMmry6eM'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)