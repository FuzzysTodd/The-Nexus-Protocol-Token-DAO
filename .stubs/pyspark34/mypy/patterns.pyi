from mypy.nodes import Expression as Expression, NameExpr as NameExpr, Node as Node, RefExpr as RefExpr
from mypy.visitor import PatternVisitor as PatternVisitor
from typing import TypeVar

T = TypeVar('T')

class Pattern(Node):
    """A pattern node."""
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class AsPattern(Pattern):
    """The pattern <pattern> as <name>"""
    pattern: Pattern | None
    name: NameExpr | None
    def __init__(self, pattern: Pattern | None, name: NameExpr | None) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class OrPattern(Pattern):
    """The pattern <pattern> | <pattern> | ..."""
    patterns: list[Pattern]
    def __init__(self, patterns: list[Pattern]) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class ValuePattern(Pattern):
    """The pattern x.y (or x.y.z, ...)"""
    expr: Expression
    def __init__(self, expr: Expression) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class SingletonPattern(Pattern):
    value: bool | None
    def __init__(self, value: bool | None) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class SequencePattern(Pattern):
    """The pattern [<pattern>, ...]"""
    patterns: list[Pattern]
    def __init__(self, patterns: list[Pattern]) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class StarredPattern(Pattern):
    capture: NameExpr | None
    def __init__(self, capture: NameExpr | None) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class MappingPattern(Pattern):
    keys: list[Expression]
    values: list[Pattern]
    rest: NameExpr | None
    def __init__(self, keys: list[Expression], values: list[Pattern], rest: NameExpr | None) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...

class ClassPattern(Pattern):
    """The pattern Cls(...)"""
    class_ref: RefExpr
    positionals: list[Pattern]
    keyword_keys: list[str]
    keyword_values: list[Pattern]
    def __init__(self, class_ref: RefExpr, positionals: list[Pattern], keyword_keys: list[str], keyword_values: list[Pattern]) -> None: ...
    def accept(self, visitor: PatternVisitor[T]) -> T: ...
