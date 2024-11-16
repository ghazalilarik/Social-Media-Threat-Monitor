import tweepy
import praw
import requests
import re
import json
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import schedule
import time
from datetime import datetime

# Set up Twitter API credentials
twitter_api_key = 'YOUR_TWITTER_API_KEY'
twitter_api_secret = 'YOUR_TWITTER_API_SECRET'
twitter_access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
twitter_access_secret = 'YOUR_TWITTER_ACCESS_SECRET'

# Set up Reddit API credentials
reddit_client_id = 'YOUR_REDDIT_CLIENT_ID'
reddit_client_secret = 'YOUR_REDDIT_CLIENT_SECRET'
reddit_user_agent = 'YOUR_USER_AGENT'

# Facebook is more restricted; so we'll omit real-time scraping here for simplicity
# Facebook Graph API can be used but requires special permissions

# Keywords to monitor
keywords = ["data breach", "cyber attack", "vulnerability", "zero-day", "cybersecurity threat"]

# Setup Twitter API
def setup_twitter_api():
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# Setup Reddit API
def setup_reddit_api():
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)
    return reddit

# Fetch Twitter mentions
def fetch_twitter_mentions(api, keywords):
    tweets = []
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang='en').items(50):
            tweets.append(tweet.text)
    return tweets

# Fetch Reddit mentions
def fetch_reddit_mentions(reddit, keywords):
    mentions = []
    for keyword in keywords:
        for submission in reddit.subreddit("all").search(keyword, limit=50):
            mentions.append(submission.title + " " + submission.selftext)
    return mentions

# Pre-process text data
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters
    return text.lower()

# Categorize threats using NLP
def categorize_threats(texts):
    categories = ["Data Breach", "Vulnerability", "General Threat"]
    
    # Simple TF-IDF Vectorizer + Logistic Regression as an example classifier
    vectorizer = TfidfVectorizer(stop_words='english')
    sample_data = ["data breach at company", "zero-day vulnerability found", "cybersecurity threat discovered"]
    sample_labels = [0, 1, 2]
    
    X_train = vectorizer.fit_transform(sample_data)
    model = LogisticRegression()
    model.fit(X_train, sample_labels)
    
    categorized_results = []
    for text in texts:
        processed_text = preprocess_text(text)
        X_test = vectorizer.transform([processed_text])
        predicted_category = model.predict(X_test)[0]
        categorized_results.append((text, categories[predicted_category]))
    
    return categorized_results

# Monitor threats on social media
def monitor_threats():
    twitter_api = setup_twitter_api()
    reddit_api = setup_reddit_api()

    print(f"[{datetime.now()}] Fetching mentions from Twitter...")
    twitter_mentions = fetch_twitter_mentions(twitter_api, keywords)
    print(f"[{datetime.now()}] Fetching mentions from Reddit...")
    reddit_mentions = fetch_reddit_mentions(reddit_api, keywords)

    all_mentions = twitter_mentions + reddit_mentions
    categorized_threats = categorize_threats(all_mentions)

    # Save to CSV for record-keeping and analysis
    df = pd.DataFrame(categorized_threats, columns=["Text", "Category"])
    df.to_csv("threat_mentions.csv", index=False)

    # Display the results
    for text, category in categorized_threats:
        print(f"Category: {category}, Text: {text[:50]}...")

# Schedule the monitoring to run every hour
schedule.every(1).hours.do(monitor_threats)

if __name__ == "__main__":
    print("Starting Social Media Threat Monitoring Tool...")
    while True:
        schedule.run_pending()
        time.sleep(1)
