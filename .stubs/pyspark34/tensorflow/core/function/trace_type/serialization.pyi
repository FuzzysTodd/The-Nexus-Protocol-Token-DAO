import abc
from _typeshed import Incomplete
from google.protobuf import message as message
from tensorflow.core.function.trace_type import serialization_pb2 as serialization_pb2
from typing import Type

SerializedTraceType: Incomplete
PROTO_CLASS_TO_PY_CLASS: Incomplete

class Serializable(metaclass=abc.ABCMeta):
    """TraceTypes implementing this additional interface are portable."""
    @classmethod
    @abc.abstractmethod
    def experimental_type_proto(cls) -> Type[message.Message]:
        """Returns the unique type of proto associated with this class."""
    @classmethod
    @abc.abstractmethod
    def experimental_from_proto(cls, proto: message.Message) -> Serializable:
        """Returns an instance based on a proto."""
    @abc.abstractmethod
    def experimental_as_proto(self) -> message.Message:
        """Returns a proto representing this instance."""

def register_serializable(cls):
    """Registers a Python class to support serialization.

  Only register standard TF types. Custom types should NOT be registered.

  Args:
    cls: Python class to register.
  """
def serialize(to_serialize: Serializable) -> SerializedTraceType:
    """Converts Serializable to a proto SerializedTraceType."""
def deserialize(proto: SerializedTraceType) -> Serializable:
    """Converts a proto SerializedTraceType to instance of Serializable."""
