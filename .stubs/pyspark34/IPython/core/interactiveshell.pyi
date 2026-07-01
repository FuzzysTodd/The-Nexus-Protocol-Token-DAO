import abc
from IPython.core import magic as magic, oinspect as oinspect, page as page, prefilter as prefilter, ultratb as ultratb
from IPython.core.alias import Alias as Alias, AliasManager as AliasManager
from IPython.core.autocall import ExitAutocall as ExitAutocall
from IPython.core.builtin_trap import BuiltinTrap as BuiltinTrap
from IPython.core.compilerop import CachingCompiler as CachingCompiler
from IPython.core.debugger import InterruptiblePdb as InterruptiblePdb
from IPython.core.display_trap import DisplayTrap as DisplayTrap
from IPython.core.displayhook import DisplayHook as DisplayHook
from IPython.core.displaypub import DisplayPublisher as DisplayPublisher
from IPython.core.error import InputRejected as InputRejected, UsageError as UsageError
from IPython.core.events import EventManager as EventManager, available_events as available_events
from IPython.core.extensions import ExtensionManager as ExtensionManager
from IPython.core.formatters import DisplayFormatter as DisplayFormatter
from IPython.core.history import HistoryManager as HistoryManager
from IPython.core.inputtransformer2 import ESC_MAGIC as ESC_MAGIC, ESC_MAGIC2 as ESC_MAGIC2
from IPython.core.logger import Logger as Logger
from IPython.core.macro import Macro as Macro
from IPython.core.oinspect import OInfo as OInfo
from IPython.core.payload import PayloadManager as PayloadManager
from IPython.core.prefilter import PrefilterManager as PrefilterManager
from IPython.core.profiledir import ProfileDir as ProfileDir
from IPython.core.usage import default_banner as default_banner
from IPython.display import display as display
from IPython.paths import get_ipython_dir as get_ipython_dir
from IPython.testing.skipdoctest import skip_doctest as skip_doctest
from IPython.utils import PyColorize as PyColorize, io as io, openpy as openpy, py3compat as py3compat
from IPython.utils.decorators import undoc as undoc
from IPython.utils.io import ask_yes_no as ask_yes_no
from IPython.utils.ipstruct import Struct as Struct
from IPython.utils.path import ensure_dir_exists as ensure_dir_exists, get_home_dir as get_home_dir, get_py_filename as get_py_filename
from IPython.utils.process import getoutput as getoutput, system as system
from IPython.utils.strdispatch import StrDispatch as StrDispatch
from IPython.utils.syspathcontext import prepended_to_syspath as prepended_to_syspath
from IPython.utils.text import DollarFormatter as DollarFormatter, LSString as LSString, SList as SList, format_screen as format_screen
from _typeshed import Incomplete
from ast import stmt
from pathlib import Path
from traitlets import Unicode
from traitlets.config.configurable import SingletonConfigurable
from typing import Any as AnyType, Callable, List as ListType, Tuple

sphinxify: Callable | None

class ProvisionalWarning(DeprecationWarning):
    """
    Warning class for unstable features
    """

dedent_re: Incomplete

def is_integer_string(s: str):
    '''
    Variant of "str.isnumeric()" that allow negative values and other ints.
    '''
def softspace(file, newvalue):
    """Copied from code.py, to remove the dependency"""
def no_op(*a, **kw) -> None: ...

class SpaceInInput(Exception): ...

class SeparateUnicode(Unicode):
    """A Unicode subclass to validate separate_in, separate_out, etc.

    This is a Unicode based trait that converts '0'->'' and ``'\\\\n'->'\\n'``.
    """
    def validate(self, obj, value): ...

class DummyMod:
    """A dummy module used for IPython's interactive module when
    a namespace must be assigned to the module's __dict__."""

class ExecutionInfo:
    """The arguments used for a call to :meth:`InteractiveShell.run_cell`

    Stores information about what is going to happen.
    """
    raw_cell: Incomplete
    store_history: bool
    silent: bool
    shell_futures: bool
    cell_id: Incomplete
    def __init__(self, raw_cell, store_history, silent, shell_futures, cell_id) -> None: ...

class ExecutionResult:
    """The result of a call to :meth:`InteractiveShell.run_cell`

    Stores information about what took place.
    """
    execution_count: Incomplete
    error_before_exec: Incomplete
    error_in_exec: BaseException | None
    info: Incomplete
    result: Incomplete
    def __init__(self, info) -> None: ...
    @property
    def success(self): ...
    def raise_error(self) -> None:
        """Reraises error if `success` is `False`, otherwise does nothing"""

