import enum
import typing as t
import typing_extensions as te
from . import types as types
from .exceptions import Abort as Abort, BadParameter as BadParameter, ClickException as ClickException, Exit as Exit, MissingParameter as MissingParameter, UsageError as UsageError
from .formatting import HelpFormatter as HelpFormatter, join_options as join_options
from .globals import pop_context as pop_context, push_context as push_context
from .parser import OptionParser as OptionParser, split_opt as split_opt
from .shell_completion import CompletionItem as CompletionItem
from .termui import confirm as confirm, prompt as prompt, style as style
from .utils import PacifyFlushWrapper as PacifyFlushWrapper, echo as echo, make_default_short_help as make_default_short_help, make_str as make_str
from _typeshed import Incomplete
from types import TracebackType

F = t.TypeVar('F', bound=t.Callable[..., t.Any])
V = t.TypeVar('V')

def batch(iterable: t.Iterable[V], batch_size: int) -> t.List[t.Tuple[V, ...]]: ...
def augment_usage_errors(ctx: Context, param: Parameter | None = None) -> t.Iterator[None]:
    """Context manager that attaches extra information to exceptions."""
def iter_params_for_processing(invocation_order: t.Sequence['Parameter'], declaration_order: t.Sequence['Parameter']) -> t.List['Parameter']:
    """Given a sequence of parameters in the order as should be considered
    for processing and an iterable of parameters that exist, this returns
    a list in the correct order as they should be processed.
    """

class ParameterSource(enum.Enum):
    """This is an :class:`~enum.Enum` that indicates the source of a
    parameter's value.

    Use :meth:`click.Context.get_parameter_source` to get the
    source for a parameter by name.

    .. versionchanged:: 8.0
        Use :class:`~enum.Enum` and drop the ``validate`` method.

    .. versionchanged:: 8.0
        Added the ``PROMPT`` value.
    """
    COMMANDLINE: Incomplete
    ENVIRONMENT: Incomplete
    DEFAULT: Incomplete
    DEFAULT_MAP: Incomplete
    PROMPT: Incomplete

