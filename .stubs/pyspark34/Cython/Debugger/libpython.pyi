import gdb
import os
from _typeshed import Incomplete
from collections.abc import Generator

unichr = chr
xrange = range
long = int
Py_TPFLAGS_HEAPTYPE: Incomplete
Py_TPFLAGS_LONG_SUBCLASS: Incomplete
Py_TPFLAGS_LIST_SUBCLASS: Incomplete
Py_TPFLAGS_TUPLE_SUBCLASS: Incomplete
Py_TPFLAGS_BYTES_SUBCLASS: Incomplete
Py_TPFLAGS_UNICODE_SUBCLASS: Incomplete
Py_TPFLAGS_DICT_SUBCLASS: Incomplete
Py_TPFLAGS_BASE_EXC_SUBCLASS: Incomplete
Py_TPFLAGS_TYPE_SUBCLASS: Incomplete
MAX_OUTPUT_LEN: int
hexdigits: str
ENCODING: Incomplete
FRAME_INFO_OPTIMIZED_OUT: str
UNABLE_READ_INFO_PYTHON_FRAME: str
EVALFRAME: str

class NullPyObjectPtr(RuntimeError): ...

def safety_limit(val): ...
def safe_range(val): ...
def write_unicode(file, text) -> None: ...
os_fsencode = os.fsencode

class StringTruncated(RuntimeError): ...

class TruncatedStringIO:
    """Similar to io.StringIO, but can truncate the output by raising a
    StringTruncated exception"""
    maxlen: Incomplete
    def __init__(self, maxlen: Incomplete | None = None) -> None: ...
    def write(self, data) -> None: ...
    def getvalue(self): ...

class PyObjectPtr:
    """
    Class wrapping a gdb.Value that's either a (PyObject*) within the
    inferior process, or some subclass pointer e.g. (PyBytesObject*)

    There will be a subclass for every refined PyObject type that we care
    about.

    Note that at every stage the underlying pointer could be NULL, point
    to corrupt data, etc; this is the debugger, after all.
    """
    def __init__(self, gdbval, cast_to: Incomplete | None = None) -> None: ...
    def field(self, name):
        '''
        Get the gdb.Value for the given field within the PyObject, coping with
        some python 2 versus python 3 differences.

        Various libpython types are defined using the "PyObject_HEAD" and
        "PyObject_VAR_HEAD" macros.

        In Python 2, this these are defined so that "ob_type" and (for a var
        object) "ob_size" are fields of the type in question.

        In Python 3, this is defined as an embedded PyVarObject type thus:
           PyVarObject ob_base;
        so that the "ob_size" field is located insize the "ob_base" field, and
        the "ob_type" is most easily accessed by casting back to a (PyObject*).
        '''
    def pyop_field(self, name):
        """
        Get a PyObjectPtr for the given PyObject* field within this PyObject,
        coping with some python 2 versus python 3 differences.
        """
    def write_field_repr(self, name, out, visited) -> None:
        '''
        Extract the PyObject* field named "name", and write its representation
        to file-like object "out"
        '''
    def get_truncated_repr(self, maxlen):
        '''
        Get a repr-like string for the data, but truncate it at "maxlen" bytes
        (ending the object graph traversal as soon as you do)
        '''
    def type(self): ...
    def is_null(self): ...
    def is_optimized_out(self):
        '''
        Is the value of the underlying PyObject* visible to the debugger?

        This can vary with the precise version of the compiler used to build
        Python, and the precise version of gdb.

        See e.g. https://bugzilla.redhat.com/show_bug.cgi?id=556975 with
        PyEval_EvalFrameEx\'s "f"
        '''
    def safe_tp_name(self): ...
    tp_name: Incomplete
    address: Incomplete
    def proxyval(self, visited):
        """
        Scrape a value from the inferior process, and try to represent it
        within the gdb process, whilst (hopefully) avoiding crashes when
        the remote data is corrupt.

        Derived classes will override this.

        For example, a PyIntObject* with ob_ival 42 in the inferior process
        should result in an int(42) in this process.

        visited: a set of all gdb.Value pyobject pointers already visited
        whilst generating this value (to guard against infinite recursion when
        visiting object graphs with loops).  Analogous to Py_ReprEnter and
        Py_ReprLeave
        """
    def write_repr(self, out, visited):
        '''
        Write a string representation of the value scraped from the inferior
        process to "out", a file-like object.
        '''
    @classmethod
    def subclass_from_type(cls, t):
        '''
        Given a PyTypeObjectPtr instance wrapping a gdb.Value that\'s a
        (PyTypeObject*), determine the corresponding subclass of PyObjectPtr
        to use

        Ideally, we would look up the symbols for the global types, but that
        isn\'t working yet:
          (gdb) python print gdb.lookup_symbol(\'PyList_Type\')[0].value
          Traceback (most recent call last):
            File "<string>", line 1, in <module>
          NotImplementedError: Symbol type not yet supported in Python scripts.
          Error while executing Python code.

        For now, we use tp_flags, after doing some string comparisons on the
        tp_name for some special-cases that don\'t seem to be visible through
        flags
        '''
    @classmethod
    def from_pyobject_ptr(cls, gdbval):
        """
        Try to locate the appropriate derived class dynamically, and cast
        the pointer accordingly.
        """
    @classmethod
    def get_gdb_type(cls): ...
    def as_address(self): ...

