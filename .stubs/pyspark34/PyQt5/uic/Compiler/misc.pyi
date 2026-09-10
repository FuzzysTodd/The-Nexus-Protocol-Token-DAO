from _typeshed import Incomplete

def moduleMember(module, name): ...

class Literal:
    """Literal(string) -> new literal

    string will not be quoted when put into an argument list"""
    string: Incomplete
    def __init__(self, string) -> None: ...
    def __or__(self, r_op): ...
