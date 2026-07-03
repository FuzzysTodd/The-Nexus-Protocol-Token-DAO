import typing as t
from .core import Argument as Argument, BaseCommand as BaseCommand, Context as Context, MultiCommand as MultiCommand, Option as Option, Parameter as Parameter, ParameterSource as ParameterSource
from .parser import split_arg_string as split_arg_string
from .utils import echo as echo
from _typeshed import Incomplete

def shell_complete(cli: BaseCommand, ctx_args: t.MutableMapping[str, t.Any], prog_name: str, complete_var: str, instruction: str) -> int:
    """Perform shell completion for the given CLI program.

    :param cli: Command being called.
    :param ctx_args: Extra arguments to pass to
        ``cli.make_context``.
    :param prog_name: Name of the executable in the shell.
    :param complete_var: Name of the environment variable that holds
        the completion instruction.
    :param instruction: Value of ``complete_var`` with the completion
        instruction and shell, in the form ``instruction_shell``.
    :return: Status code to exit with.
    """

class CompletionItem:
    '''Represents a completion value and metadata about the value. The
    default metadata is ``type`` to indicate special shell handling,
    and ``help`` if a shell supports showing a help string next to the
    value.

    Arbitrary parameters can be passed when creating the object, and
    accessed using ``item.attr``. If an attribute wasn\'t passed,
    accessing it returns ``None``.

    :param value: The completion suggestion.
    :param type: Tells the shell script to provide special completion
        support for the type. Click uses ``"dir"`` and ``"file"``.
    :param help: String shown next to the value if supported.
    :param kwargs: Arbitrary metadata. The built-in implementations
        don\'t use this, but custom type completions paired with custom
        shell support could use it.
    '''
    value: Incomplete
    type: Incomplete
    help: Incomplete
    def __init__(self, value: t.Any, type: str = 'plain', help: str | None = None, **kwargs: t.Any) -> None: ...
    def __getattr__(self, name: str) -> t.Any: ...

class ShellComplete:
    """Base class for providing shell completion support. A subclass for
    a given shell will override attributes and methods to implement the
    completion instructions (``source`` and ``complete``).

    :param cli: Command being called.
    :param prog_name: Name of the executable in the shell.
    :param complete_var: Name of the environment variable that holds
        the completion instruction.

    .. versionadded:: 8.0
    """
    name: t.ClassVar[str]
    source_template: t.ClassVar[str]
    cli: Incomplete
    ctx_args: Incomplete
    prog_name: Incomplete
    complete_var: Incomplete
    def __init__(self, cli: BaseCommand, ctx_args: t.MutableMapping[str, t.Any], prog_name: str, complete_var: str) -> None: ...
    @property
    def func_name(self) -> str:
        """The name of the shell function defined by the completion
        script.
        """
    def source_vars(self) -> t.Dict[str, t.Any]:
        """Vars for formatting :attr:`source_template`.

        By default this provides ``complete_func``, ``complete_var``,
        and ``prog_name``.
        """
    def source(self) -> str:
        """Produce the shell script that defines the completion
        function. By default this ``%``-style formats
        :attr:`source_template` with the dict returned by
        :meth:`source_vars`.
        """
    def get_completion_args(self) -> t.Tuple[t.List[str], str]:
        """Use the env vars defined by the shell script to return a
        tuple of ``args, incomplete``. This must be implemented by
        subclasses.
        """
    def get_completions(self, args: t.List[str], incomplete: str) -> t.List[CompletionItem]:
        """Determine the context and last complete command or parameter
        from the complete args. Call that object's ``shell_complete``
        method to get the completions for the incomplete value.

        :param args: List of complete args before the incomplete value.
        :param incomplete: Value being completed. May be empty.
        """
    def format_completion(self, item: CompletionItem) -> str:
        """Format a completion item into the form recognized by the
        shell script. This must be implemented by subclasses.

        :param item: Completion item to format.
        """
    def complete(self) -> str:
        """Produce the completion data to send back to the shell.

        By default this calls :meth:`get_completion_args`, gets the
        completions, then calls :meth:`format_completion` for each
        completion.
        """

class BashComplete(ShellComplete):
    """Shell completion for Bash."""
    name: str
    source_template: Incomplete
    def source(self) -> str: ...
    def get_completion_args(self) -> t.Tuple[t.List[str], str]: ...
    def format_completion(self, item: CompletionItem) -> str: ...

class ZshComplete(ShellComplete):
    """Shell completion for Zsh."""
    name: str
    source_template: Incomplete
    def get_completion_args(self) -> t.Tuple[t.List[str], str]: ...
    def format_completion(self, item: CompletionItem) -> str: ...

class FishComplete(ShellComplete):
    """Shell completion for Fish."""
    name: str
    source_template: Incomplete
    def get_completion_args(self) -> t.Tuple[t.List[str], str]: ...
    def format_completion(self, item: CompletionItem) -> str: ...
ShellCompleteType = t.TypeVar('ShellCompleteType', bound=t.Type[ShellComplete])

def add_completion_class(cls, name: str | None = None) -> ShellCompleteType:
    """Register a :class:`ShellComplete` subclass under the given name.
    The name will be provided by the completion instruction environment
    variable during completion.

    :param cls: The completion class that will handle completion for the
        shell.
    :param name: Name to register the class under. Defaults to the
        class's ``name`` attribute.
    """
def get_completion_class(shell: str) -> t.Type[ShellComplete] | None:
    """Look up a registered :class:`ShellComplete` subclass by the name
    provided by the completion instruction environment variable. If the
    name isn't registered, returns ``None``.

    :param shell: Name the class is registered under.
    """
