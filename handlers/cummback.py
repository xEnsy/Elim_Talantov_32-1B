from config import bot
from aiogram import types, Dispatcher
from database.commands import Database
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


async def gay_list(call: types.CallbackQuery):
    users = Database().sql_user()
    print(users)
    print(str(users))
    doto = []
    for i in users:
        if not i["username"]:
            doto.append("None Username")
        else:
            doto.append(i("username"))

    doto = '\n'.join(doto)
    await call.message.reply(f"{doto}")


def register_handlers_cummback(dp: Dispatcher):
    dp.register_callback_query_handler(gay_list, lambda call: call.data == "gay_list")
