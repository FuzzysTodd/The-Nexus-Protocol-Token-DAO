from _typeshed import Incomplete
from py4j.compat import range as range

def make_id(func): ...

NONE_ID: Incomplete

class Signal:
    """Basic signal class that can register receivers (listeners) and dispatch
    events to these receivers.

    As opposed to many signals libraries, receivers are not stored as weak
    references, so it is us to the client application to unregister them.

    Greatly inspired from Django Signals:
    https://github.com/django/django/blob/master/django/dispatch/dispatcher.py
    """
    lock: Incomplete
    receivers: Incomplete
    def __init__(self) -> None: ...
    def connect(self, receiver, sender: Incomplete | None = None, unique_id: Incomplete | None = None) -> None:
        """Registers a receiver for this signal.

        The receiver must be a callable (e.g., function or instance method)
        that accepts named arguments (i.e., ``**kwargs``).

        In case that the connect method might be called multiple time, it is
        best to provide the receiver with a unique id to make sure that the
        receiver is not registered more than once.

        :param receiver: The callable that will receive the signal.
        :param sender: The sender to which the receiver will respond to. If
            None, signals from any sender are sent to this receiver
        :param unique_id: The unique id of the callable to make sure it is not
            registered more than once. Optional.
        """
    def disconnect(self, receiver, sender: Incomplete | None = None, unique_id: Incomplete | None = None):
        """Unregisters a receiver for this signal.

        :param receiver: The callable that was registered to receive the
            signal.
        :param unique_id: The unique id of the callable if it was provided.
            Optional.
        :return: True if the receiver was found and disconnected. False
            otherwise.
        :rtype: bool
        """
    def send(self, sender, **params):
        """Sends the signal to all connected receivers.

        If a receiver raises an error, the error is propagated back and
        interrupts the sending processing. It is thus possible that not all
        receivers will receive the signal.

        :param: named parameters to send to the receivers.
        :param: the sender of the signal. Optional.
        :return: List of (receiver, response) from receivers.
        :rtype: list
        """
