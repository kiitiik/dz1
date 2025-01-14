import requests

API_KEY = "AIzaSyAfOP0ojhye9KEop8eYvMgr_xhr6SyMJDY"
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "type": "video",
    "q": "технологии",
    "maxResults": 5,
    "key": API_KEY,
}

response = requests.get(SEARCH_URL, params=params)
data = response.json()

print("=== Найденные видео ===")
for item in data.get("items", []):
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    print(f"Название: {title}, Ссылка: https://www.youtube.com/watch?v={video_id}")
