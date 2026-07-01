import argparse
import cmd
from . import ansi as ansi, argparse_completer as argparse_completer, argparse_custom as argparse_custom, constants as constants, plugin as plugin, utils as utils
from .argparse_custom import ChoicesProviderFunc as ChoicesProviderFunc, CompleterFunc as CompleterFunc, CompletionItem as CompletionItem
from .clipboard import can_clip as can_clip, get_paste_buffer as get_paste_buffer, write_to_paste_buffer as write_to_paste_buffer
from .command_definition import CommandFunc as CommandFunc, CommandSet as CommandSet
from .constants import CLASS_ATTR_DEFAULT_HELP_CATEGORY as CLASS_ATTR_DEFAULT_HELP_CATEGORY, COMMAND_FUNC_PREFIX as COMMAND_FUNC_PREFIX, COMPLETER_FUNC_PREFIX as COMPLETER_FUNC_PREFIX, HELP_FUNC_PREFIX as HELP_FUNC_PREFIX
from .decorators import as_subcommand_to as as_subcommand_to, with_argparser as with_argparser
from .exceptions import Cmd2ShlexError as Cmd2ShlexError, CommandSetRegistrationError as CommandSetRegistrationError, CompletionError as CompletionError, EmbeddedConsoleExit as EmbeddedConsoleExit, EmptyStatement as EmptyStatement, PassThroughException as PassThroughException, RedirectionError as RedirectionError, SkipPostcommandHooks as SkipPostcommandHooks
from .history import History as History, HistoryItem as HistoryItem
from .parsing import Macro as Macro, MacroArg as MacroArg, Statement as Statement, StatementParser as StatementParser, shlex_split as shlex_split
from .rl_utils import RlType as RlType, readline as readline, readline_lib as readline_lib, rl_escape_prompt as rl_escape_prompt, rl_force_redisplay as rl_force_redisplay, rl_get_point as rl_get_point, rl_get_prompt as rl_get_prompt, rl_set_prompt as rl_set_prompt, rl_type as rl_type, rl_warning as rl_warning, vt100_support as vt100_support
from .table_creator import Column as Column, SimpleTable as SimpleTable
from .utils import Settable as Settable, get_defining_class as get_defining_class, strip_doc_annotations as strip_doc_annotations
from _typeshed import Incomplete
from types import FrameType
from typing import Any, Callable, Dict, Iterable, List, Mapping, NamedTuple, TextIO, Tuple, Type, TypeVar

orig_rl_delims: Incomplete
orig_pyreadline_display: Incomplete
rl_basic_quote_characters: Incomplete
orig_rl_basic_quotes: Incomplete

class _SavedReadlineSettings:
    """readline settings that are backed up when switching between readline environments"""
    completer: Incomplete
    delims: str
    basic_quotes: Incomplete
    def __init__(self) -> None: ...

class _SavedCmd2Env:
    """cmd2 environment settings that are backed up when entering an interactive Python shell"""
    readline_settings: Incomplete
    readline_module: Incomplete
    history: Incomplete
    sys_stdout: Incomplete
    sys_stdin: Incomplete
    def __init__(self) -> None: ...

class DisabledCommand(NamedTuple):
    command_function: Incomplete
    help_function: Incomplete
    completer_function: Incomplete

