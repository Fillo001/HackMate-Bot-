from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help menu\n"
        "/resources - Get hackathon learning resources\n"
    )

async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Hackathon Resources:\n"
        "1. GitHub for beginners → https://docs.github.com/en/get-started\n"
        "2. FreeCodeCamp → https://www.freecodecamp.org/\n"
        "3. Hackathon Guide → https://hackathon.guide"
    )

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤔 Sorry, I didn’t understand that.\nType /help to see available commands."
    )
