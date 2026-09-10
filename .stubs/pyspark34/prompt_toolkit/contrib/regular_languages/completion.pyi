from .compiler import _CompiledGrammar
from _typeshed import Incomplete
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from typing import Iterable

__all__ = ['GrammarCompleter']

class GrammarCompleter(Completer):
    """
    Completer which can be used for autocompletion according to variables in
    the grammar. Each variable can have a different autocompleter.

    :param compiled_grammar: `GrammarCompleter` instance.
    :param completers: `dict` mapping variable names of the grammar to the
                       `Completer` instances to be used for each variable.
    """
    compiled_grammar: Incomplete
    completers: Incomplete
    def __init__(self, compiled_grammar: _CompiledGrammar, completers: dict[str, Completer]) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
