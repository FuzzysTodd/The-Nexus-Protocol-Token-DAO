import abc
from _typeshed import Incomplete
from typing import Dict, List, NamedTuple

__all__ = ['DefaultPager', 'UserSpecifiedPager', 'PlatformPager', 'CustomPager', 'More', 'Less', 'LV']

class PagerConfig(NamedTuple):
    color: Incomplete
    line_buffering_requested: Incomplete
    reset_terminal: Incomplete

class PagerCommand(metaclass=abc.ABCMeta):
    """
    Abstract base class for pager commands.

    A subclass implementing this interface can be used to specify a particular
    pager command to run and its environment.
    """
    @abc.abstractmethod
    def command(self) -> List[str]:
        """Return the list of command arguments."""
    @abc.abstractmethod
    def environment_variables(self, config: PagerConfig) -> Dict[str, str] | None:
        """Return the dict of any environment variables to set."""

class More(PagerCommand):
    """The pager command ``more``."""
    def command(self) -> List[str]: ...
    def environment_variables(self, config: PagerConfig) -> Dict[str, str] | None: ...

class Less(PagerCommand):
    """The pager command ``less``."""
    def command(self) -> List[str]: ...
    def environment_variables(self, config: PagerConfig) -> Dict[str, str] | None: ...

class LV(PagerCommand):
    """The pager command ``lv``."""
    def command(self) -> List[str]: ...
    def environment_variables(self, config: PagerConfig) -> Dict[str, str] | None: ...

class CustomPager(PagerCommand):
    """A pager command parsed from a user-specified string."""
    def __init__(self, pager_cmdline: str) -> None: ...
    def command(self) -> List[str]: ...
    def environment_variables(self, config: PagerConfig) -> Dict[str, str] | None: ...

def PlatformPager() -> PagerCommand:
    """
    Return the default pager command for the current platform.
    """
def UserSpecifiedPager(*env_vars: str) -> PagerCommand:
    """
    Return the pager command for the current environment.

    Each of the specified environment variables is searched in order; the first
    one that is set will be used as the pager command. If none of the
    environment variables is set, the default pager for the platform will be
    used.
    """
def DefaultPager() -> PagerCommand:
    """
    Return the default pager command for the current environment.

    If there is a $PAGER environment variable configured, this command will be
    used. Otherwise, the default pager for the platform will be used.
    """
