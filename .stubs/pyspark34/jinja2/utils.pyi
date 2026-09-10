import enum
import markupsafe
import typing as t
from _typeshed import Incomplete
from types import CodeType

F = t.TypeVar('F', bound=t.Callable[..., t.Any])
missing: t.Any
internal_code: t.MutableSet[CodeType]
concat: Incomplete

def pass_context(f: F) -> F:
    """Pass the :class:`~jinja2.runtime.Context` as the first argument
    to the decorated function when called while rendering a template.

    Can be used on functions, filters, and tests.

    If only ``Context.eval_context`` is needed, use
    :func:`pass_eval_context`. If only ``Context.environment`` is
    needed, use :func:`pass_environment`.

    .. versionadded:: 3.0.0
        Replaces ``contextfunction`` and ``contextfilter``.
    """
def pass_eval_context(f: F) -> F:
    """Pass the :class:`~jinja2.nodes.EvalContext` as the first argument
    to the decorated function when called while rendering a template.
    See :ref:`eval-context`.

    Can be used on functions, filters, and tests.

    If only ``EvalContext.environment`` is needed, use
    :func:`pass_environment`.

    .. versionadded:: 3.0.0
        Replaces ``evalcontextfunction`` and ``evalcontextfilter``.
    """
def pass_environment(f: F) -> F:
    """Pass the :class:`~jinja2.Environment` as the first argument to
    the decorated function when called while rendering a template.

    Can be used on functions, filters, and tests.

    .. versionadded:: 3.0.0
        Replaces ``environmentfunction`` and ``environmentfilter``.
    """

class _PassArg(enum.Enum):
    context: Incomplete
    eval_context: Incomplete
    environment: Incomplete
    @classmethod
    def from_obj(cls, obj: F) -> _PassArg | None: ...

def internalcode(f: F) -> F:
    """Marks the function as internally used"""
def is_undefined(obj: t.Any) -> bool:
    """Check if the object passed is undefined.  This does nothing more than
    performing an instance check against :class:`Undefined` but looks nicer.
    This can be used for custom filters or tests that want to react to
    undefined variables.  For example a custom default filter can look like
    this::

        def default(var, default=''):
            if is_undefined(var):
                return default
            return var
    """
def consume(iterable: t.Iterable[t.Any]) -> None:
    """Consumes an iterable without doing anything with it."""
def clear_caches() -> None:
    """Jinja keeps internal caches for environments and lexers.  These are
    used so that Jinja doesn't have to recreate environments and lexers all
    the time.  Normally you don't have to care about that but if you are
    measuring memory consumption you may want to clean the caches.
    """
def import_string(import_name: str, silent: bool = False) -> t.Any:
    """Imports an object based on a string.  This is useful if you want to
    use import paths as endpoints or something similar.  An import path can
    be specified either in dotted notation (``xml.sax.saxutils.escape``)
    or with a colon as object delimiter (``xml.sax.saxutils:escape``).

    If the `silent` is True the return value will be `None` if the import
    fails.

    :return: imported object
    """
def open_if_exists(filename: str, mode: str = 'rb') -> t.IO | None:
    """Returns a file descriptor for the filename if that file exists,
    otherwise ``None``.
    """
def object_type_repr(obj: t.Any) -> str:
    """Returns the name of the object's type.  For some recognized
    singletons the name of the object is returned instead. (For
    example for `None` and `Ellipsis`).
    """
def pformat(obj: t.Any) -> str:
    """Format an object using :func:`pprint.pformat`."""
def urlize(text: str, trim_url_limit: int | None = None, rel: str | None = None, target: str | None = None, extra_schemes: t.Iterable[str] | None = None) -> str:
    """Convert URLs in text into clickable links.

    This may not recognize links in some situations. Usually, a more
    comprehensive formatter, such as a Markdown library, is a better
    choice.

    Works on ``http://``, ``https://``, ``www.``, ``mailto:``, and email
    addresses. Links with trailing punctuation (periods, commas, closing
    parentheses) and leading punctuation (opening parentheses) are
    recognized excluding the punctuation. Email addresses that include
    header fields are not recognized (for example,
    ``mailto:address@example.com?cc=copy@example.com``).

    :param text: Original text containing URLs to link.
    :param trim_url_limit: Shorten displayed URL values to this length.
    :param target: Add the ``target`` attribute to links.
    :param rel: Add the ``rel`` attribute to links.
    :param extra_schemes: Recognize URLs that start with these schemes
        in addition to the default behavior.

    .. versionchanged:: 3.0
        The ``extra_schemes`` parameter was added.

    .. versionchanged:: 3.0
        Generate ``https://`` links for URLs without a scheme.

    .. versionchanged:: 3.0
        The parsing rules were updated. Recognize email addresses with
        or without the ``mailto:`` scheme. Validate IP addresses. Ignore
        parentheses and brackets in more cases.
    """
def generate_lorem_ipsum(n: int = 5, html: bool = True, min: int = 20, max: int = 100) -> str:
    """Generate some lorem ipsum for the template."""
def url_quote(obj: t.Any, charset: str = 'utf-8', for_qs: bool = False) -> str:
    '''Quote a string for use in a URL using the given charset.

    :param obj: String or bytes to quote. Other types are converted to
        string then encoded to bytes using the given charset.
    :param charset: Encode text to bytes using this charset.
    :param for_qs: Quote "/" and use "+" for spaces.
    '''

