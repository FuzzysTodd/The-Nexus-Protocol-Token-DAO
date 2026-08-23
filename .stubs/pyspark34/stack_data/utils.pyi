import ast
from _typeshed import Incomplete
from asttokens import ASTText as ASTText
from collections.abc import Generator
from types import FrameType, TracebackType
from typing import Callable, Iterable, Iterator, List, Mapping, Tuple, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def truncate(seq, max_length: int, middle): ...
def unique_in_order(it: Iterable[T]) -> List[T]: ...
def line_range(atok: ASTText, node: ast.AST) -> Tuple[int, int]:
    """
    Returns a pair of numbers representing a half open range
    (i.e. suitable as arguments to the `range()` builtin)
    of line numbers of the given AST nodes.
    """
def highlight_unique(lst: List[T]) -> Iterator[Tuple[T, bool]]: ...
def identity(x: T) -> T: ...
def collapse_repeated(lst, *, collapser, mapper=..., key=...) -> Generator[Incomplete, Incomplete, Incomplete]: ...
def is_frame(frame_or_tb: FrameType | TracebackType) -> bool: ...
def iter_stack(frame_or_tb: FrameType | TracebackType) -> Iterator[FrameType | TracebackType]: ...
def frame_and_lineno(frame_or_tb: FrameType | TracebackType) -> Tuple[FrameType, int]: ...
def group_by_key_func(iterable: Iterable[T], key_func: Callable[[T], R]) -> Mapping[R, List[T]]:
    '''
    Create a dictionary from an iterable such that the keys are the result of evaluating a key function on elements
    of the iterable and the values are lists of elements all of which correspond to the key.

    >>> def si(d): return sorted(d.items())
    >>> si(group_by_key_func("a bb ccc d ee fff".split(), len))
    [(1, [\'a\', \'d\']), (2, [\'bb\', \'ee\']), (3, [\'ccc\', \'fff\'])]
    >>> si(group_by_key_func([-1, 0, 1, 3, 6, 8, 9, 2], lambda x: x % 2))
    [(0, [0, 6, 8, 2]), (1, [-1, 1, 3, 9])]
    '''

class cached_property:
    """
    A property that is only computed once per instance and then replaces itself
    with an ordinary attribute. Deleting the attribute resets the property.

    Based on https://github.com/pydanny/cached-property/blob/master/cached_property.py
    """
    __doc__: Incomplete
    func: Incomplete
    def __init__(self, func) -> None: ...
    def cached_property_wrapper(self, obj, _cls): ...
    __get__ = cached_property_wrapper

def assert_(condition, error: str = '') -> None: ...
def some_str(value): ...
