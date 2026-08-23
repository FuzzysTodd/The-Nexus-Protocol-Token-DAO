from typing import Callable

def experimental(fn: Callable) -> Callable:
    '''Decorator to flag a feature as experimental.

    An experimental feature trigger a warning when used as it might be subject to breaking changes in the future.

    Args:
        fn (`Callable`):
            The function to flag as experimental.

    Returns:
        `Callable`: The decorated function.

    Example:

    ```python
    >>> from datasets.utils import experimental

    >>> @experimental
    ... def my_function():
    ...     print("Hello world!")

    >>> my_function()
    UserWarning: \'my_function\' is experimental and might be subject to breaking changes in the future.
    Hello world!
    ```
    '''
