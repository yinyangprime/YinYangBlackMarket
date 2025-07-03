from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

KEY_FILE = "YinYangKeys.json"

def load_keys():
    try:
        with open(KEY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route("/")
def root():
    return jsonify({"status": "API is online", "usage": "/check?key=YOURKEY"})

@app.route("/check")
def check_key():
    key = request.args.get("key")
    if not key:
        return jsonify({"status": "error", "message": "No key provided"}), 400

    keys = load_keys()
    key_data = keys.get(key)

    if not key_data:
        return jsonify({"status": "error", "message": "Key not found"}), 404

    expired = key_data.get("expired")
    if expired == "never":
        return jsonify({"status": "success", "plan": key_data["plan"], "message": "Lifetime key"}), 200

    current_time = datetime.now()
    expired_time = datetime.strptime(expired, "%Y-%m-%d %H:%M:%S")

    if current_time > expired_time:
        return jsonify({"status": "error", "message": "Key expired"}), 403

    return jsonify({
        "status": "success",
        "plan": key_data["plan"],
        "created": key_data["created"],
        "expired": key_data["expired"]
    }), 200

if __name__ == "__main__":
    app.run(debug=False)
