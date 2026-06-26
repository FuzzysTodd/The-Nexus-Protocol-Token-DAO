import logging
import typing as t
import typing_extensions as te
from .async_utils import auto_aiter as auto_aiter, auto_await as auto_await
from .environment import Environment as Environment
from .exceptions import TemplateNotFound as TemplateNotFound, TemplateRuntimeError as TemplateRuntimeError, UndefinedError as UndefinedError
from .nodes import EvalContext as EvalContext
from .utils import Namespace as Namespace, concat as concat, internalcode as internalcode, missing as missing, object_type_repr as object_type_repr, pass_eval_context as pass_eval_context
from _typeshed import Incomplete
from markupsafe import escape as escape

V = t.TypeVar('V')
F = t.TypeVar('F', bound=t.Callable[..., t.Any])

class LoopRenderFunc(te.Protocol):
    def __call__(self, reciter: t.Iterable[V], loop_render_func: LoopRenderFunc, depth: int = 0) -> str: ...

exported: Incomplete
async_exported: Incomplete

def identity(x: V) -> V:
    """Returns its argument. Useful for certain things in the
    environment.
    """
def markup_join(seq: t.Iterable[t.Any]) -> str:
    """Concatenation that escapes if necessary and converts to string."""
def str_join(seq: t.Iterable[t.Any]) -> str:
    """Simple args to string conversion and concatenation."""
def new_context(environment: Environment, template_name: str | None, blocks: t.Dict[str, t.Callable[[Context], t.Iterator[str]]], vars: t.Dict[str, t.Any] | None = None, shared: bool = False, globals: t.MutableMapping[str, t.Any] | None = None, locals: t.Mapping[str, t.Any] | None = None) -> Context:
    """Internal helper for context creation."""

class TemplateReference:
    """The `self` in templates."""
    def __init__(self, context: Context) -> None: ...
    def __getitem__(self, name: str) -> t.Any: ...

class Context:
    """The template context holds the variables of a template.  It stores the
    values passed to the template and also the names the template exports.
    Creating instances is neither supported nor useful as it's created
    automatically at various stages of the template evaluation and should not
    be created by hand.

    The context is immutable.  Modifications on :attr:`parent` **must not**
    happen and modifications on :attr:`vars` are allowed from generated
    template code only.  Template filters and global functions marked as
    :func:`pass_context` get the active context passed as first argument
    and are allowed to access the context read-only.

    The template context supports read only dict operations (`get`,
    `keys`, `values`, `items`, `iterkeys`, `itervalues`, `iteritems`,
    `__getitem__`, `__contains__`).  Additionally there is a :meth:`resolve`
    method that doesn't fail with a `KeyError` but returns an
    :class:`Undefined` object for missing variables.
    """
    parent: Incomplete
    vars: Incomplete
    environment: Incomplete
    eval_ctx: Incomplete
    exported_vars: Incomplete
    name: Incomplete
    globals_keys: Incomplete
    blocks: Incomplete
    def __init__(self, environment: Environment, parent: t.Dict[str, t.Any], name: str | None, blocks: t.Dict[str, t.Callable[[Context], t.Iterator[str]]], globals: t.MutableMapping[str, t.Any] | None = None) -> None: ...
    def super(self, name: str, current: t.Callable[[Context], t.Iterator[str]]) -> BlockReference | Undefined:
        """Render a parent block."""
    def get(self, key: str, default: t.Any = None) -> t.Any:
        """Look up a variable by name, or return a default if the key is
        not found.

        :param key: The variable name to look up.
        :param default: The value to return if the key is not found.
        """
    def resolve(self, key: str) -> t.Any | Undefined:
        """Look up a variable by name, or return an :class:`Undefined`
        object if the key is not found.

        If you need to add custom behavior, override
        :meth:`resolve_or_missing`, not this method. The various lookup
        functions use that method, not this one.

        :param key: The variable name to look up.
        """
    def resolve_or_missing(self, key: str) -> t.Any:
        """Look up a variable by name, or return a ``missing`` sentinel
        if the key is not found.

        Override this method to add custom lookup behavior.
        :meth:`resolve`, :meth:`get`, and :meth:`__getitem__` use this
        method. Don't call this method directly.

        :param key: The variable name to look up.
        """
    def get_exported(self) -> t.Dict[str, t.Any]:
        """Get a new dict with the exported variables."""
    def get_all(self) -> t.Dict[str, t.Any]:
        """Return the complete context as dict including the exported
        variables.  For optimizations reasons this might not return an
        actual copy so be careful with using it.
        """
    def call(__self, __obj: t.Callable, *args: t.Any, **kwargs: t.Any) -> t.Any | Undefined:
        """Call the callable with the arguments and keyword arguments
        provided but inject the active context or environment as first
        argument if the callable has :func:`pass_context` or
        :func:`pass_environment`.
        """
    def derived(self, locals: t.Dict[str, t.Any] | None = None) -> Context:
        """Internal helper function to create a derived context.  This is
        used in situations where the system needs a new context in the same
        template that is independent.
        """
    keys: Incomplete
    values: Incomplete
    items: Incomplete
    def __contains__(self, name: str) -> bool: ...
    def __getitem__(self, key: str) -> t.Any:
        """Look up a variable by name with ``[]`` syntax, or raise a
        ``KeyError`` if the key is not found.
        """

