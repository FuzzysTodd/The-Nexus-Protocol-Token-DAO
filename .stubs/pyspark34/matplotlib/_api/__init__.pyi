from .deprecation import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning, delete_parameter as delete_parameter, deprecate_method_override as deprecate_method_override, deprecate_privatize_attribute as deprecate_privatize_attribute, deprecated as deprecated, make_keyword_only as make_keyword_only, rename_parameter as rename_parameter, suppress_matplotlib_deprecation_warning as suppress_matplotlib_deprecation_warning, warn_deprecated as warn_deprecated
from _typeshed import Incomplete
from collections.abc import Generator

class classproperty:
    '''
    Like `property`, but also triggers on access via the class, and it is the
    *class* that\'s passed as argument.

    Examples
    --------
    ::

        class C:
            @classproperty
            def foo(cls):
                return cls.__name__

        assert C.foo == "C"
    '''
    fset: Incomplete
    fdel: Incomplete
    def __init__(self, fget, fset: Incomplete | None = None, fdel: Incomplete | None = None, doc: Incomplete | None = None) -> None: ...
    def __get__(self, instance, owner): ...
    @property
    def fget(self): ...

def check_isinstance(_types, **kwargs):
    """
    For each *key, value* pair in *kwargs*, check that *value* is an instance
    of one of *_types*; if not, raise an appropriate TypeError.

    As a special case, a ``None`` entry in *_types* is treated as NoneType.

    Examples
    --------
    >>> _api.check_isinstance((SomeClass, None), arg=arg)
    """
def check_in_list(_values, *, _print_supported_values: bool = True, **kwargs) -> None:
    '''
    For each *key, value* pair in *kwargs*, check that *value* is in *_values*.

    Parameters
    ----------
    _values : iterable
        Sequence of values to check on.
    _print_supported_values : bool, default: True
        Whether to print *_values* when raising ValueError.
    **kwargs : dict
        *key, value* pairs as keyword arguments to find in *_values*.

    Raises
    ------
    ValueError
        If any *value* in *kwargs* is not found in *_values*.

    Examples
    --------
    >>> _api.check_in_list(["foo", "bar"], arg=arg, other_arg=other_arg)
    '''
def check_shape(_shape, **kwargs) -> None:
    '''
    For each *key, value* pair in *kwargs*, check that *value* has the shape
    *_shape*, if not, raise an appropriate ValueError.

    *None* in the shape is treated as a "free" size that can have any length.
    e.g. (None, 2) -> (N, 2)

    The values checked must be numpy arrays.

    Examples
    --------
    To check for (N, 2) shaped arrays

    >>> _api.check_shape((None, 2), arg=arg, other_arg=other_arg)
    '''
def check_getitem(_mapping, **kwargs):
    '''
    *kwargs* must consist of a single *key, value* pair.  If *key* is in
    *_mapping*, return ``_mapping[value]``; else, raise an appropriate
    ValueError.

    Examples
    --------
    >>> _api.check_getitem({"foo": "bar"}, arg=arg)
    '''
def caching_module_getattr(cls):
    """
    Helper decorator for implementing module-level ``__getattr__`` as a class.

    This decorator must be used at the module toplevel as follows::

        @caching_module_getattr
        class __getattr__:  # The class *must* be named ``__getattr__``.
            @property  # Only properties are taken into account.
            def name(self): ...

    The ``__getattr__`` class will be replaced by a ``__getattr__``
    function such that trying to access ``name`` on the module will
    resolve the corresponding property (which may be decorated e.g. with
    ``_api.deprecated`` for deprecating module globals).  The properties are
    all implicitly cached.  Moreover, a suitable AttributeError is generated
    and raised if no property with the given name exists.
    """
def define_aliases(alias_d, cls: Incomplete | None = None):
    '''
    Class decorator for defining property aliases.

    Use as ::

        @_api.define_aliases({"property": ["alias", ...], ...})
        class C: ...

    For each property, if the corresponding ``get_property`` is defined in the
    class so far, an alias named ``get_alias`` will be defined; the same will
    be done for setters.  If neither the getter nor the setter exists, an
    exception will be raised.

    The alias map is stored as the ``_alias_map`` attribute on the class and
    can be used by `.normalize_kwargs` (which assumes that higher priority
    aliases come last).
    '''
def select_matching_signature(funcs, *args, **kwargs):
    '''
    Select and call the function that accepts ``*args, **kwargs``.

    *funcs* is a list of functions which should not raise any exception (other
    than `TypeError` if the arguments passed do not match their signature).

    `select_matching_signature` tries to call each of the functions in *funcs*
    with ``*args, **kwargs`` (in the order in which they are given).  Calls
    that fail with a `TypeError` are silently skipped.  As soon as a call
    succeeds, `select_matching_signature` returns its return value.  If no
    function accepts ``*args, **kwargs``, then the `TypeError` raised by the
    last failing call is re-raised.

    Callers should normally make sure that any ``*args, **kwargs`` can only
    bind a single *func* (to avoid any ambiguity), although this is not checked
    by `select_matching_signature`.

    Notes
    -----
    `select_matching_signature` is intended to help implementing
    signature-overloaded functions.  In general, such functions should be
    avoided, except for back-compatibility concerns.  A typical use pattern is
    ::

        def my_func(*args, **kwargs):
            params = select_matching_signature(
                [lambda old1, old2: locals(), lambda new: locals()],
                *args, **kwargs)
            if "old1" in params:
                warn_deprecated(...)
                old1, old2 = params.values()  # note that locals() is ordered.
            else:
                new, = params.values()
            # do things with params

    which allows *my_func* to be called either with two parameters (*old1* and
    *old2*) or a single one (*new*).  Note that the new signature is given
    last, so that callers get a `TypeError` corresponding to the new signature
    if the arguments they passed in do not match any signature.
    '''
def nargs_error(name, takes, given):
    """Generate a TypeError to be raised by function calls with wrong arity."""
def kwarg_error(name, kw):
    """
    Generate a TypeError to be raised by function calls with wrong kwarg.

    Parameters
    ----------
    name : str
        The name of the calling function.
    kw : str or Iterable[str]
        Either the invalid keyword argument name, or an iterable yielding
        invalid keyword arguments (e.g., a ``kwargs`` dict).
    """
def recursive_subclasses(cls) -> Generator[Incomplete, Incomplete, None]:
    """Yield *cls* and direct and indirect subclasses of *cls*."""
def warn_external(message, category: Incomplete | None = None) -> None:
    '''
    `warnings.warn` wrapper that sets *stacklevel* to "outside Matplotlib".

    The original emitter of the warning can be obtained by patching this
    function back to `warnings.warn`, i.e. ``_api.warn_external =
    warnings.warn`` (or ``functools.partial(warnings.warn, stacklevel=2)``,
    etc.).
    '''
