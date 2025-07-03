import os
import time

def intro():
    print("YIN YANG BLACK MARKET SYSTEM - INITIALIZING..\n")
    time.sleep(0.5)
    print("• @ Booting core modules...")
    time.sleep(0.5)
    print("• Establishing encrypted connection...")
    time.sleep(0.5)
    print("• Injecting payload...")
    time.sleep(0.5)
    print("• Verifying license key...")
    time.sleep(0.5)
    print("• Authentication success.\n")
    time.sleep(0.5)
    print("AMARAN: Sebarang akses tanpa kebenaran akan dijejak.")
    print("Setiap tindakan anda sedang dipantau.")
    print("Tiada ruang untuk kesilapan.\n")
    print("Developer: @xiixmmi")
    print("TikTok: Yin Yang\n")
    time.sleep(1)

def run_bot():
    from yinyangbot import start_bot
    start_bot()

def run_api():
    from main import app
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    intro()
    mode = os.getenv("MODE", "bot").lower()
    
    if mode == "bot":
        print("Starting Telegram Bot Mode...\n")
        run_bot()
    elif mode == "api":
        print("Starting Web API Mode (Flask)...\n")
        run_api()
    else:
        print(f"Invalid MODE '{mode}'! Use 'bot' or 'api'.")
