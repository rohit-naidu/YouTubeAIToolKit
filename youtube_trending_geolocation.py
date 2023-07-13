from googleapiclient.discovery import build

# Set up the YouTube Data API v3
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

def analyze_trending_geolocation():
    # Get trending videos in a specific region (e.g., US)
    region_code = "US"
    trending_response = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode=region_code
    ).execute()

    # Extract video details
    videos = trending_response['items']
    for video in videos:
        title = video['snippet']['title']
        video_id = video['id']
        print("Title:", title)
        print("Video ID:", video_id)
        print("--------------------")

# Analyze trending videos in a specific region
analyze_trending_geolocation()
