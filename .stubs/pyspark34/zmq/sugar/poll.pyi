from typing import Any, List, Tuple

__all__ = ['Poller', 'select']

class Poller:
    """A stateful poll interface that mirrors Python's built-in poll."""
    sockets: List[Tuple[Any, int]]
    def __init__(self) -> None: ...
    def __contains__(self, socket: Any) -> bool: ...
    def register(self, socket: Any, flags: int = ...):
        """p.register(socket, flags=POLLIN|POLLOUT)

        Register a 0MQ socket or native fd for I/O monitoring.

        register(s,0) is equivalent to unregister(s).

        Parameters
        ----------
        socket : zmq.Socket or native socket
            A zmq.Socket or any Python object having a ``fileno()``
            method that returns a valid file descriptor.
        flags : int
            The events to watch for.  Can be POLLIN, POLLOUT or POLLIN|POLLOUT.
            If `flags=0`, socket will be unregistered.
        """
    def modify(self, socket, flags=...) -> None:
        """Modify the flags for an already registered 0MQ socket or native fd."""
    def unregister(self, socket: Any):
        """Remove a 0MQ socket or native fd for I/O monitoring.

        Parameters
        ----------
        socket : Socket
            The socket instance to stop polling.
        """
    def poll(self, timeout: int | None = None) -> List[Tuple[Any, int]]:
        """Poll the registered 0MQ or native fds for I/O.

        If there are currently events ready to be processed, this function will return immediately.
        Otherwise, this function will return as soon the first event is available or after timeout
        milliseconds have elapsed.

        Parameters
        ----------
        timeout : int
            The timeout in milliseconds. If None, no `timeout` (infinite). This
            is in milliseconds to be compatible with ``select.poll()``.

        Returns
        -------
        events : list of tuples
            The list of events that are ready to be processed.
            This is a list of tuples of the form ``(socket, event_mask)``, where the 0MQ Socket
            or integer fd is the first element, and the poll event mask (POLLIN, POLLOUT) is the second.
            It is common to call ``events = dict(poller.poll())``,
            which turns the list of tuples into a mapping of ``socket : event_mask``.
        """

def select(rlist: List, wlist: List, xlist: List, timeout: float | None = None):
    """select(rlist, wlist, xlist, timeout=None) -> (rlist, wlist, xlist)

    Return the result of poll as a lists of sockets ready for r/w/exception.

    This has the same interface as Python's built-in ``select.select()`` function.

    Parameters
    ----------
    timeout : float, int, optional
        The timeout in seconds. If None, no timeout (infinite). This is in seconds to be
        compatible with ``select.select()``.
    rlist : list of sockets/FDs
        sockets/FDs to be polled for read events
    wlist : list of sockets/FDs
        sockets/FDs to be polled for write events
    xlist : list of sockets/FDs
        sockets/FDs to be polled for error events

    Returns
    -------
    (rlist, wlist, xlist) : tuple of lists of sockets (length 3)
        Lists correspond to sockets available for read/write/error events respectively.
    """
