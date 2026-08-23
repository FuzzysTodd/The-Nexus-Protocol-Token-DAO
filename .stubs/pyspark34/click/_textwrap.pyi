import textwrap
import typing as t
from _typeshed import Incomplete

class TextWrapper(textwrap.TextWrapper):
    initial_indent: Incomplete
    subsequent_indent: Incomplete
    def extra_indent(self, indent: str) -> t.Iterator[None]: ...
    def indent_only(self, text: str) -> str: ...
