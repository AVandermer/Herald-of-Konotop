from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_keyboard = [
    [KeyboardButton(text="Weather report")],
    [KeyboardButton(text="Air Raid ")],
    [KeyboardButton(text="Donation"), KeyboardButton(text="About")],
]
main = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=main_keyboard)