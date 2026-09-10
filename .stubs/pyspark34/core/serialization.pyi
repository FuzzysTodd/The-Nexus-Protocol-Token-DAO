from _typeshed import Incomplete
from json import JSONEncoder
from typing import Any

__all__ = ['NULL', 'AzureJSONEncoder']

class _Null:
    """To create a Falsy object"""
    def __bool__(self) -> bool: ...

NULL: Incomplete

class AzureJSONEncoder(JSONEncoder):
    """A JSON encoder that's capable of serializing datetime objects and bytes."""
    def default(self, o: Any) -> Any: ...
