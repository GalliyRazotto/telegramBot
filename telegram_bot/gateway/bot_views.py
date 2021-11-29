import logging

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from telegram_bot.keyboards.client_keyboard import kb_client

from config_bot import TOKEN
import telegram_bot.usecase.add_words_users as usecase

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    add_word = State()
    request_word = State()


@dp.message_handler(commands='add', state=None)
async def cm_add_word(message: types.Message):
    await FSMAdmin.add_word.set()
    await message.reply('Input word to translate')


@dp.message_handler(content_types=['text'], state=FSMAdmin.add_word)
async def pull_word(message: types.Message, state: FSMContext):
    word = message.text.lower()
    user_name = message.from_user.first_name
    msg = 'Word already added'
    if usecase.add_new_word(word, user_name):
        async with state.proxy() as data:
            data['word'] = word
        msg = 'Word added'
    await message.reply(msg)
    await state.finish()


@dp.message_handler(commands='request', state=None)
async def request_word(message: types.Message, state: FSMContext):
    user_name = message.from_user.first_name
    msg = 'No words added to dictionary'
    word = usecase.request_random_word(user_name)
    await FSMAdmin.request_word.set()
    if word:
        async with state.proxy() as data:
            data['word'] = word.translation
            msg = f'Напишите перевод слова {word.word}'
    await message.reply(msg)


@dp.message_handler(content_types=['text'], state=FSMAdmin.request_word)
async def pull_word(message: types.Message, state: FSMContext):
    translation = message.text.lower()
    msg = 'You should learn it again. Would you like to /request once more?'
    async with state.proxy() as data:
        if translation == data['word']:
            msg = 'Great! /request to try once more!'
    await message.reply(msg)
    await state.finish()


@dp.message_handler(CommandStart())
async def echo(message: types.Message):
    user = types.User.get_current()
    usecase.add_new_user(user.first_name)

    await message.answer(
        f'Hi {user.first_name}! I am ScienceWordBot! Let me help you to learn english words! Just choose what you are '
        f'going to do!',
        reply_markup=kb_client,
    )