class InteractiveShell(SingletonConfigurable):
    """An enhanced, interactive shell for Python."""
    ast_transformers: Incomplete
    autocall: Incomplete
    autoindent: Incomplete
    autoawait: Incomplete
    loop_runner_map: Incomplete
    loop_runner: Incomplete
    automagic: Incomplete
    banner1: Incomplete
    banner2: Incomplete
    cache_size: Incomplete
    color_info: Incomplete
    colors: Incomplete
    debug: Incomplete
    disable_failing_post_execute: Incomplete
    display_formatter: Incomplete
    displayhook_class: Incomplete
    display_pub_class: Incomplete
    compiler_class: Incomplete
    inspector_class: Incomplete
    sphinxify_docstring: Incomplete
    enable_html_pager: Incomplete
    data_pub_class: Incomplete
    exit_now: Incomplete
    exiter: Incomplete
    execution_count: Incomplete
    filename: Incomplete
    ipython_dir: Incomplete
    input_transformer_manager: Incomplete
    @property
    def input_transformers_cleanup(self): ...
    input_transformers_post: Incomplete
    @property
    def input_splitter(self):
        """Make this available for backward compatibility (pre-7.0 release) with existing code.

        For example, ipykernel ipykernel currently uses
        `shell.input_splitter.check_complete`
        """
    logstart: Incomplete
    logfile: Incomplete
    logappend: Incomplete
    object_info_string_level: Incomplete
    pdb: Incomplete
    display_page: Incomplete
    show_rewritten_input: Incomplete
    quiet: Incomplete
    history_length: Incomplete
    history_load_length: Incomplete
    ast_node_interactivity: Incomplete
    warn_venv: Incomplete
    separate_in: Incomplete
    separate_out: Incomplete
    separate_out2: Incomplete
    wildcards_case_sensitive: Incomplete
    xmode: Incomplete
    alias_manager: Incomplete
    prefilter_manager: Incomplete
    builtin_trap: Incomplete
    display_trap: Incomplete
    extension_manager: Incomplete
    payload_manager: Incomplete
    history_manager: Incomplete
    magics_manager: Incomplete
    profile_dir: Incomplete
    @property
    def profile(self): ...
    pylab_gui_select: Incomplete
    last_execution_succeeded: Incomplete
    last_execution_result: Incomplete
    configurables: Incomplete
    db: Incomplete
    raw_input_original: Incomplete
    trio_runner: Incomplete
    def __init__(self, ipython_dir: Incomplete | None = None, profile_dir: Incomplete | None = None, user_module: Incomplete | None = None, user_ns: Incomplete | None = None, custom_exceptions=((), None), **kwargs) -> None: ...
    def get_ipython(self):
        """Return the currently running IPython instance."""
    def set_autoindent(self, value: Incomplete | None = None) -> None:
        """Set the autoindent flag.

        If called with no arguments, it acts as a toggle."""
    def set_trio_runner(self, tr) -> None: ...
    def init_ipython_dir(self, ipython_dir) -> None: ...
    def init_profile_dir(self, profile_dir) -> None: ...
    more: bool
    compile: Incomplete
    meta: Incomplete
    tempfiles: Incomplete
    tempdirs: Incomplete
    starting_dir: Incomplete
    indent_current_nsp: int
    def init_instance_attrs(self) -> None: ...
    def init_environment(self) -> None:
        """Any changes we need to make to the user's environment."""
    stdin_encoding: Incomplete
    def init_encoding(self) -> None: ...
    pycolorize: Incomplete
    def init_syntax_highlighting(self, changes: Incomplete | None = None): ...
    def refresh_style(self) -> None: ...
    home_dir: Incomplete
    dir_stack: Incomplete
    def init_pushd_popd_magic(self) -> None: ...
    logger: Incomplete
    def init_logger(self) -> None: ...
    def init_logstart(self) -> None:
        """Initialize logging in case it was requested at the command line.
        """
    def init_builtins(self) -> None: ...
    inspector: Incomplete
    def init_inspector(self, changes: Incomplete | None = None) -> None: ...
    def init_io(self) -> None: ...
    def init_prompts(self) -> None: ...
    def init_display_formatter(self) -> None: ...
    display_pub: Incomplete
    def init_display_pub(self) -> None: ...
    data_pub: Incomplete
    def init_data_pub(self) -> None: ...
    displayhook: Incomplete
    def init_displayhook(self) -> None: ...
    @staticmethod
    def get_path_links(p: Path):
        """Gets path links including all symlinks

        Examples
        --------
        In [1]: from IPython.core.interactiveshell import InteractiveShell

        In [2]: import sys, pathlib

        In [3]: paths = InteractiveShell.get_path_links(pathlib.Path(sys.executable))

        In [4]: len(paths) == len(set(paths))
        Out[4]: True

        In [5]: bool(paths)
        Out[5]: True
        """
    def init_virtualenv(self) -> None:
        """Add the current virtualenv to sys.path so the user can import modules from it.
        This isn't perfect: it doesn't use the Python interpreter with which the
        virtualenv was built, and it ignores the --no-site-packages option. A
        warning will appear suggesting the user installs IPython in the
        virtualenv, but for many cases, it probably works well enough.

        Adapted from code snippets online.

        http://blog.ufsoft.org/2009/1/29/ipython-and-virtualenv
        """
    def save_sys_module_state(self) -> None:
        """Save the state of hooks in the sys module.

        This has to be called after self.user_module is created.
        """
    def restore_sys_module_state(self) -> None:
        """Restore the state of the sys module."""
    @property
    def banner(self): ...
    def show_banner(self, banner: Incomplete | None = None) -> None: ...
    hooks: Incomplete
    strdispatchers: Incomplete
    def init_hooks(self) -> None: ...
    def set_hook(self, name, hook, priority: int = 50, str_key: Incomplete | None = None, re_key: Incomplete | None = None) -> None:
        """set_hook(name,hook) -> sets an internal IPython hook.

        IPython exposes some of its internal API as user-modifiable hooks.  By
        adding your function to one of these hooks, you can modify IPython's
        behavior to call at runtime your own routines."""
    events: Incomplete
    def init_events(self) -> None: ...
    def register_post_execute(self, func) -> None:
        """DEPRECATED: Use ip.events.register('post_run_cell', func)

        Register a function for calling after code execution.
        """
    def new_main_mod(self, filename, modname):
        """Return a new 'main' module object for user code execution.

        ``filename`` should be the path of the script which will be run in the
        module. Requests with the same filename will get the same module, with
        its namespace cleared.

        ``modname`` should be the module name - normally either '__main__' or
        the basename of the file without the extension.

        When scripts are executed via %run, we must keep a reference to their
        __main__ module around so that Python doesn't
        clear it, rendering references to module globals useless.

        This method keeps said reference in a private dict, keyed by the
        absolute path of the script. This way, for multiple executions of the
        same script we only keep one copy of the namespace (the last one),
        thus preventing memory leaks from old references while allowing the
        objects from the last execution to be accessible.
        """
    def clear_main_mod_cache(self) -> None:
        """Clear the cache of main modules.

        Mainly for use by utilities like %reset.

        Examples
        --------
        In [15]: import IPython

        In [16]: m = _ip.new_main_mod(IPython.__file__, 'IPython')

        In [17]: len(_ip._main_mod_cache) > 0
        Out[17]: True

        In [18]: _ip.clear_main_mod_cache()

        In [19]: len(_ip._main_mod_cache) == 0
        Out[19]: True
        """
    call_pdb: Incomplete
    def init_pdb(self) -> None: ...
    def debugger(self, force: bool = False) -> None:
        """Call the pdb debugger.

        Keywords:

          - force(False): by default, this routine checks the instance call_pdb
            flag and does not actually invoke the debugger if the flag is false.
            The 'force' option forces the debugger to activate even if the flag
            is false.
        """
    default_user_namespaces: bool
    user_ns_hidden: Incomplete
    ns_table: Incomplete
    def init_create_namespaces(self, user_module: Incomplete | None = None, user_ns: Incomplete | None = None) -> None: ...
    @property
    def user_global_ns(self): ...
    def prepare_user_module(self, user_module: Incomplete | None = None, user_ns: Incomplete | None = None):
        """Prepare the module and namespace in which user code will be run.

        When IPython is started normally, both parameters are None: a new module
        is created automatically, and its __dict__ used as the namespace.

        If only user_module is provided, its __dict__ is used as the namespace.
        If only user_ns is provided, a dummy module is created, and user_ns
        becomes the global namespace. If both are provided (as they may be
        when embedding), user_ns is the local namespace, and user_module
        provides the global namespace.

        Parameters
        ----------
        user_module : module, optional
            The current user module in which IPython is being run. If None,
            a clean module will be created.
        user_ns : dict, optional
            A namespace in which to run interactive commands.

        Returns
        -------
        A tuple of user_module and user_ns, each properly initialised.
        """
    def init_sys_modules(self) -> None: ...
    def init_user_ns(self) -> None:
        """Initialize all user-visible namespaces to their minimum defaults.

        Certain history lists are also initialized here, as they effectively
        act as user namespaces.

        Notes
        -----
        All data structures here are only filled in, they are NOT reset by this
        method.  If they were not empty before, data will simply be added to
        them.
        """
    @property
    def all_ns_refs(self):
        """Get a list of references to all the namespace dictionaries in which
        IPython might store a user-created object.

        Note that this does not include the displayhook, which also caches
        objects from the output."""
    def reset(self, new_session: bool = True, aggressive: bool = False) -> None:
        """Clear all internal namespaces, and attempt to release references to
        user objects.

        If new_session is True, a new history session will be opened.
        """
    def del_var(self, varname, by_name: bool = False) -> None:
        """Delete a variable from the various namespaces, so that, as
        far as possible, we're not keeping any hidden references to it.

        Parameters
        ----------
        varname : str
            The name of the variable to delete.
        by_name : bool
            If True, delete variables with the given name in each
            namespace. If False (default), find the variable in the user
            namespace, and delete references to it.
        """
    def reset_selective(self, regex: Incomplete | None = None) -> None:
        """Clear selective variables from internal namespaces based on a
        specified regular expression.

        Parameters
        ----------
        regex : string or compiled pattern, optional
            A regular expression pattern that will be used in searching
            variable names in the users namespaces.
        """
    def push(self, variables, interactive: bool = True) -> None:
        """Inject a group of variables into the IPython user namespace.

        Parameters
        ----------
        variables : dict, str or list/tuple of str
            The variables to inject into the user's namespace.  If a dict, a
            simple update is done.  If a str, the string is assumed to have
            variable names separated by spaces.  A list/tuple of str can also
            be used to give the variable names.  If just the variable names are
            give (list/tuple/str) then the variable values looked up in the
            callers frame.
        interactive : bool
            If True (default), the variables will be listed with the ``who``
            magic.
        """
    def drop_by_id(self, variables) -> None:
        """Remove a dict of variables from the user namespace, if they are the
        same as the values in the dictionary.

        This is intended for use by extensions: variables that they've added can
        be taken back out if they are unloaded, without removing any that the
        user has overwritten.

        Parameters
        ----------
        variables : dict
            A dictionary mapping object names (as strings) to the objects.
        """
    def object_inspect(self, oname, detail_level: int = 0):
        """Get object info about oname"""
    def object_inspect_text(self, oname, detail_level: int = 0):
        """Get object info as formatted text"""
    def object_inspect_mime(self, oname, detail_level: int = 0, omit_sections=()):
        """Get object info as a mimebundle of formatted representations.

        A mimebundle is a dictionary, keyed by mime-type.
        It must always have the key `'text/plain'`.
        """
    def init_history(self) -> None:
        """Sets up the command history, and starts regular autosaves."""
    debugger_cls = InterruptiblePdb
    SyntaxTB: Incomplete
    InteractiveTB: Incomplete
    sys_excepthook: Incomplete
    def init_traceback_handlers(self, custom_exceptions) -> None: ...
    CustomTB: Incomplete
    custom_exceptions: Incomplete
    def set_custom_exc(self, exc_tuple, handler):
        """set_custom_exc(exc_tuple, handler)

        Set a custom exception handler, which will be called if any of the
        exceptions in exc_tuple occur in the mainloop (specifically, in the
        run_code() method).

        Parameters
        ----------
        exc_tuple : tuple of exception classes
            A *tuple* of exception classes, for which to call the defined
            handler.  It is very important that you use a tuple, and NOT A
            LIST here, because of the way Python's except statement works.  If
            you only want to trap a single exception, use a singleton tuple::

                exc_tuple == (MyCustomException,)

        handler : callable
            handler must have the following signature::

                def my_handler(self, etype, value, tb, tb_offset=None):
                    ...
                    return structured_traceback

            Your handler must return a structured traceback (a list of strings),
            or None.

            This will be made into an instance method (via types.MethodType)
            of IPython itself, and it will be called if any of the exceptions
            listed in the exc_tuple are caught. If the handler is None, an
            internal basic one is used, which just prints basic info.

            To protect IPython from crashes, if your handler ever raises an
            exception or returns an invalid result, it will be immediately
            disabled.

        Notes
        -----
        WARNING: by putting in your own exception handler into IPython's main
        execution loop, you run a very good chance of nasty crashes.  This
        facility should only be used if you really know what you are doing.
        """
    def excepthook(self, etype, value, tb) -> None:
        """One more defense for GUI apps that call sys.excepthook.

        GUI frameworks like wxPython trap exceptions and call
        sys.excepthook themselves.  I guess this is a feature that
        enables them to keep running after exceptions that would
        otherwise kill their mainloop. This is a bother for IPython
        which expects to catch all of the program exceptions with a try:
        except: statement.

        Normally, IPython sets sys.excepthook to a CrashHandler instance, so if
        any app directly invokes sys.excepthook, it will look to the user like
        IPython crashed.  In order to work around this, we can disable the
        CrashHandler and replace it with this excepthook instead, which prints a
        regular traceback using our InteractiveTB.  In this fashion, apps which
        call sys.excepthook will generate a regular-looking exception from
        IPython, and the CrashHandler will only be triggered by real IPython
        crashes.

        This hook should be used sparingly, only in places which are not likely
        to be true IPython errors.
        """
    def show_usage_error(self, exc) -> None:
        """Show a short message for UsageErrors

        These are special exceptions that shouldn't show a traceback.
        """
    def get_exception_only(self, exc_tuple: Incomplete | None = None):
        """
        Return as a string (ending with a newline) the exception that
        just occurred, without any traceback.
        """
    def showtraceback(self, exc_tuple: Incomplete | None = None, filename: Incomplete | None = None, tb_offset: Incomplete | None = None, exception_only: bool = False, running_compiled_code: bool = False) -> None:
        """Display the exception that just occurred.

        If nothing is known about the exception, this is the method which
        should be used throughout the code for presenting user tracebacks,
        rather than directly invoking the InteractiveTB object.

        A specific showsyntaxerror() also exists, but this method can take
        care of calling it if needed, so unless you are explicitly catching a
        SyntaxError exception, don't try to analyze the stack manually and
        simply call this method."""
    def showsyntaxerror(self, filename: Incomplete | None = None, running_compiled_code: bool = False) -> None:
        '''Display the syntax error that just occurred.

        This doesn\'t display a stack trace because there isn\'t one.

        If a filename is given, it is stuffed in the exception instead
        of what was there before (because Python\'s parser always uses
        "<string>" when reading from a string).

        If the syntax error occurred when running a compiled code (i.e. running_compile_code=True),
        longer stack trace will be displayed.
        '''
    def showindentationerror(self) -> None:
        """Called by _run_cell when there's an IndentationError in code entered
        at the prompt.

        This is overridden in TerminalInteractiveShell to show a message about
        the %paste magic."""
    rl_next_input: Incomplete
    def set_next_input(self, s, replace: bool = False) -> None:
        ''' Sets the \'default\' input string for the next command line.

        Example::

            In [1]: _ip.set_next_input("Hello Word")
            In [2]: Hello Word_  # cursor is here
        '''
    Completer: Incomplete
    def init_completer(self) -> None:
        """Initialize the completion machinery.

        This creates completion machinery that can be used by client code,
        either interactively in-process (typically triggered by the readline
        library), programmatically (such as in test suites) or out-of-process
        (typically over the network by remote frontends).
        """
    def complete(self, text, line: Incomplete | None = None, cursor_pos: Incomplete | None = None):
        """Return the completed text and a list of completions.

        Parameters
        ----------
        text : string
            A string of text to be completed on.  It can be given as empty and
            instead a line/position pair are given.  In this case, the
            completer itself will split the line like readline does.
        line : string, optional
            The complete line that text is part of.
        cursor_pos : int, optional
            The position of the cursor on the input line.

        Returns
        -------
        text : string
            The actual text that was completed.
        matches : list
            A sorted list with all possible completions.

        Notes
        -----
        The optional arguments allow the completion to take more context into
        account, and are part of the low-level completion API.

        This is a wrapper around the completion mechanism, similar to what
        readline does at the command line when the TAB key is hit.  By
        exposing it as a method, it can be used by other non-readline
        environments (such as GUIs) for text completion.

        Examples
        --------
        In [1]: x = 'hello'

        In [2]: _ip.complete('x.l')
        Out[2]: ('x.l', ['x.ljust', 'x.lower', 'x.lstrip'])
        """
    def set_custom_completer(self, completer, pos: int = 0) -> None:
        """Adds a new custom completer function.

        The position argument (defaults to 0) is the index in the completers
        list where you want the completer to be inserted.

        `completer` should have the following signature::

            def completion(self: Completer, text: string) -> List[str]:
                raise NotImplementedError

        It will be bound to the current Completer instance and pass some text
        and return a list with current completions to suggest to the user.
        """
    def set_completer_frame(self, frame: Incomplete | None = None) -> None:
        """Set the frame of the completer."""
    register_magics: Incomplete
    def init_magics(self) -> None: ...
    def register_magic_function(self, func, magic_kind: str = 'line', magic_name: Incomplete | None = None) -> None: ...
    def run_line_magic(self, magic_name: str, line, _stack_depth: int = 1):
        """Execute the given line magic.

        Parameters
        ----------
        magic_name : str
            Name of the desired magic function, without '%' prefix.
        line : str
            The rest of the input line as a single string.
        _stack_depth : int
            If run_line_magic() is called from magic() then _stack_depth=2.
            This is added to ensure backward compatibility for use of 'get_ipython().magic()'
        """
    def get_local_scope(self, stack_depth):
        """Get local scope at given stack depth.

        Parameters
        ----------
        stack_depth : int
            Depth relative to calling frame
        """
    def run_cell_magic(self, magic_name, line, cell):
        """Execute the given cell magic.

        Parameters
        ----------
        magic_name : str
            Name of the desired magic function, without '%' prefix.
        line : str
            The rest of the first input line as a single string.
        cell : str
            The body of the cell as a (possibly multiline) string.
        """
    def find_line_magic(self, magic_name):
        """Find and return a line magic by name.

        Returns None if the magic isn't found."""
    def find_cell_magic(self, magic_name):
        """Find and return a cell magic by name.

        Returns None if the magic isn't found."""
    def find_magic(self, magic_name, magic_kind: str = 'line'):
        """Find and return a magic of the given type by name.

        Returns None if the magic isn't found."""
    def magic(self, arg_s):
        """
        DEPRECATED

        Deprecated since IPython 0.13 (warning added in
        8.1), use run_line_magic(magic_name, parameter_s).

        Call a magic function by name.

        Input: a string containing the name of the magic function to call and
        any additional arguments to be passed to the magic.

        magic('name -opt foo bar') is equivalent to typing at the ipython
        prompt:

        In[1]: %name -opt foo bar

        To call a magic without arguments, simply use magic('name').

        This provides a proper Python function to call IPython's magics in any
        valid Python code you can type at the interpreter, including loops and
        compound statements.
        """
    def define_macro(self, name, themacro) -> None:
        """Define a new macro

        Parameters
        ----------
        name : str
            The name of the macro.
        themacro : str or Macro
            The action to do upon invoking the macro.  If a string, a new
            Macro object is created by passing the string to it.
        """
    def system_piped(self, cmd) -> None:
        """Call the given cmd in a subprocess, piping stdout/err

        Parameters
        ----------
        cmd : str
            Command to execute (can not end in '&', as background processes are
            not supported.  Should not be a command that expects input
            other than simple text.
        """
    def system_raw(self, cmd) -> None:
        """Call the given cmd in a subprocess using os.system on Windows or
        subprocess.call using the system shell on other platforms.

        Parameters
        ----------
        cmd : str
            Command to execute.
        """
    system = system_piped
    def getoutput(self, cmd, split: bool = True, depth: int = 0):
        """Get output (possibly including stderr) from a subprocess.

        Parameters
        ----------
        cmd : str
            Command to execute (can not end in '&', as background processes are
            not supported.
        split : bool, optional
            If True, split the output into an IPython SList.  Otherwise, an
            IPython LSString is returned.  These are objects similar to normal
            lists and strings, with a few convenience attributes for easier
            manipulation of line-based output.  You can use '?' on them for
            details.
        depth : int, optional
            How many frames above the caller are the local variables which should
            be expanded in the command string? The default (0) assumes that the
            expansion variables are in the stack frame calling this function.
        """
    def init_alias(self) -> None: ...
    def init_extension_manager(self) -> None: ...
    def init_payload(self) -> None: ...
    prefilter: Incomplete
    def init_prefilter(self) -> None: ...
    def auto_rewrite_input(self, cmd) -> None:
        """Print to the screen the rewritten form of the user's command.

        This shows visual feedback by rewriting input lines that cause
        automatic calling to kick in, like::

          /f x

        into::

          ------> f(x)

        after the user's input prompt.  This helps the user understand that the
        input line was transformed automatically by IPython.
        """
    def user_expressions(self, expressions):
        """Evaluate a dict of expressions in the user's namespace.

        Parameters
        ----------
        expressions : dict
            A dict with string keys and string values.  The expression values
            should be valid Python expressions, each of which will be evaluated
            in the user namespace.

        Returns
        -------
        A dict, keyed like the input expressions dict, with the rich mime-typed
        display_data of each value.
        """
    def ex(self, cmd) -> None:
        """Execute a normal python statement in user namespace."""
    def ev(self, expr):
        """Evaluate python expression expr in user namespace.

        Returns the result of evaluation
        """
    def safe_execfile(self, fname, *where, exit_ignore: bool = False, raise_exceptions: bool = False, shell_futures: bool = False) -> None:
        """A safe version of the builtin execfile().

        This version will never throw an exception, but instead print
        helpful error messages to the screen.  This only works on pure
        Python files with the .py extension.

        Parameters
        ----------
        fname : string
            The name of the file to be executed.
        *where : tuple
            One or two namespaces, passed to execfile() as (globals,locals).
            If only one is given, it is passed as both.
        exit_ignore : bool (False)
            If True, then silence SystemExit for non-zero status (it is always
            silenced for zero status, as it is so common).
        raise_exceptions : bool (False)
            If True raise exceptions everywhere. Meant for testing.
        shell_futures : bool (False)
            If True, the code will share future statements with the interactive
            shell. It will both be affected by previous __future__ imports, and
            any __future__ imports in the code will affect the shell. If False,
            __future__ imports are not shared in either direction.

        """
    def safe_execfile_ipy(self, fname, shell_futures: bool = False, raise_exceptions: bool = False) -> None:
        """Like safe_execfile, but for .ipy or .ipynb files with IPython syntax.

        Parameters
        ----------
        fname : str
            The name of the file to execute.  The filename must have a
            .ipy or .ipynb extension.
        shell_futures : bool (False)
            If True, the code will share future statements with the interactive
            shell. It will both be affected by previous __future__ imports, and
            any __future__ imports in the code will affect the shell. If False,
            __future__ imports are not shared in either direction.
        raise_exceptions : bool (False)
            If True raise exceptions everywhere.  Meant for testing.
        """
    def safe_run_module(self, mod_name, where) -> None:
        """A safe version of runpy.run_module().

        This version will never throw an exception, but instead print
        helpful error messages to the screen.

        `SystemExit` exceptions with status code 0 or None are ignored.

        Parameters
        ----------
        mod_name : string
            The name of the module to be executed.
        where : dict
            The globals namespace.
        """
    def run_cell(self, raw_cell, store_history: bool = False, silent: bool = False, shell_futures: bool = True, cell_id: Incomplete | None = None):
        """Run a complete IPython cell.

        Parameters
        ----------
        raw_cell : str
            The code (including IPython code such as %magic functions) to run.
        store_history : bool
            If True, the raw and translated cell will be stored in IPython's
            history. For user code calling back into IPython's machinery, this
            should be set to False.
        silent : bool
            If True, avoid side-effects, such as implicit displayhooks and
            and logging.  silent=True forces store_history=False.
        shell_futures : bool
            If True, the code will share future statements with the interactive
            shell. It will both be affected by previous __future__ imports, and
            any __future__ imports in the code will affect the shell. If False,
            __future__ imports are not shared in either direction.

        Returns
        -------
        result : :class:`ExecutionResult`
        """
    def should_run_async(self, raw_cell: str, *, transformed_cell: Incomplete | None = None, preprocessing_exc_tuple: Incomplete | None = None) -> bool:
        """Return whether a cell should be run asynchronously via a coroutine runner

        Parameters
        ----------
        raw_cell : str
            The code to be executed

        Returns
        -------
        result: bool
            Whether the code needs to be run with a coroutine runner or not
        .. versionadded:: 7.0
        """
    async def run_cell_async(self, raw_cell: str, store_history: bool = False, silent: bool = False, shell_futures: bool = True, *, transformed_cell: str | None = None, preprocessing_exc_tuple: AnyType | None = None, cell_id: Incomplete | None = None) -> ExecutionResult:
        """Run a complete IPython cell asynchronously.

        Parameters
        ----------
        raw_cell : str
          The code (including IPython code such as %magic functions) to run.
        store_history : bool
          If True, the raw and translated cell will be stored in IPython's
          history. For user code calling back into IPython's machinery, this
          should be set to False.
        silent : bool
          If True, avoid side-effects, such as implicit displayhooks and
          and logging.  silent=True forces store_history=False.
        shell_futures : bool
          If True, the code will share future statements with the interactive
          shell. It will both be affected by previous __future__ imports, and
          any __future__ imports in the code will affect the shell. If False,
          __future__ imports are not shared in either direction.
        transformed_cell: str
          cell that was passed through transformers
        preprocessing_exc_tuple:
          trace if the transformation failed.

        Returns
        -------
        result : :class:`ExecutionResult`

        .. versionadded:: 7.0
        """
    def transform_cell(self, raw_cell):
        """Transform an input cell before parsing it.

        Static transformations, implemented in IPython.core.inputtransformer2,
        deal with things like ``%magic`` and ``!system`` commands.
        These run on all input.
        Dynamic transformations, for things like unescaped magics and the exit
        autocall, depend on the state of the interpreter.
        These only apply to single line inputs.

        These string-based transformations are followed by AST transformations;
        see :meth:`transform_ast`.
        """
    def transform_ast(self, node):
        """Apply the AST transformations from self.ast_transformers

        Parameters
        ----------
        node : ast.Node
            The root node to be transformed. Typically called with the ast.Module
            produced by parsing user input.

        Returns
        -------
        An ast.Node corresponding to the node it was called with. Note that it
        may also modify the passed object, so don't rely on references to the
        original AST.
        """
    async def run_ast_nodes(self, nodelist: ListType[stmt], cell_name: str, interactivity: str = 'last_expr', compiler=..., result: Incomplete | None = None):
        """Run a sequence of AST nodes. The execution mode depends on the
        interactivity parameter.

        Parameters
        ----------
        nodelist : list
          A sequence of AST nodes to run.
        cell_name : str
          Will be passed to the compiler as the filename of the cell. Typically
          the value returned by ip.compile.cache(cell).
        interactivity : str
          'all', 'last', 'last_expr' , 'last_expr_or_assign' or 'none',
          specifying which nodes should be run interactively (displaying output
          from expressions). 'last_expr' will run the last node interactively
          only if it is an expression (i.e. expressions in loops or other blocks
          are not displayed) 'last_expr_or_assign' will run the last expression
          or the last assignment. Other values for this parameter will raise a
          ValueError.

        compiler : callable
          A function with the same interface as the built-in compile(), to turn
          the AST nodes into code objects. Default is the built-in compile().
        result : ExecutionResult, optional
          An object to store exceptions that occur during execution.

        Returns
        -------
        True if an exception occurred while running code, False if it finished
        running.
        """
    async def run_code(self, code_obj, result: Incomplete | None = None, *, async_: bool = False):
        """Execute a code object.

        When an exception occurs, self.showtraceback() is called to display a
        traceback.

        Parameters
        ----------
        code_obj : code object
          A compiled code object, to be executed
        result : ExecutionResult, optional
          An object to store exceptions that occur during execution.
        async_ :  Bool (Experimental)
          Attempt to run top-level asynchronous code in a default loop.

        Returns
        -------
        False : successful execution.
        True : an error occurred.
        """
    runcode = run_code
    def check_complete(self, code: str) -> Tuple[str, str]:
        """Return whether a block of code is ready to execute, or should be continued

        Parameters
        ----------
        code : string
            Python input code, which can be multiline.

        Returns
        -------
        status : str
            One of 'complete', 'incomplete', or 'invalid' if source is not a
            prefix of valid code.
        indent : str
            When status is 'incomplete', this is some whitespace to insert on
            the next line of the prompt.
        """
    active_eventloop: Incomplete
    def enable_gui(self, gui: Incomplete | None = None) -> None: ...
    def enable_matplotlib(self, gui: Incomplete | None = None):
        """Enable interactive matplotlib and inline figure support.

        This takes the following steps:

        1. select the appropriate eventloop and matplotlib backend
        2. set up matplotlib for interactive use with that backend
        3. configure formatters for inline figure display
        4. enable the selected gui eventloop

        Parameters
        ----------
        gui : optional, string
            If given, dictates the choice of matplotlib GUI backend to use
            (should be one of IPython's supported backends, 'qt', 'osx', 'tk',
            'gtk', 'wx' or 'inline'), otherwise we use the default chosen by
            matplotlib (as dictated by the matplotlib build-time options plus the
            user's matplotlibrc configuration file).  Note that not all backends
            make sense in all contexts, for example a terminal ipython can't
            display figures inline.
        """
    def enable_pylab(self, gui: Incomplete | None = None, import_all: bool = True, welcome_message: bool = False):
        """Activate pylab support at runtime.

        This turns on support for matplotlib, preloads into the interactive
        namespace all of numpy and pylab, and configures IPython to correctly
        interact with the GUI event loop.  The GUI backend to be used can be
        optionally selected with the optional ``gui`` argument.

        This method only adds preloading the namespace to InteractiveShell.enable_matplotlib.

        Parameters
        ----------
        gui : optional, string
            If given, dictates the choice of matplotlib GUI backend to use
            (should be one of IPython's supported backends, 'qt', 'osx', 'tk',
            'gtk', 'wx' or 'inline'), otherwise we use the default chosen by
            matplotlib (as dictated by the matplotlib build-time options plus the
            user's matplotlibrc configuration file).  Note that not all backends
            make sense in all contexts, for example a terminal ipython can't
            display figures inline.
        import_all : optional, bool, default: True
            Whether to do `from numpy import *` and `from pylab import *`
            in addition to module imports.
        welcome_message : deprecated
            This argument is ignored, no welcome message will be displayed.
        """
    def var_expand(self, cmd, depth: int = 0, formatter=...):
        """Expand python variables in a string.

        The depth argument indicates how many frames above the caller should
        be walked to look for the local namespace where to expand variables.

        The global namespace for expansion is always the user's interactive
        namespace.
        """
    def mktempfile(self, data: Incomplete | None = None, prefix: str = 'ipython_edit_'):
        """Make a new tempfile and return its filename.

        This makes a call to tempfile.mkstemp (created in a tempfile.mkdtemp),
        but it registers the created filename internally so ipython cleans it up
        at exit time.

        Optional inputs:

          - data(None): if data is given, it gets written out to the temp file
            immediately, and the file is closed again."""
    def ask_yes_no(self, prompt, default: Incomplete | None = None, interrupt: Incomplete | None = None): ...
    def show_usage(self) -> None:
        """Show a usage message"""
    def extract_input_lines(self, range_str, raw: bool = False):
        '''Return as a string a set of input history slices.

        Parameters
        ----------
        range_str : str
            The set of slices is given as a string, like "~5/6-~4/2 4:8 9",
            since this function is for use by magic functions which get their
            arguments as strings. The number before the / is the session
            number: ~n goes n back from the current session.

            If empty string is given, returns history of current session
            without the last input.

        raw : bool, optional
            By default, the processed input is used.  If this is true, the raw
            input history is used instead.

        Notes
        -----
        Slices can be described with two notations:

        * ``N:M`` -> standard python form, means including items N...(M-1).
        * ``N-M`` -> include items N..M (closed endpoint).
        '''
    def find_user_code(self, target, raw: bool = True, py_only: bool = False, skip_encoding_cookie: bool = True, search_ns: bool = False):
        """Get a code string from history, file, url, or a string or macro.

        This is mainly used by magic functions.

        Parameters
        ----------
        target : str
            A string specifying code to retrieve. This will be tried respectively
            as: ranges of input history (see %history for syntax), url,
            corresponding .py file, filename, or an expression evaluating to a
            string or Macro in the user namespace.

            If empty string is given, returns complete history of current
            session, without the last line.

        raw : bool
            If true (default), retrieve raw history. Has no effect on the other
            retrieval mechanisms.

        py_only : bool (default False)
            Only try to fetch python code, do not try alternative methods to decode file
            if unicode fails.

        Returns
        -------
        A string of code.
        ValueError is raised if nothing is found, and TypeError if it evaluates
        to an object of another type. In each case, .args[0] is a printable
        message.
        """
    def atexit_operations(self) -> None:
        """This will be executed at the time of exit.

        Cleanup operations and saving of persistent data that is done
        unconditionally by IPython should be performed here.

        For things that may depend on startup flags or platform specifics (such
        as having readline or not), register a separate atexit function in the
        code that has the appropriate information, rather than trying to
        clutter
        """
    def cleanup(self) -> None: ...
    def switch_doctest_mode(self, mode) -> None: ...

class InteractiveShellABC(metaclass=abc.ABCMeta):
    """An abstract base class for InteractiveShell."""
