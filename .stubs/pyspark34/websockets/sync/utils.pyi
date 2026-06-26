from _typeshed import Incomplete

__all__ = ['Deadline']

class Deadline:
    """
    Manage timeouts across multiple steps.

    Args:
        timeout: Time available in seconds or :obj:`None` if there is no limit.

    """
    deadline: Incomplete
    def __init__(self, timeout: float | None) -> None: ...
    def timeout(self, *, raise_if_elapsed: bool = True) -> float | None:
        """
        Calculate a timeout from a deadline.

        Args:
            raise_if_elapsed (bool): Whether to raise :exc:`TimeoutError`
                if the deadline lapsed.

        Raises:
            TimeoutError: If the deadline lapsed.

        Returns:
            Time left in seconds or :obj:`None` if there is no limit.

        """
