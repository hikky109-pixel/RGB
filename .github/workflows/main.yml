from datetime import datetime
import requests
import os

# ================== 設定 ==================
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# X API情報（GitHub Secretsから取得）
X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
# ============================================

def get_today_color():
    today = datetime.now().day
    base = 10
    diff = (today - base) % 3

    if diff == 0:
        return "🔴", "赤"
    elif diff == 1:
        return "🟢", "緑"
    else:
        return "🔵", "青"

def main():
    emoji, color_name = get_today_color()
    message = f"{emoji} 本日の名古屋駅入構標の色は「{color_name}」です {emoji}"

    print(f"投稿内容: {message}")

    # Discord投稿
    if DISCORD_WEBHOOK:
        try:
            payload = {"content": message, "username": "名古屋駅RGB"}
            response = requests.post(DISCORD_WEBHOOK, json=payload)
            if response.status_code == 204:
                print("✅ Discordに投稿しました")
            else:
                print(f"❌ Discord投稿エラー: {response.status_code}")
        except Exception as e:
            print(f"❌ Discord投稿例外: {e}")
    else:
        print("⚠️ DISCORD_WEBHOOK が設定されていません")

    print("X投稿は後で実装します")

if __name__ == "__main__":
    main()