class LRUCache:
    """A simple LRU Cache implementation."""
    capacity: Incomplete
    def __init__(self, capacity: int) -> None: ...
    def __getnewargs__(self) -> t.Tuple: ...
    def copy(self) -> LRUCache:
        """Return a shallow copy of the instance."""
    def get(self, key: t.Any, default: t.Any = None) -> t.Any:
        """Return an item from the cache dict or `default`"""
    def setdefault(self, key: t.Any, default: t.Any = None) -> t.Any:
        """Set `default` if the key is not in the cache otherwise
        leave unchanged. Return the value of this key.
        """
    def clear(self) -> None:
        """Clear the cache."""
    def __contains__(self, key: t.Any) -> bool:
        """Check if a key exists in this cache."""
    def __len__(self) -> int:
        """Return the current size of the cache."""
    def __getitem__(self, key: t.Any) -> t.Any:
        """Get an item from the cache. Moves the item up so that it has the
        highest priority then.

        Raise a `KeyError` if it does not exist.
        """
    def __setitem__(self, key: t.Any, value: t.Any) -> None:
        """Sets the value for an item. Moves the item up so that it
        has the highest priority then.
        """
    def __delitem__(self, key: t.Any) -> None:
        """Remove an item from the cache dict.
        Raise a `KeyError` if it does not exist.
        """
    def items(self) -> t.Iterable[t.Tuple[t.Any, t.Any]]:
        """Return a list of items."""
    def values(self) -> t.Iterable[t.Any]:
        """Return a list of all values."""
    def keys(self) -> t.Iterable[t.Any]:
        """Return a list of all keys ordered by most recent usage."""
    def __iter__(self) -> t.Iterator[t.Any]: ...
    def __reversed__(self) -> t.Iterator[t.Any]:
        """Iterate over the keys in the cache dict, oldest items
        coming first.
        """
    __copy__ = copy

def select_autoescape(enabled_extensions: t.Collection[str] = ('html', 'htm', 'xml'), disabled_extensions: t.Collection[str] = (), default_for_string: bool = True, default: bool = False) -> t.Callable[[str | None], bool]:
    """Intelligently sets the initial value of autoescaping based on the
    filename of the template.  This is the recommended way to configure
    autoescaping if you do not want to write a custom function yourself.

    If you want to enable it for all templates created from strings or
    for all templates with `.html` and `.xml` extensions::

        from jinja2 import Environment, select_autoescape
        env = Environment(autoescape=select_autoescape(
            enabled_extensions=('html', 'xml'),
            default_for_string=True,
        ))

    Example configuration to turn it on at all times except if the template
    ends with `.txt`::

        from jinja2 import Environment, select_autoescape
        env = Environment(autoescape=select_autoescape(
            disabled_extensions=('txt',),
            default_for_string=True,
            default=True,
        ))

    The `enabled_extensions` is an iterable of all the extensions that
    autoescaping should be enabled for.  Likewise `disabled_extensions` is
    a list of all templates it should be disabled for.  If a template is
    loaded from a string then the default from `default_for_string` is used.
    If nothing matches then the initial value of autoescaping is set to the
    value of `default`.

    For security reasons this function operates case insensitive.

    .. versionadded:: 2.9
    """
def htmlsafe_json_dumps(obj: t.Any, dumps: t.Callable[..., str] | None = None, **kwargs: t.Any) -> markupsafe.Markup:
    '''Serialize an object to a string of JSON with :func:`json.dumps`,
    then replace HTML-unsafe characters with Unicode escapes and mark
    the result safe with :class:`~markupsafe.Markup`.

    This is available in templates as the ``|tojson`` filter.

    The following characters are escaped: ``<``, ``>``, ``&``, ``\'``.

    The returned string is safe to render in HTML documents and
    ``<script>`` tags. The exception is in HTML attributes that are
    double quoted; either use single quotes or the ``|forceescape``
    filter.

    :param obj: The object to serialize to JSON.
    :param dumps: The ``dumps`` function to use. Defaults to
        ``env.policies["json.dumps_function"]``, which defaults to
        :func:`json.dumps`.
    :param kwargs: Extra arguments to pass to ``dumps``. Merged onto
        ``env.policies["json.dumps_kwargs"]``.

    .. versionchanged:: 3.0
        The ``dumper`` parameter is renamed to ``dumps``.

    .. versionadded:: 2.9
    '''

class Cycler:
    '''Cycle through values by yield them one at a time, then restarting
    once the end is reached. Available as ``cycler`` in templates.

    Similar to ``loop.cycle``, but can be used outside loops or across
    multiple loops. For example, render a list of folders and files in a
    list, alternating giving them "odd" and "even" classes.

    .. code-block:: html+jinja

        {% set row_class = cycler("odd", "even") %}
        <ul class="browser">
        {% for folder in folders %}
          <li class="folder {{ row_class.next() }}">{{ folder }}
        {% endfor %}
        {% for file in files %}
          <li class="file {{ row_class.next() }}">{{ file }}
        {% endfor %}
        </ul>

    :param items: Each positional argument will be yielded in the order
        given for each cycle.

    .. versionadded:: 2.1
    '''
    items: Incomplete
    pos: int
    def __init__(self, *items: t.Any) -> None: ...
    def reset(self) -> None:
        """Resets the current item to the first item."""
    @property
    def current(self) -> t.Any:
        """Return the current item. Equivalent to the item that will be
        returned next time :meth:`next` is called.
        """
    def next(self) -> t.Any:
        """Return the current item, then advance :attr:`current` to the
        next item.
        """
    __next__ = next

class Joiner:
    """A joining helper for templates."""
    sep: Incomplete
    used: bool
    def __init__(self, sep: str = ', ') -> None: ...
    def __call__(self) -> str: ...

class Namespace:
    """A namespace object that can hold arbitrary attributes.  It may be
    initialized from a dictionary or with keyword arguments."""
    def __init__(*args: t.Any, **kwargs: t.Any) -> None: ...
    def __getattribute__(self, name: str) -> t.Any: ...
    def __setitem__(self, name: str, value: t.Any) -> None: ...
