from _plotly_utils.utils import *
from _plotly_utils.data_utils import *
from _typeshed import Incomplete
from collections.abc import Generator
from pprint import PrettyPrinter

class ElidedWrapper:
    """
    Helper class that wraps values of certain types and produces a custom
    __repr__() that may be elided and is suitable for use during pretty
    printing
    """
    v: Incomplete
    indent: Incomplete
    threshold: Incomplete
    def __init__(self, v, threshold, indent) -> None: ...
    @staticmethod
    def is_wrappable(v): ...

class ElidedPrettyPrinter(PrettyPrinter):
    """
    PrettyPrinter subclass that elides long lists/arrays/strings
    """
    threshold: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

def node_generator(node, path=()) -> Generator[Incomplete, None, None]:
    """
    General, node-yielding generator.

    Yields (node, path) tuples when it finds values that are dict
    instances.

    A path is a sequence of hashable values that can be used as either keys to
    a mapping (dict) or indices to a sequence (list). A path is always wrt to
    some object. Given an object, a path explains how to get from the top level
    of that object to a nested value in the object.

    :param (dict) node: Part of a dict to be traversed.
    :param (tuple[str]) path: Defines the path of the current node.
    :return: (Generator)

    Example:

        >>> for node, path in node_generator({'a': {'b': 5}}):
        ...     print(node, path)
        {'a': {'b': 5}} ()
        {'b': 5} ('a',)

    """
def get_by_path(obj, path):
    """
    Iteratively get on obj for each key in path.

    :param (list|dict) obj: The top-level object.
    :param (tuple[str]|tuple[int]) path: Keys to access parts of obj.

    :return: (*)

    Example:

        >>> figure = {'data': [{'x': [5]}]}
        >>> path = ('data', 0, 'x')
        >>> get_by_path(figure, path)
        [5]
    """
def decode_unicode(coll): ...
