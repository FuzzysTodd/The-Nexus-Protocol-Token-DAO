__all__ = ['NoLock', 'validate_utf8', 'extract_err_message', 'extract_error_code']

class NoLock:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def validate_utf8(utfbytes: str | bytes) -> bool:
    """
    validate utf8 byte string.
    utfbytes: utf byte string to check.
    return value: if valid utf8 string, return true. Otherwise, return false.
    """
def extract_err_message(exception: Exception) -> str | None: ...
def extract_error_code(exception: Exception) -> int | None: ...
