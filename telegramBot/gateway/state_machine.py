# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types
# from telegramBot.gateway.bot_views import dp
#
#
# class FSMAdmin(StatesGroup):
#     word = State()
#
#
# @dp.message_handler(commands='add', state=None)
# async def cm_add_word(message: types.Message):
#     await FSMAdmin.word.set()
#     await message.reply('Input word to translate')
#
#
# @dp.message_handler(content_types=['text'], state=FSMAdmin.word)
# async def pull_word(message: types.Message, state: FSMContext):
#     print(message.text)
#     async with state.proxy() as data:
#         data['word'] = message.text
#     await state.finish()
#     await message.reply('Word added')
#
