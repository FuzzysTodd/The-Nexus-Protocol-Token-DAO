from _typeshed import Incomplete
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from typing import Any, Iterable, Mapping, Set

__all__ = ['NestedCompleter']

NestedDict = Mapping[str, Any | Set[str] | None | Completer]

class NestedCompleter(Completer):
    """
    Completer which wraps around several other completers, and calls any the
    one that corresponds with the first word of the input.

    By combining multiple `NestedCompleter` instances, we can achieve multiple
    hierarchical levels of autocompletion. This is useful when `WordCompleter`
    is not sufficient.

    If you need multiple levels, check out the `from_nested_dict` classmethod.
    """
    options: Incomplete
    ignore_case: Incomplete
    def __init__(self, options: dict[str, Completer | None], ignore_case: bool = True) -> None: ...
    @classmethod
    def from_nested_dict(cls, data: NestedDict) -> NestedCompleter:
        """
        Create a `NestedCompleter`, starting from a nested dictionary data
        structure, like this:

        .. code::

            data = {
                'show': {
                    'version': None,
                    'interfaces': None,
                    'clock': None,
                    'ip': {'interface': {'brief'}}
                },
                'exit': None
                'enable': None
            }

        The value should be `None` if there is no further completion at some
        point. If all values in the dictionary are None, it is also possible to
        use a set instead.

        Values in this data structure can be a completers as well.
        """
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
