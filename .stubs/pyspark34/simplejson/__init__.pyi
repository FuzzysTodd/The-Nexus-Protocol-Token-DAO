from .decoder import JSONDecoder as JSONDecoder
from .encoder import JSONEncoder as JSONEncoder
from .errors import JSONDecodeError as JSONDecodeError
from .raw_json import RawJSON as RawJSON
from _typeshed import Incomplete

__all__ = ['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecodeError', 'JSONEncoder', 'OrderedDict', 'simple_first', 'RawJSON']

OrderedDict: Incomplete

def dump(obj, fp, skipkeys: bool = False, ensure_ascii: bool = True, check_circular: bool = True, allow_nan: bool = False, cls: Incomplete | None = None, indent: Incomplete | None = None, separators: Incomplete | None = None, encoding: str = 'utf-8', default: Incomplete | None = None, use_decimal: bool = True, namedtuple_as_object: bool = True, tuple_as_array: bool = True, bigint_as_string: bool = False, sort_keys: bool = False, item_sort_key: Incomplete | None = None, for_json: bool = False, ignore_nan: bool = False, int_as_string_bitcount: Incomplete | None = None, iterable_as_array: bool = False, **kw) -> None:
    """Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).

    If *skipkeys* is true then ``dict`` keys that are not basic types
    (``str``, ``int``, ``long``, ``float``, ``bool``, ``None``)
    will be skipped instead of raising a ``TypeError``.

    If *ensure_ascii* is false (default: ``True``), then the output may
    contain non-ASCII characters, so long as they do not need to be escaped
    by JSON. When it is true, all non-ASCII characters are escaped.

    If *allow_nan* is true (default: ``False``), then out of range ``float``
    values (``nan``, ``inf``, ``-inf``) will be serialized to
    their JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``)
    instead of raising a ValueError. See
    *ignore_nan* for ECMA-262 compliant behavior.

    If *indent* is a string, then JSON array elements and object members
    will be pretty-printed with a newline followed by that string repeated
    for each level of nesting. ``None`` (the default) selects the most compact
    representation without any newlines.

    If specified, *separators* should be an
    ``(item_separator, key_separator)`` tuple.  The default is ``(', ', ': ')``
    if *indent* is ``None`` and ``(',', ': ')`` otherwise.  To get the most
    compact JSON representation, you should specify ``(',', ':')`` to eliminate
    whitespace.

    *encoding* is the character encoding for str instances, default is UTF-8.

    *default(obj)* is a function that should return a serializable version
    of obj or raise ``TypeError``. The default simply raises ``TypeError``.

    If *use_decimal* is true (default: ``True``) then decimal.Decimal
    will be natively serialized to JSON with full precision.

    If *namedtuple_as_object* is true (default: ``True``),
    :class:`tuple` subclasses with ``_asdict()`` methods will be encoded
    as JSON objects.

    If *tuple_as_array* is true (default: ``True``),
    :class:`tuple` (and subclasses) will be encoded as JSON arrays.

    If *iterable_as_array* is true (default: ``False``),
    any object not in the above table that implements ``__iter__()``
    will be encoded as a JSON array.

    If *bigint_as_string* is true (default: ``False``), ints 2**53 and higher
    or lower than -2**53 will be encoded as strings. This is to avoid the
    rounding that happens in Javascript otherwise. Note that this is still a
    lossy operation that will not round-trip correctly and should be used
    sparingly.

    If *int_as_string_bitcount* is a positive number (n), then int of size
    greater than or equal to 2**n or lower than or equal to -2**n will be
    encoded as strings.

    If specified, *item_sort_key* is a callable used to sort the items in
    each dictionary. This is useful if you want to sort items other than
    in alphabetical order by key. This option takes precedence over
    *sort_keys*.

    If *sort_keys* is true (default: ``False``), the output of dictionaries
    will be sorted by item.

    If *for_json* is true (default: ``False``), objects with a ``for_json()``
    method will use the return value of that method for encoding as JSON
    instead of the object.

    If *ignore_nan* is true (default: ``False``), then out of range
    :class:`float` values (``nan``, ``inf``, ``-inf``) will be serialized as
    ``null`` in compliance with the ECMA-262 specification. If true, this will
    override *allow_nan*.

    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg. NOTE: You should use *default* or *for_json* instead
    of subclassing whenever possible.

    """
