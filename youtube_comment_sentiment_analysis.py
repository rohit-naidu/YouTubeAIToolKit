from google.cloud import language_v1
from google.cloud.language_v1 import enums

def analyze_comment_sentiment(comment):
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {"content": comment, "type": type_}

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print("Comment:", comment)
    print("Sentiment Score:", sentiment.score)
    print("Sentiment Magnitude:", sentiment.magnitude)
    print("--------------------")

comments = [
    "Great video! Loved the content.",
    "This is amazing!",
    "Meh, not impressed.",
    "I don't agree with your points.",
    "Excellent job, keep it up!"
]

for comment in comments:
    analyze_comment_sentiment(comment)
