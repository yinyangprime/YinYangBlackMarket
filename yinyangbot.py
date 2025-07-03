import os
import json
import datetime
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging untuk debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")
KEYS_FILE = "YinYangKeys.json"

# Fungsi load key
def load_keys():
    try:
        with open(KEYS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi semak status key
def is_key_valid(key_data):
    if key_data["expired"] == "never":
        return True
    expired = datetime.datetime.strptime(key_data["expired"], "%Y-%m-%d %H:%M:%S")
    return datetime.datetime.now() < expired

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Selamat datang ke sistem BLACK MARKET. Sila hantar kunci akses (key) anda untuk semakan.")

# Bila user hantar mesej (key)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    user_id = update.message.from_user.id
    keys = load_keys()

    if user_input not in keys:
        await update.message.reply_text("❌ Kunci tidak sah atau tidak wujud.")
        return

    key_data = keys[user_input]

    # Semak ID jika dikunci kepada ID
    if "user_id" in key_data and str(key_data["user_id"]) != str(user_id):
        await update.message.reply_text("❌ Kunci ini hanya sah untuk pengguna tertentu.")
        return

    # Semak expired
    if not is_key_valid(key_data):
        await update.message.reply_text("❌ Kunci telah tamat tempoh.")
        return

    plan = key_data["plan"]
    expired = key_data["expired"]
    await update.message.reply_text(f"✅ Kunci sah.\n🔑 Pelan: {plan}\n📅 Tamat: {expired}")

# Setup bot
if __name__ == '__main__':
    if not TOKEN:
        print("❌ BOT_TOKEN tidak ditetapkan dalam environment.")
        exit()

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("id", start))
    app.add_handler(CommandHandler("verify", start))
    app.add_handler(CommandHandler("semak", start))
    app.add_handler(CommandHandler("key", start))
    app.add_handler(CommandHandler("kunci", start))
    app.add_handler(CommandHandler("unlock", start))
    app.add_handler(CommandHandler("aktifkan", start))
    app.add_handler(CommandHandler("mula", start))
    app.add_handler(CommandHandler("license", start))

    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot sedang berjalan...")
    app.run_polling()
