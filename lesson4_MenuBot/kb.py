from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

SMILE = ['❓', '📆', '📚']

start_menu = InlineKeyboardMarkup(resize_keyboard=True)
help_menu = InlineKeyboardMarkup(resize_keyboard=True)
exam_menu = InlineKeyboardMarkup(resize_keyboard=True)
books_menu = InlineKeyboardMarkup(resize_keyboard=True)

button_help = InlineKeyboardButton("❓\nВопросы", callback_data="faq")
button_exam = InlineKeyboardButton("Даты экзаменов 📆", callback_data="exams")
button_books = InlineKeyboardButton("Сдача учебников📚", callback_data="books")
button_cancel = InlineKeyboardButton("Отмена", callback_data="cancel")
button_menu = InlineKeyboardButton("Вернуться в меню", callback_data="menu")
button_9grade = InlineKeyboardButton("Информация для 9-классников", callback_data="9thgrade")
button_11grade = InlineKeyboardButton("Информация для 11-классников", callback_data="11thgrade")


start_menu.add(button_help).row(button_exam, button_books).add(button_cancel)
help_menu.add(button_menu)
exam_menu.row(button_9grade, button_11grade).add(button_menu)
books_menu.add(button_menu)