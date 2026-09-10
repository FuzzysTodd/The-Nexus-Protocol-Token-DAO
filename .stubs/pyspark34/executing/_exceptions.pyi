from _typeshed import Incomplete

class KnownIssue(Exception):
    """
    Raised in case of an known problem. Mostly because of cpython bugs.
    Executing.node gets set to None in this case.
    """

class VerifierFailure(Exception):
    """
    Thrown for an unexpected mapping from instruction to ast node
    Executing.node gets set to None in this case.
    """
    node: Incomplete
    instruction: Incomplete
    def __init__(self, title: object, node: object, instruction: object) -> None: ...
