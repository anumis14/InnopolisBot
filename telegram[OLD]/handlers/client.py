from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.dispatcher import filters

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс')

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, "Круглосуточно!")

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Город Бузулук. Красноармейская 20')

# @dp.message_handler()
async def empty(message : types.Message):
    await message.answer('Нет такой команды. Напишите /start')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(empty)