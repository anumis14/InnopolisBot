from config import *

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class FilmTest(StatesGroup):
    name = State()
    age = State()
    country = State()
    genre = State()


def get_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/vote"))
    return kb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет для начала опроса напиши команду /vote", reply_markup=get_kb())


@dp.message_handler(commands=["vote"])
async def cmd_name(message: types.Message):
    await message.answer("Для начала опроса напишите свое имя!")
    await FilmTest.name.set()


@dp.message_handler(state=FilmTest.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Теперь отправьте свой возраст")
    await FilmTest.next()


@dp.message_handler(state=FilmTest.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
    await message.reply("Теперь отправьте любимую страну-кинематограф")
    await FilmTest.next()


@dp.message_handler(state=FilmTest.country)
async def load_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["country"] = message.text
    await message.reply("Отправьте свой любимый жанр фильма")
    await FilmTest.next()


@dp.message_handler(state=FilmTest.genre)
async def load_genre(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["genre"] = message.text
    await message.reply(f"Опрос пройден, вот ваши ответы:\n"
                        f"Имя: {data['name']}\n"
                        f"Возраст: {data['age']}\n"
                        f"Любимая страна-кинематограф: {data['country']}\n"
                        f"Любимый жанр: {data['genre']}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)