from _typeshed import Incomplete

__all__ = ['PatsyError']

class PatsyError(Exception):
    """This is the main error type raised by Patsy functions.

    In addition to the usual Python exception features, you can pass a second
    argument to this function specifying the origin of the error; this is
    included in any error message, and used to help the user locate errors
    arising from malformed formulas. This second argument should be an
    :class:`Origin` object, or else an arbitrary object with a ``.origin``
    attribute. (If it is neither of these things, then it will simply be
    ignored.)

    For ordinary display to the user with default formatting, use
    ``str(exc)``. If you want to do something cleverer, you can use the
    ``.message`` and ``.origin`` attributes directly. (The latter may be
    None.)
    """
    message: Incomplete
    origin: Incomplete
    def __init__(self, message, origin: Incomplete | None = None) -> None: ...
    def set_origin(self, origin) -> None: ...
