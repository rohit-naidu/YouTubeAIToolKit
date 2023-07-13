import os
import json
from googleapiclient.discovery import build

# Set up the YouTube Data API v3
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_transcript(video_id):
    # Get video captions
    captions = youtube.captions().list(
        part='snippet',
        videoId=video_id
    ).execute()

    # Get transcript for the first available language
    if captions['items']:
        caption_id = captions['items'][0]['id']
        transcript = youtube.captions().download(
            id=caption_id
        ).execute()
        return transcript['body']
    else:
        return None

def analyze_transcript(transcript, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}
    transcript = transcript.lower()

    # Count occurrences of each keyword
    for keyword in keywords:
        keyword_counts[keyword] = transcript.count(keyword.lower())

    return keyword_counts

# YouTube video ID to analyze
video_id = "YOUR_VIDEO_ID"

# Keywords to search for in the transcript
keywords = ['keyword1', 'keyword2', 'keyword3']

# Get the video transcript
transcript = get_video_transcript(video_id)

if transcript:
    # Analyze the transcript for keyword counts
    keyword_counts = analyze_transcript(transcript, keywords)
    print("Keyword counts:", keyword_counts)
else:
    print("No transcript available for the video.")
