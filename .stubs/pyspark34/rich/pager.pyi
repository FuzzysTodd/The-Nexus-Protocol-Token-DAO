import abc
from abc import ABC, abstractmethod

class Pager(ABC, metaclass=abc.ABCMeta):
    """Base class for a pager."""
    @abstractmethod
    def show(self, content: str) -> None:
        """Show content in pager.

        Args:
            content (str): Content to be displayed.
        """

class SystemPager(Pager):
    """Uses the pager installed on the system."""
    def show(self, content: str) -> None:
        """Use the same pager used by pydoc."""
