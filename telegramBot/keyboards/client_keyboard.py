from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn1 = KeyboardButton('/add')
btn2 = KeyboardButton('/request')
btn3 = KeyboardButton('/request')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(btn1, btn2)
