import gdb
from Cython.Debugger import libpython as libpython
from _typeshed import Incomplete

input = raw_input
UNICODE = unicode
BYTES = str
UNICODE = str
BYTES = bytes
have_lxml: bool
CObject: str
PythonObject: str

def default_selected_gdb_frame(err: bool = True): ...
def require_cython_frame(function): ...
def dispatch_on_frame(c_command, python_command: Incomplete | None = None): ...
def require_running_program(function): ...
def gdb_function_value_to_unicode(function): ...

class CythonModule:
    name: Incomplete
    filename: Incomplete
    c_filename: Incomplete
    globals: Incomplete
    lineno_cy2c: Incomplete
    lineno_c2cy: Incomplete
    functions: Incomplete
    def __init__(self, module_name, filename, c_filename) -> None: ...

class CythonVariable:
    name: Incomplete
    cname: Incomplete
    qualified_name: Incomplete
    type: Incomplete
    lineno: Incomplete
    def __init__(self, name, cname, qualified_name, type, lineno) -> None: ...

class CythonFunction(CythonVariable):
    module: Incomplete
    pf_cname: Incomplete
    is_initmodule_function: Incomplete
    locals: Incomplete
    arguments: Incomplete
    step_into_functions: Incomplete
    def __init__(self, module, name, cname, pf_cname, qualified_name, lineno, type=..., is_initmodule_function: str = 'False') -> None: ...

class CythonBase:
    def is_cython_function(self, frame): ...
    def is_python_function(self, frame):
        """
        Tells if a frame is associated with a Python function.
        If we can't read the Python frame information, don't regard it as such.
        """
    def get_c_function_name(self, frame): ...
    def get_c_lineno(self, frame): ...
    def get_cython_function(self, frame): ...
    def get_cython_lineno(self, frame):
        """
        Get the current Cython line number. Returns 0 if there is no
        correspondence between the C and Cython code.
        """
    def get_source_desc(self, frame): ...
    def get_source_line(self, frame): ...
    def is_relevant_function(self, frame):
        """
        returns whether we care about a frame on the user-level when debugging
        Cython code
        """
    def print_stackframe(self, frame, index, is_c: bool = False):
        """
        Print a C, Cython or Python stack frame and the line of source code
        if available.
        """
    def get_remote_cython_globals_dict(self): ...
    def get_cython_globals_dict(self):
        """
        Get the Cython globals dict where the remote names are turned into
        local strings.
        """
    def print_gdb_value(self, name, value, max_name_length: Incomplete | None = None, prefix: str = '') -> None: ...
    def is_initialized(self, cython_func, local_name): ...

class SourceFileDescriptor:
    filename: Incomplete
    lexer: Incomplete
    formatter: Incomplete
    def __init__(self, filename, lexer, formatter: Incomplete | None = None) -> None: ...
    def valid(self): ...
    def lex(self, code): ...
    def get_source(self, start, stop: Incomplete | None = None, lex_source: bool = True, mark_line: int = 0, lex_entire: bool = False): ...

class CyGDBError(gdb.GdbError):
    """
    Base class for Cython-command related errors
    """
    def __init__(self, *args) -> None: ...

class NoCythonFunctionInFrameError(CyGDBError):
    """
    raised when the user requests the current cython function, which is
    unavailable
    """
    msg: str

class NoFunctionNameInFrameError(NoCythonFunctionInFrameError):
    """
    raised when the name of the C function could not be determined
    in the current C stack frame
    """
    msg: str

class CythonParameter(gdb.Parameter):
    """
    Base class for cython parameters
    """
    show_doc: Incomplete
    value: Incomplete
    def __init__(self, name, command_class, parameter_class, default: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class CompleteUnqualifiedFunctionNames(CythonParameter):
    """
    Have 'cy break' complete unqualified function or method names.
    """
class ColorizeSourceCode(CythonParameter):
    """
    Tell cygdb whether to colorize source code.
    """
class TerminalBackground(CythonParameter):
    """
    Tell cygdb about the user's terminal background (light or dark).
    """

class CythonParameters:
    """
    Simple container class that might get more functionality in the distant
    future (mostly to remind us that we're dealing with parameters).
    """
    complete_unqualified: Incomplete
    colorize_code: Incomplete
    terminal_background: Incomplete
    def __init__(self) -> None: ...

parameters: Incomplete

class CythonCommand(gdb.Command, CythonBase):
    """
    Base class for Cython commands
    """
    command_class: Incomplete
    @classmethod
    def register(cls, *args, **kwargs): ...

class CyCy(CythonCommand):
    """
    Invoke a Cython command. Available commands are:

        cy import
        cy break
        cy step
        cy next
        cy run
        cy cont
        cy finish
        cy up
        cy down
        cy select
        cy bt / cy backtrace
        cy list
        cy print
        cy set
        cy locals
        cy globals
        cy exec
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    cy: Incomplete
    cython_namespace: Incomplete
    functions_by_qualified_name: Incomplete
    functions_by_cname: Incomplete
    functions_by_name: Incomplete
    def __init__(self, name, command_class, completer_class) -> None: ...

class CyImport(CythonCommand):
    """
    Import debug information outputted by the Cython compiler
    Example: cy import FILE...
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, args, from_tty) -> None: ...

