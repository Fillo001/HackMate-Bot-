from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
from config import API_TOKEN
from src import handlers

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I’m HackMate Bot.\n"
        "I’ll help you with hackathon updates, FAQs, resources, and submissions."
    )

# Main function
def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(CommandHandler("resources", handlers.resources))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.fallback))

    logger.info("✅ HackMate Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
