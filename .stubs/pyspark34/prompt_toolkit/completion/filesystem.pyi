from _typeshed import Incomplete
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from typing import Callable, Iterable

__all__ = ['PathCompleter', 'ExecutableCompleter']

class PathCompleter(Completer):
    """
    Complete for Path variables.

    :param get_paths: Callable which returns a list of directories to look into
                      when the user enters a relative path.
    :param file_filter: Callable which takes a filename and returns whether
                        this file should show up in the completion. ``None``
                        when no filtering has to be done.
    :param min_input_len: Don't do autocompletion when the input string is shorter.
    """
    only_directories: Incomplete
    get_paths: Incomplete
    file_filter: Incomplete
    min_input_len: Incomplete
    expanduser: Incomplete
    def __init__(self, only_directories: bool = False, get_paths: Callable[[], list[str]] | None = None, file_filter: Callable[[str], bool] | None = None, min_input_len: int = 0, expanduser: bool = False) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...

class ExecutableCompleter(PathCompleter):
    """
    Complete only executable files in the current path.
    """
    def __init__(self) -> None: ...
