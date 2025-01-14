import requests

API_KEY = "AIzaSyAfOP0ojhye9KEop8eYvMgr_xhr6SyMJDY"
COMMENTS_URL = "https://www.googleapis.com/youtube/v3/commentThreads"

params = {
    "part": "snippet",
    "videoId": "v2ebNID3T34",  # Замените на ID видео
    "maxResults": 5,
    "key": API_KEY,
}

response = requests.get(COMMENTS_URL, params=params)
data = response.json()

print("=== Комментарии к видео ===")
for item in data.get("items", []):
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
    print(f"{author}: {comment}")