class PyVarObjectPtr(PyObjectPtr): ...

class ProxyAlreadyVisited:
    """
    Placeholder proxy to use when protecting against infinite recursion due to
    loops in the object graph.

    Analogous to the values emitted by the users of Py_ReprEnter and Py_ReprLeave
    """
    def __init__(self, rep) -> None: ...

class InstanceProxy:
    cl_name: Incomplete
    attrdict: Incomplete
    address: Incomplete
    def __init__(self, cl_name, attrdict, address) -> None: ...

class HeapTypeObjectPtr(PyObjectPtr):
    def get_attr_dict(self):
        """
        Get the PyDictObject ptr representing the attribute dictionary
        (or None if there's a problem)
        """
    def proxyval(self, visited):
        """
        Support for classes.

        Currently we just locate the dictionary using a transliteration to
        python of _PyObject_GetDictPtr, ignoring descriptors
        """
    def write_repr(self, out, visited) -> None: ...

class ProxyException(Exception):
    tp_name: Incomplete
    args: Incomplete
    def __init__(self, tp_name, args) -> None: ...

class PyBaseExceptionObjectPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyBaseExceptionObject* i.e. an exception
    within the process being debugged.
    """
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyClassObjectPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyClassObject* i.e. a <classobj>
    instance within the process being debugged.
    """

class BuiltInFunctionProxy:
    ml_name: Incomplete
    def __init__(self, ml_name) -> None: ...

class BuiltInMethodProxy:
    ml_name: Incomplete
    pyop_m_self: Incomplete
    def __init__(self, ml_name, pyop_m_self) -> None: ...

class PyCFunctionObjectPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyCFunctionObject*
    (see Include/methodobject.h and Objects/methodobject.c)
    """
    def proxyval(self, visited): ...

class PyCodeObjectPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyCodeObject* i.e. a <code> instance
    within the process being debugged.
    """
    def addr2line(self, addrq):
        """
        Get the line number for a given bytecode offset

        Analogous to PyCode_Addr2Line; translated from pseudocode in
        Objects/lnotab_notes.txt
        """

class PyDictObjectPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyDictObject* i.e. a dict instance
    within the process being debugged.
    """
    def iteritems(self) -> Generator[Incomplete, None, None]:
        """
        Yields a sequence of (PyObjectPtr key, PyObjectPtr value) pairs,
        analogous to dict.iteritems()
        """
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyListObjectPtr(PyObjectPtr):
    def __getitem__(self, i): ...
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyLongObjectPtr(PyObjectPtr):
    def proxyval(self, visited):
        """
        Python's Include/longobjrep.h has this declaration:
           struct _longobject {
               PyObject_VAR_HEAD
               digit ob_digit[1];
           };

        with this description:
            The absolute value of a number is equal to
                 SUM(for i=0 through abs(ob_size)-1) ob_digit[i] * 2**(SHIFT*i)
            Negative numbers are represented with ob_size < 0;
            zero is represented by ob_size == 0.

        where SHIFT can be either:
            #define PyLong_SHIFT        30
            #define PyLong_SHIFT        15
        """
    def write_repr(self, out, visited) -> None: ...

class PyBoolObjectPtr(PyLongObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyBoolObject* i.e. one of the two
    <bool> instances (Py_True/Py_False) within the process being debugged.
    """
    def proxyval(self, visited): ...

