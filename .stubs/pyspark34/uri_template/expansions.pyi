from .charset import Charset as Charset
from .variable import Variable as Variable
from collections.abc import Iterable, Mapping
from typing import Any

class ExpansionFailedError(Exception):
    """Exception thrown when expansions fail."""
    variable: str
    def __init__(self, variable: str) -> None: ...

class Expansion:
    """
    Base class for template expansions.

    https://tools.ietf.org/html/rfc6570#section-3
    """
    def __init__(self) -> None: ...
    @property
    def variables(self) -> Iterable[Variable]:
        """Get all variables in this expansion."""
    @property
    def variable_names(self) -> Iterable[str]:
        """Get the names of all variables in this expansion."""
    def expand(self, values: Mapping[str, Any]) -> str | None:
        """Expand values."""
    def partial(self, values: Mapping[str, Any]) -> str:
        """Perform partial expansion."""

class Literal(Expansion):
    """
    A literal expansion.

    https://tools.ietf.org/html/rfc6570#section-3.1
    """
    value: str
    def __init__(self, value: str) -> None: ...
    def expand(self, values: Mapping[str, Any]) -> str | None:
        """Perform exansion."""

class ExpressionExpansion(Expansion):
    """
    Base class for expression expansions.

    https://tools.ietf.org/html/rfc6570#section-3.2
    """
    operator: str
    partial_operator: str
    output_prefix: str
    var_joiner: str
    partial_joiner: str
    vars: list[Variable]
    trailing_joiner: str
    def __init__(self, variables: str) -> None: ...
    @property
    def variables(self) -> Iterable[Variable]:
        """Get all variables."""
    @property
    def variable_names(self) -> Iterable[str]:
        """Get names of all variables."""
    def expand(self, values: Mapping[str, Any]) -> str | None:
        """Expand all variables, skip missing values."""
    def partial(self, values: Mapping[str, Any]) -> str:
        """Expand all variables, replace missing values with expansions."""

class SimpleExpansion(ExpressionExpansion):
    """
    Simple String expansion {var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.2

    """
    def __init__(self, variables: str) -> None: ...

class ReservedExpansion(ExpressionExpansion):
    """
    Reserved Expansion {+var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.3
    """
    operator: str
    partial_operator: str
    def __init__(self, variables: str) -> None: ...

class FragmentExpansion(ReservedExpansion):
    """
    Fragment Expansion {#var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.4
    """
    operator: str
    output_prefix: str
    def __init__(self, variables: str) -> None: ...

class LabelExpansion(ExpressionExpansion):
    """
    Label Expansion with Dot-Prefix {.var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.5
    """
    operator: str
    partial_operator: str
    output_prefix: str
    var_joiner: str
    partial_joiner: str
    def __init__(self, variables: str) -> None: ...

class PathExpansion(ExpressionExpansion):
    """
    Path Segment Expansion {/var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.6
    """
    operator: str
    partial_operator: str
    output_prefix: str
    var_joiner: str
    partial_joiner: str
    def __init__(self, variables: str) -> None: ...

class PathStyleExpansion(ExpressionExpansion):
    """
    Path-Style Parameter Expansion {;var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.7
    """
    operator: str
    partial_operator: str
    output_prefix: str
    var_joiner: str
    partial_joiner: str
    def __init__(self, variables: str) -> None: ...

class FormStyleQueryExpansion(PathStyleExpansion):
    """
    Form-Style Query Expansion {?var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.8
    """
    operator: str
    partial_operator: str
    output_prefix: str
    var_joiner: str
    partial_joiner: str
    def __init__(self, variables: str) -> None: ...

class FormStyleQueryContinuation(FormStyleQueryExpansion):
    """
    Form-Style Query Continuation {&var}.

    https://tools.ietf.org/html/rfc6570#section-3.2.9
    """
    operator: str
    output_prefix: str
    def __init__(self, variables: str) -> None: ...

class CommaExpansion(ExpressionExpansion):
    """
    Label Expansion with Comma-Prefix {,var}.

    Non-standard extension to support partial expansions.
    """
    operator: str
    output_prefix: str
    def __init__(self, variables: str) -> None: ...

class ReservedCommaExpansion(ReservedExpansion):
    """
    Reserved Expansion with comma prefix {,+var}.

    Non-standard extension to support partial expansions.
    """
    operator: str
    output_prefix: str
    def __init__(self, variables: str) -> None: ...