class BlockReference:
    """One block on a template reference."""
    name: Incomplete
    def __init__(self, name: str, context: Context, stack: t.List[t.Callable[[Context], t.Iterator[str]]], depth: int) -> None: ...
    @property
    def super(self) -> BlockReference | Undefined:
        """Super the block."""
    def __call__(self) -> str: ...

class LoopContext:
    """A wrapper iterable for dynamic ``for`` loops, with information
    about the loop and iteration.
    """
    index0: int
    depth0: Incomplete
    def __init__(self, iterable: t.Iterable[V], undefined: t.Type['Undefined'], recurse: LoopRenderFunc | None = None, depth0: int = 0) -> None:
        """
        :param iterable: Iterable to wrap.
        :param undefined: :class:`Undefined` class to use for next and
            previous items.
        :param recurse: The function to render the loop body when the
            loop is marked recursive.
        :param depth0: Incremented when looping recursively.
        """
    @property
    def length(self) -> int:
        """Length of the iterable.

        If the iterable is a generator or otherwise does not have a
        size, it is eagerly evaluated to get a size.
        """
    def __len__(self) -> int: ...
    @property
    def depth(self) -> int:
        """How many levels deep a recursive loop currently is, starting at 1."""
    @property
    def index(self) -> int:
        """Current iteration of the loop, starting at 1."""
    @property
    def revindex0(self) -> int:
        """Number of iterations from the end of the loop, ending at 0.

        Requires calculating :attr:`length`.
        """
    @property
    def revindex(self) -> int:
        """Number of iterations from the end of the loop, ending at 1.

        Requires calculating :attr:`length`.
        """
    @property
    def first(self) -> bool:
        """Whether this is the first iteration of the loop."""
    @property
    def last(self) -> bool:
        """Whether this is the last iteration of the loop.

        Causes the iterable to advance early. See
        :func:`itertools.groupby` for issues this can cause.
        The :func:`groupby` filter avoids that issue.
        """
    @property
    def previtem(self) -> t.Any | Undefined:
        """The item in the previous iteration. Undefined during the
        first iteration.
        """
    @property
    def nextitem(self) -> t.Any | Undefined:
        """The item in the next iteration. Undefined during the last
        iteration.

        Causes the iterable to advance early. See
        :func:`itertools.groupby` for issues this can cause.
        The :func:`jinja-filters.groupby` filter avoids that issue.
        """
    def cycle(self, *args: V) -> V:
        """Return a value from the given args, cycling through based on
        the current :attr:`index0`.

        :param args: One or more values to cycle through.
        """
    def changed(self, *value: t.Any) -> bool:
        """Return ``True`` if previously called with a different value
        (including when called for the first time).

        :param value: One or more values to compare to the last call.
        """
    def __iter__(self) -> LoopContext: ...
    def __next__(self) -> t.Tuple[t.Any, 'LoopContext']: ...
    def __call__(self, iterable: t.Iterable[V]) -> str:
        """When iterating over nested data, render the body of the loop
        recursively with the given inner iterable data.

        The loop must have the ``recursive`` marker for this to work.
        """

