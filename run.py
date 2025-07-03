import os
import subprocess

def banner():
    print("\nYIN YANG BLACK MARKET SYSTEM - INITIALIZING..\n•")
    print("@ Booting core modules...")
    print("Establishing encrypted connection...")
    print("Injecting payload...")
    print("Verifying license key...")
    print("Authentication success.\n")
    print("AMARAN: Sebarang akses tanpa kebenaran akan dijejak.")
    print("Setiap tindakan anda sedang dipantau.")
    print("Tiada ruang untuk kesilapan.\n")
    print("Developer: @xiixmmi")
    print("TikTok: Yin Yang\n")

def main():
    banner()
    mode = os.getenv("MODE", "bot")

    if mode == "bot":
        print("Starting Telegram Bot Mode...\n")
        subprocess.run(["python3", "yinyangbot.py"])
    elif mode == "api":
        print("Starting Web API Mode (Flask)...\n")
        subprocess.run(["python3", "main.py"])
    else:
        print("❌ MODE tidak dikenali. Sila set 'MODE=bot' atau 'MODE=api' dalam Replit Secrets.")

if __name__ == "__main__":
    main()
