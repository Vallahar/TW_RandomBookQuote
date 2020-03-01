# -*- coding: utf-8 -*-
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

# Function generating the actual tweet text
def generate(fileName):
    fd = open(fileName, "r")
    content = fd.read()

    content = content.split(".")

    while(True):
        tweet = content[randrange(len(content))].strip()
        if ((len(tweet) + 1) <= CHAR_LIMIT and tweet.strip() != "" and checkDuplicate(tweet) == False):
            break

    # I acknowledge this could be done with regex
    if (tweet[-1] != "!" or tweet[-1] != "?"):
        tweet += "."

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

# Function that searches for duplicates in the tweetLog
def checkDuplicate(str):
    with open('tweetLog.txt') as tweetLog:
        if str in tweetLog.read():
            return True
        else: 
            return False

def writeLog(tweetContent):
    fd = open("tweetLog.txt", "a+")
    now = datetime.now()
    string = "Tweet sent on " + now.strftime("%H:%M:%S - %d/%m/%Y (GMT)")
    string += "\n\t" + tweetContent + "\n''''''''''\n"
    fd.write(string)
    fd.close


# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Object
api = tweepy.API(auth)

# Tweet sender
newTweet = tweet()
api.update_status(newTweet)
writeLog(newTweet)

# Success notice to be redirected to a log file (a bit dirty, I know)
print("# Success")
