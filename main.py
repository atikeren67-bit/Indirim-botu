import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={
        "chat_id": CHANNEL_ID,
        "text": text
    })
    print(f"Mesaj gönderildi: {response.json()}")

print(f"BOT_TOKEN: {BOT_TOKEN[:10] if BOT_TOKEN else 'YOK'}")
print(f"CHANNEL_ID: {CHANNEL_ID}")
send_message("✅ Bot test mesajı!")
print("Bitti")
