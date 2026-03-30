import os
import time
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
MIN_DISCOUNT = int(os.environ.get("MIN_DISCOUNT", "30"))

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"})

def check_trendyol():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get("https://www.trendyol.com/kampanyalar", headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.select(".product-card")
        for item in items[:10]:
            try:
                name = item.select_one(".product-name")
                discount = item.select_one(".discount-badge")
                link = item.select_one("a")
                if discount and name and link:
                    pct = int(''.join(filter(str.isdigit, discount.text)))
                    if pct >= MIN_DISCOUNT:
                        msg = f"🔥 <b>Trendyol İndirim!</b>\n{name.text.strip()}\n💸 %{pct} indirim\n🔗 https://trendyol.com{link['href']}"
                        send_message(msg)
            except:
                pass
    except Exception as e:
        print(f"Trendyol hata: {e}")

def check_amazon():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get("https://www.amazon.com.tr/deals", headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.select(".deal-card")
        for item in items[:10]:
            try:
                name = item.select_one(".deal-title")
                discount = item.select_one(".discount-tag")
                link = item.select_one("a")
                if discount and name and link:
                    pct = int(''.join(filter(str.isdigit, discount.text)))
                    if pct >= MIN_DISCOUNT:
                        msg = f"🛒 <b>Amazon İndirim!</b>\n{name.text.strip()}\n💸 %{pct} indirim\n🔗 https://amazon.com.tr{link['href']}"
                        send_message(msg)
            except:
                pass
    except Exception as e:
        print(f"Amazon hata: {e}")

send_message("✅ İndirim Sepeti botu başladı! Fırsatları takip ediyorum...")
print("Bot başladı...")
while True:
    check_trendyol()
    check_amazon()
    time.sleep(3600)