class Context:
    """The context is a special internal object that holds state relevant
    for the script execution at every single level.  It's normally invisible
    to commands unless they opt-in to getting access to it.

    The context is useful as it can pass internal objects around and can
    control special execution features such as reading data from
    environment variables.

    A context can be used as context manager in which case it will call
    :meth:`close` on teardown.

    :param command: the command class for this context.
    :param parent: the parent context.
    :param info_name: the info name for this invocation.  Generally this
                      is the most descriptive name for the script or
                      command.  For the toplevel script it is usually
                      the name of the script, for commands below it it's
                      the name of the script.
    :param obj: an arbitrary object of user data.
    :param auto_envvar_prefix: the prefix to use for automatic environment
                               variables.  If this is `None` then reading
                               from environment variables is disabled.  This
                               does not affect manually set environment
                               variables which are always read.
    :param default_map: a dictionary (like object) with default values
                        for parameters.
    :param terminal_width: the width of the terminal.  The default is
                           inherit from parent context.  If no context
                           defines the terminal width then auto
                           detection will be applied.
    :param max_content_width: the maximum width for content rendered by
                              Click (this currently only affects help
                              pages).  This defaults to 80 characters if
                              not overridden.  In other words: even if the
                              terminal is larger than that, Click will not
                              format things wider than 80 characters by
                              default.  In addition to that, formatters might
                              add some safety mapping on the right.
    :param resilient_parsing: if this flag is enabled then Click will
                              parse without any interactivity or callback
                              invocation.  Default values will also be
                              ignored.  This is useful for implementing
                              things such as completion support.
    :param allow_extra_args: if this is set to `True` then extra arguments
                             at the end will not raise an error and will be
                             kept on the context.  The default is to inherit
                             from the command.
    :param allow_interspersed_args: if this is set to `False` then options
                                    and arguments cannot be mixed.  The
                                    default is to inherit from the command.
    :param ignore_unknown_options: instructs click to ignore options it does
                                   not know and keeps them for later
                                   processing.
    :param help_option_names: optionally a list of strings that define how
                              the default help parameter is named.  The
                              default is ``['--help']``.
    :param token_normalize_func: an optional function that is used to
                                 normalize tokens (options, choices,
                                 etc.).  This for instance can be used to
                                 implement case insensitive behavior.
    :param color: controls if the terminal supports ANSI colors or not.  The
                  default is autodetection.  This is only needed if ANSI
                  codes are used in texts that Click prints which is by
                  default not the case.  This for instance would affect
                  help output.
    :param show_default: Show the default value for commands. If this
        value is not set, it defaults to the value from the parent
        context. ``Command.show_default`` overrides this default for the
        specific command.

    .. versionchanged:: 8.1
        The ``show_default`` parameter is overridden by
        ``Command.show_default``, instead of the other way around.

    .. versionchanged:: 8.0
        The ``show_default`` parameter defaults to the value from the
        parent context.

    .. versionchanged:: 7.1
       Added the ``show_default`` parameter.

    .. versionchanged:: 4.0
        Added the ``color``, ``ignore_unknown_options``, and
        ``max_content_width`` parameters.

    .. versionchanged:: 3.0
        Added the ``allow_extra_args`` and ``allow_interspersed_args``
        parameters.

    .. versionchanged:: 2.0
        Added the ``resilient_parsing``, ``help_option_names``, and
        ``token_normalize_func`` parameters.
    """
    formatter_class: t.Type['HelpFormatter']
    parent: Incomplete
    command: Incomplete
    info_name: Incomplete
    params: Incomplete
    args: Incomplete
    protected_args: Incomplete
    obj: Incomplete
    default_map: Incomplete
    invoked_subcommand: Incomplete
    terminal_width: Incomplete
    max_content_width: Incomplete
    allow_extra_args: Incomplete
    allow_interspersed_args: Incomplete
    ignore_unknown_options: Incomplete
    help_option_names: Incomplete
    token_normalize_func: Incomplete
    resilient_parsing: Incomplete
    auto_envvar_prefix: Incomplete
    color: Incomplete
    show_default: Incomplete
    def __init__(self, command: Command, parent: Context | None = None, info_name: str | None = None, obj: t.Any | None = None, auto_envvar_prefix: str | None = None, default_map: t.MutableMapping[str, t.Any] | None = None, terminal_width: int | None = None, max_content_width: int | None = None, resilient_parsing: bool = False, allow_extra_args: bool | None = None, allow_interspersed_args: bool | None = None, ignore_unknown_options: bool | None = None, help_option_names: t.List[str] | None = None, token_normalize_func: t.Callable[[str], str] | None = None, color: bool | None = None, show_default: bool | None = None) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]:
        """Gather information that could be useful for a tool generating
        user-facing documentation. This traverses the entire CLI
        structure.

        .. code-block:: python

            with Context(cli) as ctx:
                info = ctx.to_info_dict()

        .. versionadded:: 8.0
        """
    def __enter__(self) -> Context: ...
    def __exit__(self, exc_type: t.Type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None: ...
    def scope(self, cleanup: bool = True) -> t.Iterator['Context']:
        """This helper method can be used with the context object to promote
        it to the current thread local (see :func:`get_current_context`).
        The default behavior of this is to invoke the cleanup functions which
        can be disabled by setting `cleanup` to `False`.  The cleanup
        functions are typically used for things such as closing file handles.

        If the cleanup is intended the context object can also be directly
        used as a context manager.

        Example usage::

            with ctx.scope():
                assert get_current_context() is ctx

        This is equivalent::

            with ctx:
                assert get_current_context() is ctx

        .. versionadded:: 5.0

        :param cleanup: controls if the cleanup functions should be run or
                        not.  The default is to run these functions.  In
                        some situations the context only wants to be
                        temporarily pushed in which case this can be disabled.
                        Nested pushes automatically defer the cleanup.
        """
    @property
    def meta(self) -> t.Dict[str, t.Any]:
        """This is a dictionary which is shared with all the contexts
        that are nested.  It exists so that click utilities can store some
        state here if they need to.  It is however the responsibility of
        that code to manage this dictionary well.

        The keys are supposed to be unique dotted strings.  For instance
        module paths are a good choice for it.  What is stored in there is
        irrelevant for the operation of click.  However what is important is
        that code that places data here adheres to the general semantics of
        the system.

        Example usage::

            LANG_KEY = f'{__name__}.lang'

            def set_language(value):
                ctx = get_current_context()
                ctx.meta[LANG_KEY] = value

            def get_language():
                return get_current_context().meta.get(LANG_KEY, 'en_US')

        .. versionadded:: 5.0
        """
    def make_formatter(self) -> HelpFormatter:
        """Creates the :class:`~click.HelpFormatter` for the help and
        usage output.

        To quickly customize the formatter class used without overriding
        this method, set the :attr:`formatter_class` attribute.

        .. versionchanged:: 8.0
            Added the :attr:`formatter_class` attribute.
        """
    def with_resource(self, context_manager: t.ContextManager[V]) -> V:
        '''Register a resource as if it were used in a ``with``
        statement. The resource will be cleaned up when the context is
        popped.

        Uses :meth:`contextlib.ExitStack.enter_context`. It calls the
        resource\'s ``__enter__()`` method and returns the result. When
        the context is popped, it closes the stack, which calls the
        resource\'s ``__exit__()`` method.

        To register a cleanup function for something that isn\'t a
        context manager, use :meth:`call_on_close`. Or use something
        from :mod:`contextlib` to turn it into a context manager first.

        .. code-block:: python

            @click.group()
            @click.option("--name")
            @click.pass_context
            def cli(ctx):
                ctx.obj = ctx.with_resource(connect_db(name))

        :param context_manager: The context manager to enter.
        :return: Whatever ``context_manager.__enter__()`` returns.

        .. versionadded:: 8.0
        '''
    def call_on_close(self, f: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
        """Register a function to be called when the context tears down.

        This can be used to close resources opened during the script
        execution. Resources that support Python's context manager
        protocol which would be used in a ``with`` statement should be
        registered with :meth:`with_resource` instead.

        :param f: The function to execute on teardown.
        """
    def close(self) -> None:
        """Invoke all close callbacks registered with
        :meth:`call_on_close`, and exit all context managers entered
        with :meth:`with_resource`.
        """
    @property
    def command_path(self) -> str:
        """The computed command path.  This is used for the ``usage``
        information on the help page.  It's automatically created by
        combining the info names of the chain of contexts to the root.
        """
    def find_root(self) -> Context:
        """Finds the outermost context."""
    def find_object(self, object_type: t.Type[V]) -> V | None:
        """Finds the closest object of a given type."""
    def ensure_object(self, object_type: t.Type[V]) -> V:
        """Like :meth:`find_object` but sets the innermost object to a
        new instance of `object_type` if it does not exist.
        """
    @t.overload
    def lookup_default(self, name: str, call: te.Literal[True] = True) -> t.Any | None: ...
    @t.overload
    def lookup_default(self, name: str, call: te.Literal[False] = ...) -> t.Any | t.Callable[[], t.Any] | None: ...
    def fail(self, message: str) -> te.NoReturn:
        """Aborts the execution of the program with a specific error
        message.

        :param message: the error message to fail with.
        """
    def abort(self) -> te.NoReturn:
        """Aborts the script."""
    def exit(self, code: int = 0) -> te.NoReturn:
        """Exits the application with a given exit code."""
    def get_usage(self) -> str:
        """Helper method to get formatted usage string for the current
        context and command.
        """
    def get_help(self) -> str:
        """Helper method to get formatted help page for the current
        context and command.
        """
    @t.overload
    def invoke(__self, __callback: t.Callable[..., V], *args: t.Any, **kwargs: t.Any) -> V: ...
    @t.overload
    def invoke(__self, __callback: Command, *args: t.Any, **kwargs: t.Any) -> t.Any: ...
    def forward(__self, __cmd: Command, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Similar to :meth:`invoke` but fills in default keyword
        arguments from the current context if the other command expects
        it.  This cannot invoke callbacks directly, only other commands.

        .. versionchanged:: 8.0
            All ``kwargs`` are tracked in :attr:`params` so they will be
            passed if ``forward`` is called at multiple levels.
        """
    def set_parameter_source(self, name: str, source: ParameterSource) -> None:
        """Set the source of a parameter. This indicates the location
        from which the value of the parameter was obtained.

        :param name: The name of the parameter.
        :param source: A member of :class:`~click.core.ParameterSource`.
        """
    def get_parameter_source(self, name: str) -> ParameterSource | None:
        """Get the source of a parameter. This indicates the location
        from which the value of the parameter was obtained.

        This can be useful for determining when a user specified a value
        on the command line that is the same as the default value. It
        will be :attr:`~click.core.ParameterSource.DEFAULT` only if the
        value was actually taken from the default.

        :param name: The name of the parameter.
        :rtype: ParameterSource

        .. versionchanged:: 8.0
            Returns ``None`` if the parameter was not provided from any
            source.
        """

class BaseCommand:
    """The base command implements the minimal API contract of commands.
    Most code will never use this as it does not implement a lot of useful
    functionality but it can act as the direct subclass of alternative
    parsing methods that do not depend on the Click parser.

    For instance, this can be used to bridge Click and other systems like
    argparse or docopt.

    Because base commands do not implement a lot of the API that other
    parts of Click take for granted, they are not supported for all
    operations.  For instance, they cannot be used with the decorators
    usually and they have no built-in callback system.

    .. versionchanged:: 2.0
       Added the `context_settings` parameter.

    :param name: the name of the command to use unless a group overrides it.
    :param context_settings: an optional dictionary with defaults that are
                             passed to the context object.
    """
    context_class: t.Type[Context]
    allow_extra_args: bool
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    name: Incomplete
    context_settings: Incomplete
    def __init__(self, name: str | None, context_settings: t.MutableMapping[str, t.Any] | None = None) -> None: ...
    def to_info_dict(self, ctx: Context) -> t.Dict[str, t.Any]:
        """Gather information that could be useful for a tool generating
        user-facing documentation. This traverses the entire structure
        below this command.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        :param ctx: A :class:`Context` representing this command.

        .. versionadded:: 8.0
        """
    def get_usage(self, ctx: Context) -> str: ...
    def get_help(self, ctx: Context) -> str: ...
    def make_context(self, info_name: str | None, args: t.List[str], parent: Context | None = None, **extra: t.Any) -> Context:
        """This function when given an info name and arguments will kick
        off the parsing and create a new :class:`Context`.  It does not
        invoke the actual command callback though.

        To quickly customize the context class used without overriding
        this method, set the :attr:`context_class` attribute.

        :param info_name: the info name for this invocation.  Generally this
                          is the most descriptive name for the script or
                          command.  For the toplevel script it's usually
                          the name of the script, for commands below it's
                          the name of the command.
        :param args: the arguments to parse as list of strings.
        :param parent: the parent context if available.
        :param extra: extra keyword arguments forwarded to the context
                      constructor.

        .. versionchanged:: 8.0
            Added the :attr:`context_class` attribute.
        """
    def parse_args(self, ctx: Context, args: t.List[str]) -> t.List[str]:
        """Given a context and a list of arguments this creates the parser
        and parses the arguments, then modifies the context as necessary.
        This is automatically invoked by :meth:`make_context`.
        """
    def invoke(self, ctx: Context) -> t.Any:
        """Given a context, this invokes the command.  The default
        implementation is raising a not implemented error.
        """
    def shell_complete(self, ctx: Context, incomplete: str) -> t.List['CompletionItem']:
        """Return a list of completions for the incomplete value. Looks
        at the names of chained multi-commands.

        Any command could be part of a chained multi-command, so sibling
        commands are valid at any point during command completion. Other
        command classes will return more completions.

        :param ctx: Invocation context for this command.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """
    @t.overload
    def main(self, args: t.Sequence[str] | None = None, prog_name: str | None = None, complete_var: str | None = None, standalone_mode: te.Literal[True] = True, **extra: t.Any) -> te.NoReturn: ...
    @t.overload
    def main(self, args: t.Sequence[str] | None = None, prog_name: str | None = None, complete_var: str | None = None, standalone_mode: bool = ..., **extra: t.Any) -> t.Any: ...
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Alias for :meth:`main`."""

class Command(BaseCommand):
    """Commands are the basic building block of command line interfaces in
    Click.  A basic command handles command line parsing and might dispatch
    more parsing to commands nested below it.

    :param name: the name of the command to use unless a group overrides it.
    :param context_settings: an optional dictionary with defaults that are
                             passed to the context object.
    :param callback: the callback to invoke.  This is optional.
    :param params: the parameters to register with this command.  This can
                   be either :class:`Option` or :class:`Argument` objects.
    :param help: the help string to use for this command.
    :param epilog: like the help string but it's printed at the end of the
                   help page after everything else.
    :param short_help: the short help to use for this command.  This is
                       shown on the command listing of the parent command.
    :param add_help_option: by default each command registers a ``--help``
                            option.  This can be disabled by this parameter.
    :param no_args_is_help: this controls what happens if no arguments are
                            provided.  This option is disabled by default.
                            If enabled this will add ``--help`` as argument
                            if no arguments are passed
    :param hidden: hide this command from help outputs.

    :param deprecated: issues a message indicating that
                             the command is deprecated.

    .. versionchanged:: 8.1
        ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
        all formatting is done when outputting help text, not at init,
        and is done even if not using the ``@command`` decorator.

    .. versionchanged:: 8.0
        Added a ``repr`` showing the command name.

    .. versionchanged:: 7.1
        Added the ``no_args_is_help`` parameter.

    .. versionchanged:: 2.0
        Added the ``context_settings`` parameter.
    """
    callback: Incomplete
    params: Incomplete
    help: Incomplete
    epilog: Incomplete
    options_metavar: Incomplete
    short_help: Incomplete
    add_help_option: Incomplete
    no_args_is_help: Incomplete
    hidden: Incomplete
    deprecated: Incomplete
    def __init__(self, name: str | None, context_settings: t.MutableMapping[str, t.Any] | None = None, callback: t.Callable[..., t.Any] | None = None, params: t.List['Parameter'] | None = None, help: str | None = None, epilog: str | None = None, short_help: str | None = None, options_metavar: str | None = '[OPTIONS]', add_help_option: bool = True, no_args_is_help: bool = False, hidden: bool = False, deprecated: bool = False) -> None: ...
    def to_info_dict(self, ctx: Context) -> t.Dict[str, t.Any]: ...
    def get_usage(self, ctx: Context) -> str:
        """Formats the usage line into a string and returns it.

        Calls :meth:`format_usage` internally.
        """
    def get_params(self, ctx: Context) -> t.List['Parameter']: ...
    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Writes the usage line into the formatter.

        This is a low-level method called by :meth:`get_usage`.
        """
    def collect_usage_pieces(self, ctx: Context) -> t.List[str]:
        """Returns all the pieces that go into the usage line and returns
        it as a list of strings.
        """
    def get_help_option_names(self, ctx: Context) -> t.List[str]:
        """Returns the names for the help option."""
    def get_help_option(self, ctx: Context) -> Option | None:
        """Returns the help option object."""
    def make_parser(self, ctx: Context) -> OptionParser:
        """Creates the underlying option parser for this command."""
    def get_help(self, ctx: Context) -> str:
        """Formats the help into a string and returns it.

        Calls :meth:`format_help` internally.
        """
    def get_short_help_str(self, limit: int = 45) -> str:
        """Gets short help for the command or makes it by shortening the
        long help string.
        """
    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Writes the help into the formatter if it exists.

        This is a low-level method called by :meth:`get_help`.

        This calls the following methods:

        -   :meth:`format_usage`
        -   :meth:`format_help_text`
        -   :meth:`format_options`
        -   :meth:`format_epilog`
        """
    def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Writes the help text to the formatter if it exists."""
    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Writes all the options into the formatter if they exist."""
    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Writes the epilog into the formatter if it exists."""
    def parse_args(self, ctx: Context, args: t.List[str]) -> t.List[str]: ...
    def invoke(self, ctx: Context) -> t.Any:
        """Given a context, this invokes the attached callback (if it exists)
        in the right way.
        """
    def shell_complete(self, ctx: Context, incomplete: str) -> t.List['CompletionItem']:
        """Return a list of completions for the incomplete value. Looks
        at the names of options and chained multi-commands.

        :param ctx: Invocation context for this command.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class MultiCommand(Command):
    """A multi command is the basic implementation of a command that
    dispatches to subcommands.  The most common version is the
    :class:`Group`.

    :param invoke_without_command: this controls how the multi command itself
                                   is invoked.  By default it's only invoked
                                   if a subcommand is provided.
    :param no_args_is_help: this controls what happens if no arguments are
                            provided.  This option is enabled by default if
                            `invoke_without_command` is disabled or disabled
                            if it's enabled.  If enabled this will add
                            ``--help`` as argument if no arguments are
                            passed.
    :param subcommand_metavar: the string that is used in the documentation
                               to indicate the subcommand place.
    :param chain: if this is set to `True` chaining of multiple subcommands
                  is enabled.  This restricts the form of commands in that
                  they cannot have optional arguments but it allows
                  multiple commands to be chained together.
    :param result_callback: The result callback to attach to this multi
        command. This can be set or changed later with the
        :meth:`result_callback` decorator.
    :param attrs: Other command arguments described in :class:`Command`.
    """
    allow_extra_args: bool
    allow_interspersed_args: bool
    no_args_is_help: Incomplete
    invoke_without_command: Incomplete
    subcommand_metavar: Incomplete
    chain: Incomplete
    def __init__(self, name: str | None = None, invoke_without_command: bool = False, no_args_is_help: bool | None = None, subcommand_metavar: str | None = None, chain: bool = False, result_callback: t.Callable[..., t.Any] | None = None, **attrs: t.Any) -> None: ...
    def to_info_dict(self, ctx: Context) -> t.Dict[str, t.Any]: ...
    def collect_usage_pieces(self, ctx: Context) -> t.List[str]: ...
    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def result_callback(self, replace: bool = False) -> t.Callable[[F], F]:
        """Adds a result callback to the command.  By default if a
        result callback is already registered this will chain them but
        this can be disabled with the `replace` parameter.  The result
        callback is invoked with the return value of the subcommand
        (or the list of return values from all subcommands if chaining
        is enabled) as well as the parameters as they would be passed
        to the main callback.

        Example::

            @click.group()
            @click.option('-i', '--input', default=23)
            def cli(input):
                return 42

            @cli.result_callback()
            def process_result(result, input):
                return result + input

        :param replace: if set to `True` an already existing result
                        callback will be removed.

        .. versionchanged:: 8.0
            Renamed from ``resultcallback``.

        .. versionadded:: 3.0
        """
    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        """Extra format methods for multi methods that adds all the commands
        after the options.
        """
    def parse_args(self, ctx: Context, args: t.List[str]) -> t.List[str]: ...
    def invoke(self, ctx: Context) -> t.Any: ...
    def resolve_command(self, ctx: Context, args: t.List[str]) -> t.Tuple[str | None, Command | None, t.List[str]]: ...
    def get_command(self, ctx: Context, cmd_name: str) -> Command | None:
        """Given a context and a command name, this returns a
        :class:`Command` object if it exists or returns `None`.
        """
    def list_commands(self, ctx: Context) -> t.List[str]:
        """Returns a list of subcommand names in the order they should
        appear.
        """
    def shell_complete(self, ctx: Context, incomplete: str) -> t.List['CompletionItem']:
        """Return a list of completions for the incomplete value. Looks
        at the names of options, subcommands, and chained
        multi-commands.

        :param ctx: Invocation context for this command.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class Group(MultiCommand):
    """A group allows a command to have subcommands attached. This is
    the most common way to implement nesting in Click.

    :param name: The name of the group command.
    :param commands: A dict mapping names to :class:`Command` objects.
        Can also be a list of :class:`Command`, which will use
        :attr:`Command.name` to create the dict.
    :param attrs: Other command arguments described in
        :class:`MultiCommand`, :class:`Command`, and
        :class:`BaseCommand`.

    .. versionchanged:: 8.0
        The ``commands`` argument can be a list of command objects.
    """
    command_class: t.Type[Command] | None
    group_class: t.Type['Group'] | t.Type[type] | None
    commands: Incomplete
    def __init__(self, name: str | None = None, commands: t.MutableMapping[str, Command] | t.Sequence[Command] | None = None, **attrs: t.Any) -> None: ...
    def add_command(self, cmd: Command, name: str | None = None) -> None:
        """Registers another :class:`Command` with this group.  If the name
        is not provided, the name of the command is used.
        """
    @t.overload
    def command(self, __func: t.Callable[..., t.Any]) -> Command: ...
    @t.overload
    def command(self, *args: t.Any, **kwargs: t.Any) -> t.Callable[[t.Callable[..., t.Any]], Command]: ...
    @t.overload
    def group(self, __func: t.Callable[..., t.Any]) -> Group: ...
    @t.overload
    def group(self, *args: t.Any, **kwargs: t.Any) -> t.Callable[[t.Callable[..., t.Any]], 'Group']: ...
    def get_command(self, ctx: Context, cmd_name: str) -> Command | None: ...
    def list_commands(self, ctx: Context) -> t.List[str]: ...

class CommandCollection(MultiCommand):
    """A command collection is a multi command that merges multiple multi
    commands together into one.  This is a straightforward implementation
    that accepts a list of different multi commands as sources and
    provides all the commands for each of them.

    See :class:`MultiCommand` and :class:`Command` for the description of
    ``name`` and ``attrs``.
    """
    sources: Incomplete
    def __init__(self, name: str | None = None, sources: t.List[MultiCommand] | None = None, **attrs: t.Any) -> None: ...
    def add_source(self, multi_cmd: MultiCommand) -> None:
        """Adds a new multi command to the chain dispatcher."""
    def get_command(self, ctx: Context, cmd_name: str) -> Command | None: ...
    def list_commands(self, ctx: Context) -> t.List[str]: ...

class Parameter:
    """A parameter to a command comes in two versions: they are either
    :class:`Option`\\s or :class:`Argument`\\s.  Other subclasses are currently
    not supported by design as some of the internals for parsing are
    intentionally not finalized.

    Some settings are supported by both options and arguments.

    :param param_decls: the parameter declarations for this option or
                        argument.  This is a list of flags or argument
                        names.
    :param type: the type that should be used.  Either a :class:`ParamType`
                 or a Python type.  The latter is converted into the former
                 automatically if supported.
    :param required: controls if this is optional or not.
    :param default: the default value if omitted.  This can also be a callable,
                    in which case it's invoked when the default is needed
                    without any arguments.
    :param callback: A function to further process or validate the value
        after type conversion. It is called as ``f(ctx, param, value)``
        and must return the value. It is called for all sources,
        including prompts.
    :param nargs: the number of arguments to match.  If not ``1`` the return
                  value is a tuple instead of single value.  The default for
                  nargs is ``1`` (except if the type is a tuple, then it's
                  the arity of the tuple). If ``nargs=-1``, all remaining
                  parameters are collected.
    :param metavar: how the value is represented in the help page.
    :param expose_value: if this is `True` then the value is passed onwards
                         to the command callback and stored on the context,
                         otherwise it's skipped.
    :param is_eager: eager values are processed before non eager ones.  This
                     should not be set for arguments or it will inverse the
                     order of processing.
    :param envvar: a string or list of strings that are environment variables
                   that should be checked.
    :param shell_complete: A function that returns custom shell
        completions. Used instead of the param's type completion if
        given. Takes ``ctx, param, incomplete`` and must return a list
        of :class:`~click.shell_completion.CompletionItem` or a list of
        strings.

    .. versionchanged:: 8.0
        ``process_value`` validates required parameters and bounded
        ``nargs``, and invokes the parameter callback before returning
        the value. This allows the callback to validate prompts.
        ``full_process_value`` is removed.

    .. versionchanged:: 8.0
        ``autocompletion`` is renamed to ``shell_complete`` and has new
        semantics described above. The old name is deprecated and will
        be removed in 8.1, until then it will be wrapped to match the
        new requirements.

    .. versionchanged:: 8.0
        For ``multiple=True, nargs>1``, the default must be a list of
        tuples.

    .. versionchanged:: 8.0
        Setting a default is no longer required for ``nargs>1``, it will
        default to ``None``. ``multiple=True`` or ``nargs=-1`` will
        default to ``()``.

    .. versionchanged:: 7.1
        Empty environment variables are ignored rather than taking the
        empty string value. This makes it possible for scripts to clear
        variables if they can't unset them.

    .. versionchanged:: 2.0
        Changed signature for parameter callback to also be passed the
        parameter. The old callback format will still work, but it will
        raise a warning to give you a chance to migrate the code easier.
    """
    param_type_name: str
    name: Incomplete
    opts: Incomplete
    secondary_opts: Incomplete
    type: Incomplete
    required: Incomplete
    callback: Incomplete
    nargs: Incomplete
    multiple: Incomplete
    expose_value: Incomplete
    default: Incomplete
    is_eager: Incomplete
    metavar: Incomplete
    envvar: Incomplete
    def __init__(self, param_decls: t.Sequence[str] | None = None, type: types.ParamType | t.Any | None = None, required: bool = False, default: t.Any | t.Callable[[], t.Any] | None = None, callback: t.Callable[[Context, Parameter, t.Any], t.Any] | None = None, nargs: int | None = None, multiple: bool = False, metavar: str | None = None, expose_value: bool = True, is_eager: bool = False, envvar: str | t.Sequence[str] | None = None, shell_complete: t.Callable[[Context, Parameter, str], t.List['CompletionItem'] | t.List[str]] | None = None) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]:
        """Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionadded:: 8.0
        """
    @property
    def human_readable_name(self) -> str:
        """Returns the human readable name of this parameter.  This is the
        same as the name for options, but the metavar for arguments.
        """
    def make_metavar(self) -> str: ...
    @t.overload
    def get_default(self, ctx: Context, call: te.Literal[True] = True) -> t.Any | None: ...
    @t.overload
    def get_default(self, ctx: Context, call: bool = ...) -> t.Any | t.Callable[[], t.Any] | None: ...
    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None: ...
    def consume_value(self, ctx: Context, opts: t.Mapping[str, t.Any]) -> t.Tuple[t.Any, ParameterSource]: ...
    def type_cast_value(self, ctx: Context, value: t.Any) -> t.Any:
        """Convert and validate a value against the option's
        :attr:`type`, :attr:`multiple`, and :attr:`nargs`.
        """
    def value_is_missing(self, value: t.Any) -> bool: ...
    def process_value(self, ctx: Context, value: t.Any) -> t.Any: ...
    def resolve_envvar_value(self, ctx: Context) -> str | None: ...
    def value_from_envvar(self, ctx: Context) -> t.Any | None: ...
    def handle_parse_result(self, ctx: Context, opts: t.Mapping[str, t.Any], args: t.List[str]) -> t.Tuple[t.Any, t.List[str]]: ...
    def get_help_record(self, ctx: Context) -> t.Tuple[str, str] | None: ...
    def get_usage_pieces(self, ctx: Context) -> t.List[str]: ...
    def get_error_hint(self, ctx: Context) -> str:
        """Get a stringified version of the param for use in error messages to
        indicate which param caused the error.
        """
    def shell_complete(self, ctx: Context, incomplete: str) -> t.List['CompletionItem']:
        """Return a list of completions for the incomplete value. If a
        ``shell_complete`` function was given during init, it is used.
        Otherwise, the :attr:`type`
        :meth:`~click.types.ParamType.shell_complete` function is used.

        :param ctx: Invocation context for this command.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class Option(Parameter):
    """Options are usually optional values on the command line and
    have some extra features that arguments don't have.

    All other parameters are passed onwards to the parameter constructor.

    :param show_default: Show the default value for this option in its
        help text. Values are not shown by default, unless
        :attr:`Context.show_default` is ``True``. If this value is a
        string, it shows that string in parentheses instead of the
        actual value. This is particularly useful for dynamic options.
        For single option boolean flags, the default remains hidden if
        its value is ``False``.
    :param show_envvar: Controls if an environment variable should be
        shown on the help page. Normally, environment variables are not
        shown.
    :param prompt: If set to ``True`` or a non empty string then the
        user will be prompted for input. If set to ``True`` the prompt
        will be the option name capitalized.
    :param confirmation_prompt: Prompt a second time to confirm the
        value if it was prompted for. Can be set to a string instead of
        ``True`` to customize the message.
    :param prompt_required: If set to ``False``, the user will be
        prompted for input only when the option was specified as a flag
        without a value.
    :param hide_input: If this is ``True`` then the input on the prompt
        will be hidden from the user. This is useful for password input.
    :param is_flag: forces this option to act as a flag.  The default is
                    auto detection.
    :param flag_value: which value should be used for this flag if it's
                       enabled.  This is set to a boolean automatically if
                       the option string contains a slash to mark two options.
    :param multiple: if this is set to `True` then the argument is accepted
                     multiple times and recorded.  This is similar to ``nargs``
                     in how it works but supports arbitrary number of
                     arguments.
    :param count: this flag makes an option increment an integer.
    :param allow_from_autoenv: if this is enabled then the value of this
                               parameter will be pulled from an environment
                               variable in case a prefix is defined on the
                               context.
    :param help: the help string.
    :param hidden: hide this option from help outputs.
    :param attrs: Other command arguments described in :class:`Parameter`.

    .. versionchanged:: 8.1.0
        Help text indentation is cleaned here instead of only in the
        ``@option`` decorator.

    .. versionchanged:: 8.1.0
        The ``show_default`` parameter overrides
        ``Context.show_default``.

    .. versionchanged:: 8.1.0
        The default of a single option boolean flag is not shown if the
        default value is ``False``.

    .. versionchanged:: 8.0.1
        ``type`` is detected from ``flag_value`` if given.
    """
    param_type_name: str
    prompt: Incomplete
    confirmation_prompt: Incomplete
    prompt_required: Incomplete
    hide_input: Incomplete
    hidden: Incomplete
    default: Incomplete
    type: Incomplete
    is_flag: Incomplete
    is_bool_flag: Incomplete
    flag_value: Incomplete
    count: Incomplete
    allow_from_autoenv: Incomplete
    help: Incomplete
    show_default: Incomplete
    show_choices: Incomplete
    show_envvar: Incomplete
    def __init__(self, param_decls: t.Sequence[str] | None = None, show_default: bool | str | None = None, prompt: bool | str = False, confirmation_prompt: bool | str = False, prompt_required: bool = True, hide_input: bool = False, is_flag: bool | None = None, flag_value: t.Any | None = None, multiple: bool = False, count: bool = False, allow_from_autoenv: bool = True, type: types.ParamType | t.Any | None = None, help: str | None = None, hidden: bool = False, show_choices: bool = True, show_envvar: bool = False, **attrs: t.Any) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None: ...
    def get_help_record(self, ctx: Context) -> t.Tuple[str, str] | None: ...
    @t.overload
    def get_default(self, ctx: Context, call: te.Literal[True] = True) -> t.Any | None: ...
    @t.overload
    def get_default(self, ctx: Context, call: bool = ...) -> t.Any | t.Callable[[], t.Any] | None: ...
    def prompt_for_value(self, ctx: Context) -> t.Any:
        """This is an alternative flow that can be activated in the full
        value processing if a value does not exist.  It will prompt the
        user until a valid value exists and then returns the processed
        value as result.
        """
    def resolve_envvar_value(self, ctx: Context) -> str | None: ...
    def value_from_envvar(self, ctx: Context) -> t.Any | None: ...
    def consume_value(self, ctx: Context, opts: t.Mapping[str, 'Parameter']) -> t.Tuple[t.Any, ParameterSource]: ...

class Argument(Parameter):
    """Arguments are positional parameters to a command.  They generally
    provide fewer features than options but can have infinite ``nargs``
    and are required by default.

    All parameters are passed onwards to the constructor of :class:`Parameter`.
    """
    param_type_name: str
    def __init__(self, param_decls: t.Sequence[str], required: bool | None = None, **attrs: t.Any) -> None: ...
    @property
    def human_readable_name(self) -> str: ...
    def make_metavar(self) -> str: ...
    def get_usage_pieces(self, ctx: Context) -> t.List[str]: ...
    def get_error_hint(self, ctx: Context) -> str: ...
    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None: ...
