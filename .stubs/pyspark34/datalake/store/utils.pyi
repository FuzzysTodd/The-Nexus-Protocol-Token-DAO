from _typeshed import Incomplete

PY2: Incomplete
WIN: Incomplete
datadir: Incomplete

def ensure_writable(b): ...
def write_stdout(data) -> None:
    """ Write bytes or strings to standard output
    """
def read_block(f, offset, length, delimiter: Incomplete | None = None):
    """ Read a block of bytes from a file

    Parameters
    ----------
    fn: file object
        a file object that supports seek, tell and read.
    offset: int
        Byte offset to start read
    length: int
        Maximum number of bytes to read
    delimiter: bytes (optional)
        Ensure reading stops at delimiter bytestring

    If using the ``delimiter=`` keyword argument we ensure that the read
    stops at or before the delimiter boundaries that follow the location
    ``offset + length``. For ADL, if no delimiter is found and the data
    requested is > 4MB an exception is raised, since a single record cannot
    exceed 4MB and be guaranteed to land contiguously in ADL.
    The bytestring returned WILL include the
    terminating delimiter string.

    Examples
    --------

    >>> from io import BytesIO  # doctest: +SKIP
    >>> f = BytesIO(b'Alice, 100\\nBob, 200\\nCharlie, 300')  # doctest: +SKIP
    >>> read_block(f, 0, 13)  # doctest: +SKIP
    b'Alice, 100\\nBo'

    >>> read_block(f, 0, 13, delimiter=b'\\n')  # doctest: +SKIP
    b'Alice, 100\\n'

    >>> read_block(f, 10, 10, delimiter=b'\\n')  # doctest: +SKIP
    b'\\nCharlie, 300'
    >>> f  = BytesIO(bytearray(2**22))  # doctest: +SKIP
    >>> read_block(f,0,2**22, delimiter=b'\\n')  # doctest: +SKIP
    IndexError: No delimiter found within max record size of 4MB. 
    Transfer without specifying a delimiter (as binary) instead.
    """
def tokenize(*args, **kwargs):
    """ Deterministic token

    >>> tokenize('Hello') == tokenize('Hello')
    True
    """
def commonprefix(paths):
    """ Find common directory for all paths

    Python's ``os.path.commonprefix`` will not return a valid directory path in
    some cases, so we wrote this convenience method.

    Examples
    --------

    >>> # os.path.commonprefix returns '/disk1/foo'
    >>> commonprefix(['/disk1/foobar', '/disk1/foobaz'])
    '/disk1'

    >>> commonprefix(['a/b/c', 'a/b/d', 'a/c/d'])
    'a'

    >>> commonprefix(['a/b/c', 'd/e/f', 'g/h/i'])
    ''
    """
def clamp(n, smallest, largest):
    """ Limit a value to a given range

    This is equivalent to smallest <= n <= largest.

    Examples
    --------

    >>> clamp(0, 1, 100)
    1

    >>> clamp(42, 2, 128)
    42

    >>> clamp(1024, 1, 32)
    32
    """

class CountUpDownLatch:
    """CountUpDownLatch provides a thread safe implementation of Up Down latch
    """
    lock: Incomplete
    val: int
    total: int
    def __init__(self) -> None: ...
    def increment(self) -> None: ...
    def decrement(self) -> None: ...
    def total_processed(self): ...
    def is_zero(self): ...
