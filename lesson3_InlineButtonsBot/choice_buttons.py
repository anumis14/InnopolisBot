from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


choice = InlineKeyboardMarkup(row_width=2)

film_100 = InlineKeyboardButton(text="Топ 100 фильмов от Кинопоиска", url='https://www.kinopoisk.ru/lists/movies/top_100_by_total_film/?utm_referrer=yandex.ru')
film_fav = InlineKeyboardButton(text="Любимый фильм создателя бота", url='https://www.kinopoisk.ru/film/45185/')
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")

choice.insert(film_100)
choice.insert(film_fav)
choice.insert(cancel_button)