from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_keyboard = [
    [KeyboardButton(text="btn1")],
    [KeyboardButton(text="btn2")],
    [KeyboardButton(text="btn3"), KeyboardButton(text="btn4")],
]
main = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=main_keyboard)