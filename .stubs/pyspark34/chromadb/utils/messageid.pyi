import pulsar
from _typeshed import Incomplete

def pulsar_to_int(message_id: pulsar.MessageId) -> int: ...
def int_to_pulsar(message_id: int) -> pulsar.MessageId: ...
def int_to_bytes(int: int) -> bytes:
    """Convert int to a 24 byte big endian byte string"""
def bytes_to_int(bytes: bytes) -> int:
    """Convert a 24 byte big endian byte string to an int"""

base85: Incomplete

def int_to_str(n: int) -> str: ...
def str_to_int(s: str) -> int: ...
