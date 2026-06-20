import typing
import typing as t
import typing_extensions as te
from .async_utils import async_variant as async_variant, auto_aiter as auto_aiter, auto_await as auto_await, auto_to_list as auto_to_list
from .environment import Environment as Environment
from .exceptions import FilterArgumentError as FilterArgumentError
from .nodes import EvalContext as EvalContext
from .runtime import Context as Context, Undefined as Undefined
from .sandbox import SandboxedEnvironment as SandboxedEnvironment
from .utils import htmlsafe_json_dumps as htmlsafe_json_dumps, pass_context as pass_context, pass_environment as pass_environment, pass_eval_context as pass_eval_context, pformat as pformat, url_quote as url_quote, urlize as urlize
from _typeshed import Incomplete
from markupsafe import Markup

class HasHTML(te.Protocol):
    def __html__(self) -> str: ...
F = t.TypeVar('F', bound=t.Callable[..., t.Any])
K = t.TypeVar('K')
V = t.TypeVar('V')

def ignore_case(value: V) -> V:
    """For use as a postprocessor for :func:`make_attrgetter`. Converts strings
    to lowercase and returns other types as-is."""
def make_attrgetter(environment: Environment, attribute: str | int | None, postprocess: t.Callable[[t.Any], t.Any] | None = None, default: t.Any | None = None) -> t.Callable[[t.Any], t.Any]:
    """Returns a callable that looks up the given attribute from a
    passed object with the rules of the environment.  Dots are allowed
    to access attributes of attributes.  Integer parts in paths are
    looked up as integers.
    """
def make_multi_attrgetter(environment: Environment, attribute: str | int | None, postprocess: t.Callable[[t.Any], t.Any] | None = None) -> t.Callable[[t.Any], t.List[t.Any]]:
    '''Returns a callable that looks up the given comma separated
    attributes from a passed object with the rules of the environment.
    Dots are allowed to access attributes of each attribute.  Integer
    parts in paths are looked up as integers.

    The value returned by the returned callable is a list of extracted
    attribute values.

    Examples of attribute: "attr1,attr2", "attr1.inner1.0,attr2.inner2.0", etc.
    '''
def do_forceescape(value: str | HasHTML) -> Markup:
    """Enforce HTML escaping.  This will probably double escape variables."""
def do_urlencode(value: str | t.Mapping[str, t.Any] | t.Iterable[t.Tuple[str, t.Any]]) -> str:
    '''Quote data for use in a URL path or query using UTF-8.

    Basic wrapper around :func:`urllib.parse.quote` when given a
    string, or :func:`urllib.parse.urlencode` for a dict or iterable.

    :param value: Data to quote. A string will be quoted directly. A
        dict or iterable of ``(key, value)`` pairs will be joined as a
        query string.

    When given a string, "/" is not quoted. HTTP servers treat "/" and
    "%2F" equivalently in paths. If you need quoted slashes, use the
    ``|replace("/", "%2F")`` filter.

    .. versionadded:: 2.7
    '''
def do_replace(eval_ctx: EvalContext, s: str, old: str, new: str, count: int | None = None) -> str:
    '''Return a copy of the value with all occurrences of a substring
    replaced with a new one. The first argument is the substring
    that should be replaced, the second is the replacement string.
    If the optional third argument ``count`` is given, only the first
    ``count`` occurrences are replaced:

    .. sourcecode:: jinja

        {{ "Hello World"|replace("Hello", "Goodbye") }}
            -> Goodbye World

        {{ "aaaaargh"|replace("a", "d\'oh, ", 2) }}
            -> d\'oh, d\'oh, aaargh
    '''
def do_upper(s: str) -> str:
    """Convert a value to uppercase."""
def do_lower(s: str) -> str:
    """Convert a value to lowercase."""
def do_items(value: t.Mapping[K, V] | Undefined) -> t.Iterator[t.Tuple[K, V]]:
    """Return an iterator over the ``(key, value)`` items of a mapping.

    ``x|items`` is the same as ``x.items()``, except if ``x`` is
    undefined an empty iterator is returned.

    This filter is useful if you expect the template to be rendered with
    an implementation of Jinja in another programming language that does
    not have a ``.items()`` method on its mapping type.

    .. code-block:: html+jinja

        <dl>
        {% for key, value in my_dict|items %}
            <dt>{{ key }}
            <dd>{{ value }}
        {% endfor %}
        </dl>

    .. versionadded:: 3.1
    """