class PyNoneStructPtr(PyObjectPtr):
    """
    Class wrapping a gdb.Value that's a PyObject* pointing to the
    singleton (we hope) _Py_NoneStruct with ob_type PyNone_Type
    """
    def proxyval(self, visited) -> None: ...

class PyFrameObjectPtr(PyObjectPtr):
    co: Incomplete
    co_name: Incomplete
    co_filename: Incomplete
    f_lineno: Incomplete
    f_lasti: Incomplete
    co_nlocals: Incomplete
    co_varnames: Incomplete
    def __init__(self, gdbval, cast_to: Incomplete | None = None) -> None: ...
    def iter_locals(self) -> Generator[Incomplete, None, None]:
        """
        Yield a sequence of (name,value) pairs of PyObjectPtr instances, for
        the local variables of this frame
        """
    def iter_globals(self):
        """
        Yield a sequence of (name,value) pairs of PyObjectPtr instances, for
        the global variables of this frame
        """
    def iter_builtins(self):
        """
        Yield a sequence of (name,value) pairs of PyObjectPtr instances, for
        the builtin variables
        """
    def get_var_by_name(self, name):
        """
        Look for the named local variable, returning a (PyObjectPtr, scope) pair
        where scope is a string 'local', 'global', 'builtin'

        If not found, return (None, None)
        """
    def filename(self):
        """Get the path of the current Python source file, as a string"""
    def current_line_num(self):
        """Get current line number as an integer (1-based)

        Translated from PyFrame_GetLineNumber and PyCode_Addr2Line

        See Objects/lnotab_notes.txt
        """
    def current_line(self):
        """Get the text of the current source line as a string, with a trailing
        newline character"""
    def write_repr(self, out, visited) -> None: ...
    def print_traceback(self) -> None: ...

class PySetObjectPtr(PyObjectPtr):
    def __iter__(self): ...
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyBytesObjectPtr(PyObjectPtr):
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyTupleObjectPtr(PyObjectPtr):
    def __getitem__(self, i): ...
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class PyTypeObjectPtr(PyObjectPtr): ...

class PyUnicodeObjectPtr(PyObjectPtr):
    def char_width(self): ...
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

class wrapperobject(PyObjectPtr):
    def safe_name(self): ...
    def safe_tp_name(self): ...
    def safe_self_addresss(self): ...
    def proxyval(self, visited): ...
    def write_repr(self, out, visited) -> None: ...

def int_from_int(gdbval): ...
def stringify(val): ...

class PyObjectPtrPrinter:
    """Prints a (PyObject*)"""
    gdbval: Incomplete
    def __init__(self, gdbval) -> None: ...
    def to_string(self): ...

def pretty_printer_lookup(gdbval): ...
def register(obj) -> None: ...

class Frame:
    """
    Wrapper for gdb.Frame, adding various methods
    """
    def __init__(self, gdbframe) -> None: ...
    def older(self): ...
    def newer(self): ...
    def select(self):
        """If supported, select this frame and return True; return False if unsupported

        Not all builds have a gdb.Frame.select method; seems to be present on Fedora 12
        onwards, but absent on Ubuntu buildbot"""
    def get_index(self):
        """Calculate index of frame, starting at 0 for the newest frame within
        this thread"""
    def is_python_frame(self):
        '''Is this a _PyEval_EvalFrameDefault frame, or some other important
        frame? (see is_other_python_frame for what "important" means in this
        context)'''
    def is_evalframe(self):
        """Is this a _PyEval_EvalFrameDefault frame?"""
    def is_other_python_frame(self):
        """Is this frame worth displaying in python backtraces?
        Examples:
          - waiting on the GIL
          - garbage-collecting
          - within a CFunction
         If it is, return a descriptive string
         For other frames, return False
         """
    def is_waiting_for_gil(self):
        """Is this frame waiting on the GIL?"""
    def is_gc_collect(self):
        '''Is this frame "collect" within the garbage-collector?'''
    def get_pyop(self): ...
    @classmethod
    def get_selected_frame(cls): ...
    @classmethod
    def get_selected_python_frame(cls):
        """Try to obtain the Frame for the python-related code in the selected
        frame, or None"""
    @classmethod
    def get_selected_bytecode_frame(cls):
        """Try to obtain the Frame for the python bytecode interpreter in the
        selected GDB frame, or None"""
    def print_summary(self) -> None: ...
    def print_traceback(self) -> None: ...

