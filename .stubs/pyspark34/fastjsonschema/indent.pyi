from _typeshed import Incomplete

def indent(func):
    """
    Decorator for allowing to use method as normal method or with
    context manager for auto-indenting code blocks.
    """

class Indent:
    instance: Incomplete
    line: Incomplete
    def __init__(self, instance, line) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
