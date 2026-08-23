import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from datetime import tzinfo

class LocalTimezoneOffsetWithUTC(tzinfo, metaclass=abc.ABCMeta):
    """
    This is not intended to be a general purpose class for dealing with the
    local timezone. In particular:

    * it assumes that the date passed has been created using
      `datetime(..., tzinfo=Local)`, where `Local` is an instance of
      the object `LocalTimezoneOffsetWithUTC`;
    * for such an object, it returns the offset with UTC, used for date comparisons.

    Reference: https://docs.python.org/3/library/datetime.html
    """
    STDOFFSET: Incomplete
    DSTOFFSET: Incomplete
    DSTOFFSET = STDOFFSET
    def utcoffset(self, dt):
        """
        Access the relevant time offset.
        """

LOCAL: Incomplete

class BasicTweetHandler(metaclass=ABCMeta):
    """
    Minimal implementation of `TweetHandler`.

    Counts the number of Tweets and decides when the client should stop
    fetching them.
    """
    limit: Incomplete
    counter: int
    do_stop: bool
    max_id: Incomplete
    def __init__(self, limit: int = 20) -> None: ...
    def do_continue(self):
        """
        Returns `False` if the client should stop fetching Tweets.
        """

class TweetHandlerI(BasicTweetHandler, metaclass=abc.ABCMeta):
    """
    Interface class whose subclasses should implement a handle method that
    Twitter clients can delegate to.
    """
    upper_date_limit: Incomplete
    lower_date_limit: Incomplete
    startingup: bool
    def __init__(self, limit: int = 20, upper_date_limit: Incomplete | None = None, lower_date_limit: Incomplete | None = None) -> None:
        """
        :param int limit: The number of data items to process in the current        round of processing.

        :param tuple upper_date_limit: The date at which to stop collecting        new data. This should be entered as a tuple which can serve as the        argument to `datetime.datetime`.        E.g. `date_limit=(2015, 4, 1, 12, 40)` for 12:30 pm on April 1 2015.

        :param tuple lower_date_limit: The date at which to stop collecting        new data. See `upper_data_limit` for formatting.
        """
    @abstractmethod
    def handle(self, data):
        """
        Deal appropriately with data returned by the Twitter API
        """
    @abstractmethod
    def on_finish(self):
        """
        Actions when the tweet limit has been reached
        """
    do_stop: bool
    def check_date_limit(self, data, verbose: bool = False) -> None:
        """
        Validate date limits.
        """
