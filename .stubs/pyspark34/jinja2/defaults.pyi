import typing as t
import typing_extensions as te
from .utils import Cycler as Cycler, Joiner as Joiner, Namespace as Namespace, generate_lorem_ipsum as generate_lorem_ipsum
from _typeshed import Incomplete

BLOCK_START_STRING: str
BLOCK_END_STRING: str
VARIABLE_START_STRING: str
VARIABLE_END_STRING: str
COMMENT_START_STRING: str
COMMENT_END_STRING: str
LINE_STATEMENT_PREFIX: str | None
LINE_COMMENT_PREFIX: str | None
TRIM_BLOCKS: bool
LSTRIP_BLOCKS: bool
NEWLINE_SEQUENCE: te.Literal['\n', '\r\n', '\r']
KEEP_TRAILING_NEWLINE: bool
DEFAULT_NAMESPACE: Incomplete
DEFAULT_POLICIES: t.Dict[str, t.Any]
