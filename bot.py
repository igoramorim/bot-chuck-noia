import os
import tweepy
import requests
from secrets import *
from time import gmtime, strftime


BOT_NAME = 'chuck_noia'
LOGFILE_NAME = BOT_NAME + ".log"

TWEET_MAX_LENGTH = 280

API_URL = 'https://api.chucknorris.io/jokes/random'
HASHTAG = ' #ChuckNorris'


def create_tweet():
    """Create the text of the tweet you want to send."""
    text = get_joke()
    if (text):
        tweet(text + HASHTAG)


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.response.message)
    else:
        log("Tweeted: " + text)


def get_joke():
    """Request a joke to the API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        joke = response.json()['value']
        # Make sure the joke length is valid for a tweet
        if (len(joke) < TWEET_MAX_LENGTH):
            return joke
        else:
            get_joke()
    except requests.exceptions.RequestException as e:
        log(str(e))


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, LOGFILE_NAME), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


def teste():
    print('Heello!')
    

# if __name__ == "__main__":
#     create_tweet()