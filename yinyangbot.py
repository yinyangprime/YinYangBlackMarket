import os
import json
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

KEY_FILE = "YinYangKeys.json"
OWNER_ID = 754978535  # Gantikan dengan ID Telegram boss kalau nak ubah

# --- Fungsi untuk semak key dari fail JSON ---
def load_keys():
    try:
        with open(KEY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def check_key_validity(user_id, key):
    keys = load_keys()
    data = keys.get(key)

    if not data:
        return "❌ Kunci tidak sah atau telah tamat tempoh."

    # --- Logik untuk lock key kepada Telegram ID ---
    if "user_id" in data and str(user_id) != str(data["user_id"]):
        return "🚫 Kunci ini telah dikunci kepada ID Telegram lain."

    # --- Semak tarikh tamat ---
    expired = data.get("expired")
    if expired == "never":
        return f"✅ Kunci SAH! Pelan: {data['plan'].upper()} (Tiada tarikh luput)"

    expired_time = datetime.strptime(expired, "%Y-%m-%d %H:%M:%S")
    if datetime.now() > expired_time:
        return "❌ Kunci anda telah tamat tempoh."

    return f"✅ Kunci SAH!\n• Pelan: {data['plan'].upper()}\n• Luput: {data['expired']}"

# --- Command /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌀 *Yin Yang Black Market Bot*\n"
        "Hantar kunci anda untuk semakan status.\n\n"
        "Developer: @xiixmmi\nTikTok: Yin Yang",
        parse_mode="Markdown"
    )

# --- Bila user reply dengan key ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    key = update.message.text.strip()

    # Semak dan respon
    response = check_key_validity(user_id, key)
    await update.message.reply_text(response)

# --- Mula bot ---
def start_bot():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("❌ BOT_TOKEN tidak dijumpai dalam environment variable.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("info", start))
    app.add_handler(CommandHandler("check", start))
    app.add_handler(CommandHandler("status", start))
    app.add_handler(CommandHandler("key", start))
    app.add_handler(CommandHandler("id", start))
    app.add_handler(CommandHandler("ping", start))
    app.add_handler(CommandHandler("alive", start))

    app.add_handler(CommandHandler("owner", lambda u, c: u.message.reply_text("👑 Developer: @xiixmmi")))

    app.add_handler(CommandHandler("idku", lambda u, c: u.message.reply_text(f"🆔 ID anda: {u.effective_user.id}")))

    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram bot sedang berjalan...")
    app.run_polling()
