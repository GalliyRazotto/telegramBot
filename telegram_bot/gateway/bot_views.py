import logging

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from telegram_bot.keyboards.client_keyboard import kb_client

from telegram_bot.config_bot import token
import telegram_bot.usecase.add_words_users as usecase
from telegram_bot.usecase.translation_requests import word_translation

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    add_word = State()
    request_word = State()
    translate = State()


@dp.message_handler(commands='add', state=None)
async def cm_add_word(message: types.Message):
    await FSMAdmin.add_word.set()
    await message.reply('Input word to translate')


@dp.message_handler(content_types=['text'], state=FSMAdmin.add_word)
async def pull_word(message: types.Message, state: FSMContext):
    word = message.text.lower()
    user_id = message.from_user.id
    msg = 'Word already added'
    word_to_add = usecase.add_new_word(word, user_id)
    if word_to_add:
        async with state.proxy() as data:
            data['word'] = word_to_add.word
        msg = 'Word added. Translation: {}'.format(word_to_add.translation)
    await message.reply(msg)
    await state.finish()


@dp.message_handler(commands='request', state=None)
async def request_word(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    msg = 'No words added to dictionary'
    word = usecase.request_random_word(user_id)
    await FSMAdmin.request_word.set()
    if word:
        async with state.proxy() as data:
            data['word'] = word.translation
            msg = f'How do you translate: {word.word}'
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


@dp.message_handler(commands='translate', state=None)
async def request_word(message: types.Message):
    await FSMAdmin.translate.set()
    msg = f'Write word to translate'
    await message.reply(msg)


@dp.message_handler(content_types=['text'], state=FSMAdmin.translate)
async def pull_word(message: types.Message, state: FSMContext):
    word = message.text.lower()
    translated_word = word_translation(word)
    msg = '404 translation not found'
    if translated_word:
        msg = 'Translated word: {}'.format(translated_word)
    await message.reply(msg)
    await state.finish()


@dp.message_handler(CommandStart())
async def echo(message: types.Message):
    user = types.User.get_current()
    usecase.add_new_user(user.id, user.first_name)

    await message.answer(
        f'Hi {user.first_name}! I am ScienceWordBot! Let me help you to learn english words! Just choose what you are '
        f'going to do!',
        reply_markup=kb_client,
    )

