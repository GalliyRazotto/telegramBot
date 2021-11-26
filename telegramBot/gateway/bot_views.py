import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from telegramBot.keyboards.client_keyboard import kb_client

from bot_config import TOKEN
import telegramBot.usecase.add_words_users as usecase

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    word = State()


@dp.message_handler(commands='add', state=None)
async def cm_add_word(message: types.Message):
    await FSMAdmin.word.set()
    await message.reply('Input word to translate')


@dp.message_handler(content_types=['text'], state=FSMAdmin.word)
async def pull_word(message: types.Message, state: FSMContext):
    word = message.text.lower()
    user_name = message.from_user.first_name
    if usecase.add_new_word(word, user_name):
        async with state.proxy() as data:
            data['word'] = message.text
        await message.reply('Word added')
    else:
        await message.reply('Word already added')
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

