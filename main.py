# Use dotenv for set invironment variables
from dotenv import load_dotenv
load_dotenv('.env')

import logging
import os

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

API_TOKEN = str(os.getenv('TELEGRAM_API_TOKEN'))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def auth(func):
    async def wrapper(message):
        if str(message['from']['id']) != str(os.getenv('MY_TELEGRAM_USER_ID')):
            return await message.reply("Access Denide!", reply=False)
        return await func(message)
    return wrapper

@dp.message_handler(commands=['start', 'help'])
@auth
async def send_welcome(message: types.Message):
    await message.reply(
        "Бот для учетов финансов\n\n"
        "Сегодняшняя статистика: /today\n"
        "За текущий месяц: /mounth\n"
        "Последние внесенные расходы: /expenses\n"
        "Категории трат: /categories\n"
        "Внести новый расход: 250 такси"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)