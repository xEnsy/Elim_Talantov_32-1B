from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def secter_bruh(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(
        'гейский список',
        callback_data="gay_list"
    )
    markup.add(button1)
    if message.chat.id != -1001740577981:
        await message.reply("yes?",
                            reply_markup=markup)


async def bruh(message: types.Message):
    ban_word = ["gay", "nefor", "offnic", "negor", ]
    print(message.chat.id)
    if message.chat.id == -1001740577981:
        for word in ban_word:
            if word in message.text.lower().replace(" ", ''):
                await bot.send_message(message.chat.id,
                                       "ban polu4ich!")
                await bot.delete_message(chat_id=message.chat.id,
                                         message_id=message.message_id)


def register_handlers_chating(dp: Dispatcher):
    dp.register_message_handler(secter_bruh, lambda word: "bruh69" in word.text)
    dp.register_message_handler(bruh)
