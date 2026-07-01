from .base import CompleteEvent, Completer, Completion
from _typeshed import Incomplete
from prompt_toolkit.document import Document
from prompt_toolkit.filters import FilterOrBool
from typing import Callable, Iterable, NamedTuple

__all__ = ['FuzzyCompleter', 'FuzzyWordCompleter']

class FuzzyCompleter(Completer):
    '''
    Fuzzy completion.
    This wraps any other completer and turns it into a fuzzy completer.

    If the list of words is: ["leopard" , "gorilla", "dinosaur", "cat", "bee"]
    Then trying to complete "oar" would yield "leopard" and "dinosaur", but not
    the others, because they match the regular expression \'o.*a.*r\'.
    Similar, in another application "djm" could expand to "django_migrations".

    The results are sorted by relevance, which is defined as the start position
    and the length of the match.

    Notice that this is not really a tool to work around spelling mistakes,
    like what would be possible with difflib. The purpose is rather to have a
    quicker or more intuitive way to filter the given completions, especially
    when many completions have a common prefix.

    Fuzzy algorithm is based on this post:
    https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python

    :param completer: A :class:`~.Completer` instance.
    :param WORD: When True, use WORD characters.
    :param pattern: Regex pattern which selects the characters before the
        cursor that are considered for the fuzzy matching.
    :param enable_fuzzy: (bool or `Filter`) Enabled the fuzzy behavior. For
        easily turning fuzzyness on or off according to a certain condition.
    '''
    completer: Incomplete
    pattern: Incomplete
    WORD: Incomplete
    enable_fuzzy: Incomplete
    def __init__(self, completer: Completer, WORD: bool = False, pattern: str | None = None, enable_fuzzy: FilterOrBool = True) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...

class FuzzyWordCompleter(Completer):
    """
    Fuzzy completion on a list of words.

    (This is basically a `WordCompleter` wrapped in a `FuzzyCompleter`.)

    :param words: List of words or callable that returns a list of words.
    :param meta_dict: Optional dict mapping words to their meta-information.
    :param WORD: When True, use WORD characters.
    """
    words: Incomplete
    meta_dict: Incomplete
    WORD: Incomplete
    word_completer: Incomplete
    fuzzy_completer: Incomplete
    def __init__(self, words: list[str] | Callable[[], list[str]], meta_dict: dict[str, str] | None = None, WORD: bool = False) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...

class _FuzzyMatch(NamedTuple):
    match_length: int
    start_pos: int
    completion: Completion
