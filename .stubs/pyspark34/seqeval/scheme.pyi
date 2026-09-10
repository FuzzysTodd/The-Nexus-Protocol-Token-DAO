import enum
from _typeshed import Incomplete
from typing import List, Set, Tuple, Type

class Entity:
    sent_id: Incomplete
    start: Incomplete
    end: Incomplete
    tag: Incomplete
    def __init__(self, sent_id: int, start: int, end: int, tag: str) -> None: ...
    def __eq__(self, other: Entity): ...
    def __hash__(self): ...
    def to_tuple(self): ...

class Prefix(enum.Flag):
    I: Incomplete
    O: Incomplete
    B: Incomplete
    E: Incomplete
    S: Incomplete
    U: Incomplete
    L: Incomplete
    ANY: Incomplete

Prefixes: Incomplete

class Tag(enum.Flag):
    SAME: Incomplete
    DIFF: Incomplete
    ANY: Incomplete

class Token:
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete
    token: Incomplete
    prefix: Incomplete
    tag: Incomplete
    def __init__(self, token: str, suffix: bool = False, delimiter: str = '-') -> None: ...
    def is_valid(self):
        """Check whether the prefix is allowed or not."""
    def is_start(self, prev: Token):
        """Check whether the current token is the start of chunk."""
    def is_inside(self, prev: Token):
        """Check whether the current token is inside of chunk."""
    def is_end(self, prev: Token):
        """Check whether the previous token is the end of chunk."""
    def check_tag(self, prev: Token, cond: Tag):
        """Check whether the tag pattern is matched."""
    def check_patterns(self, prev: Token, patterns: Set[Tuple[Prefix, Prefix, Tag]]):
        """Check whether the prefix patterns are matched."""

class IOB1(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class IOE1(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class IOB2(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class IOE2(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class IOBES(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class BILOU(Token):
    allowed_prefix: Incomplete
    start_patterns: Incomplete
    inside_patterns: Incomplete
    end_patterns: Incomplete

class Tokens:
    outside_token: Incomplete
    tokens: Incomplete
    extended_tokens: Incomplete
    sent_id: Incomplete
    def __init__(self, tokens: List[str], scheme: Type[Token], suffix: bool = False, delimiter: str = '-', sent_id: int = None) -> None: ...
    @property
    def entities(self):
        """Extract entities from tokens.

        Returns:
            list: list of Entity.

        Example:
            >>> tokens = Tokens(['B-PER', 'I-PER', 'O', 'B-LOC'], IOB2)
            >>> tokens.entities
            [('PER', 0, 2), ('LOC', 3, 4)]
        """

class Entities:
    entities: Incomplete
    def __init__(self, sequences: List[List[str]], scheme: Type[Token], suffix: bool = False, delimiter: str = '-') -> None: ...
    def filter(self, tag_name: str): ...
    @property
    def unique_tags(self): ...

def auto_detect(sequences: List[List[str]], suffix: bool = False, delimiter: str = '-'):
    """Detects scheme automatically.

    auto_detect supports the following schemes:
    - IOB2
    - IOE2
    - IOBES
    """
