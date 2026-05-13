from datetime import datetime
import requests

# ================== 設定 ==================
WEBHOOK_URL = "https://discord.com/api/webhooks/1502792629354500326/x26-wV3DGyyeZoQld_6HOP-GMQ6dycXCUkeUkpjeUNozsoFzvmxp143hS7so3zZFnakg"
# =========================================

today = datetime.now().day  # 今日の日付（10日なら10）

# 5月10日が赤なので、そこから計算
base = 10
diff = (today - base) % 3

if diff == 0:
    color_emoji = "🔴"
    color_name = "赤"
elif diff == 1:
    color_emoji = "🟢"
    color_name = "緑"
else:
    color_emoji = "🔵"
    color_name = "青"

message = f"{color_emoji} **本日の名古屋駅専色は「{color_name}」です** {color_emoji}"

payload = {
    "content": message,
    "username": "JR名古屋駅駅色BOT"
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print(f"✅ Discordに投稿しました: {color_name}")
else:
    print(f"❌ エラー: {response.status_code}")
    print(response.text)
