from _typeshed import Incomplete
from typing import Iterable, List
from typing_extensions import Protocol, TypeGuard

__all__ = ['OneStyleAndTextTuple', 'StyleAndTextTuples', 'MagicFormattedText', 'AnyFormattedText', 'to_formatted_text', 'is_formatted_text', 'Template', 'merge_formatted_text', 'FormattedText']

OneStyleAndTextTuple: Incomplete
StyleAndTextTuples = List[OneStyleAndTextTuple]

class MagicFormattedText(Protocol):
    """
        Any object that implements ``__pt_formatted_text__`` represents formatted
        text.
        """
    def __pt_formatted_text__(self) -> StyleAndTextTuples: ...

AnyFormattedText: Incomplete

def to_formatted_text(value: AnyFormattedText, style: str = '', auto_convert: bool = False) -> FormattedText:
    """
    Convert the given value (which can be formatted text) into a list of text
    fragments. (Which is the canonical form of formatted text.) The outcome is
    always a `FormattedText` instance, which is a list of (style, text) tuples.

    It can take a plain text string, an `HTML` or `ANSI` object, anything that
    implements `__pt_formatted_text__` or a callable that takes no arguments and
    returns one of those.

    :param style: An additional style string which is applied to all text
        fragments.
    :param auto_convert: If `True`, also accept other types, and convert them
        to a string first.
    """
def is_formatted_text(value: object) -> TypeGuard[AnyFormattedText]:
    """
    Check whether the input is valid formatted text (for use in assert
    statements).
    In case of a callable, it doesn't check the return type.
    """

class FormattedText(StyleAndTextTuples):
    """
    A list of ``(style, text)`` tuples.

    (In some situations, this can also be ``(style, text, mouse_handler)``
    tuples.)
    """
    def __pt_formatted_text__(self) -> StyleAndTextTuples: ...

class Template:
    """
    Template for string interpolation with formatted text.

    Example::

        Template(' ... {} ... ').format(HTML(...))

    :param text: Plain text.
    """
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def format(self, *values: AnyFormattedText) -> AnyFormattedText: ...

def merge_formatted_text(items: Iterable[AnyFormattedText]) -> AnyFormattedText:
    """
    Merge (Concatenate) several pieces of formatted text together.
    """
