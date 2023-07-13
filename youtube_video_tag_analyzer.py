from googleapiclient.discovery import build

# Set up the YouTube Data API v3
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

def analyze_video_tags(video_id):
    # Get video details
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    # Extract video tags
    tags = video_response['items'][0]['snippet']['tags']

    # Print video tags
    print("Video Tags:")
    for tag in tags:
        print(tag)

# YouTube video ID to analyze
video_id = "YOUR_VIDEO_ID"

# Analyze video tags
analyze_video_tags(video_id)
