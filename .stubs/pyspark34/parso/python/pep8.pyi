from _typeshed import Incomplete
from collections.abc import Generator
from parso.normalizer import Rule as Rule
from parso.python.errors import ErrorFinder as ErrorFinder, ErrorFinderConfig as ErrorFinderConfig
from parso.python.tree import Flow as Flow, Scope as Scope

class IndentationTypes:
    VERTICAL_BRACKET: Incomplete
    HANGING_BRACKET: Incomplete
    BACKSLASH: Incomplete
    SUITE: Incomplete
    IMPLICIT: Incomplete

class IndentationNode:
    type: Incomplete
    bracket_indentation: Incomplete
    parent: Incomplete
    def __init__(self, config, indentation, parent: Incomplete | None = None) -> None: ...
    def get_latest_suite_node(self): ...

class BracketNode(IndentationNode):
    leaf: Incomplete
    bracket_indentation: Incomplete
    indentation: Incomplete
    type: Incomplete
    parent: Incomplete
    def __init__(self, config, leaf, parent, in_suite_introducer: bool = False) -> None: ...

class ImplicitNode(BracketNode):
    """
    Implicit indentation after keyword arguments, default arguments,
    annotations and dict values.
    """
    type: Incomplete
    def __init__(self, config, leaf, parent) -> None: ...

class BackslashNode(IndentationNode):
    type: Incomplete
    indentation: Incomplete
    bracket_indentation: Incomplete
    parent: Incomplete
    def __init__(self, config, parent_indentation, containing_leaf, spacing, parent: Incomplete | None = None) -> None: ...

class PEP8Normalizer(ErrorFinder):
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_node(self, node) -> Generator[None, None, None]: ...
    def visit_leaf(self, leaf): ...
    def add_issue(self, node, code, message) -> None: ...

class PEP8NormalizerConfig(ErrorFinderConfig):
    normalizer_class = PEP8Normalizer
    indentation: Incomplete
    hanging_indentation: Incomplete
    closing_bracket_hanging_indentation: str
    break_after_binary: bool
    max_characters: Incomplete
    spaces_before_comment: Incomplete
    def __init__(self, indentation=..., hanging_indentation: Incomplete | None = None, max_characters: int = 79, spaces_before_comment: int = 2) -> None: ...

class BlankLineAtEnd(Rule):
    code: int
    message: str
    def is_issue(self, leaf): ...
