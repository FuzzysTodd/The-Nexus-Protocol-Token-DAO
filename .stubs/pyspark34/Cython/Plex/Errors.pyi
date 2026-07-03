from _typeshed import Incomplete

class PlexError(Exception):
    message: str

class PlexTypeError(PlexError, TypeError): ...
class PlexValueError(PlexError, ValueError): ...

class InvalidToken(PlexError):
    def __init__(self, token_number, message) -> None: ...

class InvalidScanner(PlexError): ...

class AmbiguousAction(PlexError):
    message: str
    def __init__(self) -> None: ...

class UnrecognizedInput(PlexError):
    scanner: Incomplete
    position: Incomplete
    state_name: Incomplete
    def __init__(self, scanner, state_name) -> None: ...
