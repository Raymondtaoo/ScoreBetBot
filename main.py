import tweepy
import keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path: str = None):
    if image_path is not None:
        api.update_with_media(message: str, image_path:None):
    else:
        api.update_status(message)

    print('Tweeted Successfully!')

if __name__ == '__main__':
    api = api()
    tweet(api, 'Hello, World!')