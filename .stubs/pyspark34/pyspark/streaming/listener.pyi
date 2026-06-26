from _typeshed import Incomplete
from typing import Any

__all__ = ['StreamingListener']

class StreamingListener:
    def __init__(self) -> None: ...
    def onStreamingStarted(self, streamingStarted: Any) -> None:
        """
        Called when the streaming has been started.
        """
    def onReceiverStarted(self, receiverStarted: Any) -> None:
        """
        Called when a receiver has been started
        """
    def onReceiverError(self, receiverError: Any) -> None:
        """
        Called when a receiver has reported an error
        """
    def onReceiverStopped(self, receiverStopped: Any) -> None:
        """
        Called when a receiver has been stopped
        """
    def onBatchSubmitted(self, batchSubmitted: Any) -> None:
        """
        Called when a batch of jobs has been submitted for processing.
        """
    def onBatchStarted(self, batchSubmitted: Any) -> None:
        """
        Called when processing of a batch of jobs has started.
        """
    def onBatchCompleted(self, batchCompleted: Any) -> None:
        """
        Called when processing of a batch of jobs has completed.
        """
    def onOutputOperationStarted(self, outputOperationStarted: Any) -> None:
        """
        Called when processing of a job of a batch has started.
        """
    def onOutputOperationCompleted(self, outputOperationCompleted: Any) -> None:
        """
        Called when processing of a job of a batch has completed
        """
    class Java:
        implements: Incomplete
