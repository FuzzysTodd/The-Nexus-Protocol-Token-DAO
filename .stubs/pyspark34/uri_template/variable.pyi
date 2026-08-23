from .charset import Charset as Charset

class VariableInvalidError(Exception):
    """Exception thrown for invalid variables."""
    variable: str
    def __init__(self, variable: str) -> None: ...

class Variable:
    """
    A template variable.

    https://tools.ietf.org/html/rfc6570#section-2.3
    """
    name: str
    key: str
    max_length: int
    explode: bool
    array: bool
    default: str | None
    def __init__(self, var_spec: str) -> None: ...
