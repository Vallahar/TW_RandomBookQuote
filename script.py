# -*- coding: utf-8 -*-
import tweepy
from key import consumer_key, consumer_secret, access_token, access_token_secret
from random import randrange

# 'key' is a file with the API authentication tokens and keys, which
# isn't in the repository to protect the integrity of the account.

# Constants 'for readability' (I just kinda like to do this, I reckon is niche)
INTRO = 0
LEGENDS = 1
LETTERS = 2
POEMS = 3
CHAR_LIMIT = 240

# Function generating the actual tweet text
def generate(fileName):
    fd = open(fileName, "r")
    content = fd.read()

    content = content.split(".")

    while(True):
        tweet = content[randrange(len(content))].strip()
        if (len(tweet) <= CHAR_LIMIT and tweet.strip() != ""):
            break

    return tweet

# Function that decides the source of the tweet
def tweet():
    choice = randrange(4)

    if (choice == INTRO):
        tweet = generate("sources/intro.txt")
    elif (choice == LEGENDS):
        tweet = generate("sources/legends.txt")
    elif (choice == LETTERS):
        tweet = generate("sources/letters.txt")
    elif (choice == POEMS):
        tweet = generate("sources/poems.txt")

    return tweet

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Object
api = tweepy.API(auth)

# Tweet sender
api.update_status(tweet())
