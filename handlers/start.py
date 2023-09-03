from config import bot
from aiogram import types, Dispatcher
from database.commands import Database
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


async def start_button(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.first_name
    first_name = message.from_user.first_name
    last_name = message.from_user.first_name
    Database().sql_insert_start(telegram_id=telegram_id,
                                username=username,
                                first_name=first_name,
                                last_name=last_name)
    await message.reply(text=f"Команды которые есть\n"
                             f"/start\n"
                             f"/quiz\n"
                             f"/signup"
                        )


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(
        'Некст',
        callback_data="button1"
    )
    markup.add(button1)

    question = "Я нефор или оффник?"
    option = [
        "Что такое нефор?",
        "Что такое оффник?",
        "Ты нефор",
        "Ты оффник",
        "Ты недопайтонщик"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="This is so easy not gonna explain",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup

    )


async def quiz2(call: types.CallbackQuery):
    question = 'кто я буду в будущем?'
    option = [
        "Ты будешь нефор",
        "ты будешь недопайтонщик",
        "Ты будешь профессиАНАЛЬНЫЙ пайтонщиком яуяу",
        "Пока"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="This is so easy not gonna explain",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button1")
