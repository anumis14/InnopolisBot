
import logging
import os

from config import BOT_TOKEN
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def user_start(message: types.Message):
   await message.reply('Hello')
   await set_starting_commands(message.bot, message.from_user.id)

@dp.message_handler(commands='help')
async def user_start(message: types.Message):
   await message.reply('В скором времени я как-то смогу вам помочь!')

@dp.message_handler(commands='get_commands')
async def user_start(message: types.Message):
   await message.reply(f'На данный момент доступны три команды:\n/help. /reset_commands, /get_commands')


@dp.message_handler(commands='reset_commands')
async def user_start(message: types.Message):
   await message.reply('В данное время команда недоступна')


async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS= {
        'ru': [
            types.BotCommand('start', 'Начать заново'),
            types.BotCommand('get_commands', 'Получить список команд'),
            types.BotCommand('reset_commands', 'Сбросить команды')
        ],
        'en': [
            types.BotCommand('start', 'Restart bot'),
            types.BotCommand('get_commands', 'Retrieve command list'),
            types.BotCommand('reset_commands', 'Reset commands')
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=types.BotCommandScopeChat(chat_id),
            language_code=language_code

        )


# # Пересылка гифки в ответ
# @dp.message_handler(content_types=[types.ContentType.ANIMATION])
# async def echo_document(message:types.Message):
#     await message.reply_animation(message.animation.file_id)
#
# @dp.message_handler(content_types=['photo'])
# async def echo_photo(message:types.Message):
#     await message.reply_photo(message.photo[-1].file_id)
#

@dp.message_handler()
async def echo(message : types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)