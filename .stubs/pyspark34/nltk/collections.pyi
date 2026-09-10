from _typeshed import Incomplete
from collections import Counter as Counter, defaultdict as defaultdict, deque as deque
from collections.abc import Generator
from nltk.internals import raise_unorderable_types as raise_unorderable_types, slice_bounds as slice_bounds

class OrderedDict(dict):
    def __init__(self, data: Incomplete | None = None, **kwargs) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __missing__(self, key): ...
    def __setitem__(self, key, item) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def items(self): ...
    def keys(self, data: Incomplete | None = None, keys: Incomplete | None = None): ...
    def popitem(self): ...
    def setdefault(self, key, failobj: Incomplete | None = None) -> None: ...
    def update(self, data) -> None: ...
    def values(self): ...

class AbstractLazySequence:
    """
    An abstract base class for read-only sequences whose values are
    computed as needed.  Lazy sequences act like tuples -- they can be
    indexed, sliced, and iterated over; but they may not be modified.

    The most common application of lazy sequences in NLTK is for
    corpus view objects, which provide access to the contents of a
    corpus without loading the entire corpus into memory, by loading
    pieces of the corpus from disk as needed.

    The result of modifying a mutable element of a lazy sequence is
    undefined.  In particular, the modifications made to the element
    may or may not persist, depending on whether and when the lazy
    sequence caches that element's value or reconstructs it from
    scratch.

    Subclasses are required to define two methods: ``__len__()``
    and ``iterate_from()``.
    """
    def __len__(self) -> int:
        """
        Return the number of tokens in the corpus file underlying this
        corpus view.
        """
    def iterate_from(self, start) -> None:
        """
        Return an iterator that generates the tokens in the corpus
        file underlying this corpus view, starting at the token number
        ``start``.  If ``start>=len(self)``, then this iterator will
        generate no tokens.
        """
    def __getitem__(self, i):
        """
        Return the *i* th token in the corpus file underlying this
        corpus view.  Negative indices and spans are both supported.
        """
    def __iter__(self):
        """Return an iterator that generates the tokens in the corpus
        file underlying this corpus view."""
    def count(self, value):
        """Return the number of times this list contains ``value``."""
    def index(self, value, start: Incomplete | None = None, stop: Incomplete | None = None):
        """Return the index of the first occurrence of ``value`` in this
        list that is greater than or equal to ``start`` and less than
        ``stop``.  Negative start and stop values are treated like negative
        slice bounds -- i.e., they count from the end of the list."""
    def __contains__(self, value) -> bool:
        """Return true if this list contains ``value``."""
    def __add__(self, other):
        """Return a list concatenating self with other."""
    def __radd__(self, other):
        """Return a list concatenating other with self."""
    def __mul__(self, count):
        """Return a list concatenating self with itself ``count`` times."""
    def __rmul__(self, count):
        """Return a list concatenating self with itself ``count`` times."""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self):
        """
        :raise ValueError: Corpus view objects are unhashable.
        """

class LazySubsequence(AbstractLazySequence):
    """
    A subsequence produced by slicing a lazy sequence.  This slice
    keeps a reference to its source sequence, and generates its values
    by looking them up in the source sequence.
    """
    MIN_SIZE: int
    def __new__(cls, source, start, stop):
        """
        Construct a new slice from a given underlying sequence.  The
        ``start`` and ``stop`` indices should be absolute indices --
        i.e., they should not be negative (for indexing from the back
        of a list) or greater than the length of ``source``.
        """
    def __init__(self, source, start, stop) -> None: ...
    def __len__(self) -> int: ...
    def iterate_from(self, start): ...

class LazyConcatenation(AbstractLazySequence):
    """
    A lazy sequence formed by concatenating a list of lists.  This
    underlying list of lists may itself be lazy.  ``LazyConcatenation``
    maintains an index that it uses to keep track of the relationship
    between offsets in the concatenated lists and offsets in the
    sublists.
    """
    def __init__(self, list_of_lists) -> None: ...
    def __len__(self) -> int: ...
    def iterate_from(self, start_index) -> Generator[Incomplete, Incomplete, None]: ...

class LazyMap(AbstractLazySequence):
    """
    A lazy sequence whose elements are formed by applying a given
    function to each element in one or more underlying lists.  The
    function is applied lazily -- i.e., when you read a value from the
    list, ``LazyMap`` will calculate that value by applying its
    function to the underlying lists' value(s).  ``LazyMap`` is
    essentially a lazy version of the Python primitive function
    ``map``.  In particular, the following two expressions are
    equivalent:

        >>> from nltk.collections import LazyMap
        >>> function = str
        >>> sequence = [1,2,3]
        >>> map(function, sequence) # doctest: +SKIP
        ['1', '2', '3']
        >>> list(LazyMap(function, sequence))
        ['1', '2', '3']

    Like the Python ``map`` primitive, if the source lists do not have
    equal size, then the value None will be supplied for the
    'missing' elements.

    Lazy maps can be useful for conserving memory, in cases where
    individual values take up a lot of space.  This is especially true
    if the underlying list's values are constructed lazily, as is the
    case with many corpus readers.

    A typical example of a use case for this class is performing
    feature detection on the tokens in a corpus.  Since featuresets
    are encoded as dictionaries, which can take up a lot of memory,
    using a ``LazyMap`` can significantly reduce memory usage when
    training and running classifiers.
    """
    def __init__(self, function, *lists, **config) -> None:
        """
        :param function: The function that should be applied to
            elements of ``lists``.  It should take as many arguments
            as there are ``lists``.
        :param lists: The underlying lists.
        :param cache_size: Determines the size of the cache used
            by this lazy map.  (default=5)
        """
    def iterate_from(self, index) -> Generator[Incomplete, None, None]: ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...

