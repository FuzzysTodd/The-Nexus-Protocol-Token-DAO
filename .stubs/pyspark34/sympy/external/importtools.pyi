from _typeshed import Incomplete

WARN_NOT_INSTALLED: Incomplete
WARN_OLD_VERSION: Incomplete

def version_tuple(vstring): ...
def import_module(module, min_module_version: Incomplete | None = None, min_python_version: Incomplete | None = None, warn_not_installed: Incomplete | None = None, warn_old_version: Incomplete | None = None, module_version_attr: str = '__version__', module_version_attr_call_args: Incomplete | None = None, import_kwargs={}, catch=()):
    """
    Import and return a module if it is installed.

    If the module is not installed, it returns None.

    A minimum version for the module can be given as the keyword argument
    min_module_version.  This should be comparable against the module version.
    By default, module.__version__ is used to get the module version.  To
    override this, set the module_version_attr keyword argument.  If the
    attribute of the module to get the version should be called (e.g.,
    module.version()), then set module_version_attr_call_args to the args such
    that module.module_version_attr(*module_version_attr_call_args) returns the
    module's version.

    If the module version is less than min_module_version using the Python <
    comparison, None will be returned, even if the module is installed. You can
    use this to keep from importing an incompatible older version of a module.

    You can also specify a minimum Python version by using the
    min_python_version keyword argument.  This should be comparable against
    sys.version_info.

    If the keyword argument warn_not_installed is set to True, the function will
    emit a UserWarning when the module is not installed.

    If the keyword argument warn_old_version is set to True, the function will
    emit a UserWarning when the library is installed, but cannot be imported
    because of the min_module_version or min_python_version options.

    Note that because of the way warnings are handled, a warning will be
    emitted for each module only once.  You can change the default warning
    behavior by overriding the values of WARN_NOT_INSTALLED and WARN_OLD_VERSION
    in sympy.external.importtools.  By default, WARN_NOT_INSTALLED is False and
    WARN_OLD_VERSION is True.

    This function uses __import__() to import the module.  To pass additional
    options to __import__(), use the import_kwargs keyword argument.  For
    example, to import a submodule A.B, you must pass a nonempty fromlist option
    to __import__.  See the docstring of __import__().

    This catches ImportError to determine if the module is not installed.  To
    catch additional errors, pass them as a tuple to the catch keyword
    argument.

    Examples
    ========

    >>> from sympy.external import import_module

    >>> numpy = import_module('numpy')

    >>> numpy = import_module('numpy', min_python_version=(2, 7),
    ... warn_old_version=False)

    >>> numpy = import_module('numpy', min_module_version='1.5',
    ... warn_old_version=False) # numpy.__version__ is a string

    >>> # gmpy does not have __version__, but it does have gmpy.version()

    >>> gmpy = import_module('gmpy', min_module_version='1.14',
    ... module_version_attr='version', module_version_attr_call_args=(),
    ... warn_old_version=False)

    >>> # To import a submodule, you must pass a nonempty fromlist to
    >>> # __import__().  The values do not matter.
    >>> p3 = import_module('mpl_toolkits.mplot3d',
    ... import_kwargs={'fromlist':['something']})

    >>> # matplotlib.pyplot can raise RuntimeError when the display cannot be opened
    >>> matplotlib = import_module('matplotlib',
    ... import_kwargs={'fromlist':['pyplot']}, catch=(RuntimeError,))

    """
