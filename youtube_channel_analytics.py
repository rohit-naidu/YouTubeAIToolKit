from googleapiclient.discovery import build

# Set up the YouTube Data API v3
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(channel_id):
    # Get channel statistics
    channel_response = youtube.channels().list(
        part='statistics',
        id=channel_id
    ).execute()

    # Extract relevant metrics
    view_count = channel_response['items'][0]['statistics']['viewCount']
    subscriber_count = channel_response['items'][0]['statistics']['subscriberCount']
    video_count = channel_response['items'][0]['statistics']['videoCount']

    # Calculate engagement rate
    engagement_rate = int(view_count) / int(subscriber_count)

    # Print channel statistics
    print("Channel Statistics:")
    print("Total Views:", view_count)
    print("Subscribers:", subscriber_count)
    print("Video Count:", video_count)
    print("Engagement Rate:", engagement_rate)

# YouTube channel ID to analyze
channel_id = "YOUR_CHANNEL_ID"

# Get channel statistics
get_channel_stats(channel_id)
