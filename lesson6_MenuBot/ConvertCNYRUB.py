from config import *
from bs4 import BeautifulSoup
import requests


class Currency:
    CNY_RUB = "https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=APwXEde8Rqy50gl-gzvtK0R2zJuca_AOdA%3A1687704142721&source=hp&ei=TlKYZJnfJ7GPxc8PjIG-oA8&iflsig=AOEireoAAAAAZJhgXkUZRWA5gJW1oESxQbyaDcJpJwH-&ved=0ahUKEwiZvqLv097_AhWxR_EDHYyAD_QQ4dUDCAk&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egdnd3Mtd2l6Ih_QutGD0YDRgSDRjtCw0L3QsCDQuiDRgNGD0LHQu9GOMgwQABiABBgKGEYYggIyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApIihlQAFisF3AAeACQAQGYAfQCoAG7GaoBCDAuMTQuMS4yuAEDyAEA-AEBwgIEECMYJ8ICCxAAGIAEGLEDGIMBwgILEAAYigUYsQMYgwHCAgUQLhiABMICBRAAGIAEwgIIEAAYgAQYsQPCAg0QABiABBixAxiDARgKwgIKEAAYgAQYsQMYCg&sclient=gws-wiz"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def get_currency_price(self):
        full_page = requests.get(self.CNY_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text.replace(",", ".")


bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


def get_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/monitoring"))
    return kb


class CurrencyStates(StatesGroup):
    monitoring = State()


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет, это бот для мониторинга курса рубля к юаню. Для просмотра цены напишите команду /monitoring",
        reply_markup=get_kb())


@dp.message_handler(commands=["monitoring"])
async def enter_monitoring(message: types.Message):
    await message.answer("Напишите число в рублях, которое вы хотите перевести в юани")
    await CurrencyStates.monitoring.set()


@dp.message_handler(state=CurrencyStates.monitoring)
async def start_monitoring(message: types.Message, state: FSMContext):
    currency = Currency()
    transfer_sum = int(message.text)*float(currency.get_currency_price())
    await message.answer(f"{message.text} рублей равен {transfer_sum}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)