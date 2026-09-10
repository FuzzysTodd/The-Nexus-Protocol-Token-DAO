from . import get_console as get_console
from .console import Console as Console
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from typing import Generic, List, TextIO, TypeVar, overload

PromptType = TypeVar('PromptType')
DefaultType = TypeVar('DefaultType')

class PromptError(Exception):
    """Exception base class for prompt related errors."""

class InvalidResponse(PromptError):
    """Exception to indicate a response was invalid. Raise this within process_response() to indicate an error
    and provide an error message.

    Args:
        message (Union[str, Text]): Error message.
    """
    message: Incomplete
    def __init__(self, message: TextType) -> None: ...
    def __rich__(self) -> TextType: ...

class PromptBase(Generic[PromptType]):
    '''Ask the user for input until a valid response is received. This is the base class, see one of
    the concrete classes for examples.

    Args:
        prompt (TextType, optional): Prompt text. Defaults to "".
        console (Console, optional): A Console instance or None to use global console. Defaults to None.
        password (bool, optional): Enable password input. Defaults to False.
        choices (List[str], optional): A list of valid choices. Defaults to None.
        show_default (bool, optional): Show default in prompt. Defaults to True.
        show_choices (bool, optional): Show choices in prompt. Defaults to True.
    '''
    response_type: type
    validate_error_message: str
    illegal_choice_message: str
    prompt_suffix: str
    choices: List[str] | None
    console: Incomplete
    prompt: Incomplete
    password: Incomplete
    show_default: Incomplete
    show_choices: Incomplete
    def __init__(self, prompt: TextType = '', *, console: Console | None = None, password: bool = False, choices: List[str] | None = None, show_default: bool = True, show_choices: bool = True) -> None: ...
    @classmethod
    @overload
    def ask(cls, prompt: TextType = '', *, console: Console | None = None, password: bool = False, choices: List[str] | None = None, show_default: bool = True, show_choices: bool = True, default: DefaultType, stream: TextIO | None = None) -> DefaultType | PromptType: ...
    @classmethod
    @overload
    def ask(cls, prompt: TextType = '', *, console: Console | None = None, password: bool = False, choices: List[str] | None = None, show_default: bool = True, show_choices: bool = True, stream: TextIO | None = None) -> PromptType: ...
    def render_default(self, default: DefaultType) -> Text:
        """Turn the supplied default in to a Text instance.

        Args:
            default (DefaultType): Default value.

        Returns:
            Text: Text containing rendering of default value.
        """
    def make_prompt(self, default: DefaultType) -> Text:
        """Make prompt text.

        Args:
            default (DefaultType): Default value.

        Returns:
            Text: Text to display in prompt.
        """
    @classmethod
    def get_input(cls, console: Console, prompt: TextType, password: bool, stream: TextIO | None = None) -> str:
        """Get input from user.

        Args:
            console (Console): Console instance.
            prompt (TextType): Prompt text.
            password (bool): Enable password entry.

        Returns:
            str: String from user.
        """
    def check_choice(self, value: str) -> bool:
        """Check value is in the list of valid choices.

        Args:
            value (str): Value entered by user.

        Returns:
            bool: True if choice was valid, otherwise False.
        """
    def process_response(self, value: str) -> PromptType:
        """Process response from user, convert to prompt type.

        Args:
            value (str): String typed by user.

        Raises:
            InvalidResponse: If ``value`` is invalid.

        Returns:
            PromptType: The value to be returned from ask method.
        """
    def on_validate_error(self, value: str, error: InvalidResponse) -> None:
        """Called to handle validation error.

        Args:
            value (str): String entered by user.
            error (InvalidResponse): Exception instance the initiated the error.
        """
    def pre_prompt(self) -> None:
        """Hook to display something before the prompt."""
    @overload
    def __call__(self, *, stream: TextIO | None = None) -> PromptType: ...
    @overload
    def __call__(self, *, default: DefaultType, stream: TextIO | None = None) -> PromptType | DefaultType: ...

class Prompt(PromptBase[str]):
    '''A prompt that returns a str.

    Example:
        >>> name = Prompt.ask("Enter your name")


    '''
    response_type = str

class IntPrompt(PromptBase[int]):
    '''A prompt that returns an integer.

    Example:
        >>> burrito_count = IntPrompt.ask("How many burritos do you want to order")

    '''
    response_type = int
    validate_error_message: str

class FloatPrompt(PromptBase[int]):
    '''A prompt that returns a float.

    Example:
        >>> temperature = FloatPrompt.ask("Enter desired temperature")

    '''
    response_type = float
    validate_error_message: str

class Confirm(PromptBase[bool]):
    '''A yes / no confirmation prompt.

    Example:
        >>> if Confirm.ask("Continue"):
                run_job()

    '''
    response_type = bool
    validate_error_message: str
    choices: List[str]
    def render_default(self, default: DefaultType) -> Text:
        """Render the default as (y) or (n) rather than True/False."""
    def process_response(self, value: str) -> bool:
        """Convert choices to a bool."""
