from _typeshed import Incomplete
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import Lambda as Lambda
from sympy.core.relational import Eq as Eq
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.tensor.indexed import Idx as Idx, IndexedBase as IndexedBase
from sympy.utilities.codegen import C99CodeGen as C99CodeGen, CodeGenArgumentListError as CodeGenArgumentListError, InOutArgument as InOutArgument, InputArgument as InputArgument, OutputArgument as OutputArgument, Result as Result, ResultBase as ResultBase, get_code_generator as get_code_generator, make_routine as make_routine
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.iterables import iterable as iterable
from sympy.utilities.lambdify import implemented_function as implemented_function

class CodeWrapError(Exception): ...

class CodeWrapper:
    """Base Class for code wrappers"""
    @property
    def filename(self): ...
    @property
    def module_name(self): ...
    generator: Incomplete
    filepath: Incomplete
    flags: Incomplete
    quiet: Incomplete
    def __init__(self, generator, filepath: Incomplete | None = None, flags=[], verbose: bool = False) -> None:
        """
        generator -- the code generator to use
        """
    @property
    def include_header(self): ...
    @property
    def include_empty(self): ...
    def wrap_code(self, routine, helpers: Incomplete | None = None): ...

class DummyWrapper(CodeWrapper):
    """Class used for testing independent of backends """
    template: str

class CythonCodeWrapper(CodeWrapper):
    """Wrapper that uses Cython"""
    setup_template: str
    pyx_imports: str
    pyx_header: str
    pyx_func: str
    std_compile_flag: str
    def __init__(self, *args, **kwargs) -> None:
        '''Instantiates a Cython code wrapper.

        The following optional parameters get passed to ``setuptools.Extension``
        for building the Python extension module. Read its documentation to
        learn more.

        Parameters
        ==========
        include_dirs : [list of strings]
            A list of directories to search for C/C++ header files (in Unix
            form for portability).
        library_dirs : [list of strings]
            A list of directories to search for C/C++ libraries at link time.
        libraries : [list of strings]
            A list of library names (not filenames or paths) to link against.
        extra_compile_args : [list of strings]
            Any extra platform- and compiler-specific information to use when
            compiling the source files in \'sources\'.  For platforms and
            compilers where "command line" makes sense, this is typically a
            list of command-line arguments, but for other platforms it could be
            anything. Note that the attribute ``std_compile_flag`` will be
            appended to this list.
        extra_link_args : [list of strings]
            Any extra platform- and compiler-specific information to use when
            linking object files together to create the extension (or to create
            a new static Python interpreter). Similar interpretation as for
            \'extra_compile_args\'.
        cythonize_options : [dictionary]
            Keyword arguments passed on to cythonize.

        '''
    @property
    def command(self): ...
    def dump_pyx(self, routines, f, prefix) -> None:
        """Write a Cython file with Python wrappers

        This file contains all the definitions of the routines in c code and
        refers to the header file.

        Arguments
        ---------
        routines
            List of Routine instances
        f
            File-like object to write the file to
        prefix
            The filename prefix, used to refer to the proper header file.
            Only the basename of the prefix is used.
        """

class F2PyCodeWrapper(CodeWrapper):
    """Wrapper that uses f2py"""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def command(self): ...

def autowrap(expr, language: Incomplete | None = None, backend: str = 'f2py', tempdir: Incomplete | None = None, args: Incomplete | None = None, flags: Incomplete | None = None, verbose: bool = False, helpers: Incomplete | None = None, code_gen: Incomplete | None = None, **kwargs):
    '''Generates Python callable binaries based on the math expression.

    Parameters
    ==========

    expr
        The SymPy expression that should be wrapped as a binary routine.
    language : string, optional
        If supplied, (options: \'C\' or \'F95\'), specifies the language of the
        generated code. If ``None`` [default], the language is inferred based
        upon the specified backend.
    backend : string, optional
        Backend used to wrap the generated code. Either \'f2py\' [default],
        or \'cython\'.
    tempdir : string, optional
        Path to directory for temporary files. If this argument is supplied,
        the generated code and the wrapper input files are left intact in the
        specified path.
    args : iterable, optional
        An ordered iterable of symbols. Specifies the argument sequence for the
        function.
    flags : iterable, optional
        Additional option flags that will be passed to the backend.
    verbose : bool, optional
        If True, autowrap will not mute the command line backends. This can be
        helpful for debugging.
    helpers : 3-tuple or iterable of 3-tuples, optional
        Used to define auxiliary expressions needed for the main expr. If the
        main expression needs to call a specialized function it should be
        passed in via ``helpers``. Autowrap will then make sure that the
        compiled main expression can link to the helper routine. Items should
        be 3-tuples with (<function_name>, <sympy_expression>,
        <argument_tuple>). It is mandatory to supply an argument sequence to
        helper routines.
    code_gen : CodeGen instance
        An instance of a CodeGen subclass. Overrides ``language``.
    include_dirs : [string]
        A list of directories to search for C/C++ header files (in Unix form
        for portability).
    library_dirs : [string]
        A list of directories to search for C/C++ libraries at link time.
    libraries : [string]
        A list of library names (not filenames or paths) to link against.
    extra_compile_args : [string]
        Any extra platform- and compiler-specific information to use when
        compiling the source files in \'sources\'.  For platforms and compilers
        where "command line" makes sense, this is typically a list of
        command-line arguments, but for other platforms it could be anything.
    extra_link_args : [string]
        Any extra platform- and compiler-specific information to use when
        linking object files together to create the extension (or to create a
        new static Python interpreter).  Similar interpretation as for
        \'extra_compile_args\'.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.utilities.autowrap import autowrap
    >>> expr = ((x - y + z)**(13)).expand()
    >>> binary_func = autowrap(expr)
    >>> binary_func(1, 4, 2)
    -1.0

    '''