class PyList(gdb.Command):
    """List the current Python source code, if any

    Use
       py-list START
    to list at a different line number within the python source.

    Use
       py-list START, END
    to list a specific range of lines within the python source.
    """
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

def move_in_stack(move_up) -> None:
    """Move up or down the stack (for the py-up/py-down command)"""

class PyUp(gdb.Command):
    """Select and print the python stack frame that called this one (if any)"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

class PyDown(gdb.Command):
    """Select and print the python stack frame called by this one (if any)"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

class PyBacktraceFull(gdb.Command):
    """Display the current python frame and all the frames within its call stack (if any)"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

class PyBacktrace(gdb.Command):
    """Display the current python frame and all the frames within its call stack (if any)"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

class PyPrint(gdb.Command):
    """Look up the given python variable name, and print it"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

class PyLocals(gdb.Command):
    """Look up the given python variable name, and print it"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...

def dont_suppress_errors(function):
    """*sigh*, readline"""

class PyGlobals(gdb.Command):
    """List all the globals in the currently select Python frame"""
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty) -> None: ...
    def get_namespace(self, pyop_frame): ...

def is_evalframeex(frame):
    """Is this a PyEval_EvalFrameEx frame?"""

class PyNameEquals(gdb.Function):
    def invoke(self, funcname): ...

class PyModEquals(PyNameEquals):
    def invoke(self, modname): ...

class PyBreak(gdb.Command):
    """
    Set a Python breakpoint. Examples:

    Break on any function or method named 'func' in module 'modname'

        py-break modname.func

    Break on any function or method named 'func'

        py-break func
    """
    def invoke(self, funcname, from_tty) -> None: ...

class _LoggingState:
    """
    State that helps to provide a reentrant gdb.execute() function.
    """
    file: Incomplete
    filename: Incomplete
    fd: Incomplete
    file_position_stack: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def getoutput(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, tb: types.TracebackType | None) -> None: ...

def execute(command, from_tty: bool = False, to_string: bool = False):
    """
    Replace gdb.execute() with this function and have it accept a 'to_string'
    argument (new in 7.2). Have it properly capture stderr also. Ensure
    reentrancy.
    """
def get_selected_inferior():
    """
    Return the selected inferior in gdb.
    """
def source_gdb_script(script_contents, to_string: bool = False) -> None:
    """
    Source a gdb script with script_contents passed as a string. This is useful
    to provide defines for py-step and py-next to make them repeatable (this is
    not possible with gdb.execute()). See
    http://sourceware.org/bugzilla/show_bug.cgi?id=12216
    """
def register_defines() -> None: ...
def stackdepth(frame):
    """Tells the stackdepth of a gdb frame."""

class ExecutionControlCommandBase(gdb.Command):
    """
    Superclass for language specific execution control. Language specific
    features should be implemented by lang_info using the LanguageInfo
    interface. 'name' is the name of the command.
    """
    lang_info: Incomplete
    def __init__(self, name, lang_info) -> None: ...
    def install_breakpoints(self) -> Generator[Incomplete, None, None]: ...
    def delete_breakpoints(self, breakpoint_list) -> None: ...
    def filter_output(self, result): ...
    def stopped(self): ...
    def finish_executing(self, result) -> None:
        """
        After doing some kind of code running in the inferior, print the line
        of source code or the result of the last executed gdb command (passed
        in as the `result` argument).
        """
    def finish(self, *args) -> None:
        """Implements the finish command."""
    def step(self, stepinto, stepover_command: str = 'next') -> None:
        '''
        Do a single step or step-over. Returns the result of the last gdb
        command that made execution stop.

        This implementation, for stepping, sets (conditional) breakpoints for
        all functions that are deemed relevant. It then does a step over until
        either something halts execution, or until the next line is reached.

        If, however, stepover_command is given, it should be a string gdb
        command that continues execution in some way. The idea is that the
        caller has set a (conditional) breakpoint or watchpoint that can work
        more efficiently than the step-over loop. For Python this means setting
        a watchpoint for f->f_lasti, which means we can then subsequently
        "finish" frames.
        We want f->f_lasti instead of f->f_lineno, because the latter only
        works properly with local trace functions, see
        PyFrameObjectPtr.current_line_num and PyFrameObjectPtr.addr2line.
        '''
    def run(self, args, from_tty) -> None: ...
    def cont(self, *args) -> None: ...

