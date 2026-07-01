import typing as t
from .core import Argument as CoreArgument, Context as Context, Option as CoreOption, Parameter as CoreParameter
from .exceptions import BadArgumentUsage as BadArgumentUsage, BadOptionUsage as BadOptionUsage, NoSuchOption as NoSuchOption, UsageError as UsageError
from _typeshed import Incomplete

V = t.TypeVar('V')

def split_opt(opt: str) -> t.Tuple[str, str]: ...
def normalize_opt(opt: str, ctx: Context | None) -> str: ...
def split_arg_string(string: str) -> t.List[str]:
    '''Split an argument string as with :func:`shlex.split`, but don\'t
    fail if the string is incomplete. Ignores a missing closing quote or
    incomplete escape sequence and uses the partial token as-is.

    .. code-block:: python

        split_arg_string("example \'my file")
        ["example", "my file"]

        split_arg_string("example my\\")
        ["example", "my"]

    :param string: String to split.
    '''

class Option:
    prefixes: Incomplete
    dest: Incomplete
    action: Incomplete
    nargs: Incomplete
    const: Incomplete
    obj: Incomplete
    def __init__(self, obj: CoreOption, opts: t.Sequence[str], dest: str | None, action: str | None = None, nargs: int = 1, const: t.Any | None = None) -> None: ...
    @property
    def takes_value(self) -> bool: ...
    def process(self, value: t.Any, state: ParsingState) -> None: ...

class Argument:
    dest: Incomplete
    nargs: Incomplete
    obj: Incomplete
    def __init__(self, obj: CoreArgument, dest: str | None, nargs: int = 1) -> None: ...
    def process(self, value: str | None | t.Sequence[str | None], state: ParsingState) -> None: ...

class ParsingState:
    opts: Incomplete
    largs: Incomplete
    rargs: Incomplete
    order: Incomplete
    def __init__(self, rargs: t.List[str]) -> None: ...

class OptionParser:
    """The option parser is an internal class that is ultimately used to
    parse options and arguments.  It's modelled after optparse and brings
    a similar but vastly simplified API.  It should generally not be used
    directly as the high level Click classes wrap it for you.

    It's not nearly as extensible as optparse or argparse as it does not
    implement features that are implemented on a higher level (such as
    types or defaults).

    :param ctx: optionally the :class:`~click.Context` where this parser
                should go with.
    """
    ctx: Incomplete
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    def __init__(self, ctx: Context | None = None) -> None: ...
    def add_option(self, obj: CoreOption, opts: t.Sequence[str], dest: str | None, action: str | None = None, nargs: int = 1, const: t.Any | None = None) -> None:
        """Adds a new option named `dest` to the parser.  The destination
        is not inferred (unlike with optparse) and needs to be explicitly
        provided.  Action can be any of ``store``, ``store_const``,
        ``append``, ``append_const`` or ``count``.

        The `obj` can be used to identify the option in the order list
        that is returned from the parser.
        """
    def add_argument(self, obj: CoreArgument, dest: str | None, nargs: int = 1) -> None:
        """Adds a positional argument named `dest` to the parser.

        The `obj` can be used to identify the option in the order list
        that is returned from the parser.
        """
    def parse_args(self, args: t.List[str]) -> t.Tuple[t.Dict[str, t.Any], t.List[str], t.List['CoreParameter']]:
        """Parses positional arguments and returns ``(values, args, order)``
        for the parsed options and arguments as well as the leftover
        arguments if there are any.  The order is a list of objects as they
        appear on the command line.  If arguments appear multiple times they
        will be memorized multiple times as well.
        """
