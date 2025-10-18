from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Желаю тебе прекрасного дня! 🌞")

async def handle_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пожалуйста! 😊")

async def handle_greeting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Список приветственных ответов для разнообразия
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

def main():
    # ВСТАВЬТЕ СВОЙ ТОКЕН В КАВЫЧКИ
    application = Application.builder().token("ВАШ_ТОКЕН_ЗДЕСЬ").build()
    
    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Обработчик приветствий
    application.add_handler(MessageHandler(
        filters.TEXT & (
            filters.Regex(r"(?i)(привет|здравствуй|здравствуйте|хай|hello|hi|добрый день|доброе утро|добрый вечер)") |
            filters.Regex(r"(?i)(ку|салют|прив|здаров|здарова|хелло|хэллоу)")
        ), 
        handle_greeting
    ))
    
    # Обработчик благодарностей
    application.add_handler(MessageHandler(
        filters.TEXT & (
            filters.Regex(r"(?i)(спасибо|благодарю|thanks|thank you)") |
            filters.Regex(r"(?i)(пасиб|сябки|thx)")
        ), 
        handle_thanks
    ))
    
    print("Бот запущен! Нажмите Ctrl+C чтобы остановить")
    application.run_polling()

if __name__ == "__main__":
    main()
