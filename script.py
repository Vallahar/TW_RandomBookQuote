# -*- coding: utf-8 -*-
import time
from datetime import datetime
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
TIME_TO_WAIT = 1800


def generate(fileName):
    """Generate the actual tweet text"""
    fd = open(fileName, "r")
    content = fd.read()

    content = content.split(".")

    while(True):
        tweet = content[randrange(len(content))].strip()
	# TODO: add a notice when we've run out of original tweets
        if ((len(tweet) + 1) <= CHAR_LIMIT and tweet.strip() != "" and checkDuplicate(tweet) == False):
            break

    # I acknowledge this could be done with regex
    if (tweet[-1] != "!" or tweet[-1] != "?"):
        tweet += "."

    return tweet


def tweet():
    """Picks the tweet's source"""
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


def checkDuplicate(str):
    """Searches for duplicates in the tweetLog"""
    with open('tweetLog.txt') as tweetLog:
        if str in tweetLog.read():
            return True
        else: 
            return False


def writeLog(tweetContent):
    """Writes to the log"""
    fd = open("tweetLog.txt", "a+")
    now = datetime.now()
    string = "Tweet sent on " + now.strftime("%H:%M:%S - %d/%m/%Y (GMT)")
    string += "\n\t" + tweetContent + "\n''''''''''\n"
    fd.write(string)
    fd.close


if __name__ == "__main__":
    while(True):
        # Twitter authentication
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # API Object
        api = tweepy.API(auth)

        # Tweet sender
        newTweet = tweet()
        api.update_status(newTweet)
        writeLog(newTweet)

        # Dirty way to make the script wait 30mins to tweet again
        time.sleep(TIME_TO_WAIT)