class LazyZip(LazyMap):
    """
    A lazy sequence whose elements are tuples, each containing the i-th
    element from each of the argument sequences.  The returned list is
    truncated in length to the length of the shortest argument sequence. The
    tuples are constructed lazily -- i.e., when you read a value from the
    list, ``LazyZip`` will calculate that value by forming a tuple from
    the i-th element of each of the argument sequences.

    ``LazyZip`` is essentially a lazy version of the Python primitive function
    ``zip``.  In particular, an evaluated LazyZip is equivalent to a zip:

        >>> from nltk.collections import LazyZip
        >>> sequence1, sequence2 = [1, 2, 3], ['a', 'b', 'c']
        >>> zip(sequence1, sequence2) # doctest: +SKIP
        [(1, 'a'), (2, 'b'), (3, 'c')]
        >>> list(LazyZip(sequence1, sequence2))
        [(1, 'a'), (2, 'b'), (3, 'c')]
        >>> sequences = [sequence1, sequence2, [6,7,8,9]]
        >>> list(zip(*sequences)) == list(LazyZip(*sequences))
        True

    Lazy zips can be useful for conserving memory in cases where the argument
    sequences are particularly long.

    A typical example of a use case for this class is combining long sequences
    of gold standard and predicted values in a classification or tagging task
    in order to calculate accuracy.  By constructing tuples lazily and
    avoiding the creation of an additional long sequence, memory usage can be
    significantly reduced.
    """
    def __init__(self, *lists) -> None:
        """
        :param lists: the underlying lists
        :type lists: list(list)
        """
    def iterate_from(self, index) -> Generator[Incomplete, None, None]: ...
    def __len__(self) -> int: ...

class LazyEnumerate(LazyZip):
    """
    A lazy sequence whose elements are tuples, each containing a count (from
    zero) and a value yielded by underlying sequence.  ``LazyEnumerate`` is
    useful for obtaining an indexed list. The tuples are constructed lazily
    -- i.e., when you read a value from the list, ``LazyEnumerate`` will
    calculate that value by forming a tuple from the count of the i-th
    element and the i-th element of the underlying sequence.

    ``LazyEnumerate`` is essentially a lazy version of the Python primitive
    function ``enumerate``.  In particular, the following two expressions are
    equivalent:

        >>> from nltk.collections import LazyEnumerate
        >>> sequence = ['first', 'second', 'third']
        >>> list(enumerate(sequence))
        [(0, 'first'), (1, 'second'), (2, 'third')]
        >>> list(LazyEnumerate(sequence))
        [(0, 'first'), (1, 'second'), (2, 'third')]

    Lazy enumerations can be useful for conserving memory in cases where the
    argument sequences are particularly long.

    A typical example of a use case for this class is obtaining an indexed
    list for a long sequence of values.  By constructing tuples lazily and
    avoiding the creation of an additional long sequence, memory usage can be
    significantly reduced.
    """
    def __init__(self, lst) -> None:
        """
        :param lst: the underlying list
        :type lst: list
        """

class LazyIteratorList(AbstractLazySequence):
    """
    Wraps an iterator, loading its elements on demand
    and making them subscriptable.
    __repr__ displays only the first few elements.
    """
    def __init__(self, it, known_len: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def iterate_from(self, start) -> Generator[Incomplete, None, None]:
        """Create a new iterator over this list starting at the given offset."""
    def __add__(self, other):
        """Return a list concatenating self with other."""
    def __radd__(self, other):
        """Return a list concatenating other with self."""

class Trie(dict):
    """A Trie implementation for strings"""
    LEAF: bool
    def __init__(self, strings: Incomplete | None = None) -> None:
        """Builds a Trie object, which is built around a ``dict``

        If ``strings`` is provided, it will add the ``strings``, which
        consist of a ``list`` of ``strings``, to the Trie.
        Otherwise, it'll construct an empty Trie.

        :param strings: List of strings to insert into the trie
            (Default is ``None``)
        :type strings: list(str)

        """
    def insert(self, string) -> None:
        '''Inserts ``string`` into the Trie

        :param string: String to insert into the trie
        :type string: str

        :Example:

        >>> from nltk.collections import Trie
        >>> trie = Trie(["abc", "def"])
        >>> expected = {\'a\': {\'b\': {\'c\': {True: None}}},                         \'d\': {\'e\': {\'f\': {True: None}}}}
        >>> trie == expected
        True

        '''
    def __missing__(self, key): ...