def do_xmlattr(eval_ctx: EvalContext, d: t.Mapping[str, t.Any], autospace: bool = True) -> str:
    '''Create an SGML/XML attribute string based on the items in a dict.
    All values that are neither `none` nor `undefined` are automatically
    escaped:

    .. sourcecode:: html+jinja

        <ul{{ {\'class\': \'my_list\', \'missing\': none,
                \'id\': \'list-%d\'|format(variable)}|xmlattr }}>
        ...
        </ul>

    Results in something like this:

    .. sourcecode:: html

        <ul class="my_list" id="list-42">
        ...
        </ul>

    As you can see it automatically prepends a space in front of the item
    if the filter returned something unless the second parameter is false.
    '''
def do_capitalize(s: str) -> str:
    """Capitalize a value. The first character will be uppercase, all others
    lowercase.
    """
def do_title(s: str) -> str:
    """Return a titlecased version of the value. I.e. words will start with
    uppercase letters, all remaining characters are lowercase.
    """
def do_dictsort(value: t.Mapping[K, V], case_sensitive: bool = False, by: te.Literal['key', 'value'] = 'key', reverse: bool = False) -> t.List[t.Tuple[K, V]]:
    """Sort a dict and yield (key, value) pairs. Python dicts may not
    be in the order you want to display them in, so sort them first.

    .. sourcecode:: jinja

        {% for key, value in mydict|dictsort %}
            sort the dict by key, case insensitive

        {% for key, value in mydict|dictsort(reverse=true) %}
            sort the dict by key, case insensitive, reverse order

        {% for key, value in mydict|dictsort(true) %}
            sort the dict by key, case sensitive

        {% for key, value in mydict|dictsort(false, 'value') %}
            sort the dict by value, case insensitive
    """
def do_sort(environment: Environment, value: t.Iterable[V], reverse: bool = False, case_sensitive: bool = False, attribute: str | int | None = None) -> t.List[V]:
    '''Sort an iterable using Python\'s :func:`sorted`.

    .. sourcecode:: jinja

        {% for city in cities|sort %}
            ...
        {% endfor %}

    :param reverse: Sort descending instead of ascending.
    :param case_sensitive: When sorting strings, sort upper and lower
        case separately.
    :param attribute: When sorting objects or dicts, an attribute or
        key to sort by. Can use dot notation like ``"address.city"``.
        Can be a list of attributes like ``"age,name"``.

    The sort is stable, it does not change the relative order of
    elements that compare equal. This makes it is possible to chain
    sorts on different attributes and ordering.

    .. sourcecode:: jinja

        {% for user in users|sort(attribute="name")
            |sort(reverse=true, attribute="age") %}
            ...
        {% endfor %}

    As a shortcut to chaining when the direction is the same for all
    attributes, pass a comma separate list of attributes.

    .. sourcecode:: jinja

        {% for user in users|sort(attribute="age,name") %}
            ...
        {% endfor %}

    .. versionchanged:: 2.11.0
        The ``attribute`` parameter can be a comma separated list of
        attributes, e.g. ``"age,name"``.

    .. versionchanged:: 2.6
       The ``attribute`` parameter was added.
    '''
def do_unique(environment: Environment, value: t.Iterable[V], case_sensitive: bool = False, attribute: str | int | None = None) -> t.Iterator[V]:
    """Returns a list of unique items from the given iterable.

    .. sourcecode:: jinja

        {{ ['foo', 'bar', 'foobar', 'FooBar']|unique|list }}
            -> ['foo', 'bar', 'foobar']

    The unique items are yielded in the same order as their first occurrence in
    the iterable passed to the filter.

    :param case_sensitive: Treat upper and lower case strings as distinct.
    :param attribute: Filter objects with unique values for this attribute.
    """
def do_min(environment: Environment, value: t.Iterable[V], case_sensitive: bool = False, attribute: str | int | None = None) -> V | Undefined:
    """Return the smallest item from the sequence.

    .. sourcecode:: jinja

        {{ [1, 2, 3]|min }}
            -> 1

    :param case_sensitive: Treat upper and lower case strings as distinct.
    :param attribute: Get the object with the min value of this attribute.
    """
