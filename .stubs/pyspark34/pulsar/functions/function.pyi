import abc
from abc import abstractmethod

class Function(metaclass=abc.ABCMeta):
    """Interface for Pulsar Function"""
    @abstractmethod
    def process(self, input, context):
        """Process input message"""
