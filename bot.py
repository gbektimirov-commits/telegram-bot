from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from flask import Flask
import threading
import os

# Веб-сервер для поддержания активности
app = Flask('')

@app.route('/')
def home():
    return "Бот работает! ✅"

def run_web():
    app.run(host='0.0.0.0', port=8080)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Желаю тебе прекрасного дня! 🌞")

async def handle_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пожалуйста! 😊")

async def handle_greeting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    greetings = [
        "Привет! Хорошего дня! 🌞",
        "Здравствуй! Пусть день будет замечательным! ✨", 
        "Приветствую! Желаю отличного настроения! 😊",
        "Привет! Пусть сегодняшний день принесет много радости! 🌈",
        "Здорово! Хорошего тебе дня! 👍"
    ]
    
    import random
    greeting = random.choice(greetings)
    await update.message.reply_text(greeting)

def run_bot():
    # Токен берем из секретных переменных
    token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & (
            filters.Regex(r"(?i)(привет|здравствуй|здравствуйте|хай|hello|hi|добрый день|доброе утро|добрый вечер)") |
            filters.Regex(r"(?i)(ку|салют|прив|здаров|здарова|хелло|хэллоу)")
        ), 
        handle_greeting
    ))
    application.add_handler(MessageHandler(
        filters.TEXT & (
            filters.Regex(r"(?i)(спасибо|благодарю|thanks|thank you)") |
            filters.Regex(r"(?i)(пасиб|сябки|thx)")
        ), 
        handle_thanks
    ))
    
    print("🤖 Бот запущен и работает 24/7!")
    application.run_polling()

if __name__ == "__main__":
    # Запускаем веб-сервер в отдельном потоке
    threading.Thread(target=run_web).start()
    # Запускаем бота
    run_bot()
