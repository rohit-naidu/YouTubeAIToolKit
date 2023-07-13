import requests

def get_trending_videos():
    API_URL = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "maxResults": 10,
        "key": "YOUR_API_KEY"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    for video in data["items"]:
        title = video["snippet"]["title"]
        views = video["statistics"]["viewCount"]
        likes = video["statistics"]["likeCount"]
        comments = video["statistics"]["commentCount"]

        print("Title:", title)
        print("Views:", views)
        print("Likes:", likes)
        print("Comments:", comments)
        print("--------------------")

get_trending_videos()
