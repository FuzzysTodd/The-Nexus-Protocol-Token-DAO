from _typeshed import Incomplete

__all__ = ['Token', 'ParseNode', 'Operator', 'parse']

class _UniqueValue:
    def __init__(self, print_as) -> None: ...

class Token:
    """A token with possible payload.

    .. attribute:: type

       An arbitrary object indicating the type of this token. Should be
      :term:`hashable`, but otherwise it can be whatever you like.
    """
    LPAREN: Incomplete
    RPAREN: Incomplete
    type: Incomplete
    origin: Incomplete
    extra: Incomplete
    def __init__(self, type, origin, extra: Incomplete | None = None) -> None: ...

class ParseNode:
    type: Incomplete
    token: Incomplete
    args: Incomplete
    origin: Incomplete
    def __init__(self, type, token, args, origin) -> None: ...

class Operator:
    token_type: Incomplete
    arity: Incomplete
    precedence: Incomplete
    def __init__(self, token_type, arity, precedence) -> None: ...

class _StackOperator:
    op: Incomplete
    token: Incomplete
    def __init__(self, op, token) -> None: ...

class _ParseContext:
    op_stack: Incomplete
    noun_stack: Incomplete
    unary_ops: Incomplete
    binary_ops: Incomplete
    atomic_types: Incomplete
    trace: Incomplete
    def __init__(self, unary_ops, binary_ops, atomic_types, trace) -> None: ...

# Names in __all__ with no definition:
#   parse
