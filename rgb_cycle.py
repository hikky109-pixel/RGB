from datetime import datetime
import requests

# ================== 設定 ==================
WEBHOOK_URL = "https://discord.com/api/webhooks/1502187450037047306/cy-lwGP_5eisPhCj9zpSR3XAKvsOcHRdF9eS5YXPatjpys8b04jVN6J60eA-keVGNqh1"
# =========================================

base_date = datetime(2026, 5, 10)
today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

days_diff = (today - base_date).days
cycle = days_diff % 3

if cycle == 0:
    color_emoji = "🔴"
    color_name = "赤"
elif cycle == 1:
    color_emoji = "🟢"
    color_name = "緑"
else:
    color_emoji = "🔵"
    color_name = "青"

message = f"{color_emoji} **本日の名古屋駅入構標の色は「{color_name}」です** {color_emoji}"

payload = {
    "content": message,
    "username": "名古屋駅RGB"
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print(f"✅ Discordに投稿しました: {color_name}")
else:
    print(f"❌ エラー: {response.status_code}")
    print(response.text)
