from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM")  # https://t.me/Innocrs_bot
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == "__main__":
    print("Бот запущен!")
    executor.start_polling(dp)