def do_max(environment: Environment, value: t.Iterable[V], case_sensitive: bool = False, attribute: str | int | None = None) -> V | Undefined:
    """Return the largest item from the sequence.

    .. sourcecode:: jinja

        {{ [1, 2, 3]|max }}
            -> 3

    :param case_sensitive: Treat upper and lower case strings as distinct.
    :param attribute: Get the object with the max value of this attribute.
    """
def do_default(value: V, default_value: V = '', boolean: bool = False) -> V:
    """If the value is undefined it will return the passed default value,
    otherwise the value of the variable:

    .. sourcecode:: jinja

        {{ my_variable|default('my_variable is not defined') }}

    This will output the value of ``my_variable`` if the variable was
    defined, otherwise ``'my_variable is not defined'``. If you want
    to use default with variables that evaluate to false you have to
    set the second parameter to `true`:

    .. sourcecode:: jinja

        {{ ''|default('the string was empty', true) }}

    .. versionchanged:: 2.11
       It's now possible to configure the :class:`~jinja2.Environment` with
       :class:`~jinja2.ChainableUndefined` to make the `default` filter work
       on nested elements and attributes that may contain undefined values
       in the chain without getting an :exc:`~jinja2.UndefinedError`.
    """
def sync_do_join(eval_ctx: EvalContext, value: t.Iterable, d: str = '', attribute: str | int | None = None) -> str:
    """Return a string which is the concatenation of the strings in the
    sequence. The separator between elements is an empty string per
    default, you can define it with the optional parameter:

    .. sourcecode:: jinja

        {{ [1, 2, 3]|join('|') }}
            -> 1|2|3

        {{ [1, 2, 3]|join }}
            -> 123

    It is also possible to join certain attributes of an object:

    .. sourcecode:: jinja

        {{ users|join(', ', attribute='username') }}

    .. versionadded:: 2.6
       The `attribute` parameter was added.
    """
async def do_join(eval_ctx: EvalContext, value: t.AsyncIterable | t.Iterable, d: str = '', attribute: str | int | None = None) -> str: ...
def do_center(value: str, width: int = 80) -> str:
    """Centers the value in a field of a given width."""
def sync_do_first(environment: Environment, seq: t.Iterable[V]) -> V | Undefined:
    """Return the first item of a sequence."""
async def do_first(environment: Environment, seq: t.AsyncIterable[V] | t.Iterable[V]) -> V | Undefined: ...
def do_last(environment: Environment, seq: t.Reversible[V]) -> V | Undefined:
    """Return the last item of a sequence.

    Note: Does not work with generators. You may want to explicitly
    convert it to a list:

    .. sourcecode:: jinja

        {{ data | selectattr('name', '==', 'Jinja') | list | last }}
    """
def do_random(context: Context, seq: t.Sequence[V]) -> V | Undefined:
    """Return a random item from the sequence."""
def do_filesizeformat(value: str | float | int, binary: bool = False) -> str:
    """Format the value like a 'human-readable' file size (i.e. 13 kB,
    4.1 MB, 102 Bytes, etc).  Per default decimal prefixes are used (Mega,
    Giga, etc.), if the second parameter is set to `True` the binary
    prefixes are used (Mebi, Gibi).
    """
def do_pprint(value: t.Any) -> str:
    """Pretty print a variable. Useful for debugging."""
