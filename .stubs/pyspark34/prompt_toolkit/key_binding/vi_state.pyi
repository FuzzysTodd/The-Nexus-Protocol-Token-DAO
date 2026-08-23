from _typeshed import Incomplete
from enum import Enum

__all__ = ['InputMode', 'CharacterFind', 'ViState']

class InputMode(str, Enum):
    value: str
    INSERT: str
    INSERT_MULTIPLE: str
    NAVIGATION: str
    REPLACE: str
    REPLACE_SINGLE: str

class CharacterFind:
    character: Incomplete
    backwards: Incomplete
    def __init__(self, character: str, backwards: bool = False) -> None: ...

class ViState:
    """
    Mutable class to hold the state of the Vi navigation.
    """
    last_character_find: Incomplete
    operator_func: Incomplete
    operator_arg: Incomplete
    named_registers: Incomplete
    waiting_for_digraph: bool
    digraph_symbol1: Incomplete
    tilde_operator: bool
    recording_register: Incomplete
    current_recording: str
    temporary_navigation_mode: bool
    def __init__(self) -> None: ...
    @property
    def input_mode(self) -> InputMode:
        """Get `InputMode`."""
    @input_mode.setter
    def input_mode(self, value: InputMode) -> None:
        """Set `InputMode`."""
    def reset(self) -> None:
        """
        Reset state, go back to the given mode. INSERT by default.
        """