class LanguageInfo:
    """
    This class defines the interface that ExecutionControlCommandBase needs to
    provide language-specific execution control.

    Classes that implement this interface should implement:

        lineno(frame)
            Tells the current line number (only called for a relevant frame).
            If lineno is a false value it is not checked for a difference.

        is_relevant_function(frame)
            tells whether we care about frame 'frame'

        get_source_line(frame)
            get the line of source code for the current line (only called for a
            relevant frame). If the source code cannot be retrieved this
            function should return None

        exc_info(frame) -- optional
            tells whether an exception was raised, if so, it should return a
            string representation of the exception value, None otherwise.

        static_break_functions()
            returns an iterable of function names that are considered relevant
            and should halt step-into execution. This is needed to provide a
            performing step-into

        runtime_break_functions() -- optional
            list of functions that we should break into depending on the
            context
    """
    def exc_info(self, frame) -> None:
        """See this class' docstring."""
    def runtime_break_functions(self):
        """
        Implement this if the list of step-into functions depends on the
        context.
        """

class PythonInfo(LanguageInfo):
    def pyframe(self, frame): ...
    def lineno(self, frame): ...
    def is_relevant_function(self, frame): ...
    def get_source_line(self, frame): ...
    def exc_info(self, frame): ...
    def static_break_functions(self) -> Generator[Incomplete, None, None]: ...

class PythonStepperMixin:
    """
    Make this a mixin so CyStep can also inherit from this and use a
    CythonCodeStepper at the same time.
    """
    def python_step(self, stepinto) -> None:
        """
        Set a watchpoint on the Python bytecode instruction pointer and try
        to finish the frame
        """

class PyStep(ExecutionControlCommandBase, PythonStepperMixin):
    """Step through Python code."""
    stepinto: bool
    def invoke(self, args, from_tty) -> None: ...

class PyNext(PyStep):
    """Step-over Python code."""
    stepinto: bool

class PyFinish(ExecutionControlCommandBase):
    """Execute until function returns to a caller."""
    invoke: Incomplete

class PyRun(ExecutionControlCommandBase):
    """Run the program."""
    invoke: Incomplete

class PyCont(ExecutionControlCommandBase):
    invoke: Incomplete

def pointervalue(gdbval): ...
def get_inferior_unicode_postfix(): ...

class PythonCodeExecutor:
    Py_single_input: int
    Py_file_input: int
    Py_eval_input: int
    def malloc(self, size): ...
    def alloc_string(self, string): ...
    def alloc_pystring(self, string): ...
    def free(self, pointer) -> None: ...
    def incref(self, pointer) -> None:
        """Increment the reference count of a Python object in the inferior."""
    def xdecref(self, pointer) -> None:
        """Decrement the reference count of a Python object in the inferior."""
    def evalcode(self, code, input_type, global_dict: Incomplete | None = None, local_dict: Incomplete | None = None):
        """
        Evaluate python code `code` given as a string in the inferior and
        return the result as a gdb.Value. Returns a new reference in the
        inferior.

        Of course, executing any code in the inferior may be dangerous and may
        leave the debuggee in an unsafe state or terminate it altogether.
        """

class FetchAndRestoreError(PythonCodeExecutor):
    """
    Context manager that fetches the error indicator in the inferior and
    restores it on exit.
    """
    sizeof_PyObjectPtr: Incomplete
    pointer: Incomplete
    errstate: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class FixGdbCommand(gdb.Command):
    actual_command: Incomplete
    def __init__(self, command, actual_command) -> None: ...
    def fix_gdb(self) -> None:
        """
        It seems that invoking either 'cy exec' and 'py-exec' work perfectly
        fine, but after this gdb's python API is entirely broken.
        Maybe some uncleared exception value is still set?
        sys.exc_clear() didn't help. A demonstration:

        (gdb) cy exec 'hello'
        'hello'
        (gdb) python gdb.execute('cont')
        RuntimeError: Cannot convert value to int.
        Error while executing Python code.
        (gdb) python gdb.execute('cont')
        [15148 refs]

        Program exited normally.
        """
    def invoke(self, args, from_tty) -> None: ...

class PyExec(gdb.Command):
    def readcode(self, expr): ...
    def invoke(self, expr, from_tty) -> None: ...

py_step: Incomplete
py_next: Incomplete
py_finish: Incomplete
py_run: Incomplete
py_cont: Incomplete
py_exec: Incomplete
