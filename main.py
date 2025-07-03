from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

KEYS_FILE = 'YinYangKeys.json'

def load_keys():
    try:
        with open(KEYS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def is_key_valid(key_data):
    if key_data["expired"] == "never":
        return True
    expired_time = datetime.strptime(key_data["expired"], "%Y-%m-%d %H:%M:%S")
    return datetime.now() <= expired_time

@app.route("/")
def home():
    return "🧠 Yin Yang Black Market API — Use /check?key=XXXX to verify your key"

@app.route("/check")
def check_key():
    key = request.args.get("key")
    if not key:
        return jsonify({"status": "error", "message": "Key parameter missing"}), 400

    keys = load_keys()
    if key in keys:
        key_data = keys[key]
        if is_key_valid(key_data):
            return jsonify({
                "status": "success",
                "plan": key_data["plan"],
                "expired": key_data["expired"]
            })
        else:
            return jsonify({"status": "expired", "message": "Key has expired"})
    else:
        return jsonify({"status": "invalid", "message": "Key not found"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