def do_urlize(eval_ctx: EvalContext, value: str, trim_url_limit: int | None = None, nofollow: bool = False, target: str | None = None, rel: str | None = None, extra_schemes: t.Iterable[str] | None = None) -> str:
    '''Convert URLs in text into clickable links.

    This may not recognize links in some situations. Usually, a more
    comprehensive formatter, such as a Markdown library, is a better
    choice.

    Works on ``http://``, ``https://``, ``www.``, ``mailto:``, and email
    addresses. Links with trailing punctuation (periods, commas, closing
    parentheses) and leading punctuation (opening parentheses) are
    recognized excluding the punctuation. Email addresses that include
    header fields are not recognized (for example,
    ``mailto:address@example.com?cc=copy@example.com``).

    :param value: Original text containing URLs to link.
    :param trim_url_limit: Shorten displayed URL values to this length.
    :param nofollow: Add the ``rel=nofollow`` attribute to links.
    :param target: Add the ``target`` attribute to links.
    :param rel: Add the ``rel`` attribute to links.
    :param extra_schemes: Recognize URLs that start with these schemes
        in addition to the default behavior. Defaults to
        ``env.policies["urlize.extra_schemes"]``, which defaults to no
        extra schemes.

    .. versionchanged:: 3.0
        The ``extra_schemes`` parameter was added.

    .. versionchanged:: 3.0
        Generate ``https://`` links for URLs without a scheme.

    .. versionchanged:: 3.0
        The parsing rules were updated. Recognize email addresses with
        or without the ``mailto:`` scheme. Validate IP addresses. Ignore
        parentheses and brackets in more cases.

    .. versionchanged:: 2.8
       The ``target`` parameter was added.
    '''
def do_indent(s: str, width: int | str = 4, first: bool = False, blank: bool = False) -> str:
    """Return a copy of the string with each line indented by 4 spaces. The
    first line and blank lines are not indented by default.

    :param width: Number of spaces, or a string, to indent by.
    :param first: Don't skip indenting the first line.
    :param blank: Don't skip indenting empty lines.

    .. versionchanged:: 3.0
        ``width`` can be a string.

    .. versionchanged:: 2.10
        Blank lines are not indented by default.

        Rename the ``indentfirst`` argument to ``first``.
    """
def do_truncate(env: Environment, s: str, length: int = 255, killwords: bool = False, end: str = '...', leeway: int | None = None) -> str:
    '''Return a truncated copy of the string. The length is specified
    with the first parameter which defaults to ``255``. If the second
    parameter is ``true`` the filter will cut the text at length. Otherwise
    it will discard the last word. If the text was in fact
    truncated it will append an ellipsis sign (``"..."``). If you want a
    different ellipsis sign than ``"..."`` you can specify it using the
    third parameter. Strings that only exceed the length by the tolerance
    margin given in the fourth parameter will not be truncated.

    .. sourcecode:: jinja

        {{ "foo bar baz qux"|truncate(9) }}
            -> "foo..."
        {{ "foo bar baz qux"|truncate(9, True) }}
            -> "foo ba..."
        {{ "foo bar baz qux"|truncate(11) }}
            -> "foo bar baz qux"
        {{ "foo bar baz qux"|truncate(11, False, \'...\', 0) }}
            -> "foo bar..."

    The default leeway on newer Jinja versions is 5 and was 0 before but
    can be reconfigured globally.
    '''
def do_wordwrap(environment: Environment, s: str, width: int = 79, break_long_words: bool = True, wrapstring: str | None = None, break_on_hyphens: bool = True) -> str:
    """Wrap a string to the given width. Existing newlines are treated
    as paragraphs to be wrapped separately.

    :param s: Original text to wrap.
    :param width: Maximum length of wrapped lines.
    :param break_long_words: If a word is longer than ``width``, break
        it across lines.
    :param break_on_hyphens: If a word contains hyphens, it may be split
        across lines.
    :param wrapstring: String to join each wrapped line. Defaults to
        :attr:`Environment.newline_sequence`.

    .. versionchanged:: 2.11
        Existing newlines are treated as paragraphs wrapped separately.

    .. versionchanged:: 2.11
        Added the ``break_on_hyphens`` parameter.

    .. versionchanged:: 2.7
        Added the ``wrapstring`` parameter.
    """
def do_wordcount(s: str) -> int:
    """Count the words in that string."""
def do_int(value: t.Any, default: int = 0, base: int = 10) -> int:
    """Convert the value into an integer. If the
    conversion doesn't work it will return ``0``. You can
    override this default using the first parameter. You
    can also override the default base (10) in the second
    parameter, which handles input with prefixes such as
    0b, 0o and 0x for bases 2, 8 and 16 respectively.
    The base is ignored for decimal numbers and non-string values.
    """
def do_float(value: t.Any, default: float = 0.0) -> float:
    """Convert the value into a floating point number. If the
    conversion doesn't work it will return ``0.0``. You can
    override this default using the first parameter.
    """
