import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توكن البوت الخاص بكِ
TELEGRAM_BOT_TOKEN = "8950198977:AAGGZ4gm36gZjE2qqFdoBNGa1mrlcNfKhF8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك! أنا بوت الذكاء الاصطناعي الخاص بك، كيف يمكنني مساعدتك اليوم؟")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    # هنا يمكنك إضافة الربط مع RAG أو OpenAI لاحقاً
    response = f"استلمت رسالتك: '{user_text}'"
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت يعمل الان...")
    app.run_polling()
