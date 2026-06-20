from _typeshed import Incomplete

__all__ = ['Routine', 'DataType', 'default_datatypes', 'get_default_datatype', 'Argument', 'InputArgument', 'OutputArgument', 'Result', 'CodeGen', 'CCodeGen', 'FCodeGen', 'JuliaCodeGen', 'OctaveCodeGen', 'RustCodeGen', 'codegen', 'make_routine']

class Routine:
    """Generic description of evaluation routine for set of expressions.

    A CodeGen class can translate instances of this class into code in a
    particular language.  The routine specification covers all the features
    present in these languages.  The CodeGen part must raise an exception
    when certain features are not present in the target language.  For
    example, multiple return values are possible in Python, but not in C or
    Fortran.  Another example: Fortran and Python support complex numbers,
    while C does not.

    """
    name: Incomplete
    arguments: Incomplete
    results: Incomplete
    local_vars: Incomplete
    global_vars: Incomplete
    def __init__(self, name, arguments, results, local_vars, global_vars) -> None:
        """Initialize a Routine instance.

        Parameters
        ==========

        name : string
            Name of the routine.

        arguments : list of Arguments
            These are things that appear in arguments of a routine, often
            appearing on the right-hand side of a function call.  These are
            commonly InputArguments but in some languages, they can also be
            OutputArguments or InOutArguments (e.g., pass-by-reference in C
            code).

        results : list of Results
            These are the return values of the routine, often appearing on
            the left-hand side of a function call.  The difference between
            Results and OutputArguments and when you should use each is
            language-specific.

        local_vars : list of Results
            These are variables that will be defined at the beginning of the
            function.

        global_vars : list of Symbols
            Variables which will not be passed into the function.

        """
    @property
    def variables(self):
        """Returns a set of all variables possibly used in the routine.

        For routines with unnamed return values, the dummies that may or
        may not be used will be included in the set.

        """
    @property
    def result_variables(self):
        """Returns a list of OutputArgument, InOutArgument and Result.

        If return values are present, they are at the end of the list.
        """

class DataType:
    """Holds strings for a certain datatype in different languages."""
    cname: Incomplete
    fname: Incomplete
    pyname: Incomplete
    jlname: Incomplete
    octname: Incomplete
    rsname: Incomplete
    def __init__(self, cname, fname, pyname, jlname, octname, rsname) -> None: ...

default_datatypes: Incomplete

def get_default_datatype(expr, complex_allowed: Incomplete | None = None):
    """Derives an appropriate datatype based on the expression."""

class Variable:
    """Represents a typed variable."""
    dimensions: Incomplete
    precision: Incomplete
    def __init__(self, name, datatype: Incomplete | None = None, dimensions: Incomplete | None = None, precision: Incomplete | None = None) -> None:
        """Return a new variable.

        Parameters
        ==========

        name : Symbol or MatrixSymbol

        datatype : optional
            When not given, the data type will be guessed based on the
            assumptions on the symbol argument.

        dimension : sequence containing tupes, optional
            If present, the argument is interpreted as an array, where this
            sequence of tuples specifies (lower, upper) bounds for each
            index of the array.

        precision : int, optional
            Controls the precision of floating point constants.

        """
    @property
    def name(self): ...
    def get_datatype(self, language):
        """Returns the datatype string for the requested language.

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy.utilities.codegen import Variable
        >>> x = Variable(Symbol('x'))
        >>> x.get_datatype('c')
        'double'
        >>> x.get_datatype('fortran')
        'REAL*8'

        """

class Argument(Variable):
    """An abstract Argument data structure: a name and a data type.

    This structure is refined in the descendants below.

    """
class InputArgument(Argument): ...

class ResultBase:
    '''Base class for all "outgoing" information from a routine.

    Objects of this class stores a SymPy expression, and a SymPy object
    representing a result variable that will be used in the generated code
    only if necessary.

    '''
    expr: Incomplete
    result_var: Incomplete
    def __init__(self, expr, result_var) -> None: ...

