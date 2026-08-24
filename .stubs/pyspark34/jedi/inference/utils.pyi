from _typeshed import Incomplete

def to_list(func): ...
def to_tuple(func): ...
def unite(iterable):
    """Turns a two dimensional array into a one dimensional."""

class UncaughtAttributeError(Exception):
    """
    Important, because `__getattr__` and `hasattr` catch AttributeErrors
    implicitly. This is really evil (mainly because of `__getattr__`).
    Therefore this class originally had to be derived from `BaseException`
    instead of `Exception`.  But because I removed relevant `hasattr` from
    the code base, we can now switch back to `Exception`.

    :param base: return values of sys.exc_info().
    """

def safe_property(func): ...
def reraise_uncaught(func):
    '''
    Re-throw uncaught `AttributeError`.

    Usage:  Put ``@rethrow_uncaught`` in front of the function
    which does **not** suppose to raise `AttributeError`.

    AttributeError is easily get caught by `hasattr` and another
    ``except AttributeError`` clause.  This becomes problem when you use
    a lot of "dynamic" attributes (e.g., using ``@property``) because you
    can\'t distinguish if the property does not exist for real or some code
    inside of the "dynamic" attribute through that error.  In a well
    written code, such error should not exist but getting there is very
    difficult.  This decorator is to help us getting there by changing
    `AttributeError` to `UncaughtAttributeError` to avoid unexpected catch.
    This helps us noticing bugs earlier and facilitates debugging.
    '''

class PushBackIterator:
    pushes: Incomplete
    iterator: Incomplete
    current: Incomplete
    def __init__(self, iterator) -> None: ...
    def push_back(self, value) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
