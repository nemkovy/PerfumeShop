import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"{message.from_user.first_name} добро пожаловать в магазин парфюмерии")
@dp.message()
async def echo(message: types.Message):
    await message.reply('Я тебя не понимаю')

async def main():
    await dp.start_polling(bot)
asyncio.run(main())