class OutputArgument(Argument, ResultBase):
    """OutputArgument are always initialized in the routine."""
    def __init__(self, name, result_var, expr, datatype: Incomplete | None = None, dimensions: Incomplete | None = None, precision: Incomplete | None = None) -> None:
        '''Return a new variable.

        Parameters
        ==========

        name : Symbol, MatrixSymbol
            The name of this variable.  When used for code generation, this
            might appear, for example, in the prototype of function in the
            argument list.

        result_var : Symbol, Indexed
            Something that can be used to assign a value to this variable.
            Typically the same as `name` but for Indexed this should be e.g.,
            "y[i]" whereas `name` should be the Symbol "y".

        expr : object
            The expression that should be output, typically a SymPy
            expression.

        datatype : optional
            When not given, the data type will be guessed based on the
            assumptions on the symbol argument.

        dimension : sequence containing tupes, optional
            If present, the argument is interpreted as an array, where this
            sequence of tuples specifies (lower, upper) bounds for each
            index of the array.

        precision : int, optional
            Controls the precision of floating point constants.

        '''

class InOutArgument(Argument, ResultBase):
    """InOutArgument are never initialized in the routine."""
    def __init__(self, name, result_var, expr, datatype: Incomplete | None = None, dimensions: Incomplete | None = None, precision: Incomplete | None = None) -> None: ...

class Result(Variable, ResultBase):
    '''An expression for a return value.

    The name result is used to avoid conflicts with the reserved word
    "return" in the Python language.  It is also shorter than ReturnValue.

    These may or may not need a name in the destination (e.g., "return(x*y)"
    might return a value without ever naming it).

    '''
    def __init__(self, expr, name: Incomplete | None = None, result_var: Incomplete | None = None, datatype: Incomplete | None = None, dimensions: Incomplete | None = None, precision: Incomplete | None = None) -> None:
        '''Initialize a return value.

        Parameters
        ==========

        expr : SymPy expression

        name : Symbol, MatrixSymbol, optional
            The name of this return variable.  When used for code generation,
            this might appear, for example, in the prototype of function in a
            list of return values.  A dummy name is generated if omitted.

        result_var : Symbol, Indexed, optional
            Something that can be used to assign a value to this variable.
            Typically the same as `name` but for Indexed this should be e.g.,
            "y[i]" whereas `name` should be the Symbol "y".  Defaults to
            `name` if omitted.

        datatype : optional
            When not given, the data type will be guessed based on the
            assumptions on the expr argument.

        dimension : sequence containing tupes, optional
            If present, this variable is interpreted as an array,
            where this sequence of tuples specifies (lower, upper)
            bounds for each index of the array.

        precision : int, optional
            Controls the precision of floating point constants.

        '''

