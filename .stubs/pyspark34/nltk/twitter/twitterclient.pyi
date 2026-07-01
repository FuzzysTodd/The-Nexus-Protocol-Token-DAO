from _typeshed import Incomplete
from collections.abc import Generator
from nltk.twitter.api import BasicTweetHandler as BasicTweetHandler, TweetHandlerI as TweetHandlerI
from nltk.twitter.util import credsfromfile as credsfromfile, guess_path as guess_path
from twython import Twython, TwythonStreamer

class Streamer(TwythonStreamer):
    """
    Retrieve data from the Twitter Streaming API.

    The streaming API requires
    `OAuth 1.0 <https://en.wikipedia.org/wiki/OAuth>`_ authentication.
    """
    handler: Incomplete
    do_continue: bool
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret) -> None: ...
    def register(self, handler) -> None:
        """
        Register a method for handling Tweets.

        :param TweetHandlerI handler: method for viewing
        """
    def on_success(self, data) -> None:
        """
        :param data: response from Twitter API
        """
    def on_error(self, status_code, data) -> None:
        """
        :param status_code: The status code returned by the Twitter API
        :param data: The response from Twitter API

        """
    def sample(self) -> None:
        """
        Wrapper for 'statuses / sample' API call
        """
    def filter(self, track: str = '', follow: str = '', lang: str = 'en') -> None:
        """
        Wrapper for 'statuses / filter' API call
        """

class Query(Twython):
    """
    Retrieve data from the Twitter REST API.
    """
    handler: Incomplete
    do_continue: bool
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret) -> None:
        """
        :param app_key: (optional) Your applications key
        :param app_secret: (optional) Your applications secret key
        :param oauth_token: (optional) When using **OAuth 1**, combined with
            oauth_token_secret to make authenticated calls
        :param oauth_token_secret: (optional) When using **OAuth 1** combined
            with oauth_token to make authenticated calls
        """
    def register(self, handler) -> None:
        """
        Register a method for handling Tweets.

        :param TweetHandlerI handler: method for viewing or writing Tweets to a file.
        """
    def expand_tweetids(self, ids_f, verbose: bool = True):
        """
        Given a file object containing a list of Tweet IDs, fetch the
        corresponding full Tweets from the Twitter API.

        The API call `statuses/lookup` will fail to retrieve a Tweet if the
        user has deleted it.

        This call to the Twitter API is rate-limited. See
        <https://dev.twitter.com/rest/reference/get/statuses/lookup> for details.

        :param ids_f: input file object consisting of Tweet IDs, one to a line
        :return: iterable of Tweet objects in JSON format
        """
    def search_tweets(self, keywords, limit: int = 100, lang: str = 'en', max_id: Incomplete | None = None, retries_after_twython_exception: int = 0) -> Generator[Incomplete, None, None]:
        """
        Call the REST API ``'search/tweets'`` endpoint with some plausible
        defaults. See `the Twitter search documentation
        <https://dev.twitter.com/rest/public/search>`_ for more information
        about admissible search parameters.

        :param str keywords: A list of query terms to search for, written as        a comma-separated string
        :param int limit: Number of Tweets to process
        :param str lang: language
        :param int max_id: id of the last tweet fetched
        :param int retries_after_twython_exception: number of retries when        searching Tweets before raising an exception
        :rtype: python generator
        """
    def user_info_from_id(self, userids):
        """
        Convert a list of userIDs into a variety of information about the users.

        See <https://dev.twitter.com/rest/reference/get/users/show>.

        :param list userids: A list of integer strings corresponding to Twitter userIDs
        :rtype: list(json)
        """
    def user_tweets(self, screen_name, limit, include_rts: str = 'false') -> None:
        """
        Return a collection of the most recent Tweets posted by the user

        :param str user: The user's screen name; the initial '@' symbol        should be omitted
        :param int limit: The number of Tweets to recover; 200 is the maximum allowed
        :param str include_rts: Whether to include statuses which have been        retweeted by the user; possible values are 'true' and 'false'
        """