class CyBreak(CythonCommand):
    """
    Set a breakpoint for Cython code using Cython qualified name notation, e.g.:

        cy break cython_modulename.ClassName.method_name...

    or normal notation:

        cy break function_or_method_name...

    or for a line number:

        cy break cython_module:lineno...

    Set a Python breakpoint:
        Break on any function or method named 'func' in module 'modname'

            cy break -p modname.func...

        Break on any function or method named 'func'

            cy break -p func...
    """
    name: str
    command_class: Incomplete
    def invoke(self, function_names, from_tty) -> None: ...
    def complete(self, text, word): ...

class CythonInfo(CythonBase, libpython.PythonInfo):
    """
    Implementation of the interface dictated by libpython.LanguageInfo.
    """
    def lineno(self, frame): ...
    def get_source_line(self, frame): ...
    def exc_info(self, frame): ...
    def runtime_break_functions(self): ...
    def static_break_functions(self): ...

class CythonExecutionControlCommand(CythonCommand, libpython.ExecutionControlCommandBase):
    @classmethod
    def register(cls): ...

class CyStep(CythonExecutionControlCommand, libpython.PythonStepperMixin):
    """Step through Cython, Python or C code."""
    name: str
    stepinto: bool
    def invoke(self, args, from_tty) -> None: ...

class CyNext(CyStep):
    """Step-over Cython, Python or C code."""
    name: str
    stepinto: bool

class CyRun(CythonExecutionControlCommand):
    """
    Run a Cython program. This is like the 'run' command, except that it
    displays Cython or Python source lines as well
    """
    name: str
    invoke: Incomplete

class CyCont(CythonExecutionControlCommand):
    """
    Continue a Cython program. This is like the 'run' command, except that it
    displays Cython or Python source lines as well.
    """
    name: str
    invoke: Incomplete

class CyFinish(CythonExecutionControlCommand):
    """
    Execute until the function returns.
    """
    name: str
    invoke: Incomplete

class CyUp(CythonCommand):
    """
    Go up a Cython, Python or relevant C frame.
    """
    name: str
    def invoke(self, *args) -> None: ...

class CyDown(CyUp):
    """
    Go down a Cython, Python or relevant C frame.
    """
    name: str

class CySelect(CythonCommand):
    """
    Select a frame. Use frame numbers as listed in `cy backtrace`.
    This command is useful because `cy backtrace` prints a reversed backtrace.
    """
    name: str
    def invoke(self, stackno, from_tty) -> None: ...

class CyBacktrace(CythonCommand):
    """Print the Cython stack"""
    name: str
    alias: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, args, from_tty) -> None: ...

class CyList(CythonCommand):
    """
    List Cython source code. To disable to customize colouring see the cy_*
    parameters.
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, _, from_tty) -> None: ...

class CyPrint(CythonCommand):
    """
    Print a Cython variable using 'cy-print x' or 'cy-print module.function.x'
    """
    name: str
    command_class: Incomplete
    def invoke(self, name, from_tty): ...
    def complete(self): ...

sortkey: Incomplete

class CyLocals(CythonCommand):
    """
    List the locals from the current Cython frame.
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, args, from_tty) -> None: ...

class CyGlobals(CyLocals):
    """
    List the globals from the current Cython module.
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, args, from_tty) -> None: ...

class EvaluateOrExecuteCodeMixin:
    """
    Evaluate or execute Python code in a Cython or Python frame. The 'evalcode'
    method evaluations Python code, prints a traceback if an exception went
    uncaught, and returns any return value as a gdb.Value (NULL on exception).
    """
    def evalcode(self, code, input_type):
        """
        Evaluate `code` in a Python or Cython stack frame using the given
        `input_type`.
        """

class CyExec(CythonCommand, libpython.PyExec, EvaluateOrExecuteCodeMixin):
    """
    Execute Python code in the nearest Python or Cython frame.
    """
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, expr, from_tty) -> None: ...

class CySet(CythonCommand):
    '''
    Set a Cython variable to a certain value

        cy set my_cython_c_variable = 10
        cy set my_cython_py_variable = $cy_eval("{\'doner\': \'kebab\'}")

    This is equivalent to

        set $cy_value("my_cython_variable") = 10
    '''
    name: str
    command_class: Incomplete
    completer_class: Incomplete
    def invoke(self, expr, from_tty) -> None: ...

class CyCName(gdb.Function, CythonBase):
    '''
    Get the C name of a Cython variable in the current context.
    Examples:

        print $cy_cname("function")
        print $cy_cname("Class.method")
        print $cy_cname("module.function")
    '''
    def invoke(self, cyname, frame: Incomplete | None = None): ...

class CyCValue(CyCName):
    """
    Get the value of a Cython variable.
    """
    def invoke(self, cyname, frame: Incomplete | None = None): ...

class CyLine(gdb.Function, CythonBase):
    """
    Get the current Cython line.
    """
    def invoke(self): ...

class CyEval(gdb.Function, CythonBase, EvaluateOrExecuteCodeMixin):
    """
    Evaluate Python code in the nearest Python or Cython frame and return
    """
    def invoke(self, python_expression): ...

cython_info: Incomplete
cy: Incomplete

def register_defines() -> None: ...