def do_format(value: str, *args: t.Any, **kwargs: t.Any) -> str:
    '''Apply the given values to a `printf-style`_ format string, like
    ``string % values``.

    .. sourcecode:: jinja

        {{ "%s, %s!"|format(greeting, name) }}
        Hello, World!

    In most cases it should be more convenient and efficient to use the
    ``%`` operator or :meth:`str.format`.

    .. code-block:: text

        {{ "%s, %s!" % (greeting, name) }}
        {{ "{}, {}!".format(greeting, name) }}

    .. _printf-style: https://docs.python.org/library/stdtypes.html
        #printf-style-string-formatting
    '''
def do_trim(value: str, chars: str | None = None) -> str:
    """Strip leading and trailing characters, by default whitespace."""
def do_striptags(value: str | HasHTML) -> str:
    """Strip SGML/XML tags and replace adjacent whitespace by one space."""
def sync_do_slice(value: t.Collection[V], slices: int, fill_with: V | None = None) -> t.Iterator[t.List[V]]:
    '''Slice an iterator and return a list of lists containing
    those items. Useful if you want to create a div containing
    three ul tags that represent columns:

    .. sourcecode:: html+jinja

        <div class="columnwrapper">
          {%- for column in items|slice(3) %}
            <ul class="column-{{ loop.index }}">
            {%- for item in column %}
              <li>{{ item }}</li>
            {%- endfor %}
            </ul>
          {%- endfor %}
        </div>

    If you pass it a second argument it\'s used to fill missing
    values on the last iteration.
    '''
async def do_slice(value: t.AsyncIterable[V] | t.Iterable[V], slices: int, fill_with: t.Any | None = None) -> t.Iterator[t.List[V]]: ...
def do_batch(value: t.Iterable[V], linecount: int, fill_with: V | None = None) -> t.Iterator[t.List[V]]:
    """
    A filter that batches items. It works pretty much like `slice`
    just the other way round. It returns a list of lists with the
    given number of items. If you provide a second parameter this
    is used to fill up missing items. See this example:

    .. sourcecode:: html+jinja

        <table>
        {%- for row in items|batch(3, '&nbsp;') %}
          <tr>
          {%- for column in row %}
            <td>{{ column }}</td>
          {%- endfor %}
          </tr>
        {%- endfor %}
        </table>
    """
def do_round(value: float, precision: int = 0, method: te.Literal['common', 'ceil', 'floor'] = 'common') -> float:
    """Round the number to a given precision. The first
    parameter specifies the precision (default is ``0``), the
    second the rounding method:

    - ``'common'`` rounds either up or down
    - ``'ceil'`` always rounds up
    - ``'floor'`` always rounds down

    If you don't specify a method ``'common'`` is used.

    .. sourcecode:: jinja

        {{ 42.55|round }}
            -> 43.0
        {{ 42.55|round(1, 'floor') }}
            -> 42.5

    Note that even if rounded to 0 precision, a float is returned.  If
    you need a real integer, pipe it through `int`:

    .. sourcecode:: jinja

        {{ 42.55|round|int }}
            -> 43
    """

class _GroupTuple(t.NamedTuple):
    grouper: t.Any
    list: t.List

