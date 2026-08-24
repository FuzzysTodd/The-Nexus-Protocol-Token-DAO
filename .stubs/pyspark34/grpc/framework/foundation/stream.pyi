import abc

class Consumer(abc.ABC, metaclass=abc.ABCMeta):
    """Interface for consumers of finite streams of values or objects."""
    @abc.abstractmethod
    def consume(self, value):
        """Accepts a value.

    Args:
      value: Any value accepted by this Consumer.
    """
    @abc.abstractmethod
    def terminate(self):
        """Indicates to this Consumer that no more values will be supplied."""
    @abc.abstractmethod
    def consume_and_terminate(self, value):
        """Supplies a value and signals that no more values will be supplied.

    Args:
      value: Any value accepted by this Consumer.
    """
