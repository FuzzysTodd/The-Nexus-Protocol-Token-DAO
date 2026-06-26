from _typeshed import Incomplete

__all__ = ['handler']

def handler(event_class, handler_: Incomplete | None = None, _decorator: bool = False):
    """ Define an event handler for a (new-style) class.

    This can be called with a class and a handler, or with just a
    class and the result used as a handler decorator.
    """
