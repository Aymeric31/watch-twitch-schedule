import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Credentials twitter
twitter_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
twitter_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
twitter_bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
twitch_username = os.environ.get('TWITCH_USERNAME')

def send_tweet(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret, twitter_bearer_token, tweet_text):
    client = tweepy.Client( 
        twitter_bearer_token, 
        twitter_consumer_key, 
        twitter_consumer_secret, 
        twitter_access_token, 
        twitter_access_token_secret, 
        wait_on_rate_limit=True
        )
    # Envoi du tweet
    client.create_tweet(text=tweet_text)

tweet_text = f"Planning à jour ici ! ⬇️ https://www.twitch.tv/{twitch_username}/schedule"

send_tweet(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret, twitter_bearer_token, tweet_text)
