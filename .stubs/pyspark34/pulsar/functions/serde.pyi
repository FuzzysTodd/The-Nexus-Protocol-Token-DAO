import abc
from abc import abstractmethod

class SerDe(metaclass=abc.ABCMeta):
    """Interface for Serialization/Deserialization"""
    @abstractmethod
    def serialize(self, input):
        """Serialize input message into bytes"""
    @abstractmethod
    def deserialize(self, input_bytes):
        """Serialize input_bytes into an object"""

class PickleSerDe(SerDe):
    """Pickle based serializer"""
    def serialize(self, input): ...
    def deserialize(self, input_bytes): ...

class IdentitySerDe(SerDe):
    """Simple Serde that just conversion to string and back"""
    def __init__(self) -> None: ...
    def serialize(self, input): ...
    def deserialize(self, input_bytes): ...
