from _typeshed import Incomplete

__all__ = ['JSONDecodeError']

class JSONDecodeError(ValueError):
    """Subclass of ValueError with the following additional properties:

    msg: The unformatted error message
    doc: The JSON document being parsed
    pos: The start index of doc where parsing failed
    end: The end index of doc where parsing failed (may be None)
    lineno: The line corresponding to pos
    colno: The column corresponding to pos
    endlineno: The line corresponding to end (may be None)
    endcolno: The column corresponding to end (may be None)

    """
    msg: Incomplete
    doc: Incomplete
    pos: Incomplete
    end: Incomplete
    def __init__(self, msg, doc, pos, end: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...
