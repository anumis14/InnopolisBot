from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(msg: types.Message):
    await msg.reply("Привет, я бот!")


@dp.message_handler(commands="help")
async def cmd_start(msg: types.Message):
    await msg.reply("Привет, это бот. Для запуска напишите /start")


@dp.message_handler()
async def echo_message(msg : types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
