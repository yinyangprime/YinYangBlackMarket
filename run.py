import os
import subprocess

def intro():
    print("""\033[91m
YIN YANG BLACK MARKET SYSTEM - INITIALIZING..
•
@ Booting core modules...
Establishing encrypted connection...
Injecting payload...
Verifying license key...
Authentication success.
\033[93m
AMARAN: Sebarang akses tanpa kebenaran akan dijejak.
Setiap tindakan anda sedang dipantau.
Tiada ruang untuk kesilapan.
Developer: @xiixmmi
TikTok: Yin Yang
\033[0m
""")

def run_bot():
    print("🌀 Starting Telegram Bot Mode...")
    subprocess.run(["python3", "yinyangbot.py"])

def run_api():
    print("🌐 Starting Web API Mode (Flask)...")
    subprocess.run(["python3", "main.py"])

if __name__ == "__main__":
    intro()
    mode = os.getenv("MODE", "bot").lower()
    if mode == "bot":
        run_bot()
    elif mode == "api":
        run_api()
    else:
        print("❌ MODE environment variable must be 'bot' or 'api'")
