import requests

API_KEY = "AIzaSyAfOP0ojhye9KEop8eYvMgr_xhr6SyMJDY"
CHANNEL_URL = "https://www.googleapis.com/youtube/v3/channels"

params = {
    "part": "snippet,statistics",
    "id": "UCdN5gsxcdryDfzdEL9das4A",  # Замените на ID канала
    "key": API_KEY,
}

response = requests.get(CHANNEL_URL, params=params)
data = response.json()

for item in data.get("items", []):
    title = item["snippet"]["title"]
    description = item["snippet"]["description"]
    subscribers = item["statistics"]["subscriberCount"]
    video_count = item["statistics"]["videoCount"]

    print(f"Название канала: {title}")
    print(f"Описание: {description}")
    print(f"Подписчиков: {subscribers}")
    print(f"Количество видео: {video_count}")