def sync_do_groupby(environment: Environment, value: t.Iterable[V], attribute: str | int, default: t.Any | None = None, case_sensitive: bool = False) -> t.List[_GroupTuple]:
    '''Group a sequence of objects by an attribute using Python\'s
    :func:`itertools.groupby`. The attribute can use dot notation for
    nested access, like ``"address.city"``. Unlike Python\'s ``groupby``,
    the values are sorted first so only one group is returned for each
    unique value.

    For example, a list of ``User`` objects with a ``city`` attribute
    can be rendered in groups. In this example, ``grouper`` refers to
    the ``city`` value of the group.

    .. sourcecode:: html+jinja

        <ul>{% for city, items in users|groupby("city") %}
          <li>{{ city }}
            <ul>{% for user in items %}
              <li>{{ user.name }}
            {% endfor %}</ul>
          </li>
        {% endfor %}</ul>

    ``groupby`` yields namedtuples of ``(grouper, list)``, which
    can be used instead of the tuple unpacking above. ``grouper`` is the
    value of the attribute, and ``list`` is the items with that value.

    .. sourcecode:: html+jinja

        <ul>{% for group in users|groupby("city") %}
          <li>{{ group.grouper }}: {{ group.list|join(", ") }}
        {% endfor %}</ul>

    You can specify a ``default`` value to use if an object in the list
    does not have the given attribute.

    .. sourcecode:: jinja

        <ul>{% for city, items in users|groupby("city", default="NY") %}
          <li>{{ city }}: {{ items|map(attribute="name")|join(", ") }}</li>
        {% endfor %}</ul>

    Like the :func:`~jinja-filters.sort` filter, sorting and grouping is
    case-insensitive by default. The ``key`` for each group will have
    the case of the first item in that group of values. For example, if
    a list of users has cities ``["CA", "NY", "ca"]``, the "CA" group
    will have two values. This can be disabled by passing
    ``case_sensitive=True``.

    .. versionchanged:: 3.1
        Added the ``case_sensitive`` parameter. Sorting and grouping is
        case-insensitive by default, matching other filters that do
        comparisons.

    .. versionchanged:: 3.0
        Added the ``default`` parameter.

    .. versionchanged:: 2.6
        The attribute supports dot notation for nested access.
    '''
async def do_groupby(environment: Environment, value: t.AsyncIterable[V] | t.Iterable[V], attribute: str | int, default: t.Any | None = None, case_sensitive: bool = False) -> t.List[_GroupTuple]: ...
def sync_do_sum(environment: Environment, iterable: t.Iterable[V], attribute: str | int | None = None, start: V = 0) -> V:
    """Returns the sum of a sequence of numbers plus the value of parameter
    'start' (which defaults to 0).  When the sequence is empty it returns
    start.

    It is also possible to sum up only certain attributes:

    .. sourcecode:: jinja

        Total: {{ items|sum(attribute='price') }}

    .. versionchanged:: 2.6
       The ``attribute`` parameter was added to allow summing up over
       attributes.  Also the ``start`` parameter was moved on to the right.
    """
async def do_sum(environment: Environment, iterable: t.AsyncIterable[V] | t.Iterable[V], attribute: str | int | None = None, start: V = 0) -> V: ...
def sync_do_list(value: t.Iterable[V]) -> t.List[V]:
    """Convert the value into a list.  If it was a string the returned list
    will be a list of characters.
    """
async def do_list(value: t.AsyncIterable[V] | t.Iterable[V]) -> t.List[V]: ...
def do_mark_safe(value: str) -> Markup:
    """Mark the value as safe which means that in an environment with automatic
    escaping enabled this variable will not be escaped.
    """
def do_mark_unsafe(value: str) -> str:
    """Mark a value as unsafe.  This is the reverse operation for :func:`safe`."""
@typing.overload
def do_reverse(value: str) -> str: ...
@typing.overload
def do_reverse(value: t.Iterable[V]) -> t.Iterable[V]: ...
def do_attr(environment: Environment, obj: t.Any, name: str) -> Undefined | t.Any:
    '''Get an attribute of an object.  ``foo|attr("bar")`` works like
    ``foo.bar`` just that always an attribute is returned and items are not
    looked up.

    See :ref:`Notes on subscriptions <notes-on-subscriptions>` for more details.
    '''
