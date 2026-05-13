from datetime import datetime
import requests
import os
import tweepy

# ================== 設定 ==================
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

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

def post_to_discord(message):
    if DISCORD_WEBHOOK:
        try:
            payload = {"content": message, "username": "名古屋駅駅色bot"}
            response = requests.post(DISCORD_WEBHOOK, json=payload)
            if response.status_code == 204:
                print("✅ Discordに投稿しました")
            else:
                print(f"❌ Discord投稿エラー: {response.status_code}")
        except Exception as e:
            print(f"❌ Discord投稿例外: {e}")
    else:
        print("⚠️ DISCORD_WEBHOOK が設定されていません")

def post_to_x(message):
    if not all([X_CONSUMER_KEY, X_CONSUMER_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET]):
        print("⚠️ X APIキーが設定されていません")
        return

    try:
        client = tweepy.Client(
            consumer_key=X_CONSUMER_KEY,
            consumer_secret=X_CONSUMER_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_TOKEN_SECRET
        )
        response = client.create_tweet(text=message)
        print(f"✅ Xに投稿しました (Tweet ID: {response.data['id']})")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

def main():
    emoji, color_name = get_today_color()
    message = f"{emoji} 本日の名古屋駅色は「{color_name}」です {emoji}"

    print(f"投稿内容: {message}")

    post_to_discord(message)
    post_to_x(message)

if __name__ == "__main__":
    main()
