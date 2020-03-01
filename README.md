# Random Book Quotes
Test of a bot that tweets random quotes.

Hosted on Google Cloud.

Programmed in python using tweepy.

**Important:** To run the script, one has first to activate the virtual environment typing `source ./venv/bin/activate`.

Then just executing `python script.py` will do.

Otherwise, the `tweepy` module might not be recognized.

## Logic for the extraction
* One of the 4 source files is selected. They have been generated from the original text.
* The text is split at any period encountered.
* A random phrase is selected, if it's tweetable, we're up to go

### TO DO:
* Hone the method of obtaining the quotes
* Check if I run into problems of tweeting already existing quotes

### Links
[Creating a Tweeter bot tutorial](https://realpython.com/twitter-bot-python-tweepy/)

[Executing a python script from Google Cloud](https://www.youtube.com/watch?v=5OL7fu2R4M8&t=3s)

[Project Gutenberg Source file](http://www.gutenberg.org/cache/epub/53552/pg53552.txt)
