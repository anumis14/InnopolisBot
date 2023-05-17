import logging
import config

from aiogram.types import Message, CallbackQuery
from choice_buttons import choice
from aiogram import Bot, Dispatcher, executor


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['film'])
async def show_film(message: Message):
    await message.answer(text="Всё что я могу предложить:", reply_markup=choice)

@dp.callback_query_handler(text="cancel")
async def cancel_choice(call: CallbackQuery):
    await call.answer("Вы убрали кнопки", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

