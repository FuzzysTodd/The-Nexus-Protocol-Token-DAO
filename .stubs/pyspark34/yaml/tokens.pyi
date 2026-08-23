from .error import StreamMark as StreamMark
from _typeshed import Incomplete
from ruamel.yaml.compat import nprintf as nprintf
from typing import Any

SHOW_LINES: bool

class Token:
    start_mark: Incomplete
    end_mark: Incomplete
    def __init__(self, start_mark: StreamMark, end_mark: StreamMark) -> None: ...
    @property
    def column(self) -> int: ...
    @column.setter
    def column(self, pos: Any) -> None: ...
    def add_post_comment(self, comment: Any) -> None: ...
    def add_pre_comments(self, comments: Any) -> None: ...
    def add_comment_pre(self, comment: Any) -> None: ...
    def add_comment_eol(self, comment: Any, comment_type: Any) -> None: ...
    def add_comment_post(self, comment: Any) -> None: ...
    @property
    def comment(self) -> Any: ...
    def move_old_comment(self, target: Any, empty: bool = False) -> Any:
        """move a comment from this token to target (normally next token)
        used to combine e.g. comments before a BlockEntryToken to the
        ScalarToken that follows it
        empty is a special for empty values -> comment after key
        """
    def split_old_comment(self) -> Any:
        """ split the post part of a comment, and return it
        as comment to be added. Delete second part if [None, None]
         abc:  # this goes to sequence
           # this goes to first element
           - first element
        """
    def move_new_comment(self, target: Any, empty: bool = False) -> Any:
        """move a comment from this token to target (normally next token)
        used to combine e.g. comments before a BlockEntryToken to the
        ScalarToken that follows it
        empty is a special for empty values -> comment after key
        """

class DirectiveToken(Token):
    id: str
    name: Incomplete
    value: Incomplete
    def __init__(self, name: Any, value: Any, start_mark: Any, end_mark: Any) -> None: ...

class DocumentStartToken(Token):
    id: str

class DocumentEndToken(Token):
    id: str

class StreamStartToken(Token):
    id: str
    encoding: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, encoding: Any = None) -> None: ...

class StreamEndToken(Token):
    id: str

class BlockSequenceStartToken(Token):
    id: str

class BlockMappingStartToken(Token):
    id: str

class BlockEndToken(Token):
    id: str

class FlowSequenceStartToken(Token):
    id: str

class FlowMappingStartToken(Token):
    id: str

class FlowSequenceEndToken(Token):
    id: str

class FlowMappingEndToken(Token):
    id: str

class KeyToken(Token):
    id: str

class ValueToken(Token):
    id: str

class BlockEntryToken(Token):
    id: str

class FlowEntryToken(Token):
    id: str

class AliasToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value: Any, start_mark: Any, end_mark: Any) -> None: ...

class AnchorToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value: Any, start_mark: Any, end_mark: Any) -> None: ...

class TagToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value: Any, start_mark: Any, end_mark: Any) -> None: ...

class ScalarToken(Token):
    id: str
    value: Incomplete
    plain: Incomplete
    style: Incomplete
    def __init__(self, value: Any, plain: Any, start_mark: Any, end_mark: Any, style: Any = None) -> None: ...

class CommentToken(Token):
    id: str
    def __init__(self, value: Any, start_mark: Any = None, end_mark: Any = None, column: Any = None) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, val: Any) -> None: ...
    def reset(self) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
