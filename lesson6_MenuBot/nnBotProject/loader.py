from config import *
# from db import DatabaseManager

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# db = DatabaseManager('database.db')
# db.create_tables()