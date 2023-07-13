import requests

def calculate_engagement_metrics(video_id):
    API_URL = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics",
        "id": video_id,
        "key": "YOUR_API_KEY"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    likes = int(data["items"][0]["statistics"]["likeCount"])
    dislikes = int(data["items"][0]["statistics"]["dislikeCount"])
    comments = int(data["items"][0]["statistics"]["commentCount"])
    views = int(data["items"][0]["statistics"]["viewCount"])

    likes_to_dislikes_ratio = likes / dislikes
    comments_to_views_ratio = comments / views

    print("Likes-to-Dislikes Ratio:", likes_to_dislikes_ratio)
    print("Comments-to-Views Ratio:", comments_to_views_ratio)

video_id = "YOUR_VIDEO_ID"
calculate_engagement_metrics(video_id)
