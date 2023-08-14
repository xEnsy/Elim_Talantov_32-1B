from aiogram.utils import executor
from config import dp
from handlers import start, chating, cummback
from database import commands


start.register_handlers_start(dp=dp)
cummback.register_handlers_cummback(dp=dp)
chating.register_handlers_chating(dp=dp)

async def startup(_):
    db = commands.Database()
    db.sql_create()
    print("бruх бot goтоB")


if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=startup
                           )
