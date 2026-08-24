from _typeshed import Incomplete

class appended_to_syspath:
    """
    Deprecated since IPython 8.1, no replacements.

    A context for appending a directory to sys.path for a second."""
    dir: Incomplete
    def __init__(self, dir) -> None: ...
    added: bool
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...

class prepended_to_syspath:
    """A context for prepending a directory to sys.path for a second."""
    dir: Incomplete
    def __init__(self, dir) -> None: ...
    added: bool
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...
