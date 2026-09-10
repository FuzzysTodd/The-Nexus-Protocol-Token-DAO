from typing import Callable

def with_temp_dir(func: Callable | None = None) -> Callable | None:
    """
    Wrapper to initialize temp directory for distributed checkpoint.
    """