def dumps(obj, skipkeys: bool = False, ensure_ascii: bool = True, check_circular: bool = True, allow_nan: bool = False, cls: Incomplete | None = None, indent: Incomplete | None = None, separators: Incomplete | None = None, encoding: str = 'utf-8', default: Incomplete | None = None, use_decimal: bool = True, namedtuple_as_object: bool = True, tuple_as_array: bool = True, bigint_as_string: bool = False, sort_keys: bool = False, item_sort_key: Incomplete | None = None, for_json: bool = False, ignore_nan: bool = False, int_as_string_bitcount: Incomplete | None = None, iterable_as_array: bool = False, **kw):
    """Serialize ``obj`` to a JSON formatted ``str``.

    If ``skipkeys`` is true then ``dict`` keys that are not basic types
    (``str``, ``int``, ``long``, ``float``, ``bool``, ``None``)
    will be skipped instead of raising a ``TypeError``.

    If *ensure_ascii* is false (default: ``True``), then the output may
    contain non-ASCII characters, so long as they do not need to be escaped
    by JSON. When it is true, all non-ASCII characters are escaped.

    If ``check_circular`` is false, then the circular reference check
    for container types will be skipped and a circular reference will
    result in an ``OverflowError`` (or worse).

    If *allow_nan* is true (default: ``False``), then out of range ``float``
    values (``nan``, ``inf``, ``-inf``) will be serialized to
    their JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``)
    instead of raising a ValueError. See
    *ignore_nan* for ECMA-262 compliant behavior.

    If ``indent`` is a string, then JSON array elements and object members
    will be pretty-printed with a newline followed by that string repeated
    for each level of nesting. ``None`` (the default) selects the most compact
    representation without any newlines. For backwards compatibility with
    versions of simplejson earlier than 2.1.0, an integer is also accepted
    and is converted to a string with that many spaces.

    If specified, ``separators`` should be an
    ``(item_separator, key_separator)`` tuple.  The default is ``(', ', ': ')``
    if *indent* is ``None`` and ``(',', ': ')`` otherwise.  To get the most
    compact JSON representation, you should specify ``(',', ':')`` to eliminate
    whitespace.

    ``encoding`` is the character encoding for bytes instances, default is
    UTF-8.

    ``default(obj)`` is a function that should return a serializable version
    of obj or raise TypeError. The default simply raises TypeError.

    If *use_decimal* is true (default: ``True``) then decimal.Decimal
    will be natively serialized to JSON with full precision.

    If *namedtuple_as_object* is true (default: ``True``),
    :class:`tuple` subclasses with ``_asdict()`` methods will be encoded
    as JSON objects.

    If *tuple_as_array* is true (default: ``True``),
    :class:`tuple` (and subclasses) will be encoded as JSON arrays.

    If *iterable_as_array* is true (default: ``False``),
    any object not in the above table that implements ``__iter__()``
    will be encoded as a JSON array.

    If *bigint_as_string* is true (not the default), ints 2**53 and higher
    or lower than -2**53 will be encoded as strings. This is to avoid the
    rounding that happens in Javascript otherwise.

    If *int_as_string_bitcount* is a positive number (n), then int of size
    greater than or equal to 2**n or lower than or equal to -2**n will be
    encoded as strings.

    If specified, *item_sort_key* is a callable used to sort the items in
    each dictionary. This is useful if you want to sort items other than
    in alphabetical order by key. This option takes precedence over
    *sort_keys*.

    If *sort_keys* is true (default: ``False``), the output of dictionaries
    will be sorted by item.

    If *for_json* is true (default: ``False``), objects with a ``for_json()``
    method will use the return value of that method for encoding as JSON
    instead of the object.

    If *ignore_nan* is true (default: ``False``), then out of range
    :class:`float` values (``nan``, ``inf``, ``-inf``) will be serialized as
    ``null`` in compliance with the ECMA-262 specification. If true, this will
    override *allow_nan*.

    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg. NOTE: You should use *default* instead of subclassing
    whenever possible.

    """
