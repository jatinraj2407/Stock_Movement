import praw
import pandas as pd
from datetime import datetime

# Reddit API credentials
REDDIT_CLIENT_ID = "sP65pMc1oSbAUU8TLyCYAQ"
REDDIT_CLIENT_SECRET = "rdvv5Ij-u0U5Enahl58cOEwwMDK1lw"
REDDIT_USER_AGENT = "Stock Sentiment Scraper"

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def scrape_reddit(subreddit_name, post_limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    data = []

    for post in subreddit.hot(limit=post_limit):
        data.append({
            "title": post.title,
            "score": post.score,
            "comments": post.num_comments,
            "created_utc": datetime.fromtimestamp(post.created_utc),
            "text": post.selftext
        })
    
    return pd.DataFrame(data)

# Scrape data from the 'stocks' subreddit
df = scrape_reddit("stocks", post_limit=200)
df.to_csv("reddit_raw_data.csv", index=False)  # Save to CSV
df.head()  # Display first few rows
