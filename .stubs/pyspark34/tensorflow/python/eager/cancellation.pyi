from tensorflow.python import pywrap_tfe as pywrap_tfe

class CancellationManager:
    """A mechanism for cancelling blocking computation."""
    def __init__(self) -> None: ...
    @property
    def is_cancelled(self):
        """Returns `True` if `CancellationManager.start_cancel` has been called."""
    def start_cancel(self) -> None:
        """Cancels blocking operations that have been registered with this object."""
    def get_cancelable_function(self, concrete_function): ...
