import tweepy
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Credentials twitter
twitter_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
twitter_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
twitter_bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

# Discord Server Parameters
discord_webhook = os.environ.get('DISCORD_WEBHOOK')

twitch_username = os.environ.get('TWITCH_USERNAME')
notification_message = f"On maintient le planning de la semaine précédente ! ⬇️ https://www.twitch.tv/{twitch_username}/schedule"

def send_tweet(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret, twitter_bearer_token, notification_message):
    try:
        client = tweepy.Client( 
            twitter_bearer_token, 
            twitter_consumer_key, 
            twitter_consumer_secret, 
            twitter_access_token, 
            twitter_access_token_secret, 
            wait_on_rate_limit=True
            )
        # Sending the tweet
        client.create_tweet(text=notification_message)
        print('Tweet sent successfully.')
    except Exception as e:
        print('Error sending tweet:', str(e))

def send_discord(notification_message):
    # Création du message à envoyer
    message = {
        'content': notification_message
    }

    # Envoi du message via la requête HTTP POST
    response = requests.post(f"https://discord.com/api/webhooks/{discord_webhook}", json=message)

    # Vérification du code de statut de la réponse
    if response.status_code == 204:
        print('Discord notification sent successfully.')
    else:
        print('Failed to send Discord notification.')


send_tweet(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret, twitter_bearer_token, notification_message)
send_discord(notification_message)