def binary_function(symfunc, expr, **kwargs):
    """Returns a SymPy function with expr as binary implementation

    This is a convenience function that automates the steps needed to
    autowrap the SymPy expression and attaching it to a Function object
    with implemented_function().

    Parameters
    ==========

    symfunc : SymPy Function
        The function to bind the callable to.
    expr : SymPy Expression
        The expression used to generate the function.
    kwargs : dict
        Any kwargs accepted by autowrap.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.utilities.autowrap import binary_function
    >>> expr = ((x - y)**(25)).expand()
    >>> f = binary_function('f', expr)
    >>> type(f)
    <class 'sympy.core.function.UndefinedFunction'>
    >>> 2*f(x, y)
    2*f(x, y)
    >>> f(x, y).evalf(2, subs={x: 1, y: 2})
    -1.0

    """

class UfuncifyCodeWrapper(CodeWrapper):
    """Wrapper for Ufuncify"""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def command(self): ...
    def wrap_code(self, routines, helpers: Incomplete | None = None): ...
    def dump_setup(self, f) -> None: ...
    def dump_c(self, routines, f, prefix, funcname: Incomplete | None = None) -> None:
        """Write a C file with Python wrappers

        This file contains all the definitions of the routines in c code.

        Arguments
        ---------
        routines
            List of Routine instances
        f
            File-like object to write the file to
        prefix
            The filename prefix, used to name the imported module.
        funcname
            Name of the main function to be returned.
        """

def ufuncify(args, expr, language: Incomplete | None = None, backend: str = 'numpy', tempdir: Incomplete | None = None, flags: Incomplete | None = None, verbose: bool = False, helpers: Incomplete | None = None, **kwargs):
    '''Generates a binary function that supports broadcasting on numpy arrays.

    Parameters
    ==========

    args : iterable
        Either a Symbol or an iterable of symbols. Specifies the argument
        sequence for the function.
    expr
        A SymPy expression that defines the element wise operation.
    language : string, optional
        If supplied, (options: \'C\' or \'F95\'), specifies the language of the
        generated code. If ``None`` [default], the language is inferred based
        upon the specified backend.
    backend : string, optional
        Backend used to wrap the generated code. Either \'numpy\' [default],
        \'cython\', or \'f2py\'.
    tempdir : string, optional
        Path to directory for temporary files. If this argument is supplied,
        the generated code and the wrapper input files are left intact in
        the specified path.
    flags : iterable, optional
        Additional option flags that will be passed to the backend.
    verbose : bool, optional
        If True, autowrap will not mute the command line backends. This can
        be helpful for debugging.
    helpers : iterable, optional
        Used to define auxiliary expressions needed for the main expr. If
        the main expression needs to call a specialized function it should
        be put in the ``helpers`` iterable. Autowrap will then make sure
        that the compiled main expression can link to the helper routine.
        Items should be tuples with (<funtion_name>, <sympy_expression>,
        <arguments>). It is mandatory to supply an argument sequence to
        helper routines.
    kwargs : dict
        These kwargs will be passed to autowrap if the `f2py` or `cython`
        backend is used and ignored if the `numpy` backend is used.

    Notes
    =====

    The default backend (\'numpy\') will create actual instances of
    ``numpy.ufunc``. These support ndimensional broadcasting, and implicit type
    conversion. Use of the other backends will result in a "ufunc-like"
    function, which requires equal length 1-dimensional arrays for all
    arguments, and will not perform any type conversions.

    References
    ==========

    .. [1] https://numpy.org/doc/stable/reference/ufuncs.html

    Examples
    ========

    >>> from sympy.utilities.autowrap import ufuncify
    >>> from sympy.abc import x, y
    >>> import numpy as np
    >>> f = ufuncify((x, y), y + x**2)
    >>> type(f)
    <class \'numpy.ufunc\'>
    >>> f([1, 2, 3], 2)
    array([  3.,   6.,  11.])
    >>> f(np.arange(5), 3)
    array([  3.,   4.,   7.,  12.,  19.])

    For the \'f2py\' and \'cython\' backends, inputs are required to be equal length
    1-dimensional arrays. The \'f2py\' backend will perform type conversion, but
    the Cython backend will error if the inputs are not of the expected type.

    >>> f_fortran = ufuncify((x, y), y + x**2, backend=\'f2py\')
    >>> f_fortran(1, 2)
    array([ 3.])
    >>> f_fortran(np.array([1, 2, 3]), np.array([1.0, 2.0, 3.0]))
    array([  2.,   6.,  12.])
    >>> f_cython = ufuncify((x, y), y + x**2, backend=\'Cython\')
    >>> f_cython(1, 2)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    TypeError: Argument \'_x\' has incorrect type (expected numpy.ndarray, got int)
    >>> f_cython(np.array([1.0]), np.array([2.0]))
    array([ 3.])

    '''
