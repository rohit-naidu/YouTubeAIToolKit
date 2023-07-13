import requests

def get_recommendations(video_id):
    API_URL = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "relatedToVideoId": video_id,
        "type": "video",
        "maxResults": 5,
        "key": "YOUR_API_KEY"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    for video in data["items"]:
        title = video["snippet"]["title"]
        video_id = video["id"]["videoId"]

        print("Title:", title)
        print("Video ID:", video_id)
        print("--------------------")

video_id = "YOUR_VIDEO_ID"
get_recommendations(video_id)
