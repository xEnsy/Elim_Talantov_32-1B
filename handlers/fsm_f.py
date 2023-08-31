from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType

from config import bot
from database.commands import Database


class FormStates(StatesGroup):
    nickname = State()
    age = State()
    bio = State()
    gender = State()
    photo = State()


async def fsm_start(message: types.Message):
    await message.reply("напиши ник")
    await FormStates.nickname.set()


async def load_nick(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text

    await FormStates.next()
    await message.reply("напиши возраст")


async def load_age(message: types.Message,
                   state: FSMContext):
    if type(int(message.text)) != int:
        await message.reply("только цифры")
        await state.finish()
    else:
        async with state.proxy() as data:
            data["age"] = message.text
        await FormStates.next()
        await message.reply("расскажи о себе")


async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = message.text
    await FormStates.next()
    await message.reply("какого ты пола?")


async def load_gen(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["gender"] = message.text
    await FormStates.next()
    await message.reply("покажи свое лицо")


async def load_photo(message: types.Message, state: FSMContext):
    user_id = Database().select_user_id_query(telegram_id=message.from_user.id)
    path = await message.photo[-1].download(destination_dir="C:/Users/Энси/PycharmProjects/bruh/handlers/media")
    async with state.proxy() as data:
        data['photo'] = path.name
        Database().sql_insert_start_fsm(user_id=user_id['id'],
                                        telegram_id=message.from_user.id,
                                        nickname=data['nickname'],
                                        age=data['age'],
                                        bio=data['bio'],
                                        gender=data['gender'],
                                        photo=data['photo']
                                        )
    with open(path.name, 'rb') as photo:
        await message.reply('Готова')
        await state.finish()


def reg_hand_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['signup'])
    dp.register_message_handler(load_nick, state=FormStates.nickname, content_types=["text"])
    dp.register_message_handler(load_age, state=FormStates.age, content_types=["text"])
    dp.register_message_handler(load_bio, state=FormStates.bio, content_types=["text"])
    dp.register_message_handler(load_gen, state=FormStates.gender, content_types=["text"])
    dp.register_message_handler(load_photo, state=FormStates.photo, content_types=ContentType.PHOTO)
