from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters

TOKEN = '5454897047:AAFhOIOAOj2yCTjmluB_Jnb-ZSeOMmry6eM'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(filters.Text(contains=['НЛО'], ignore_case=True))
async def egg_cm(message : types.Message):
    await message.answer("Ты нашел пасхалку!")



executor.start_polling(dp, skip_updates=True)