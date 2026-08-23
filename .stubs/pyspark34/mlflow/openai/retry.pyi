from collections.abc import Generator

def openai_auto_retry_patch() -> Generator[None, None, None]:
    """
    Context manager that patches the openai python package to automatically retry on transient
    errors.
    """
