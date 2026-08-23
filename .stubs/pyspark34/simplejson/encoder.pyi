from .compat import PY3 as PY3, binary_type as binary_type, integer_types as integer_types, string_types as string_types, text_type as text_type
from .decoder import PosInf as PosInf
from .raw_json import RawJSON as RawJSON
from _typeshed import Incomplete
from collections.abc import Generator

c_encode_basestring_ascii: Incomplete
c_make_encoder: Incomplete
ESCAPE: Incomplete
ESCAPE_ASCII: Incomplete
HAS_UTF8: Incomplete
ESCAPE_DCT: Incomplete
FLOAT_REPR = repr

def encode_basestring(s, _PY3=..., _q: str = '"'):
    """Return a JSON representation of a Python string

    """
def py_encode_basestring_ascii(s, _PY3=...):
    """Return an ASCII-only JSON representation of a Python string

    """

encode_basestring_ascii: Incomplete

class JSONEncoder:
    """Extensible JSON <http://json.org> encoder for Python data structures.

    Supports the following objects and types by default:

    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict, namedtuple  | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str, unicode      | string        |
    +-------------------+---------------+
    | int, long, float  | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+

    To extend this to recognize other objects, subclass and implement a
    ``.default()`` method with another method that returns a serializable
    object for ``o`` if possible, otherwise it should call the superclass
    implementation (to raise ``TypeError``).

    """
    item_separator: str
    key_separator: str
    skipkeys: Incomplete
    ensure_ascii: Incomplete
    check_circular: Incomplete
    allow_nan: Incomplete
    sort_keys: Incomplete
    use_decimal: Incomplete
    namedtuple_as_object: Incomplete
    tuple_as_array: Incomplete
    iterable_as_array: Incomplete
    bigint_as_string: Incomplete
    item_sort_key: Incomplete
    for_json: Incomplete
    ignore_nan: Incomplete
    int_as_string_bitcount: Incomplete
    indent: Incomplete
    encoding: Incomplete
    def __init__(self, skipkeys: bool = False, ensure_ascii: bool = True, check_circular: bool = True, allow_nan: bool = False, sort_keys: bool = False, indent: Incomplete | None = None, separators: Incomplete | None = None, encoding: str = 'utf-8', default: Incomplete | None = None, use_decimal: bool = True, namedtuple_as_object: bool = True, tuple_as_array: bool = True, bigint_as_string: bool = False, item_sort_key: Incomplete | None = None, for_json: bool = False, ignore_nan: bool = False, int_as_string_bitcount: Incomplete | None = None, iterable_as_array: bool = False) -> None:
        """Constructor for JSONEncoder, with sensible defaults.

        If skipkeys is false, then it is a TypeError to attempt
        encoding of keys that are not str, int, long, float or None.  If
        skipkeys is True, such items are simply skipped.

        If ensure_ascii is true, the output is guaranteed to be str
        objects with all incoming unicode characters escaped.  If
        ensure_ascii is false, the output will be unicode object.

        If check_circular is true, then lists, dicts, and custom encoded
        objects will be checked for circular references during encoding to
        prevent an infinite recursion (which would cause an OverflowError).
        Otherwise, no such check takes place.

        If allow_nan is true (default: False), then out of range float
        values (nan, inf, -inf) will be serialized to
        their JavaScript equivalents (NaN, Infinity, -Infinity)
        instead of raising a ValueError. See
        ignore_nan for ECMA-262 compliant behavior.

        If sort_keys is true, then the output of dictionaries will be
        sorted by key; this is useful for regression tests to ensure
        that JSON serializations can be compared on a day-to-day basis.

        If indent is a string, then JSON array elements and object members
        will be pretty-printed with a newline followed by that string repeated
        for each level of nesting. ``None`` (the default) selects the most compact
        representation without any newlines. For backwards compatibility with
        versions of simplejson earlier than 2.1.0, an integer is also accepted
        and is converted to a string with that many spaces.

        If specified, separators should be an (item_separator, key_separator)
        tuple.  The default is (', ', ': ') if *indent* is ``None`` and
        (',', ': ') otherwise.  To get the most compact JSON representation,
        you should specify (',', ':') to eliminate whitespace.

        If specified, default is a function that gets called for objects
        that can't otherwise be serialized.  It should return a JSON encodable
        version of the object or raise a ``TypeError``.

        If encoding is not None, then all input strings will be
        transformed into unicode using that encoding prior to JSON-encoding.
        The default is UTF-8.

        If use_decimal is true (default: ``True``), ``decimal.Decimal`` will
        be supported directly by the encoder. For the inverse, decode JSON
        with ``parse_float=decimal.Decimal``.

        If namedtuple_as_object is true (the default), objects with
        ``_asdict()`` methods will be encoded as JSON objects.

        If tuple_as_array is true (the default), tuple (and subclasses) will
        be encoded as JSON arrays.

        If *iterable_as_array* is true (default: ``False``),
        any object not in the above table that implements ``__iter__()``
        will be encoded as a JSON array.

        If bigint_as_string is true (not the default), ints 2**53 and higher
        or lower than -2**53 will be encoded as strings. This is to avoid the
        rounding that happens in Javascript otherwise.

        If int_as_string_bitcount is a positive number (n), then int of size
        greater than or equal to 2**n or lower than or equal to -2**n will be
        encoded as strings.

        If specified, item_sort_key is a callable used to sort the items in
        each dictionary. This is useful if you want to sort items other than
        in alphabetical order by key.

        If for_json is true (not the default), objects with a ``for_json()``
        method will use the return value of that method for encoding as JSON
        instead of the object.

        If *ignore_nan* is true (default: ``False``), then out of range
        :class:`float` values (``nan``, ``inf``, ``-inf``) will be serialized
        as ``null`` in compliance with the ECMA-262 specification. If true,
        this will override *allow_nan*.

        """
    def default(self, o) -> None:
        """Implement this method in a subclass such that it returns
        a serializable object for ``o``, or calls the base implementation
        (to raise a ``TypeError``).

        For example, to support arbitrary iterators, you could
        implement default like this::

            def default(self, o):
                try:
                    iterable = iter(o)
                except TypeError:
                    pass
                else:
                    return list(iterable)
                return JSONEncoder.default(self, o)

        """
    def encode(self, o):
        '''Return a JSON string representation of a Python data structure.

        >>> from simplejson import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        \'{"foo": ["bar", "baz"]}\'

        '''
    def iterencode(self, o):
        """Encode the given object and yield each string
        representation as available.

        For example::

            for chunk in JSONEncoder().iterencode(bigobject):
                mysocket.write(chunk)

        """

class JSONEncoderForHTML(JSONEncoder):
    """An encoder that produces JSON safe to embed in HTML.

    To embed JSON content in, say, a script tag on a web page, the
    characters &, < and > should be escaped. They cannot be escaped
    with the usual entities (e.g. &amp;) because they are not expanded
    within <script> tags.

    This class also escapes the line separator and paragraph separator
    characters U+2028 and U+2029, irrespective of the ensure_ascii setting,
    as these characters are not valid in JavaScript strings (see
    http://timelessrepo.com/json-isnt-a-javascript-subset).
    """
    def encode(self, o): ...
    def iterencode(self, o) -> Generator[Incomplete, None, None]: ...