def load(fp, encoding: Incomplete | None = None, cls: Incomplete | None = None, object_hook: Incomplete | None = None, parse_float: Incomplete | None = None, parse_int: Incomplete | None = None, parse_constant: Incomplete | None = None, object_pairs_hook: Incomplete | None = None, use_decimal: bool = False, allow_nan: bool = False, **kw):
    """Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
    a JSON document as `str` or `bytes`) to a Python object.

    *encoding* determines the encoding used to interpret any
    `bytes` objects decoded by this instance (``'utf-8'`` by
    default). It has no effect when decoding `str` objects.

    *object_hook*, if specified, will be called with the result of every
    JSON object decoded and its return value will be used in place of the
    given :class:`dict`.  This can be used to provide custom
    deserializations (e.g. to support JSON-RPC class hinting).

    *object_pairs_hook* is an optional function that will be called with
    the result of any object literal decode with an ordered list of pairs.
    The return value of *object_pairs_hook* will be used instead of the
    :class:`dict`.  This feature can be used to implement custom decoders
    that rely on the order that the key and value pairs are decoded (for
    example, :func:`collections.OrderedDict` will remember the order of
    insertion). If *object_hook* is also defined, the *object_pairs_hook*
    takes priority.

    *parse_float*, if specified, will be called with the string of every
    JSON float to be decoded. By default, this is equivalent to
    ``float(num_str)``. This can be used to use another datatype or parser
    for JSON floats (e.g. :class:`decimal.Decimal`).

    *parse_int*, if specified, will be called with the string of every
    JSON int to be decoded. By default, this is equivalent to
    ``int(num_str)``.  This can be used to use another datatype or parser
    for JSON integers (e.g. :class:`float`).

    *allow_nan*, if True (default false), will allow the parser to
    accept the non-standard floats ``NaN``, ``Infinity``, and ``-Infinity``
    and enable the use of the deprecated *parse_constant*.

    If *use_decimal* is true (default: ``False``) then it implies
    parse_float=decimal.Decimal for parity with ``dump``.

    *parse_constant*, if specified, will be
    called with one of the following strings: ``'-Infinity'``,
    ``'Infinity'``, ``'NaN'``. It is not recommended to use this feature,
    as it is rare to parse non-compliant JSON containing these values.

    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg. NOTE: You should use *object_hook* or *object_pairs_hook* instead
    of subclassing whenever possible.

    """
def loads(s, encoding: Incomplete | None = None, cls: Incomplete | None = None, object_hook: Incomplete | None = None, parse_float: Incomplete | None = None, parse_int: Incomplete | None = None, parse_constant: Incomplete | None = None, object_pairs_hook: Incomplete | None = None, use_decimal: bool = False, allow_nan: bool = False, **kw):
    """Deserialize ``s`` (a ``str`` or ``unicode`` instance containing a JSON
    document) to a Python object.

    *encoding* determines the encoding used to interpret any
    :class:`bytes` objects decoded by this instance (``'utf-8'`` by
    default). It has no effect when decoding :class:`unicode` objects.

    *object_hook*, if specified, will be called with the result of every
    JSON object decoded and its return value will be used in place of the
    given :class:`dict`.  This can be used to provide custom
    deserializations (e.g. to support JSON-RPC class hinting).

    *object_pairs_hook* is an optional function that will be called with
    the result of any object literal decode with an ordered list of pairs.
    The return value of *object_pairs_hook* will be used instead of the
    :class:`dict`.  This feature can be used to implement custom decoders
    that rely on the order that the key and value pairs are decoded (for
    example, :func:`collections.OrderedDict` will remember the order of
    insertion). If *object_hook* is also defined, the *object_pairs_hook*
    takes priority.

    *parse_float*, if specified, will be called with the string of every
    JSON float to be decoded.  By default, this is equivalent to
    ``float(num_str)``. This can be used to use another datatype or parser
    for JSON floats (e.g. :class:`decimal.Decimal`).

    *parse_int*, if specified, will be called with the string of every
    JSON int to be decoded.  By default, this is equivalent to
    ``int(num_str)``.  This can be used to use another datatype or parser
    for JSON integers (e.g. :class:`float`).

    *allow_nan*, if True (default false), will allow the parser to
    accept the non-standard floats ``NaN``, ``Infinity``, and ``-Infinity``
    and enable the use of the deprecated *parse_constant*.

    If *use_decimal* is true (default: ``False``) then it implies
    parse_float=decimal.Decimal for parity with ``dump``.

    *parse_constant*, if specified, will be
    called with one of the following strings: ``'-Infinity'``,
    ``'Infinity'``, ``'NaN'``. It is not recommended to use this feature,
    as it is rare to parse non-compliant JSON containing these values.

    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg. NOTE: You should use *object_hook* or *object_pairs_hook* instead
    of subclassing whenever possible.

    """
def simple_first(kv):
    """Helper function to pass to item_sort_key to sort simple
    elements to the top, then container elements.
    """
