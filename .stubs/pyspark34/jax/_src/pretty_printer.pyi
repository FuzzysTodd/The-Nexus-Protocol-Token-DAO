import abc
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import config as config
from typing import NamedTuple

CAN_USE_COLOR: Incomplete

class Doc(abc.ABC):
    def format(self, width: int = 80, use_color: bool | None = None, annotation_prefix: str = ' # ') -> str: ...
    def __add__(self, other: Doc) -> Doc: ...

class _NilDoc(Doc): ...

class _TextDoc(Doc):
    text: str
    annotation: str | None
    def __init__(self, text: str, annotation: str | None = None) -> None: ...

class _ConcatDoc(Doc):
    children: list[Doc]
    def __init__(self, children: Sequence[Doc]) -> None: ...

class _BreakDoc(Doc):
    text: str
    def __init__(self, text: str) -> None: ...

class _GroupDoc(Doc):
    child: Doc
    def __init__(self, child: Doc) -> None: ...

class _NestDoc(Doc):
    n: int
    child: Doc
    def __init__(self, n: int, child: Doc) -> None: ...

Color: Incomplete
Intensity: Incomplete

class _ColorDoc(Doc):
    foreground: Color | None
    background: Color | None
    intensity: Intensity | None
    child: Doc
    def __init__(self, child: Doc, *, foreground: Color | None = None, background: Color | None = None, intensity: Intensity | None = None) -> None: ...

class _ColorState(NamedTuple):
    foreground: Color
    background: Color
    intensity: Intensity

class _State(NamedTuple):
    indent: int
    mode: _BreakMode
    doc: Doc
    color: _ColorState

class _Line(NamedTuple):
    text: str
    width: int
    annotations: str | None | list[str]

def nil() -> Doc:
    """An empty document."""
def text(s: str, annotation: str | None = None) -> Doc:
    """Literal text."""
def concat(docs: Sequence[Doc]) -> Doc:
    """Concatenation of documents."""
def brk(text: str = ' ') -> Doc:
    """A break.

  Prints either as a newline or as `text`, depending on the enclosing group.
  """
def group(doc: Doc) -> Doc:
    """Layout alternative groups.

  Prints the group with its breaks as their text (typically spaces) if the
  entire group would fit on the line when printed that way. Otherwise, breaks
  inside the group as printed as newlines.
  """
def nest(n: int, doc: Doc) -> Doc:
    """Increases the indentation level by `n`."""
def color(doc: Doc, *, foreground: Color | None = None, background: Color | None = None, intensity: Intensity | None = None):
    """ANSI colors.

  Overrides the foreground/background/intensity of the text for the child doc.
  Requires use_colors=True to be set when printing and the `colorama` package
  to be installed; otherwise does nothing.
  """

type_annotation: Incomplete
keyword: Incomplete

def join(sep: Doc, docs: Sequence[Doc]) -> Doc:
    """Concatenates `docs`, separated by `sep`."""
