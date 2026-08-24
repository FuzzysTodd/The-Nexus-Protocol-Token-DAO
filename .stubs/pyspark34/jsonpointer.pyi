from _typeshed import Incomplete

__version__: str
__website__: str
str = unicode
encode_str: Incomplete
izip = zip

def set_pointer(doc, pointer, value, inplace: bool = True):
    """Resolves pointer against doc and sets the value of the target within doc.

    With inplace set to true, doc is modified as long as pointer is not the
    root.

    >>> obj = {'foo': {'anArray': [ {'prop': 44}], 'another prop': {'baz': 'A string' }}}

    >>> set_pointer(obj, '/foo/anArray/0/prop', 55) ==     {'foo': {'another prop': {'baz': 'A string'}, 'anArray': [{'prop': 55}]}}
    True

    >>> set_pointer(obj, '/foo/yet another prop', 'added prop') ==     {'foo': {'another prop': {'baz': 'A string'}, 'yet another prop': 'added prop', 'anArray': [{'prop': 55}]}}
    True

    >>> obj = {'foo': {}}
    >>> set_pointer(obj, '/foo/a%20b', 'x') ==     {'foo': {'a%20b': 'x' }}
    True
    """
def resolve_pointer(doc, pointer, default=...):
    """ Resolves pointer against doc and returns the referenced object

    >>> obj = {'foo': {'anArray': [ {'prop': 44}], 'another prop': {'baz': 'A string' }}, 'a%20b': 1, 'c d': 2}

    >>> resolve_pointer(obj, '') == obj
    True

    >>> resolve_pointer(obj, '/foo') == obj['foo']
    True

    >>> resolve_pointer(obj, '/foo/another prop') == obj['foo']['another prop']
    True

    >>> resolve_pointer(obj, '/foo/another prop/baz') == obj['foo']['another prop']['baz']
    True

    >>> resolve_pointer(obj, '/foo/anArray/0') == obj['foo']['anArray'][0]
    True

    >>> resolve_pointer(obj, '/some/path', None) == None
    True

    >>> resolve_pointer(obj, '/a b', None) == None
    True

    >>> resolve_pointer(obj, '/a%20b') == 1
    True

    >>> resolve_pointer(obj, '/c d') == 2
    True

    >>> resolve_pointer(obj, '/c%20d', None) == None
    True
    """
def pairwise(iterable):
    """ Transforms a list to a list of tuples of adjacent items

    s -> (s0,s1), (s1,s2), (s2, s3), ...

    >>> list(pairwise([]))
    []

    >>> list(pairwise([1]))
    []

    >>> list(pairwise([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    """

class JsonPointerException(Exception): ...

class EndOfList:
    '''Result of accessing element "-" of a list'''
    list_: Incomplete
    def __init__(self, list_) -> None: ...

class JsonPointer:
    """A JSON Pointer that can reference parts of a JSON document"""
    parts: Incomplete
    def __init__(self, pointer) -> None: ...
    def to_last(self, doc):
        """Resolves ptr until the last step, returns (sub-doc, last-step)"""
    def resolve(self, doc, default=...):
        """Resolves the pointer against doc and returns the referenced object"""
    get = resolve
    def set(self, doc, value, inplace: bool = True):
        """Resolve the pointer against the doc and replace the target with value."""
    @classmethod
    def get_part(cls, doc, part):
        """Returns the next step in the correct type"""
    def get_parts(self):
        """Returns the list of the parts. For example, JsonPointer('/a/b').get_parts() == ['a', 'b']"""
    def walk(self, doc, part):
        """ Walks one step in doc and returns the referenced part """
    def contains(self, ptr):
        """ Returns True if self contains the given ptr """
    def __contains__(self, item) -> bool:
        """ Returns True if self contains the given ptr """
    def join(self, suffix):
        """ Returns a new JsonPointer with the given suffix append to this ptr """
    def __truediv__(self, suffix): ...
    __div__ = __truediv__
    @property
    def path(self):
        """Returns the string representation of the pointer

        >>> ptr = JsonPointer('/~0/0/~1').path == '/~0/0/~1'
        """
    def __eq__(self, other):
        """Compares a pointer to another object

        Pointers can be compared by comparing their strings (or splitted
        strings), because no two different parts can point to the same
        structure in an object (eg no different number representations)
        """
    def __hash__(self): ...
    @classmethod
    def from_parts(cls, parts):
        """Constructs a JsonPointer from a list of (unescaped) paths

        >>> JsonPointer.from_parts(['a', '~', '/', 0]).path == '/a/~0/~1/0'
        True
        """

def escape(s): ...
def unescape(s): ...
