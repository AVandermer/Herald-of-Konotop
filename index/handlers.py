from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

import index.keyboards as keyboards

rt = Router()

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello!", reply_markup=keyboards.main)


@rt.message()
async def echo_handler(message: Message) -> None:

    try:

        await message.answer("Вітаю тебе в Конотопському вістнику! \nЯ поки що юзлесс, тому послухай мій трек")
        await message.answer("https://www.youtube.com/watch?v=uxs_HYw_mLk")
    except TypeError:
        await message.answer("Nice try!")
