# genkey_menu.py

import json, os, datetime
from uuid import uuid4

KEY_FILE = 'YinYangKeys.json'

def load_keys():
    if not os.path.exists(KEY_FILE):
        return {}
    with open(KEY_FILE, 'r') as f:
        return json.load(f)

def save_keys(keys):
    with open(KEY_FILE, 'w') as f:
        json.dump(keys, f, indent=4)

def generate_key(plan, user_id):
    key = str(uuid4()).replace("-", "")[:12].upper()
    now = datetime.datetime.now()
    if plan == '1_day':
        expired = now + datetime.timedelta(days=1)
    elif plan == '7_day':
        expired = now + datetime.timedelta(days=7)
    elif plan == '30_day':
        expired = now + datetime.timedelta(days=30)
    elif plan == 'lifetime':
        expired = "never"
    else:
        return None

    keys = load_keys()
    keys[key] = {
        'plan': plan,
        'created': now.strftime('%Y-%m-%d %H:%M:%S'),
        'expired': expired if expired == "never" else expired.strftime('%Y-%m-%d %H:%M:%S'),
        'allowed_id': user_id
    }
    save_keys(keys)
    return key

def menu():
    print("\nYin Yang Key Generator Menu")
    print("1. Generate Key")
    print("2. View Keys")
    print("3. Delete Key")
    print("4. Exit")

    while True:
        menu()
        choice = input("\nSelect menu: ")
        if choice == '1':
            plan = input("Enter plan (1_day / 7_day / 30_day / lifetime): ").strip()
            user_id = input("Enter Telegram ID to lock key to: ").strip()
            key = generate_key(plan, user_id)
            if key:
                print(f"\n✅ Key generated: {key}")
            else:
                print("❌ Invalid plan.")
        elif choice == '2':
            keys = load_keys()
            for k, v in keys.items():
                print(f"\n🔑 {k} → {v}")
        elif choice == '3':
            key_to_delete = input("Enter key to delete: ").strip()
            keys = load_keys()
            if key_to_delete in keys:
                del keys[key_to_delete]
                save_keys(keys)
                print("🗑️ Key deleted.")
            else:
                print("❌ Key not found.")
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
