import decouple
from aiogram import Bot, Dispatcher

TOKEN = decouple.config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)