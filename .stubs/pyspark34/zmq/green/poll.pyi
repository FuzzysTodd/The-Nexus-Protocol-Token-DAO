from zmq import Poller as _original_Poller

class _Poller(_original_Poller):
    """Replacement for :class:`zmq.Poller`

    Ensures that the greened Poller below is used in calls to
    :meth:`zmq.Poller.poll`.
    """
    def poll(self, timeout: int = -1):
        """Overridden method to ensure that the green version of
        Poller is used.

        Behaves the same as :meth:`zmq.core.Poller.poll`
        """
