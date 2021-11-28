from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btnAdd = KeyboardButton('/add')
btnRequest = KeyboardButton('/request')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(btnAdd, btnRequest)
