from .base import CompleteEvent, Completer, Completion
from _typeshed import Incomplete
from prompt_toolkit.document import Document
from typing import Iterable

__all__ = ['DeduplicateCompleter']

class DeduplicateCompleter(Completer):
    """
    Wrapper around a completer that removes duplicates. Only the first unique
    completions are kept.

    Completions are considered to be a duplicate if they result in the same
    document text when they would be applied.
    """
    completer: Incomplete
    def __init__(self, completer: Completer) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
