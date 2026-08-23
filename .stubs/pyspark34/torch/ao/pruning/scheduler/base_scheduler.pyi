from _typeshed import Incomplete

__all__ = ['BaseScheduler']

class BaseScheduler:
    sparsifier: Incomplete
    base_sl: Incomplete
    last_epoch: Incomplete
    verbose: Incomplete
    def __init__(self, sparsifier, last_epoch: int = -1, verbose: bool = False) -> None: ...
    def state_dict(self):
        """Returns the state of the scheduler as a :class:`dict`.

        It contains an entry for every variable in self.__dict__ which
        is not the sparsifier.
        """
    def load_state_dict(self, state_dict) -> None:
        """Loads the schedulers state.

        Args:
            state_dict (dict): scheduler state. Should be an object returned
                from a call to :meth:`state_dict`.
        """
    def get_last_sl(self):
        """ Return last computed sparsity level by current scheduler.
        """
    def get_sl(self) -> None: ...
    def print_sl(self, is_verbose, group, sl, epoch: Incomplete | None = None) -> None:
        """Display the current sparsity level.
        """
    o: Incomplete
    def step(self, epoch: Incomplete | None = None): ...
