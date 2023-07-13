import requests

def get_view_count(channel_id, time_period):
    API_URL = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "statistics",
        "id": channel_id,
        "key": "YOUR_API_KEY"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    view_count = data["items"][0]["statistics"]["viewCount"]
    subscriber_count = data["items"][0]["statistics"]["subscriberCount"]

    print("View Count:", view_count)
    print("Subscriber Count:", subscriber_count)

channel_id = "YOUR_CHANNEL_ID"
time_period = "last_30_days"
get_view_count(channel_id, time_period)
