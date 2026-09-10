from _typeshed import Incomplete

class AdalError(Exception):
    error_response: Incomplete
    def __init__(self, error_msg, error_response: Incomplete | None = None) -> None: ...
