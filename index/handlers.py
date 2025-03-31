import os
from dotenv import load_dotenv
import requests

from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

import index.keyboards as keyboards

rt = Router()

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    try:

        await message.answer("Вітаю тебе в Конотопському вістнику! \nЯ поки що юзлесс, тому послухай мій трек", reply_markup=keyboards.main)
        await message.answer("https://www.youtube.com/watch?v=uxs_HYw_mLk")
    except TypeError:
        await message.answer("Nice try!")



@rt.message(F.text == 'About')
async def about_handler(message: Message) -> None:

    try:

        await message.answer('Якщо бажаєш дізнатись про наш проєкт більше, переходь за посиланням нижче')
        await message.answer('https://github.com/AVandermer/Herald-of-Konotop')
    except TypeError:
        await message.answer("Nice try!")


@rt.message(F.text == 'Weather report')
async def weather_report_handler(message: Message) -> None:
    try:
        load_dotenv()

        lat = os.getenv("CITY_LATITUDE")
        lon = os.getenv("CITY_LONGITUDE")
        appid = os.getenv("WEATHER_API_KEY")

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=ua")
        await message.answer(response.text)
    except TypeError:
        await message.answer("Nice try!")