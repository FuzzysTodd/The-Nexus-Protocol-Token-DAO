import weakref
from .key_bindings import KeyBindingsBase
from _typeshed import Incomplete
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.keys import Keys
from typing import Any

__all__ = ['KeyProcessor', 'KeyPress', 'KeyPressEvent']

class KeyPress:
    """
    :param key: A `Keys` instance or text (one character).
    :param data: The received string on stdin. (Often vt100 escape codes.)
    """
    key: Incomplete
    data: Incomplete
    def __init__(self, key: Keys | str, data: str | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class KeyProcessor:
    """
    Statemachine that receives :class:`KeyPress` instances and according to the
    key bindings in the given :class:`KeyBindings`, calls the matching handlers.

    ::

        p = KeyProcessor(key_bindings)

        # Send keys into the processor.
        p.feed(KeyPress(Keys.ControlX, '\x18'))
        p.feed(KeyPress(Keys.ControlC, '\x03')

        # Process all the keys in the queue.
        p.process_keys()

        # Now the ControlX-ControlC callback will be called if this sequence is
        # registered in the key bindings.

    :param key_bindings: `KeyBindingsBase` instance.
    """
    before_key_press: Incomplete
    after_key_press: Incomplete
    def __init__(self, key_bindings: KeyBindingsBase) -> None: ...
    input_queue: Incomplete
    key_buffer: Incomplete
    arg: Incomplete
    def reset(self) -> None: ...
    def feed(self, key_press: KeyPress, first: bool = False) -> None:
        """
        Add a new :class:`KeyPress` to the input queue.
        (Don't forget to call `process_keys` in order to process the queue.)

        :param first: If true, insert before everything else.
        """
    def feed_multiple(self, key_presses: list[KeyPress], first: bool = False) -> None:
        """
        :param first: If true, insert before everything else.
        """
    def process_keys(self) -> None:
        """
        Process all the keys in the `input_queue`.
        (To be called after `feed`.)

        Note: because of the `feed`/`process_keys` separation, it is
              possible to call `feed` from inside a key binding.
              This function keeps looping until the queue is empty.
        """
    def empty_queue(self) -> list[KeyPress]:
        """
        Empty the input queue. Return the unprocessed input.
        """
    def send_sigint(self) -> None:
        """
        Send SIGINT. Immediately call the SIGINT key handler.
        """

class KeyPressEvent:
    """
    Key press event, delivered to key bindings.

    :param key_processor_ref: Weak reference to the `KeyProcessor`.
    :param arg: Repetition argument.
    :param key_sequence: List of `KeyPress` instances.
    :param previouskey_sequence: Previous list of `KeyPress` instances.
    :param is_repeat: True when the previous event was delivered to the same handler.
    """
    key_sequence: Incomplete
    previous_key_sequence: Incomplete
    is_repeat: Incomplete
    def __init__(self, key_processor_ref: weakref.ReferenceType[KeyProcessor], arg: str | None, key_sequence: list[KeyPress], previous_key_sequence: list[KeyPress], is_repeat: bool) -> None: ...
    @property
    def data(self) -> str: ...
    @property
    def key_processor(self) -> KeyProcessor: ...
    @property
    def app(self) -> Application[Any]:
        """
        The current `Application` object.
        """
    @property
    def current_buffer(self) -> Buffer:
        """
        The current buffer.
        """
    @property
    def arg(self) -> int:
        """
        Repetition argument.
        """
    @property
    def arg_present(self) -> bool:
        """
        True if repetition argument was explicitly provided.
        """
    def append_to_arg_count(self, data: str) -> None:
        """
        Add digit to the input argument.

        :param data: the typed digit as string
        """
    @property
    def cli(self) -> Application[Any]:
        """For backward-compatibility."""
