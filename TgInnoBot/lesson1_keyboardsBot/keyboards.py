from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('Привет!')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(button1)

button1 = KeyboardButton("1?")
button2 = KeyboardButton("2?")
button3 = KeyboardButton("3?")

kb1 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)

kb2 = ReplyKeyboardMarkup().row(button1, button2, button3)

kb3 = ReplyKeyboardMarkup().row(button1, button2, button3).add(KeyboardButton("Средний ряд"))

button4 = KeyboardButton("4")
button5 = KeyboardButton("5")
button6 = KeyboardButton("6")
kb3.row(button4, button5, button6)
kb3.insert(button6)