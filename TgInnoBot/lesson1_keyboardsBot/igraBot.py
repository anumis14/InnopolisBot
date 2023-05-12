import logging

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from keyboards import kb, kb2, kb3


# Объект бота
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def set_default_commands(dp):
   await dp.bot.set_my_commands(
      [
         types.BotCommand('help', 'Запустить бота'),  # пока добавляем только одну команду
      ]
   )



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
   await message.reply("Привет!", reply_markup=kb2)
   await set_default_commands(dp)

@dp.message_handler(commands=['starts'])
async def process_start_command(message: types.Message):
   await message.reply("Привет!", reply_markup=kb3)




if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)
