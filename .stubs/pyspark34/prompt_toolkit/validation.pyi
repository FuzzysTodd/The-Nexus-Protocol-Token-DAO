from .document import Document
from .filters import FilterOrBool
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import Callable

__all__ = ['ConditionalValidator', 'ValidationError', 'Validator', 'ThreadedValidator', 'DummyValidator', 'DynamicValidator']

class ValidationError(Exception):
    """
    Error raised by :meth:`.Validator.validate`.

    :param cursor_position: The cursor position where the error occurred.
    :param message: Text.
    """
    cursor_position: Incomplete
    message: Incomplete
    def __init__(self, cursor_position: int = 0, message: str = '') -> None: ...

class Validator(metaclass=ABCMeta):
    """
    Abstract base class for an input validator.

    A validator is typically created in one of the following two ways:

    - Either by overriding this class and implementing the `validate` method.
    - Or by passing a callable to `Validator.from_callable`.

    If the validation takes some time and needs to happen in a background
    thread, this can be wrapped in a :class:`.ThreadedValidator`.
    """
    @abstractmethod
    def validate(self, document: Document) -> None:
        """
        Validate the input.
        If invalid, this should raise a :class:`.ValidationError`.

        :param document: :class:`~prompt_toolkit.document.Document` instance.
        """
    async def validate_async(self, document: Document) -> None:
        """
        Return a `Future` which is set when the validation is ready.
        This function can be overloaded in order to provide an asynchronous
        implementation.
        """
    @classmethod
    def from_callable(cls, validate_func: Callable[[str], bool], error_message: str = 'Invalid input', move_cursor_to_end: bool = False) -> Validator:
        """
        Create a validator from a simple validate callable. E.g.:

        .. code:: python

            def is_valid(text):
                return text in ['hello', 'world']
            Validator.from_callable(is_valid, error_message='Invalid input')

        :param validate_func: Callable that takes the input string, and returns
            `True` if the input is valid input.
        :param error_message: Message to be displayed if the input is invalid.
        :param move_cursor_to_end: Move the cursor to the end of the input, if
            the input is invalid.
        """

class _ValidatorFromCallable(Validator):
    """
    Validate input from a simple callable.
    """
    func: Incomplete
    error_message: Incomplete
    move_cursor_to_end: Incomplete
    def __init__(self, func: Callable[[str], bool], error_message: str, move_cursor_to_end: bool) -> None: ...
    def validate(self, document: Document) -> None: ...

class ThreadedValidator(Validator):
    """
    Wrapper that runs input validation in a thread.
    (Use this to prevent the user interface from becoming unresponsive if the
    input validation takes too much time.)
    """
    validator: Incomplete
    def __init__(self, validator: Validator) -> None: ...
    def validate(self, document: Document) -> None: ...
    async def validate_async(self, document: Document) -> None:
        """
        Run the `validate` function in a thread.
        """

class DummyValidator(Validator):
    """
    Validator class that accepts any input.
    """
    def validate(self, document: Document) -> None: ...

class ConditionalValidator(Validator):
    """
    Validator that can be switched on/off according to
    a filter. (This wraps around another validator.)
    """
    validator: Incomplete
    filter: Incomplete
    def __init__(self, validator: Validator, filter: FilterOrBool) -> None: ...
    def validate(self, document: Document) -> None: ...

class DynamicValidator(Validator):
    """
    Validator class that can dynamically returns any Validator.

    :param get_validator: Callable that returns a :class:`.Validator` instance.
    """
    get_validator: Incomplete
    def __init__(self, get_validator: Callable[[], Validator | None]) -> None: ...
    def validate(self, document: Document) -> None: ...
    async def validate_async(self, document: Document) -> None: ...
