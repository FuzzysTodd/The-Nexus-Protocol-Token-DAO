import cmd2
from .utils import StdSim as StdSim
from typing import Any, List, NamedTuple

class CommandResult(NamedTuple):
    """Encapsulates the results from a cmd2 app command

    :stdout: str - output captured from stdout while this command is executing
    :stderr: str - output captured from stderr while this command is executing
    :stop: bool - return value of onecmd_plus_hooks after it runs the given
           command line.
    :data: possible data populated by the command.

    Any combination of these fields can be used when developing a scripting API
    for a given command. By default stdout, stderr, and stop will be captured
    for you. If there is additional command specific data, then write that to
    cmd2's last_result member. That becomes the data member of this tuple.

    In some cases, the data member may contain everything needed for a command
    and storing stdout and stderr might just be a duplication of data that
    wastes memory. In that case, the StdSim can be told not to store output
    with its pause_storage member. While this member is True, any output sent
    to StdSim won't be saved in its buffer.

    The code would look like this::

        if isinstance(self.stdout, StdSim):
            self.stdout.pause_storage = True

        if isinstance(sys.stderr, StdSim):
            sys.stderr.pause_storage = True

    See :class:`~cmd2.utils.StdSim` for more information.

    .. note::

       Named tuples are immutable. The contents are there for access,
       not for modification.
    """
    stdout: str = ...
    stderr: str = ...
    stop: bool = ...
    data: Any = ...
    def __bool__(self) -> bool:
        """Returns True if the command succeeded, otherwise False"""

class PyBridge:
    """Provides a Python API wrapper for application commands."""
    cmd_echo: bool
    stop: bool
    def __init__(self, cmd2_app: cmd2.Cmd) -> None: ...
    def __dir__(self) -> List[str]:
        """Return a custom set of attribute names"""
    def __call__(self, command: str, *, echo: bool | None = None) -> CommandResult:
        """
        Provide functionality to call application commands by calling PyBridge
        ex: app('help')
        :param command: command line being run
        :param echo: If provided, this temporarily overrides the value of self.cmd_echo while the
                     command runs. If True, output will be echoed to stdout/stderr. (Defaults to None)

        """
