# 🐉 Yin Yang Black Market

**Yin Yang Black Market** ialah sistem **CPM (Car Parking Multiplayer) automation** yang merangkumi:
- Telegram Bot untuk pengurusan akses & kunci
- Web API untuk semakan kunci secara automatik
- Sistem pengurusan kunci dengan menu terminal
- Kompatibel dengan Termux, iSH (iPhone), dan Replit

---

## 🚀 Fitur Utama

### 🤖 Telegram Bot (`yinyangbot.py`)
- Validasi kunci berasaskan masa (1 Hari, 7 Hari, 30 Hari, Lifetime)
- Respon automatik kepada pengguna
- Lock kunci mengikut ID Telegram tertentu
- Integrasi terus dari Replit / Termux / iSH

### 🌐 Web API (`main.py`)
- Endpoint: `/check?key=XXXX`
- Return JSON sama ada key sah atau tidak
- Gunakan untuk sistem automasi, jualan, integrasi dengan front-end

### 🔧 Auto Mode Switcher (`run.py`)
- Guna mode `bot` atau `api` bergantung pada environment variable `MODE`
- **MODE=bot** → jalan `yinyangbot.py`  
- **MODE=api** → jalan `main.py`

### 🔐 Key Generator Menu (`genkey_menu.py`)
- Menu terminal untuk:
  - Jana kunci (auto expiry)
  - Lock kepada Telegram ID
  - Papar dan buang key
- Sangat berguna untuk admin/pengurus

---

## 📁 Struktur Projek
YinYangBlackMarket/
├── yinyangbot.py         # Telegram bot utama
├── main.py               # Flask web API
├── run.py                # Auto-switch mode
├── genkey_menu.py        # Menu untuk jana dan urus kunci
├── YinYangKeys.json      # Database kunci
├── requirements.txt      # Senarai keperluan Python
├── README.md             # Penerangan projek ini
└── .replit               # Konfigurasi Replit

---

## 🔧 Cara Guna

### Replit / Termux / iSH

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
2. Set environment variables
   Key : BOT_TOKEN & MODE
   Value : bot atau api
3. Run Auto Mode
   python3 run.py
4. Run Key Generator Menu (Opsyenal)
   python3 genkey_menu.py

📌 Contoh API
GET /check?key=ABCDEFG12345
Response:
{
  "status": "valid",
  "plan": "7_day",
  "expired": "2025-07-09 12:00:00"
}

⚠️ Amaran

Sistem ini dilengkapi sistem pengesanan akses haram.
Setiap tindakan log masuk dan IP pengguna direkod.

👑 Developer Info
	•	Telegram: @xiixmmi
	•	TikTok: Yin Yang
  • Channel Telegram: Black Market CPM & Yin Yang CPM
