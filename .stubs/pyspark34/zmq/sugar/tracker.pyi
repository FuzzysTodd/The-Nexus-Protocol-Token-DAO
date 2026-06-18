from _typeshed import Incomplete
from threading import Event
from typing import Set, Tuple
from zmq.backend import Frame

__all__ = ['MessageTracker', '_FINISHED_TRACKER']

class MessageTracker:
    """MessageTracker(*towatch)

    A class for tracking if 0MQ is done using one or more messages.

    When you send a 0MQ message, it is not sent immediately. The 0MQ IO thread
    sends the message at some later time. Often you want to know when 0MQ has
    actually sent the message though. This is complicated by the fact that
    a single 0MQ message can be sent multiple times using different sockets.
    This class allows you to track all of the 0MQ usages of a message.

    Parameters
    ----------
    towatch : Event, MessageTracker, Message instances.
        This objects to track. This class can track the low-level
        Events used by the Message class, other MessageTrackers or
        actual Messages.
    """
    events: Set[Event]
    peers: Set['MessageTracker']
    def __init__(self, *towatch: Tuple[MessageTracker | Event | Frame]) -> None:
        """MessageTracker(*towatch)

        Create a message tracker to track a set of messages.

        Parameters
        ----------
        *towatch : tuple of Event, MessageTracker, Message instances.
            This list of objects to track. This class can track the low-level
            Events used by the Message class, other MessageTrackers or
            actual Messages.
        """
    @property
    def done(self):
        """Is 0MQ completely done with the message(s) being tracked?"""
    def wait(self, timeout: float | int = -1):
        """mt.wait(timeout=-1)

        Wait for 0MQ to be done with the message or until `timeout`.

        Parameters
        ----------
        timeout : float [default: -1, wait forever]
            Maximum time in (s) to wait before raising NotDone.

        Returns
        -------
        None
            if done before `timeout`

        Raises
        ------
        NotDone
            if `timeout` reached before I am done.
        """

_FINISHED_TRACKER: Incomplete