class Twitter:
    """
    Wrapper class with restricted functionality and fewer options.
    """
    streamer: Incomplete
    query: Incomplete
    def __init__(self) -> None: ...
    def tweets(self, keywords: str = '', follow: str = '', to_screen: bool = True, stream: bool = True, limit: int = 100, date_limit: Incomplete | None = None, lang: str = 'en', repeat: bool = False, gzip_compress: bool = False) -> None:
        """
        Process some Tweets in a simple manner.

        :param str keywords: Keywords to use for searching or filtering
        :param list follow: UserIDs to use for filtering Tweets from the public stream
        :param bool to_screen: If `True`, display the tweet texts on the screen,            otherwise print to a file

        :param bool stream: If `True`, use the live public stream,            otherwise search past public Tweets

        :param int limit: The number of data items to process in the current            round of processing.

        :param tuple date_limit: The date at which to stop collecting            new data. This should be entered as a tuple which can serve as the            argument to `datetime.datetime`.            E.g. `date_limit=(2015, 4, 1, 12, 40)` for 12:30 pm on April 1 2015.
            Note that, in the case of streaming, this is the maximum date, i.e.            a date in the future; if not, it is the minimum date, i.e. a date            in the past

        :param str lang: language

        :param bool repeat: A flag to determine whether multiple files should            be written. If `True`, the length of each file will be set by the            value of `limit`. Use only if `to_screen` is `False`. See also
            :py:func:`handle`.

        :param gzip_compress: if `True`, output files are compressed with gzip.
        """

class TweetViewer(TweetHandlerI):
    """
    Handle data by sending it to the terminal.
    """
    def handle(self, data) -> None:
        """
        Direct data to `sys.stdout`

        :return: return ``False`` if processing should cease, otherwise return ``True``.
        :rtype: bool
        :param data: Tweet object returned by Twitter API
        """
    def on_finish(self) -> None: ...

class TweetWriter(TweetHandlerI):
    """
    Handle data by writing it to a file.
    """
    fprefix: Incomplete
    subdir: Incomplete
    gzip_compress: Incomplete
    fname: Incomplete
    repeat: Incomplete
    output: Incomplete
    def __init__(self, limit: int = 2000, upper_date_limit: Incomplete | None = None, lower_date_limit: Incomplete | None = None, fprefix: str = 'tweets', subdir: str = 'twitter-files', repeat: bool = False, gzip_compress: bool = False) -> None:
        """
        The difference between the upper and lower date limits depends on
        whether Tweets are coming in an ascending date order (i.e. when
        streaming) or descending date order (i.e. when searching past Tweets).

        :param int limit: number of data items to process in the current        round of processing.

        :param tuple upper_date_limit: The date at which to stop collecting new        data. This should be entered as a tuple which can serve as the        argument to `datetime.datetime`. E.g. `upper_date_limit=(2015, 4, 1, 12,        40)` for 12:30 pm on April 1 2015.

        :param tuple lower_date_limit: The date at which to stop collecting new        data. See `upper_data_limit` for formatting.

        :param str fprefix: The prefix to use in creating file names for Tweet        collections.

        :param str subdir: The name of the directory where Tweet collection        files should be stored.

        :param bool repeat: flag to determine whether multiple files should be        written. If `True`, the length of each file will be set by the value        of `limit`. See also :py:func:`handle`.

        :param gzip_compress: if `True`, output files are compressed with gzip.
        """
    def timestamped_file(self):
        """
        :return: timestamped file name
        :rtype: str
        """
    startingup: bool
    def handle(self, data) -> None:
        """
        Write Twitter data as line-delimited JSON into one or more files.

        :return: return `False` if processing should cease, otherwise return `True`.
        :param data: tweet object returned by Twitter API
        """
    def on_finish(self) -> None: ...
    def do_continue(self): ...
