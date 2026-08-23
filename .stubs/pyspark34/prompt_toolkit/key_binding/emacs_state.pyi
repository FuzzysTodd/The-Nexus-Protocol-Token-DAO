from _typeshed import Incomplete

__all__ = ['EmacsState']

class EmacsState:
    """
    Mutable class to hold Emacs specific state.
    """
    macro: Incomplete
    current_recording: Incomplete
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    @property
    def is_recording(self) -> bool:
        """Tell whether we are recording a macro."""
    def start_macro(self) -> None:
        """Start recording macro."""
    def end_macro(self) -> None:
        """End recording macro."""
