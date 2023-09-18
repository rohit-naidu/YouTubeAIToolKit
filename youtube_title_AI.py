from pytube import Channel
import spacy
from collections import Counter

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_titles(channel_url, num_videos=10):
    channel = Channel(channel_url)

    # Fetch the given number of video titles from the channel
    titles = [video.title for video in channel.videos[:num_videos]]

    # Process the titles with spaCy
    docs = [nlp(title) for title in titles]

    # Extract named entities
    entities = [ent.text for doc in docs for ent in doc.ents]
    entity_counts = Counter(entities)

    # Get the sentiment of each title
    sentiments = ['positive' if doc.sentiment > 0.5 else 'negative' if doc.sentiment < 0.5 else 'neutral' for doc in docs]

    # Display the 5 most common named entities and their counts
    print("Top Entities:")
    for entity, count in entity_counts.most_common(5):
        print(f"{entity}: {count}")
    
    # Display sentiment distribution
    sentiment_counts = Counter(sentiments)
    print("\nSentiment Distribution:")
    for sentiment, count in sentiment_counts.items():
        print(f"{sentiment}: {count}")

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    analyze_titles(channel_url)
