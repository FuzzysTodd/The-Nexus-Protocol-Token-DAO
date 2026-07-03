from _typeshed import Incomplete
from nltk.twitter import Query as Query, Streamer as Streamer, TweetViewer as TweetViewer, TweetWriter as TweetWriter, Twitter as Twitter, credsfromfile as credsfromfile

SPACER: str

def verbose(func):
    """Decorator for demo functions"""
def yesterday():
    """
    Get yesterday's datetime as a 5-tuple.
    """
def setup() -> None:
    """
    Initialize global variables for the demos.
    """
def twitterclass_demo() -> None:
    """
    Use the simplified :class:`Twitter` class to write some tweets to a file.
    """
def sampletoscreen_demo(limit: int = 20) -> None:
    """
    Sample from the Streaming API and send output to terminal.
    """
def tracktoscreen_demo(track: str = 'taylor swift', limit: int = 10) -> None:
    """
    Track keywords from the public Streaming API and send output to terminal.
    """
def search_demo(keywords: str = 'nltk') -> None:
    """
    Use the REST API to search for past tweets containing a given keyword.
    """
def tweets_by_user_demo(user: str = 'NLTK_org', count: int = 200) -> None:
    """
    Use the REST API to search for past tweets by a given user.
    """
def lookup_by_userid_demo() -> None:
    """
    Use the REST API to convert a userID to a screen name.
    """
def followtoscreen_demo(limit: int = 10) -> None:
    """
    Using the Streaming API, select just the tweets from a specified list of
    userIDs.

    This is will only give results in a reasonable time if the users in
    question produce a high volume of tweets, and may even so show some delay.
    """
def streamtofile_demo(limit: int = 20) -> None:
    """
    Write 20 tweets sampled from the public Streaming API to a file.
    """
def limit_by_time_demo(keywords: str = 'nltk') -> None:
    """
    Query the REST API for Tweets about NLTK since yesterday and send
    the output to terminal.

    This example makes the assumption that there are sufficient Tweets since
    yesterday for the date to be an effective cut-off.
    """
def corpusreader_demo() -> None:
    """
    Use `TwitterCorpusReader` tp read a file of tweets, and print out

    * some full tweets in JSON format;
    * some raw strings from the tweets (i.e., the value of the `text` field); and
    * the result of tokenising the raw strings.

    """
def expand_tweetids_demo() -> None:
    """
    Given a file object containing a list of Tweet IDs, fetch the
    corresponding full Tweets, if available.

    """

ALL: Incomplete
DEMOS: Incomplete
