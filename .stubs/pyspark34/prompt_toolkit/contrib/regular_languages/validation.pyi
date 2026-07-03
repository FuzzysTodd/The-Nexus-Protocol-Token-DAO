from .compiler import _CompiledGrammar
from _typeshed import Incomplete
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator

__all__ = ['GrammarValidator']

class GrammarValidator(Validator):
    """
    Validator which can be used for validation according to variables in
    the grammar. Each variable can have its own validator.

    :param compiled_grammar: `GrammarCompleter` instance.
    :param validators: `dict` mapping variable names of the grammar to the
                       `Validator` instances to be used for each variable.
    """
    compiled_grammar: Incomplete
    validators: Incomplete
    def __init__(self, compiled_grammar: _CompiledGrammar, validators: dict[str, Validator]) -> None: ...
    def validate(self, document: Document) -> None: ...
