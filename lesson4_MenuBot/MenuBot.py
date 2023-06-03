import logging

import kb

from aiogram.types import CallbackQuery, message

import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message:types.Message):
    await message.answer("Привет! Это меню бота", reply_markup=kb.start_menu)


@dp.callback_query_handler(text="faq")
async def faq_command(call : CallbackQuery):
    await call.message.edit_text("Привет, это бот, помогающий школьникам в учебе")
    await call.message.edit_reply_markup(reply_markup=kb.help_menu)


@dp.callback_query_handler(text="exams")
async def exams_command(call : CallbackQuery):
    await call.message.edit_text("Информация о экзаменах для 9 и 11 класса")
    await call.message.edit_reply_markup(reply_markup=kb.exam_menu)

    @dp.callback_query_handler(text="9thgrade")
    async def ninegrade_command(call : CallbackQuery):
        await call.message.edit_text("9 класс\nОсновной период\n24 мая (среда) - история, физика, биология\n30 мая ("
                                     "вторник) - обществознание, информатика и информационно-коммуникационные "
                                     "  технологии (ИКТ), география, химия")
        await call.message.edit_reply_markup(reply_markup=kb.exam_menu)

    @dp.callback_query_handler(text="11thgrade")
    async def ninegrade_command(call: CallbackQuery):
        await call.message.edit_text("11 класс\nОсновной период\n 26 мая (пятница) - география, литература, химия\n30 "
                                     "мая - Егэ по борьба")
        await call.message.edit_reply_markup(reply_markup=kb.exam_menu)


@dp.callback_query_handler(text="books")
async def faq_command(call : CallbackQuery):
    await call.message.edit_text("23 мая 10 классы учебники сдают сами!\n25 мая 5а, 5б, 6а, 6б\n26 мая 7а, 7б, 8а, "
                                 "8б\n27 мая 9 и 11 классы")
    await call.message.edit_reply_markup(reply_markup=kb.help_menu)


@dp.callback_query_handler(text="menu")
async def end_game_command(call : CallbackQuery):
    await call.message.edit_text("Привет,это меню бота")
    await call.message.edit_reply_markup(reply_markup=kb.start_menu)


@dp.callback_query_handler(text="cancel")
async def end_game_command(call : CallbackQuery):
    await call.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)