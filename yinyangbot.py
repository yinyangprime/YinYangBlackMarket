import os
import json
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

KEYS_FILE = "YinYangKeys.json"

def load_keys():
    try:
        with open(KEYS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def is_key_valid(key_data):
    if key_data["expired"] == "never":
        return True
    expired_time = datetime.strptime(key_data["expired"], "%Y-%m-%d %H:%M:%S")
    return datetime.now() <= expired_time

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 Selamat datang ke *Yin Yang Black Market*\n"
        "Sila hantar kunci lesen (license key) anda untuk pengesahan.",
        parse_mode="Markdown"
    )

async def handle_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    input_key = update.message.text.strip()
    keys = load_keys()

    if input_key in keys:
        key_data = keys[input_key]

        if key_data.get("user_id") and key_data["user_id"] != user_id:
            await update.message.reply_text("❌ Kunci ini hanya sah digunakan oleh pengguna lain.")
            return

        if is_key_valid(key_data):
            keys[input_key]["user_id"] = user_id  # Lock key to this user
            with open(KEYS_FILE, "w") as f:
                json.dump(keys, f, indent=2)

            await update.message.reply_text(
                f"✅ Kunci disahkan!\n"
                f"• Plan: {key_data['plan']}\n"
                f"• Tamat: {key_data['expired']}\n"
                f"Selamat datang ke sistem Black Market!"
            )
        else:
            await update.message.reply_text("❌ Kunci telah tamat tempoh.")
    else:
        await update.message.reply_text("❌ Kunci tidak sah atau telah tamat tempoh.")

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("❌ BOT_TOKEN tidak ditetapkan dalam Secrets.")
        exit()

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("id", lambda u, c: u.message.reply_text(f"🆔 ID Telegram anda: `{u.effective_user.id}`", parse_mode="Markdown")))
    app.add_handler(CommandHandler("status", start))
    app.add_handler(CommandHandler("verifikasi", start))
    app.add_handler(CommandHandler("version", lambda u, c: u.message.reply_text("🧬 Versi: YinYangBot v1.0")))
    app.add_handler(CommandHandler("dev", lambda u, c: u.message.reply_text("👨‍💻 Developer: @xiixmmi")))
    app.add_handler(CommandHandler("tiktok", lambda u, c: u.message.reply_text("📲 TikTok: Yin Yang")))
    app.add_handler(CommandHandler("clear", lambda u, c: u.message.reply_text("🧹 Sesi dibersihkan.")))
    app.add_handler(CommandHandler("exit", lambda u, c: u.message.reply_text("❌ Sesi ditamatkan.")))
    app.add_handler(CommandHandler("check", start))

    app.add_handler(CommandHandler(None, handle_key))  # Catch all text as key
    app.run_polling()
