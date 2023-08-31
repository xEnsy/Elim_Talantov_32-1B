from aiogram.utils import executor
from config import dp
from handlers import start, chating, cummback, fsm_f
from database import commands


start.register_handlers_start(dp=dp)
fsm_f.reg_hand_fsm(dp=dp)
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