class Cmd(cmd.Cmd):
    """An easy but powerful framework for writing line-oriented command interpreters.

    Extends the Python Standard Library’s cmd package by adding a lot of useful features
    to the out of the box configuration.

    Line-oriented command interpreters are often useful for test harnesses, internal tools, and rapid prototypes.
    """
    DEFAULT_EDITOR: Incomplete
    INTERNAL_COMMAND_EPILOG: str
    ALPHABETICAL_SORT_KEY = utils.norm_fold
    NATURAL_SORT_KEY = utils.natural_keys
    default_to_shell: bool
    allow_redirection: Incomplete
    always_show_hint: bool
    debug: bool
    echo: bool
    editor: Incomplete
    feedback_to_output: bool
    quiet: bool
    timing: bool
    max_completion_items: int
    continuation_prompt: str
    self_in_py: bool
    hidden_commands: Incomplete
    exclude_from_history: Incomplete
    macros: Incomplete
    py_bridge_name: str
    py_locals: Incomplete
    statement_parser: Incomplete
    last_result: Incomplete
    sigint_protection: Incomplete
    doc_header: str
    help_error: str
    default_error: str
    broken_pipe_warning: str
    pager: str
    pager_chop: str
    exit_code: int
    terminal_lock: Incomplete
    disabled_commands: Incomplete
    default_category: str
    default_sort_key: Incomplete
    allow_appended_space: bool
    allow_closing_quote: bool
    completion_hint: str
    formatted_completions: str
    completion_matches: Incomplete
    display_matches: Incomplete
    matches_delimited: bool
    matches_sorted: bool
    def __init__(self, completekey: str = 'tab', stdin: TextIO | None = None, stdout: TextIO | None = None, *, persistent_history_file: str = '', persistent_history_length: int = 1000, startup_script: str = '', silence_startup_script: bool = False, include_py: bool = False, include_ipy: bool = False, allow_cli_args: bool = True, transcript_files: List[str] | None = None, allow_redirection: bool = True, multiline_commands: List[str] | None = None, terminators: List[str] | None = None, shortcuts: Dict[str, str] | None = None, command_sets: Iterable[CommandSet] | None = None, auto_load_commands: bool = True) -> None:
        '''An easy but powerful framework for writing line-oriented command
        interpreters. Extends Python\'s cmd package.

        :param completekey: readline name of a completion key, default to Tab
        :param stdin: alternate input file object, if not specified, sys.stdin is used
        :param stdout: alternate output file object, if not specified, sys.stdout is used
        :param persistent_history_file: file path to load a persistent cmd2 command history from
        :param persistent_history_length: max number of history items to write
                                          to the persistent history file
        :param startup_script: file path to a script to execute at startup
        :param silence_startup_script: if ``True``, then the startup script\'s output will be
                                       suppressed. Anything written to stderr will still display.
        :param include_py: should the "py" command be included for an embedded Python shell
        :param include_ipy: should the "ipy" command be included for an embedded IPython shell
        :param allow_cli_args: if ``True``, then :meth:`cmd2.Cmd.__init__` will process command
                               line arguments as either commands to be run or, if ``-t`` or
                               ``--test`` are given, transcript files to run. This should be
                               set to ``False`` if your application parses its own command line
                               arguments.
        :param transcript_files: pass a list of transcript files to be run on initialization.
                                 This allows running transcript tests when ``allow_cli_args``
                                 is ``False``. If ``allow_cli_args`` is ``True`` this parameter
                                 is ignored.
        :param allow_redirection: If ``False``, prevent output redirection and piping to shell
                                  commands. This parameter prevents redirection and piping, but
                                  does not alter parsing behavior. A user can still type
                                  redirection and piping tokens, and they will be parsed as such
                                  but they won\'t do anything.
        :param multiline_commands: list of commands allowed to accept multi-line input
        :param terminators: list of characters that terminate a command. These are mainly
                            intended for terminating multiline commands, but will also
                            terminate single-line commands. If not supplied, the default
                            is a semicolon. If your app only contains single-line commands
                            and you want terminators to be treated as literals by the parser,
                            then set this to an empty list.
        :param shortcuts: dictionary containing shortcuts for commands. If not supplied,
                          then defaults to constants.DEFAULT_SHORTCUTS. If you do not want
                          any shortcuts, pass an empty dictionary.
        :param command_sets: Provide CommandSet instances to load during cmd2 initialization.
                             This allows CommandSets with custom constructor parameters to be
                             loaded.  This also allows the a set of CommandSets to be provided
                             when `auto_load_commands` is set to False
        :param auto_load_commands: If True, cmd2 will check for all subclasses of `CommandSet`
                                   that are currently loaded by Python and automatically
                                   instantiate and register all commands. If False, CommandSets
                                   must be manually installed with `register_command_set`.
        '''
    def find_commandsets(self, commandset_type: Type[CommandSet], *, subclass_match: bool = False) -> List[CommandSet]:
        """
        Find all CommandSets that match the provided CommandSet type.
        By default, locates a CommandSet that is an exact type match but may optionally return all CommandSets that
        are sub-classes of the provided type
        :param commandset_type: CommandSet sub-class type to search for
        :param subclass_match: If True, return all sub-classes of provided type, otherwise only search for exact match
        :return: Matching CommandSets
        """
    def find_commandset_for_command(self, command_name: str) -> CommandSet | None:
        """
        Finds the CommandSet that registered the command name
        :param command_name: command name to search
        :return: CommandSet that provided the command
        """
    def register_command_set(self, cmdset: CommandSet) -> None:
        """
        Installs a CommandSet, loading all commands defined in the CommandSet

        :param cmdset: CommandSet to load
        """
    def unregister_command_set(self, cmdset: CommandSet) -> None:
        """
        Uninstalls a CommandSet and unloads all associated commands

        :param cmdset: CommandSet to uninstall
        """
    @property
    def always_prefix_settables(self) -> bool:
        """
        Flags whether CommandSet settable values should always be prefixed

        :return: True if CommandSet settable values will always be prefixed. False if not.
        """
    @always_prefix_settables.setter
    def always_prefix_settables(self, new_value: bool) -> None:
        """
        Set whether CommandSet settable values should always be prefixed.

        :param new_value: True if CommandSet settable values should always be prefixed. False if not.
        :raises ValueError: If a registered CommandSet does not have a defined prefix
        """
    @property
    def settables(self) -> Mapping[str, Settable]:
        """
        Get all available user-settable attributes. This includes settables defined in installed CommandSets

        :return: Mapping from attribute-name to Settable of all user-settable attributes from
        """
    def add_settable(self, settable: Settable) -> None:
        """
        Add a settable parameter to ``self.settables``

        :param settable: Settable object being added
        """
    def remove_settable(self, name: str) -> None:
        """
        Convenience method for removing a settable parameter from ``self.settables``

        :param name: name of the settable being removed
        :raises: KeyError if the Settable matches this name
        """
    def build_settables(self) -> None:
        """Create the dictionary of user-settable parameters"""
    @property
    def allow_style(self) -> ansi.AllowStyle:
        """Read-only property needed to support do_set when it reads allow_style"""
    @allow_style.setter
    def allow_style(self, new_val: ansi.AllowStyle) -> None:
        """Setter property needed to support do_set when it updates allow_style"""
    @property
    def visible_prompt(self) -> str:
        """Read-only property to get the visible prompt with any ANSI style escape codes stripped.

        Used by transcript testing to make it easier and more reliable when users are doing things like coloring the
        prompt using ANSI color codes.

        :return: prompt stripped of any ANSI escape codes
        """
    def poutput(self, msg: Any = '', *, end: str = '\n') -> None:
        """Print message to self.stdout and appends a newline by default

        Also handles BrokenPipeError exceptions for when a command's output has
        been piped to another process and that process terminates before the
        cmd2 command is finished executing.

        :param msg: object to print
        :param end: string appended after the end of the message, default a newline
        """
    def perror(self, msg: Any = '', *, end: str = '\n', apply_style: bool = True) -> None:
        """Print message to sys.stderr

        :param msg: object to print
        :param end: string appended after the end of the message, default a newline
        :param apply_style: If True, then ansi.style_error will be applied to the message text. Set to False in cases
                            where the message text already has the desired style. Defaults to True.
        """
    def pwarning(self, msg: Any = '', *, end: str = '\n', apply_style: bool = True) -> None:
        """Wraps perror, but applies ansi.style_warning by default

        :param msg: object to print
        :param end: string appended after the end of the message, default a newline
        :param apply_style: If True, then ansi.style_warning will be applied to the message text. Set to False in cases
                            where the message text already has the desired style. Defaults to True.
        """
    def pexcept(self, msg: Any, *, end: str = '\n', apply_style: bool = True) -> None:
        """Print Exception message to sys.stderr. If debug is true, print exception traceback if one exists.

        :param msg: message or Exception to print
        :param end: string appended after the end of the message, default a newline
        :param apply_style: If True, then ansi.style_error will be applied to the message text. Set to False in cases
                            where the message text already has the desired style. Defaults to True.
        """
    def pfeedback(self, msg: Any, *, end: str = '\n') -> None:
        """For printing nonessential feedback.  Can be silenced with `quiet`.
        Inclusion in redirected output is controlled by `feedback_to_output`.

        :param msg: object to print
        :param end: string appended after the end of the message, default a newline
        """
    def ppaged(self, msg: Any, *, end: str = '\n', chop: bool = False) -> None:
        """Print output using a pager if it would go off screen and stdout isn't currently being redirected.

        Never uses a pager inside of a script (Python or text) or when output is being redirected or piped or when
        stdout or stdin are not a fully functional terminal.

        :param msg: object to print
        :param end: string appended after the end of the message, default a newline
        :param chop: True -> causes lines longer than the screen width to be chopped (truncated) rather than wrapped
                              - truncated text is still accessible by scrolling with the right & left arrow keys
                              - chopping is ideal for displaying wide tabular data as is done in utilities like pgcli
                     False -> causes lines longer than the screen width to wrap to the next line
                              - wrapping is ideal when you want to keep users from having to use horizontal scrolling

        WARNING: On Windows, the text always wraps regardless of what the chop argument is set to
        """
    def tokens_for_completion(self, line: str, begidx: int, endidx: int) -> Tuple[List[str], List[str]]:
        """Used by tab completion functions to get all tokens through the one being completed.

        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :return: A 2 item tuple where the items are
                 **On Success**
                 - tokens: list of unquoted tokens - this is generally the list needed for tab completion functions
                 - raw_tokens: list of tokens with any quotes preserved = this can be used to know if a token was quoted
                 or is missing a closing quote
                 Both lists are guaranteed to have at least 1 item. The last item in both lists is the token being tab
                 completed
                 **On Failure**
                 - Two empty lists
        """
    def basic_complete(self, text: str, line: str, begidx: int, endidx: int, match_against: Iterable[str]) -> List[str]:
        """
        Basic tab completion function that matches against a list of strings without considering line contents
        or cursor position. The args required by this function are defined in the header of Python's cmd.py.

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param match_against: the strings being matched against
        :return: a list of possible tab completions
        """
    def delimiter_complete(self, text: str, line: str, begidx: int, endidx: int, match_against: Iterable[str], delimiter: str) -> List[str]:
        """
        Performs tab completion against a list but each match is split on a delimiter and only
        the portion of the match being tab completed is shown as the completion suggestions.
        This is useful if you match against strings that are hierarchical in nature and have a
        common delimiter.

        An easy way to illustrate this concept is path completion since paths are just directories/files
        delimited by a slash. If you are tab completing items in /home/user you don't get the following
        as suggestions:

        /home/user/file.txt     /home/user/program.c
        /home/user/maps/        /home/user/cmd2.py

        Instead you are shown:

        file.txt                program.c
        maps/                   cmd2.py

        For a large set of data, this can be visually more pleasing and easier to search.

        Another example would be strings formatted with the following syntax: company::department::name
        In this case the delimiter would be :: and the user could easily narrow down what they are looking
        for if they were only shown suggestions in the category they are at in the string.

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param match_against: the list being matched against
        :param delimiter: what delimits each portion of the matches (ex: paths are delimited by a slash)
        :return: a list of possible tab completions
        """
    def flag_based_complete(self, text: str, line: str, begidx: int, endidx: int, flag_dict: Dict[str, Iterable[str] | CompleterFunc], *, all_else: None | Iterable[str] | CompleterFunc = None) -> List[str]:
        """Tab completes based on a particular flag preceding the token being completed.

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param flag_dict: dictionary whose structure is the following:
                          `keys` - flags (ex: -c, --create) that result in tab completion for the next argument in the
                          command line
                          `values` - there are two types of values:
                          1. iterable list of strings to match against (dictionaries, lists, etc.)
                          2. function that performs tab completion (ex: path_complete)
        :param all_else: an optional parameter for tab completing any token that isn't preceded by a flag in flag_dict
        :return: a list of possible tab completions
        """
    def index_based_complete(self, text: str, line: str, begidx: int, endidx: int, index_dict: Mapping[int, Iterable[str] | CompleterFunc], *, all_else: Iterable[str] | CompleterFunc | None = None) -> List[str]:
        """Tab completes based on a fixed position in the input string.

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param index_dict: dictionary whose structure is the following:
                           `keys` - 0-based token indexes into command line that determine which tokens perform tab
                           completion
                           `values` - there are two types of values:
                           1. iterable list of strings to match against (dictionaries, lists, etc.)
                           2. function that performs tab completion (ex: path_complete)
        :param all_else: an optional parameter for tab completing any token that isn't at an index in index_dict
        :return: a list of possible tab completions
        """
    def path_complete(self, text: str, line: str, begidx: int, endidx: int, *, path_filter: Callable[[str], bool] | None = None) -> List[str]:
        """Performs completion of local file system paths

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param path_filter: optional filter function that determines if a path belongs in the results
                            this function takes a path as its argument and returns True if the path should
                            be kept in the results
        :return: a list of possible tab completions
        """
    def shell_cmd_complete(self, text: str, line: str, begidx: int, endidx: int, *, complete_blank: bool = False) -> List[str]:
        """Performs completion of executables either in a user's path or a given path

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param complete_blank: If True, then a blank will complete all shell commands in a user's path. If False, then
                               no completion is performed. Defaults to False to match Bash shell behavior.
        :return: a list of possible tab completions
        """
    def complete(self, text: str, state: int, custom_settings: utils.CustomCompletionSettings | None = None) -> str | None:
        """Override of cmd's complete method which returns the next possible completion for 'text'

        This completer function is called by readline as complete(text, state), for state in 0, 1, 2, …,
        until it returns a non-string value. It should return the next possible completion starting with text.

        Since readline suppresses any exception raised in completer functions, they can be difficult to debug.
        Therefore, this function wraps the actual tab completion logic and prints to stderr any exception that
        occurs before returning control to readline.

        :param text: the current word that user is typing
        :param state: non-negative integer
        :param custom_settings: used when not tab completing the main command line
        :return: the next possible completion for text or None
        """
    def in_script(self) -> bool:
        """Return whether a text script is running"""
    def in_pyscript(self) -> bool:
        """Return whether running inside a Python shell or pyscript"""
    @property
    def aliases(self) -> Dict[str, str]:
        """Read-only property to access the aliases stored in the StatementParser"""
    def get_names(self) -> List[str]:
        """Return an alphabetized list of names comprising the attributes of the cmd2 class instance."""
    def get_all_commands(self) -> List[str]:
        """Return a list of all commands"""
    def get_visible_commands(self) -> List[str]:
        """Return a list of commands that have not been hidden or disabled"""
    def get_help_topics(self) -> List[str]:
        """Return a list of help topics"""
    def sigint_handler(self, signum: int, _: FrameType) -> None:
        """Signal handler for SIGINTs which typically come from Ctrl-C events.

        If you need custom SIGINT behavior, then override this function.

        :param signum: signal number
        :param _: required param for signal handlers
        """
    def precmd(self, statement: Statement | str) -> Statement:
        """Hook method executed just before the command is executed by
        :meth:`~cmd2.Cmd.onecmd` and after adding it to history.

        :param statement: subclass of str which also contains the parsed input
        :return: a potentially modified version of the input Statement object

        See :meth:`~cmd2.Cmd.register_postparsing_hook` and
        :meth:`~cmd2.Cmd.register_precmd_hook` for more robust ways
        to run hooks before the command is executed. See
        :ref:`features/hooks:Postparsing Hooks` and
        :ref:`features/hooks:Precommand Hooks` for more information.
        """
    def postcmd(self, stop: bool, statement: Statement | str) -> bool:
        """Hook method executed just after a command is executed by
        :meth:`~cmd2.Cmd.onecmd`.

        :param stop: return `True` to request the command loop terminate
        :param statement: subclass of str which also contains the parsed input

        See :meth:`~cmd2.Cmd.register_postcmd_hook` and :meth:`~cmd2.Cmd.register_cmdfinalization_hook` for more robust ways
        to run hooks after the command is executed. See
        :ref:`features/hooks:Postcommand Hooks` and
        :ref:`features/hooks:Command Finalization Hooks` for more information.
        """
    def preloop(self) -> None:
        """Hook method executed once when the :meth:`~.cmd2.Cmd.cmdloop()`
        method is called.

        See :meth:`~cmd2.Cmd.register_preloop_hook` for a more robust way
        to run hooks before the command loop begins. See
        :ref:`features/hooks:Application Lifecycle Hooks` for more information.
        """
    def postloop(self) -> None:
        """Hook method executed once when the :meth:`~.cmd2.Cmd.cmdloop()`
        method is about to return.

        See :meth:`~cmd2.Cmd.register_postloop_hook` for a more robust way
        to run hooks after the command loop completes. See
        :ref:`features/hooks:Application Lifecycle Hooks` for more information.
        """
    def parseline(self, line: str) -> Tuple[str, str, str]:
        """Parse the line into a command name and a string containing the arguments.

        NOTE: This is an override of a parent class method.  It is only used by other parent class methods.

        Different from the parent class method, this ignores self.identchars.

        :param line: line read by readline
        :return: tuple containing (command, args, line)
        """
    def onecmd_plus_hooks(self, line: str, *, add_to_history: bool = True, raise_keyboard_interrupt: bool = False, py_bridge_call: bool = False) -> bool:
        """Top-level function called by cmdloop() to handle parsing a line and running the command and all of its hooks.

        :param line: command line to run
        :param add_to_history: If True, then add this command to history. Defaults to True.
        :param raise_keyboard_interrupt: if True, then KeyboardInterrupt exceptions will be raised if stop isn't already
                                         True. This is used when running commands in a loop to be able to stop the whole
                                         loop and not just the current command. Defaults to False.
        :param py_bridge_call: This should only ever be set to True by PyBridge to signify the beginning
                               of an app() call from Python. It is used to enable/disable the storage of the
                               command's stdout.
        :return: True if running of commands should stop
        """
    def runcmds_plus_hooks(self, cmds: List[HistoryItem] | List[str], *, add_to_history: bool = True, stop_on_keyboard_interrupt: bool = False) -> bool:
        """
        Used when commands are being run in an automated fashion like text scripts or history replays.
        The prompt and command line for each command will be printed if echo is True.

        :param cmds: commands to run
        :param add_to_history: If True, then add these commands to history. Defaults to True.
        :param stop_on_keyboard_interrupt: if True, then stop running contents of cmds if Ctrl-C is pressed instead of moving
                                           to the next command in the list. This is used when the commands are part of a
                                           group, like a text script, which should stop upon Ctrl-C. Defaults to False.
        :return: True if running of commands should stop
        """
    def cmd_func(self, command: str) -> CommandFunc | None:
        """
        Get the function for a command

        :param command: the name of the command

        :Example:

        >>> helpfunc = self.cmd_func('help')

        helpfunc now contains a reference to the ``do_help`` method
        """
    def onecmd(self, statement: Statement | str, *, add_to_history: bool = True) -> bool:
        """This executes the actual do_* method for a command.

        If the command provided doesn't exist, then it executes default() instead.

        :param statement: intended to be a Statement instance parsed command from the input stream, alternative
                          acceptance of a str is present only for backward compatibility with cmd
        :param add_to_history: If True, then add this command to history. Defaults to True.
        :return: a flag indicating whether the interpretation of commands should stop
        """
    def default(self, statement: Statement) -> bool | None:
        """Executed when the command given isn't a recognized command implemented by a do_* method.

        :param statement: Statement object with parsed input
        """
    def read_input(self, prompt: str, *, history: List[str] | None = None, completion_mode: utils.CompletionMode = ..., preserve_quotes: bool = False, choices: Iterable[Any] | None = None, choices_provider: ChoicesProviderFunc | None = None, completer: CompleterFunc | None = None, parser: argparse.ArgumentParser | None = None) -> str:
        """
        Read input from appropriate stdin value. Also supports tab completion and up-arrow history while
        input is being entered.

        :param prompt: prompt to display to user
        :param history: optional list of strings to use for up-arrow history. If completion_mode is
                        CompletionMode.COMMANDS and this is None, then cmd2's command list history will
                        be used. The passed in history will not be edited. It is the caller's responsibility
                        to add the returned input to history if desired. Defaults to None.
        :param completion_mode: tells what type of tab completion to support. Tab completion only works when
                                self.use_rawinput is True and sys.stdin is a terminal. Defaults to
                                CompletionMode.NONE.

        The following optional settings apply when completion_mode is CompletionMode.CUSTOM:

        :param preserve_quotes: if True, then quoted tokens will keep their quotes when processed by
                                ArgparseCompleter. This is helpful in cases when you're tab completing
                                flag-like tokens (e.g. -o, --option) and you don't want them to be
                                treated as argparse flags when quoted. Set this to True if you plan
                                on passing the string to argparse with the tokens still quoted.

        A maximum of one of these should be provided:

        :param choices: iterable of accepted values for single argument
        :param choices_provider: function that provides choices for single argument
        :param completer: tab completion function that provides choices for single argument
        :param parser: an argument parser which supports the tab completion of multiple arguments

        :return: the line read from stdin with all trailing new lines removed
        :raises: any exceptions raised by input() and stdin.readline()
        """
    alias_description: str
    alias_epilog: str
    alias_parser: Incomplete
    alias_subparsers: Incomplete
    def do_alias(self, args: argparse.Namespace) -> None:
        """Manage aliases"""
    alias_create_description: str
    alias_create_epilog: str
    alias_create_parser: Incomplete
    alias_delete_help: str
    alias_delete_description: str
    alias_delete_parser: Incomplete
    alias_list_help: str
    alias_list_description: str
    alias_list_parser: Incomplete
    macro_description: str
    macro_epilog: str
    macro_parser: Incomplete
    macro_subparsers: Incomplete
    def do_macro(self, args: argparse.Namespace) -> None:
        """Manage macros"""
    macro_create_help: str
    macro_create_description: str
    macro_create_epilog: str
    macro_create_parser: Incomplete
    macro_delete_help: str
    macro_delete_description: str
    macro_delete_parser: Incomplete
    macro_list_help: str
    macro_list_description: str
    macro_list_parser: Incomplete
    def complete_help_command(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Completes the command argument of help"""
    def complete_help_subcommands(self, text: str, line: str, begidx: int, endidx: int, arg_tokens: Dict[str, List[str]]) -> List[str]:
        """Completes the subcommands argument of help"""
    help_parser: Incomplete
    def do_help(self, args: argparse.Namespace) -> None:
        """List available commands or provide detailed help for a specific command"""
    def print_topics(self, header: str, cmds: List[str] | None, cmdlen: int, maxcol: int) -> None:
        """
        Print groups of commands and topics in columns and an optional header
        Override of cmd's print_topics() to handle headers with newlines, ANSI style sequences, and wide characters

        :param header: string to print above commands being printed
        :param cmds: list of topics to print
        :param cmdlen: unused, even by cmd's version
        :param maxcol: max number of display columns to fit into
        """
    def columnize(self, str_list: List[str] | None, display_width: int = 80) -> None:
        """Display a list of single-line strings as a compact set of columns.
        Override of cmd's print_topics() to handle strings with ANSI style sequences and wide characters

        Each column is only as wide as necessary.
        Columns are separated by two spaces (one was not legible enough).
        """
    shortcuts_parser: Incomplete
    def do_shortcuts(self, _: argparse.Namespace) -> None:
        """List available shortcuts"""
    eof_parser: Incomplete
    def do_eof(self, _: argparse.Namespace) -> bool | None:
        """
        Called when Ctrl-D is pressed and calls quit with no arguments.
        This can be overridden if quit should be called differently.
        """
    quit_parser: Incomplete
    def do_quit(self, _: argparse.Namespace) -> bool | None:
        """Exit this application"""
    def select(self, opts: str | List[str] | List[Tuple[Any, str | None]], prompt: str = 'Your choice? ') -> Any:
        """Presents a numbered menu to the user.  Modeled after
        the bash shell's SELECT.  Returns the item chosen.

        Argument ``opts`` can be:

          | a single string -> will be split into one-word options
          | a list of strings -> will be offered as options
          | a list of tuples -> interpreted as (value, text), so
                                that the return value can differ from
                                the text advertised to the user"""
    def complete_set_value(self, text: str, line: str, begidx: int, endidx: int, arg_tokens: Dict[str, List[str]]) -> List[str]:
        """Completes the value argument of set"""
    set_description: str
    set_parser_parent: Incomplete
    set_parser: Incomplete
    def do_set(self, args: argparse.Namespace) -> None:
        """Set a settable parameter or show current settings of parameters"""
    shell_parser: Incomplete
    def do_shell(self, args: argparse.Namespace) -> None:
        """Execute a command as if at the OS prompt"""
    py_parser: Incomplete
    def do_py(self, _: argparse.Namespace) -> bool | None:
        """
        Run an interactive Python shell
        :return: True if running of commands should stop
        """
    run_pyscript_parser: Incomplete
    def do_run_pyscript(self, args: argparse.Namespace) -> bool | None:
        """
        Run a Python script file inside the console

        :return: True if running of commands should stop
        """
    ipython_parser: Incomplete
    def do_ipy(self, _: argparse.Namespace) -> bool | None:
        """
        Enter an interactive IPython shell

        :return: True if running of commands should stop
        """
    history_description: str
    history_parser: Incomplete
    history_action_group: Incomplete
    history_format_group: Incomplete
    history_arg_help: str
    def do_history(self, args: argparse.Namespace) -> bool | None:
        """
        View, run, edit, save, or clear previously entered commands

        :return: True if running of commands should stop
        """
    edit_description: str
    edit_parser: Incomplete
    def do_edit(self, args: argparse.Namespace) -> None:
        """Run a text editor and optionally open a file with it"""
    def run_editor(self, file_path: str | None = None) -> None:
        """
        Run a text editor and optionally open a file with it

        :param file_path: optional path of the file to edit. Defaults to None.
        :raises: EnvironmentError if self.editor is not set
        """
    run_script_description: str
    run_script_parser: Incomplete
    def do_run_script(self, args: argparse.Namespace) -> bool | None:
        """Run commands in script file that is encoded as either ASCII or UTF-8 text.

        :return: True if running of commands should stop
        """
    relative_run_script_description = run_script_description
    relative_run_script_epilog: str
    relative_run_script_parser: Incomplete
    def do__relative_run_script(self, args: argparse.Namespace) -> bool | None:
        """
        Run commands in script file that is encoded as either ASCII or UTF-8 text

        :return: True if running of commands should stop
        """
    prompt: Incomplete
    def async_alert(self, alert_msg: str, new_prompt: str | None = None) -> None:
        """
        Display an important message to the user while they are at a command line prompt.
        To the user it appears as if an alert message is printed above the prompt and their current input
        text and cursor location is left alone.

        IMPORTANT: This function will not print an alert unless it can acquire self.terminal_lock to ensure
                   a prompt is onscreen. Therefore, it is best to acquire the lock before calling this function
                   to guarantee the alert prints and to avoid raising a RuntimeError.

                   This function is only needed when you need to print an alert while the main thread is blocking
                   at the prompt. Therefore, this should never be called from the main thread. Doing so will
                   raise a RuntimeError.

        :param alert_msg: the message to display to the user
        :param new_prompt: If you also want to change the prompt that is displayed, then include it here.
                           See async_update_prompt() docstring for guidance on updating a prompt.
        :raises RuntimeError: if called from the main thread.
        :raises RuntimeError: if called while another thread holds `terminal_lock`
        """
    def async_update_prompt(self, new_prompt: str) -> None:
        """
        Update the command line prompt while the user is still typing at it. This is good for alerting the user to
        system changes dynamically in between commands. For instance you could alter the color of the prompt to
        indicate a system status or increase a counter to report an event. If you do alter the actual text of the
        prompt, it is best to keep the prompt the same width as what's on screen. Otherwise the user's input text will
        be shifted and the update will not be seamless.

        IMPORTANT: This function will not update the prompt unless it can acquire self.terminal_lock to ensure
                   a prompt is onscreen. Therefore, it is best to acquire the lock before calling this function
                   to guarantee the prompt changes and to avoid raising a RuntimeError.

                   This function is only needed when you need to update the prompt while the main thread is blocking
                   at the prompt. Therefore, this should never be called from the main thread. Doing so will
                   raise a RuntimeError.

                   If user is at a continuation prompt while entering a multiline command, the onscreen prompt will
                   not change. However, self.prompt will still be updated and display immediately after the multiline
                   line command completes.

        :param new_prompt: what to change the prompt to
        :raises RuntimeError: if called from the main thread.
        :raises RuntimeError: if called while another thread holds `terminal_lock`
        """
    @staticmethod
    def set_window_title(title: str) -> None:
        """
        Set the terminal window title.

        NOTE: This function writes to stderr. Therefore, if you call this during a command run by a pyscript,
              the string which updates the title will appear in that command's CommandResult.stderr data.

        :param title: the new window title
        """
    def enable_command(self, command: str) -> None:
        """
        Enable a command by restoring its functions

        :param command: the command being enabled
        """
    def enable_category(self, category: str) -> None:
        """
        Enable an entire category of commands

        :param category: the category to enable
        """
    def disable_command(self, command: str, message_to_print: str) -> None:
        '''
        Disable a command and overwrite its functions

        :param command: the command being disabled
        :param message_to_print: what to print when this command is run or help is called on it while disabled

                                 The variable cmd2.COMMAND_NAME can be used as a placeholder for the name of the
                                 command being disabled.
                                 ex: message_to_print = f"{cmd2.COMMAND_NAME} is currently disabled"
        '''
    def disable_category(self, category: str, message_to_print: str) -> None:
        '''Disable an entire category of commands.

        :param category: the category to disable
        :param message_to_print: what to print when anything in this category is run or help is called on it
                                 while disabled. The variable cmd2.COMMAND_NAME can be used as a placeholder for the name
                                 of the command being disabled.
                                 ex: message_to_print = f"{cmd2.COMMAND_NAME} is currently disabled"
        '''
    intro: Incomplete
    def cmdloop(self, intro: str | None = None) -> int:
        """This is an outer wrapper around _cmdloop() which deals with extra features provided by cmd2.

        _cmdloop() provides the main loop equivalent to cmd.cmdloop().  This is a wrapper around that which deals with
        the following extra features provided by cmd2:
        - transcript testing
        - intro banner
        - exit code

        :param intro: if provided this overrides self.intro and serves as the intro banner printed once at start
        """
    def register_preloop_hook(self, func: Callable[[], None]) -> None:
        """Register a function to be called at the beginning of the command loop."""
    def register_postloop_hook(self, func: Callable[[], None]) -> None:
        """Register a function to be called at the end of the command loop."""
    def register_postparsing_hook(self, func: Callable[[plugin.PostparsingData], plugin.PostparsingData]) -> None:
        """Register a function to be called after parsing user input but before running the command"""
    CommandDataType = TypeVar('CommandDataType')
    def register_precmd_hook(self, func: Callable[[plugin.PrecommandData], plugin.PrecommandData]) -> None:
        """Register a hook to be called before the command function."""
    def register_postcmd_hook(self, func: Callable[[plugin.PostcommandData], plugin.PostcommandData]) -> None:
        """Register a hook to be called after the command function."""
    def register_cmdfinalization_hook(self, func: Callable[[plugin.CommandFinalizationData], plugin.CommandFinalizationData]) -> None:
        """Register a hook to be called after a command is completed, whether it completes successfully or not."""
