from _typeshed import Incomplete

__all__ = ['convert', 'get_type']

class TypeData:
    default_type: Incomplete
    as_type: Incomplete
    def __init__(self, default_type, as_type) -> None: ...
    def convert(self, value): ...

class BoolType(TypeData):
    BOOLEAN_STATES: Incomplete
    def convert(self, value): ...

class NoneType(TypeData):
    def convert(self, value): ...

class ListType(TypeData):
    def convert(self, value, flatten: bool = True): ...
    def split_values(self, value):
        """
        Split the provided value into a list.

        First this is done by newlines. If there were no newlines in the text,
        then we next try to split by comma.
        """

def convert(value, as_type, source):
    """Convert the value as a given type where the value comes from the given source."""
def get_type(action): ...
