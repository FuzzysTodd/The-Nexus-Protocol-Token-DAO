from _typeshed import Incomplete

numberTypes: Incomplete

def deprecated(msg: str = ''):
    '''Decorator factory to mark functions as deprecated with given message.

    >>> @deprecated("Enough!")
    ... def some_function():
    ...    "I just print \'hello world\'."
    ...    print("hello world")
    >>> some_function()
    hello world
    >>> some_function.__doc__ == "I just print \'hello world\'."
    True
    '''

class _VersionTupleEnumMixin:
    @property
    def major(self): ...
    @property
    def minor(self): ...
    @classmethod
    def default(cls): ...
    @classmethod
    def supported_versions(cls): ...
