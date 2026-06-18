import cmd2
from .constants import CLASS_ATTR_DEFAULT_HELP_CATEGORY as CLASS_ATTR_DEFAULT_HELP_CATEGORY, COMMAND_FUNC_PREFIX as COMMAND_FUNC_PREFIX
from .exceptions import CommandSetRegistrationError as CommandSetRegistrationError
from .utils import Settable as Settable
from typing import Callable, Mapping, Type

CommandFunc = Callable[..., bool | None]

def with_default_category(category: str, *, heritable: bool = True) -> Callable[[Type['CommandSet']], Type['CommandSet']]:
    """
    Decorator that applies a category to all ``do_*`` command methods in a class that do not already
    have a category specified.

    CommandSets that are decorated by this with `heritable` set to True (default) will set a class attribute that is
    inherited by all subclasses unless overridden. All commands of this CommandSet and all subclasses of this CommandSet
    that do not declare an explicit category will be placed in this category. Subclasses may use this decorator to
    override the default category.

    If `heritable` is set to False, then only the commands declared locally to this CommandSet will be placed in the
    specified category. Dynamically created commands, and commands declared in sub-classes will not receive this
    category.

    :param category: category to put all uncategorized commands in
    :param heritable: Flag whether this default category should apply to sub-classes. Defaults to True
    :return: decorator function
    """

class CommandSet:
    """
    Base class for defining sets of commands to load in cmd2.

    ``with_default_category`` can be used to apply a default category to all commands in the CommandSet.

    ``do_``, ``help_``, and ``complete_`` functions differ only in that self is the CommandSet instead of the cmd2 app
    """
    def __init__(self) -> None: ...
    def on_register(self, cmd: cmd2.Cmd) -> None:
        """
        Called by cmd2.Cmd as the first step to registering a CommandSet. The commands defined in this class have
        not been added to the CLI object at this point. Subclasses can override this to perform any initialization
        requiring access to the Cmd object (e.g. configure commands and their parsers based on CLI state data).

        :param cmd: The cmd2 main application
        """
    def on_registered(self) -> None:
        """
        Called by cmd2.Cmd after a CommandSet is registered and all its commands have been added to the CLI.
        Subclasses can override this to perform custom steps related to the newly added commands (e.g. setting
        them to a disabled state).
        """
    def on_unregister(self) -> None:
        """
        Called by ``cmd2.Cmd`` as the first step to unregistering a CommandSet. Subclasses can override this to
        perform any cleanup steps which require their commands being registered in the CLI.
        """
    def on_unregistered(self) -> None:
        """
        Called by ``cmd2.Cmd`` after a CommandSet has been unregistered and all its commands removed from the CLI.
        Subclasses can override this to perform remaining cleanup steps.
        """
    @property
    def settable_prefix(self) -> str: ...
    @property
    def settables(self) -> Mapping[str, Settable]: ...
    def add_settable(self, settable: Settable) -> None:
        """
        Convenience method to add a settable parameter to the CommandSet

        :param settable: Settable object being added
        """
    def remove_settable(self, name: str) -> None:
        """
        Convenience method for removing a settable parameter from the CommandSet

        :param name: name of the settable being removed
        :raises: KeyError if the Settable matches this name
        """
