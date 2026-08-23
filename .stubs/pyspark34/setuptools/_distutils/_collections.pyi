import collections
from _typeshed import Incomplete

class DictStack(list, collections.abc.Mapping):
    """
    A stack of dictionaries that behaves as a view on those dictionaries,
    giving preference to the last.

    >>> stack = DictStack([dict(a=1, c=2), dict(b=2, a=2)])
    >>> stack['a']
    2
    >>> stack['b']
    2
    >>> stack['c']
    2
    >>> len(stack)
    3
    >>> stack.push(dict(a=3))
    >>> stack['a']
    3
    >>> set(stack.keys()) == set(['a', 'b', 'c'])
    True
    >>> set(stack.items()) == set([('a', 3), ('b', 2), ('c', 2)])
    True
    >>> dict(**stack) == dict(stack) == dict(a=3, c=2, b=2)
    True
    >>> d = stack.pop()
    >>> stack['a']
    2
    >>> d = stack.pop()
    >>> stack['a']
    1
    >>> stack.get('b', None)
    >>> 'c' in stack
    True
    """
    def __iter__(self): ...
    def __getitem__(self, key): ...
    push: Incomplete
    def __contains__(self, other) -> bool: ...
    def __len__(self) -> int: ...

class RangeMap(dict):
    """
    A dictionary-like object that uses the keys as bounds for a range.
    Inclusion of the value for that range is determined by the
    key_match_comparator, which defaults to less-than-or-equal.
    A value is returned for a key if it is the first key that matches in
    the sorted list of keys.

    One may supply keyword parameters to be passed to the sort function used
    to sort keys (i.e. key, reverse) as sort_params.

    Let's create a map that maps 1-3 -> 'a', 4-6 -> 'b'

    >>> r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    Even float values should work so long as the comparison operator
    supports it.

    >>> r[4.5]
    'b'

    But you'll notice that the way rangemap is defined, it must be open-ended
    on one side.

    >>> r[0]
    'a'
    >>> r[-1]
    'a'

    One can close the open-end of the RangeMap by using undefined_value

    >>> r = RangeMap({0: RangeMap.undefined_value, 3: 'a', 6: 'b'})
    >>> r[0]
    Traceback (most recent call last):
    ...
    KeyError: 0

    One can get the first or last elements in the range by using RangeMap.Item

    >>> last_item = RangeMap.Item(-1)
    >>> r[last_item]
    'b'

    .last_item is a shortcut for Item(-1)

    >>> r[RangeMap.last_item]
    'b'

    Sometimes it's useful to find the bounds for a RangeMap

    >>> r.bounds()
    (0, 6)

    RangeMap supports .get(key, default)

    >>> r.get(0, 'not found')
    'not found'

    >>> r.get(7, 'not found')
    'not found'

    One often wishes to define the ranges by their left-most values,
    which requires use of sort params and a key_match_comparator.

    >>> r = RangeMap({1: 'a', 4: 'b'},
    ...     sort_params=dict(reverse=True),
    ...     key_match_comparator=operator.ge)
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    That wasn't nearly as easy as before, so an alternate constructor
    is provided:

    >>> r = RangeMap.left({1: 'a', 4: 'b', 7: RangeMap.undefined_value})
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    """
    sort_params: Incomplete
    match: Incomplete
    def __init__(self, source, sort_params={}, key_match_comparator=...) -> None: ...
    @classmethod
    def left(cls, source): ...
    def __getitem__(self, item): ...
    def get(self, key, default: Incomplete | None = None):
        """
        Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to None, so that this method
        never raises a KeyError.
        """
    def bounds(self): ...
    undefined_value: Incomplete
    class Item(int):
        """RangeMap Item"""
    first_item: Incomplete
    last_item: Incomplete
