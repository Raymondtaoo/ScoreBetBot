import tweepy
import keys

client = tweepy.Client(consumer_key = keys.api_key,
                    consumer_secret = keys.api_secret,
                    access_token = keys.access_token,
                    access_token_secret = keys.access_token_secret)

response = client.create_tweet(text='hello world')