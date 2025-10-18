import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import Message

# Получаем токен из переменных окружения
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Желаю тебе прекрасного дня! 🌞")

# Обработчик приветствий
@dp.message(Text(
    text=[
        "привет", "здравствуй", "здравствуйте", "хай", "hello", "hi", 
        "добрый день", "доброе утро", "добрый вечер", "ку", "салют", 
        "прив", "здаров", "здарова", "хелло", "хэллоу"
    ],
    ignore_case=True
))
async def handle_greeting(message: Message):
    greetings = [
        "Привет! Хорошего дня! 🌞",
        "Здравствуй! Пусть день будет замечательным! ✨",
        "Приветствую! Желаю отличного настроения! 😊",
        "Привет! Пусть сегодняшний день принесет много радости! 🌈",
        "Здорово! Хорошего тебе дня! 👍"
    ]
    greeting = random.choice(greetings)
    await message.answer(greeting)

# Обработчик благодарностей
@dp.message(Text(
    text=[
        "спасибо", "благодарю", "thanks", "thank you", 
        "пасиб", "сябки", "thx"
    ],
    ignore_case=True
))
async def handle_thanks(message: Message):
    await message.answer("Пожалуйста! 😊")

# Запуск бота
async def main():
    print("Бот запущен на Render!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