class CodeGen:
    """Abstract class for the code generators."""
    printer: Incomplete
    project: Incomplete
    cse: Incomplete
    def __init__(self, project: str = 'project', cse: bool = False) -> None:
        """Initialize a code generator.

        Derived classes will offer more options that affect the generated
        code.

        """
    def routine(self, name, expr, argument_sequence: Incomplete | None = None, global_vars: Incomplete | None = None):
        """Creates an Routine object that is appropriate for this language.

        This implementation is appropriate for at least C/Fortran.  Subclasses
        can override this if necessary.

        Here, we assume at most one return value (the l-value) which must be
        scalar.  Additional outputs are OutputArguments (e.g., pointers on
        right-hand-side or pass-by-reference).  Matrices are always returned
        via OutputArguments.  If ``argument_sequence`` is None, arguments will
        be ordered alphabetically, but with all InputArguments first, and then
        OutputArgument and InOutArguments.

        """
    def write(self, routines, prefix, to_files: bool = False, header: bool = True, empty: bool = True):
        """Writes all the source code files for the given routines.

        The generated source is returned as a list of (filename, contents)
        tuples, or is written to files (see below).  Each filename consists
        of the given prefix, appended with an appropriate extension.

        Parameters
        ==========

        routines : list
            A list of Routine instances to be written

        prefix : string
            The prefix for the output files

        to_files : bool, optional
            When True, the output is written to files.  Otherwise, a list
            of (filename, contents) tuples is returned.  [default: False]

        header : bool, optional
            When True, a header comment is included on top of each source
            file. [default: True]

        empty : bool, optional
            When True, empty lines are included to structure the source
            files. [default: True]

        """
    def dump_code(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None:
        """Write the code by calling language specific methods.

        The generated file contains all the definitions of the routines in
        low-level code and refers to the header file if appropriate.

        Parameters
        ==========

        routines : list
            A list of Routine instances.

        f : file-like
            Where to write the file.

        prefix : string
            The filename prefix, used to refer to the proper header file.
            Only the basename of the prefix is used.

        header : bool, optional
            When True, a header comment is included on top of each source
            file.  [default : True]

        empty : bool, optional
            When True, empty lines are included to structure the source
            files.  [default : True]

        """

class CodeGenError(Exception): ...

class CodeGenArgumentListError(Exception):
    @property
    def missing_args(self): ...

class CCodeGen(CodeGen):
    """Generator for C code.

    The .write() method inherited from CodeGen will output a code file and
    an interface file, <prefix>.c and <prefix>.h respectively.

    """
    code_extension: str
    interface_extension: str
    standard: str
    printer: Incomplete
    preprocessor_statements: Incomplete
    def __init__(self, project: str = 'project', printer: Incomplete | None = None, preprocessor_statements: Incomplete | None = None, cse: bool = False) -> None: ...
    def get_prototype(self, routine):
        """Returns a string for the function prototype of the routine.

        If the routine has multiple result objects, an CodeGenError is
        raised.

        See: https://en.wikipedia.org/wiki/Function_prototype

        """
    def dump_c(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None: ...
    def dump_h(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None:
        """Writes the C header file.

        This file contains all the function declarations.

        Parameters
        ==========

        routines : list
            A list of Routine instances.

        f : file-like
            Where to write the file.

        prefix : string
            The filename prefix, used to construct the include guards.
            Only the basename of the prefix is used.

        header : bool, optional
            When True, a header comment is included on top of each source
            file.  [default : True]

        empty : bool, optional
            When True, empty lines are included to structure the source
            files.  [default : True]

        """
    dump_fns: Incomplete

class C89CodeGen(CCodeGen):
    standard: str

class C99CodeGen(CCodeGen):
    standard: str

class FCodeGen(CodeGen):
    """Generator for Fortran 95 code

    The .write() method inherited from CodeGen will output a code file and
    an interface file, <prefix>.f90 and <prefix>.h respectively.

    """
    code_extension: str
    interface_extension: str
    printer: Incomplete
    def __init__(self, project: str = 'project', printer: Incomplete | None = None) -> None: ...
    def get_interface(self, routine):
        """Returns a string for the function interface.

        The routine should have a single result object, which can be None.
        If the routine has multiple result objects, a CodeGenError is
        raised.

        See: https://en.wikipedia.org/wiki/Function_prototype

        """
    def dump_f95(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None: ...
    def dump_h(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None:
        """Writes the interface to a header file.

        This file contains all the function declarations.

        Parameters
        ==========

        routines : list
            A list of Routine instances.

        f : file-like
            Where to write the file.

        prefix : string
            The filename prefix.

        header : bool, optional
            When True, a header comment is included on top of each source
            file.  [default : True]

        empty : bool, optional
            When True, empty lines are included to structure the source
            files.  [default : True]

        """
    dump_fns: Incomplete

class JuliaCodeGen(CodeGen):
    """Generator for Julia code.

    The .write() method inherited from CodeGen will output a code file
    <prefix>.jl.

    """
    code_extension: str
    printer: Incomplete
    def __init__(self, project: str = 'project', printer: Incomplete | None = None) -> None: ...
    def routine(self, name, expr, argument_sequence, global_vars):
        """Specialized Routine creation for Julia."""
    def dump_jl(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None: ...
    dump_fns: Incomplete

class OctaveCodeGen(CodeGen):
    """Generator for Octave code.

    The .write() method inherited from CodeGen will output a code file
    <prefix>.m.

    Octave .m files usually contain one function.  That function name should
    match the filename (``prefix``).  If you pass multiple ``name_expr`` pairs,
    the latter ones are presumed to be private functions accessed by the
    primary function.

    You should only pass inputs to ``argument_sequence``: outputs are ordered
    according to their order in ``name_expr``.

    """
    code_extension: str
    printer: Incomplete
    def __init__(self, project: str = 'project', printer: Incomplete | None = None) -> None: ...
    def routine(self, name, expr, argument_sequence, global_vars):
        """Specialized Routine creation for Octave."""
    def dump_m(self, routines, f, prefix, header: bool = True, empty: bool = True, inline: bool = True) -> None: ...
    dump_fns: Incomplete

class RustCodeGen(CodeGen):
    """Generator for Rust code.

    The .write() method inherited from CodeGen will output a code file
    <prefix>.rs

    """
    code_extension: str
    printer: Incomplete
    def __init__(self, project: str = 'project', printer: Incomplete | None = None) -> None: ...
    def routine(self, name, expr, argument_sequence, global_vars):
        """Specialized Routine creation for Rust."""
    def get_prototype(self, routine):
        """Returns a string for the function prototype of the routine.

        If the routine has multiple result objects, an CodeGenError is
        raised.

        See: https://en.wikipedia.org/wiki/Function_prototype

        """
    def dump_rs(self, routines, f, prefix, header: bool = True, empty: bool = True) -> None: ...
    dump_fns: Incomplete

def codegen(name_expr, language: Incomplete | None = None, prefix: Incomplete | None = None, project: str = 'project', to_files: bool = False, header: bool = True, empty: bool = True, argument_sequence: Incomplete | None = None, global_vars: Incomplete | None = None, standard: Incomplete | None = None, code_gen: Incomplete | None = None, printer: Incomplete | None = None):
    '''Generate source code for expressions in a given language.

    Parameters
    ==========

    name_expr : tuple, or list of tuples
        A single (name, expression) tuple or a list of (name, expression)
        tuples.  Each tuple corresponds to a routine.  If the expression is
        an equality (an instance of class Equality) the left hand side is
        considered an output argument.  If expression is an iterable, then
        the routine will have multiple outputs.

    language : string,
        A string that indicates the source code language.  This is case
        insensitive.  Currently, \'C\', \'F95\' and \'Octave\' are supported.
        \'Octave\' generates code compatible with both Octave and Matlab.

    prefix : string, optional
        A prefix for the names of the files that contain the source code.
        Language-dependent suffixes will be appended.  If omitted, the name
        of the first name_expr tuple is used.

    project : string, optional
        A project name, used for making unique preprocessor instructions.
        [default: "project"]

    to_files : bool, optional
        When True, the code will be written to one or more files with the
        given prefix, otherwise strings with the names and contents of
        these files are returned. [default: False]

    header : bool, optional
        When True, a header is written on top of each source file.
        [default: True]

    empty : bool, optional
        When True, empty lines are used to structure the code.
        [default: True]

    argument_sequence : iterable, optional
        Sequence of arguments for the routine in a preferred order.  A
        CodeGenError is raised if required arguments are missing.
        Redundant arguments are used without warning.  If omitted,
        arguments will be ordered alphabetically, but with all input
        arguments first, and then output or in-out arguments.

    global_vars : iterable, optional
        Sequence of global variables used by the routine.  Variables
        listed here will not show up as function arguments.

    standard : string

    code_gen : CodeGen instance
        An instance of a CodeGen subclass. Overrides ``language``.

    Examples
    ========

    >>> from sympy.utilities.codegen import codegen
    >>> from sympy.abc import x, y, z
    >>> [(c_name, c_code), (h_name, c_header)] = codegen(
    ...     ("f", x+y*z), "C89", "test", header=False, empty=False)
    >>> print(c_name)
    test.c
    >>> print(c_code)
    #include "test.h"
    #include <math.h>
    double f(double x, double y, double z) {
       double f_result;
       f_result = x + y*z;
       return f_result;
    }
    <BLANKLINE>
    >>> print(h_name)
    test.h
    >>> print(c_header)
    #ifndef PROJECT__TEST__H
    #define PROJECT__TEST__H
    double f(double x, double y, double z);
    #endif
    <BLANKLINE>

    Another example using Equality objects to give named outputs.  Here the
    filename (prefix) is taken from the first (name, expr) pair.

    >>> from sympy.abc import f, g
    >>> from sympy import Eq
    >>> [(c_name, c_code), (h_name, c_header)] = codegen(
    ...      [("myfcn", x + y), ("fcn2", [Eq(f, 2*x), Eq(g, y)])],
    ...      "C99", header=False, empty=False)
    >>> print(c_name)
    myfcn.c
    >>> print(c_code)
    #include "myfcn.h"
    #include <math.h>
    double myfcn(double x, double y) {
       double myfcn_result;
       myfcn_result = x + y;
       return myfcn_result;
    }
    void fcn2(double x, double y, double *f, double *g) {
       (*f) = 2*x;
       (*g) = y;
    }
    <BLANKLINE>

    If the generated function(s) will be part of a larger project where various
    global variables have been defined, the \'global_vars\' option can be used
    to remove the specified variables from the function signature

    >>> from sympy.utilities.codegen import codegen
    >>> from sympy.abc import x, y, z
    >>> [(f_name, f_code), header] = codegen(
    ...     ("f", x+y*z), "F95", header=False, empty=False,
    ...     argument_sequence=(x, y), global_vars=(z,))
    >>> print(f_code)
    REAL*8 function f(x, y)
    implicit none
    REAL*8, intent(in) :: x
    REAL*8, intent(in) :: y
    f = x + y*z
    end function
    <BLANKLINE>

    '''
def make_routine(name, expr, argument_sequence: Incomplete | None = None, global_vars: Incomplete | None = None, language: str = 'F95'):
    '''A factory that makes an appropriate Routine from an expression.

    Parameters
    ==========

    name : string
        The name of this routine in the generated code.

    expr : expression or list/tuple of expressions
        A SymPy expression that the Routine instance will represent.  If
        given a list or tuple of expressions, the routine will be
        considered to have multiple return values and/or output arguments.

    argument_sequence : list or tuple, optional
        List arguments for the routine in a preferred order.  If omitted,
        the results are language dependent, for example, alphabetical order
        or in the same order as the given expressions.

    global_vars : iterable, optional
        Sequence of global variables used by the routine.  Variables
        listed here will not show up as function arguments.

    language : string, optional
        Specify a target language.  The Routine itself should be
        language-agnostic but the precise way one is created, error
        checking, etc depend on the language.  [default: "F95"].

    Notes
    =====

    A decision about whether to use output arguments or return values is made
    depending on both the language and the particular mathematical expressions.
    For an expression of type Equality, the left hand side is typically made
    into an OutputArgument (or perhaps an InOutArgument if appropriate).
    Otherwise, typically, the calculated expression is made a return values of
    the routine.

    Examples
    ========

    >>> from sympy.utilities.codegen import make_routine
    >>> from sympy.abc import x, y, f, g
    >>> from sympy import Eq
    >>> r = make_routine(\'test\', [Eq(f, 2*x), Eq(g, x + y)])
    >>> [arg.result_var for arg in r.results]
    []
    >>> [arg.name for arg in r.arguments]
    [x, y, f, g]
    >>> [arg.name for arg in r.result_variables]
    [f, g]
    >>> r.local_vars
    set()

    Another more complicated example with a mixture of specified and
    automatically-assigned names.  Also has Matrix output.

    >>> from sympy import Matrix
    >>> r = make_routine(\'fcn\', [x*y, Eq(f, 1), Eq(g, x + g), Matrix([[x, 2]])])
    >>> [arg.result_var for arg in r.results]  # doctest: +SKIP
    [result_5397460570204848505]
    >>> [arg.expr for arg in r.results]
    [x*y]
    >>> [arg.name for arg in r.arguments]  # doctest: +SKIP
    [x, y, f, g, out_8598435338387848786]

    We can examine the various arguments more closely:

    >>> from sympy.utilities.codegen import (InputArgument, OutputArgument,
    ...                                      InOutArgument)
    >>> [a.name for a in r.arguments if isinstance(a, InputArgument)]
    [x, y]

    >>> [a.name for a in r.arguments if isinstance(a, OutputArgument)]  # doctest: +SKIP
    [f, out_8598435338387848786]
    >>> [a.expr for a in r.arguments if isinstance(a, OutputArgument)]
    [1, Matrix([[x, 2]])]

    >>> [a.name for a in r.arguments if isinstance(a, InOutArgument)]
    [g]
    >>> [a.expr for a in r.arguments if isinstance(a, InOutArgument)]
    [g + x]

    '''
