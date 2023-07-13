from google.cloud import language_v1
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(comments):
    # Combine comments into a single string
    combined_comments = " ".join(comments)

    # Generate word cloud
    wordcloud = WordCloud().generate(combined_comments)

    # Display the word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

comments = [
    "Great video! Loved the content.",
    "This is amazing!",
    "Meh, not impressed.",
    "I don't agree with your points.",
    "Excellent job, keep it up!"
]

# Generate word cloud from comments
generate_word_cloud(comments)
