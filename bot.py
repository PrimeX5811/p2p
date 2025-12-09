import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8489055225:AAHfRkvxr3jIBKdQ0JIU0aqaMhqa6MQiP0Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Создать ордер", callback_data='create')],
        [InlineKeyboardButton("📋 Мои ордера", callback_data='orders')],
        [InlineKeyboardButton("👤 Профиль", callback_data='profile')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"👋 Привет!\n\nЯ — P2P бот для обмена USDT/RUB\n\nВыбери действие:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'create':
        await query.edit_message_text("Создание ордера...")
    elif query.data == 'profile':
        await query.edit_message_text("👤 Твой профиль")
    elif query.data == 'orders':
        await query.edit_message_text("📋 Твои ордера")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