class AsyncLoopContext(LoopContext):
    @property
    async def length(self) -> int: ...
    @property
    async def revindex0(self) -> int: ...
    @property
    async def revindex(self) -> int: ...
    @property
    async def last(self) -> bool: ...
    @property
    async def nextitem(self) -> t.Any | Undefined: ...
    def __aiter__(self) -> AsyncLoopContext: ...
    async def __anext__(self) -> t.Tuple[t.Any, 'AsyncLoopContext']: ...

class Macro:
    """Wraps a macro function."""
    name: Incomplete
    arguments: Incomplete
    catch_kwargs: Incomplete
    catch_varargs: Incomplete
    caller: Incomplete
    explicit_caller: Incomplete
    def __init__(self, environment: Environment, func: t.Callable[..., str], name: str, arguments: t.List[str], catch_kwargs: bool, catch_varargs: bool, caller: bool, default_autoescape: bool | None = None) -> None: ...
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> str: ...

class Undefined:
    """The default undefined type.  This undefined type can be printed and
    iterated over, but every other access will raise an :exc:`UndefinedError`:

    >>> foo = Undefined(name='foo')
    >>> str(foo)
    ''
    >>> not foo
    True
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """
    def __init__(self, hint: str | None = None, obj: t.Any = ..., name: str | None = None, exc: t.Type[TemplateRuntimeError] = ...) -> None: ...
    def __getattr__(self, name: str) -> t.Any: ...
    __add__: Incomplete
    __radd__: Incomplete
    __sub__: Incomplete
    __rsub__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __div__: Incomplete
    __rdiv__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __floordiv__: Incomplete
    __rfloordiv__: Incomplete
    __mod__: Incomplete
    __rmod__: Incomplete
    __pos__: Incomplete
    __neg__: Incomplete
    __call__: Incomplete
    __getitem__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    __int__: Incomplete
    __float__: Incomplete
    __complex__: Incomplete
    __pow__: Incomplete
    __rpow__: Incomplete
    def __eq__(self, other: t.Any) -> bool: ...
    def __ne__(self, other: t.Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> t.Iterator[t.Any]: ...
    async def __aiter__(self) -> t.AsyncIterator[t.Any]: ...
    def __bool__(self) -> bool: ...

def make_logging_undefined(logger: logging.Logger | None = None, base: t.Type[Undefined] = ...) -> t.Type[Undefined]:
    """Given a logger object this returns a new undefined class that will
    log certain failures.  It will log iterations and printing.  If no
    logger is given a default logger is created.

    Example::

        logger = logging.getLogger(__name__)
        LoggingUndefined = make_logging_undefined(
            logger=logger,
            base=Undefined
        )

    .. versionadded:: 2.8

    :param logger: the logger to use.  If not provided, a default logger
                   is created.
    :param base: the base class to add logging functionality to.  This
                 defaults to :class:`Undefined`.
    """

class ChainableUndefined(Undefined):
    """An undefined that is chainable, where both ``__getattr__`` and
    ``__getitem__`` return itself rather than raising an
    :exc:`UndefinedError`.

    >>> foo = ChainableUndefined(name='foo')
    >>> str(foo.bar['baz'])
    ''
    >>> foo.bar['baz'] + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined

    .. versionadded:: 2.11.0
    """
    def __html__(self) -> str: ...
    def __getattr__(self, _: str) -> ChainableUndefined: ...
    __getitem__ = __getattr__

class DebugUndefined(Undefined):
    """An undefined that returns the debug info when printed.

    >>> foo = DebugUndefined(name='foo')
    >>> str(foo)
    '{{ foo }}'
    >>> not foo
    True
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """

class StrictUndefined(Undefined):
    """An undefined that barks on print and iteration as well as boolean
    tests and all kinds of comparisons.  In other words: you can do nothing
    with it except checking if it's defined using the `defined` test.

    >>> foo = StrictUndefined(name='foo')
    >>> str(foo)
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    >>> not foo
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """
    __iter__: Incomplete
    __len__: Incomplete
    __eq__: Incomplete
    __ne__: Incomplete
    __bool__: Incomplete
    __hash__: Incomplete
    __contains__: Incomplete
