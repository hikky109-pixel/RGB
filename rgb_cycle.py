from datetime import datetime
import sys

# 基準日（2026年5月10日が赤）
base_date = datetime(2026, 5, 10)
today = datetime.now()

# 日数の差を計算
days_diff = (today - base_date).days

# 3で割った余りで色を判定
cycle = days_diff % 3

if cycle == 0:
    color = "🔴 赤"
    color_name = "赤"
elif cycle == 1:
    color = "🟢 緑"
    color_name = "緑"
else:
    color = "🔵 青"
    color_name = "青"

print(f"今日は {color} です")
print(f"名古屋駅入構標の色: {color_name}")

# Discord投稿用（後で使う）
print(f"DISCORD_COLOR:{color_name}")
