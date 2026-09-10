from . import constants as constants, utils as utils
from .exceptions import Cmd2ShlexError as Cmd2ShlexError
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, List, Tuple

def shlex_split(str_to_split: str) -> List[str]:
    """
    A wrapper around shlex.split() that uses cmd2's preferred arguments.
    This allows other classes to easily call split() the same way StatementParser does.

    :param str_to_split: the string being split
    :return: A list of tokens
    """

class MacroArg:
    """
    Information used to replace or unescape arguments in a macro value when the macro is resolved
    Normal argument syntax:    {5}
    Escaped argument syntax:  {{5}}
    """
    start_index: int
    number_str: str
    is_escaped: bool
    macro_normal_arg_pattern: Incomplete
    macro_escaped_arg_pattern: Incomplete
    digit_pattern: Incomplete
    def __init__(self, start_index, number_str, is_escaped) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class Macro:
    """Defines a cmd2 macro"""
    name: str
    value: str
    minimum_arg_count: int
    arg_list: List[MacroArg]
    def __init__(self, name, value, minimum_arg_count, arg_list) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class Statement(str):
    """String subclass with additional attributes to store the results of parsing.

    The ``cmd`` module in the standard library passes commands around as a
    string. To retain backwards compatibility, ``cmd2`` does the same. However,
    we need a place to capture the additional output of the command parsing, so
    we add our own attributes to this subclass.

    Instances of this class should not be created by anything other than the
    :meth:`cmd2.parsing.StatementParser.parse` method, nor should any of the
    attributes be modified once the object is created.

    The string portion of the class contains the arguments, but not the
    command, nor the output redirection clauses.

    Tips:

    1. `argparse <https://docs.python.org/3/library/argparse.html>`_ is your
       friend for anything complex. ``cmd2`` has the decorator
       (:func:`~cmd2.decorators.with_argparser`) which you can
       use to make your command method receive a namespace of parsed arguments,
       whether positional or denoted with switches.

    2. For commands with simple positional arguments, use
       :attr:`~cmd2.Statement.args` or :attr:`~cmd2.Statement.arg_list`

    3. If you don't want to have to worry about quoted arguments, see
       :attr:`argv` for a trick which strips quotes off for you.
    """
    args: str
    raw: str
    command: str
    arg_list: List[str]
    multiline_command: str
    terminator: str
    suffix: str
    pipe_to: str
    output: str
    output_to: str
    def __new__(cls, value: object, *pos_args: Any, **kw_args: Any) -> Statement:
        """Create a new instance of Statement.

        We must override __new__ because we are subclassing `str` which is
        immutable and takes a different number of arguments as Statement.

        NOTE:  attrs takes care of initializing other members in the __init__ it
        generates.
        """
    @property
    def command_and_args(self) -> str:
        """Combine command and args with a space separating them.

        Quoted arguments remain quoted. Output redirection and piping are
        excluded, as are any command terminators.
        """
    @property
    def post_command(self) -> str:
        """A string containing any ending terminator, suffix, and redirection chars"""
    @property
    def expanded_command_line(self) -> str:
        """Concatenate :meth:`~cmd2.Statement.command_and_args`
        and :meth:`~cmd2.Statement.post_command`"""
    @property
    def argv(self) -> List[str]:
        """a list of arguments a-la ``sys.argv``.

        The first element of the list is the command after shortcut and macro
        expansion. Subsequent elements of the list contain any additional
        arguments, with quotes removed, just like bash would. This is very
        useful if you are going to use ``argparse.parse_args()``.

        If you want to strip quotes from the input, you can use ``argv[1:]``.
        """
    def to_dict(self) -> Dict[str, Any]:
        """Utility method to convert this Statement into a dictionary for use in persistent JSON history files"""
    @staticmethod
    def from_dict(source_dict: Dict[str, Any]) -> Statement:
        """
        Utility method to restore a Statement from a dictionary

        :param source_dict: source data dictionary (generated using to_dict())
        :return: Statement object
        :raises KeyError: if source_dict is missing required elements
        """
    def __init__(self, args, raw, command, arg_list, multiline_command, terminator, suffix, pipe_to, output, output_to) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class StatementParser:
    """Parse user input as a string into discrete command components."""
    terminators: Incomplete
    multiline_commands: Incomplete
    aliases: Incomplete
    shortcuts: Incomplete
    def __init__(self, terminators: Iterable[str] | None = None, multiline_commands: Iterable[str] | None = None, aliases: Dict[str, str] | None = None, shortcuts: Dict[str, str] | None = None) -> None:
        """Initialize an instance of StatementParser.

        The following will get converted to an immutable tuple before storing internally:
        terminators, multiline commands, and shortcuts.

        :param terminators: iterable containing strings which should terminate commands
        :param multiline_commands: iterable containing the names of commands that accept multiline input
        :param aliases: dictionary containing aliases
        :param shortcuts: dictionary containing shortcuts
        """
    def is_valid_command(self, word: str, *, is_subcommand: bool = False) -> Tuple[bool, str]:
        '''Determine whether a word is a valid name for a command.

        Commands cannot include redirection characters, whitespace,
        or termination characters. They also cannot start with a
        shortcut.

        :param word: the word to check as a command
        :param is_subcommand: Flag whether this command name is a subcommand name
        :return: a tuple of a boolean and an error string

        If word is not a valid command, return ``False`` and an error string
        suitable for inclusion in an error message of your choice::

            checkit = \'>\'
            valid, errmsg = statement_parser.is_valid_command(checkit)
            if not valid:
                errmsg = f"alias: {errmsg}"
        '''
    def tokenize(self, line: str) -> List[str]:
        """
        Lex a string into a list of tokens. Shortcuts and aliases are expanded and
        comments are removed.

        :param line: the command line being lexed
        :return: A list of tokens
        :raises: Cmd2ShlexError if a shlex error occurs (e.g. No closing quotation)
        """
    def parse(self, line: str) -> Statement:
        """
        Tokenize the input and parse it into a :class:`~cmd2.Statement` object,
        stripping comments, expanding aliases and shortcuts, and extracting output
        redirection directives.

        :param line: the command line being parsed
        :return: a new :class:`~cmd2.Statement` object
        :raises: Cmd2ShlexError if a shlex error occurs (e.g. No closing quotation)
        """
    def parse_command_only(self, rawinput: str) -> Statement:
        """Partially parse input into a :class:`~cmd2.Statement` object.

        The command is identified, and shortcuts and aliases are expanded.
        Multiline commands are identified, but terminators and output
        redirection are not parsed.

        This method is used by tab completion code and therefore must not
        generate an exception if there are unclosed quotes.

        The :class:`~cmd2.Statement` object returned by this method can at most
        contain values in the following attributes:
        :attr:`~cmd2.Statement.args`, :attr:`~cmd2.Statement.raw`,
        :attr:`~cmd2.Statement.command`,
        :attr:`~cmd2.Statement.multiline_command`

        :attr:`~cmd2.Statement.args` will include all output redirection
        clauses and command terminators.

        Different from :meth:`~cmd2.parsing.StatementParser.parse` this method
        does not remove redundant whitespace within args. However, it does
        ensure args has no leading or trailing whitespace.

        :param rawinput: the command line as entered by the user
        :return: a new :class:`~cmd2.Statement` object
        """
    def get_command_arg_list(self, command_name: str, to_parse: Statement | str, preserve_quotes: bool) -> Tuple[Statement, List[str]]:
        """
        Convenience method used by the argument parsing decorators.

        Retrieves just the arguments being passed to their ``do_*`` methods as a list.

        :param command_name: name of the command being run
        :param to_parse: what is being passed to the ``do_*`` method. It can be one of two types:

                             1. An already parsed :class:`~cmd2.Statement`
                             2. An argument string in cases where a ``do_*`` method is
                                explicitly called. Calling ``do_help('alias create')`` would
                                cause ``to_parse`` to be 'alias create'.

                                In this case, the string will be converted to a
                                :class:`~cmd2.Statement` and returned along with
                                the argument list.

        :param preserve_quotes: if ``True``, then quotes will not be stripped from
                                the arguments
        :return: A tuple containing the :class:`~cmd2.Statement` and a list of
                 strings representing the arguments
        """
    def split_on_punctuation(self, tokens: List[str]) -> List[str]:
        """Further splits tokens from a command line using punctuation characters.

        Punctuation characters are treated as word breaks when they are in
        unquoted strings. Each run of punctuation characters is treated as a
        single token.

        :param tokens: the tokens as parsed by shlex
        :return: a new list of tokens, further split using punctuation
        """
