import tweepy
from key import consumer_key, consumer_secret, access_token, access_token_secret

# 'key' is a file with the API authentication tokens and keys, which
# isn't in the repository to protect the integrity of the account.

# Function that generates the tweet's text
def tweetGeneration():
    # Retrieve the source file
    # Generate a random number and switch the pointer to that line
    # - Poemas
    #   - Retrieve a string up to the next period or verse.
    # - Textos
    #   - Retrieve a string up to the next period. If reached limit, try again.

    return "Bécquer era el puto amo."

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Object
api = tweepy.API(auth)

# Tweet sender
api.update_status(tweetGeneration())