@typing.overload
def sync_do_map(context: Context, value: t.Iterable, name: str, *args: t.Any, **kwargs: t.Any) -> t.Iterable: ...
@typing.overload
def sync_do_map(context: Context, value: t.Iterable, *, attribute: str = ..., default: t.Any | None = None) -> t.Iterable: ...
@typing.overload
def do_map(context: Context, value: t.AsyncIterable | t.Iterable, name: str, *args: t.Any, **kwargs: t.Any) -> t.Iterable: ...
@typing.overload
def do_map(context: Context, value: t.AsyncIterable | t.Iterable, *, attribute: str = ..., default: t.Any | None = None) -> t.Iterable: ...
def sync_do_select(context: Context, value: t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.Iterator[V]:
    '''Filters a sequence of objects by applying a test to each object,
    and only selecting the objects with the test succeeding.

    If no test is specified, each object will be evaluated as a boolean.

    Example usage:

    .. sourcecode:: jinja

        {{ numbers|select("odd") }}
        {{ numbers|select("odd") }}
        {{ numbers|select("divisibleby", 3) }}
        {{ numbers|select("lessthan", 42) }}
        {{ strings|select("equalto", "mystring") }}

    Similar to a generator comprehension such as:

    .. code-block:: python

        (n for n in numbers if test_odd(n))
        (n for n in numbers if test_divisibleby(n, 3))

    .. versionadded:: 2.7
    '''
async def do_select(context: Context, value: t.AsyncIterable[V] | t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.AsyncIterator[V]: ...
def sync_do_reject(context: Context, value: t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.Iterator[V]:
    '''Filters a sequence of objects by applying a test to each object,
    and rejecting the objects with the test succeeding.

    If no test is specified, each object will be evaluated as a boolean.

    Example usage:

    .. sourcecode:: jinja

        {{ numbers|reject("odd") }}

    Similar to a generator comprehension such as:

    .. code-block:: python

        (n for n in numbers if not test_odd(n))

    .. versionadded:: 2.7
    '''
async def do_reject(context: Context, value: t.AsyncIterable[V] | t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.AsyncIterator[V]: ...
def sync_do_selectattr(context: Context, value: t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.Iterator[V]:
    '''Filters a sequence of objects by applying a test to the specified
    attribute of each object, and only selecting the objects with the
    test succeeding.

    If no test is specified, the attribute\'s value will be evaluated as
    a boolean.

    Example usage:

    .. sourcecode:: jinja

        {{ users|selectattr("is_active") }}
        {{ users|selectattr("email", "none") }}

    Similar to a generator comprehension such as:

    .. code-block:: python

        (u for user in users if user.is_active)
        (u for user in users if test_none(user.email))

    .. versionadded:: 2.7
    '''
async def do_selectattr(context: Context, value: t.AsyncIterable[V] | t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.AsyncIterator[V]: ...
def sync_do_rejectattr(context: Context, value: t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.Iterator[V]:
    '''Filters a sequence of objects by applying a test to the specified
    attribute of each object, and rejecting the objects with the test
    succeeding.

    If no test is specified, the attribute\'s value will be evaluated as
    a boolean.

    .. sourcecode:: jinja

        {{ users|rejectattr("is_active") }}
        {{ users|rejectattr("email", "none") }}

    Similar to a generator comprehension such as:

    .. code-block:: python

        (u for user in users if not user.is_active)
        (u for user in users if not test_none(user.email))

    .. versionadded:: 2.7
    '''
async def do_rejectattr(context: Context, value: t.AsyncIterable[V] | t.Iterable[V], *args: t.Any, **kwargs: t.Any) -> t.AsyncIterator[V]: ...
def do_tojson(eval_ctx: EvalContext, value: t.Any, indent: int | None = None) -> Markup:
    """Serialize an object to a string of JSON, and mark it safe to
    render in HTML. This filter is only for use in HTML documents.

    The returned string is safe to render in HTML documents and
    ``<script>`` tags. The exception is in HTML attributes that are
    double quoted; either use single quotes or the ``|forceescape``
    filter.

    :param value: The object to serialize to JSON.
    :param indent: The ``indent`` parameter passed to ``dumps``, for
        pretty-printing the value.

    .. versionadded:: 2.9
    """
def prepare_map(context: Context, args: t.Tuple, kwargs: t.Dict[str, t.Any]) -> t.Callable[[t.Any], t.Any]: ...
def prepare_select_or_reject(context: Context, args: t.Tuple, kwargs: t.Dict[str, t.Any], modfunc: t.Callable[[t.Any], t.Any], lookup_attr: bool) -> t.Callable[[t.Any], t.Any]: ...
def select_or_reject(context: Context, value: t.Iterable[V], args: t.Tuple, kwargs: t.Dict[str, t.Any], modfunc: t.Callable[[t.Any], t.Any], lookup_attr: bool) -> t.Iterator[V]: ...
async def async_select_or_reject(context: Context, value: t.AsyncIterable[V] | t.Iterable[V], args: t.Tuple, kwargs: t.Dict[str, t.Any], modfunc: t.Callable[[t.Any], t.Any], lookup_attr: bool) -> t.AsyncIterator[V]: ...

FILTERS: Incomplete
