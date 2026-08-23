import typing as t
import uuid
from .map import Map as Map
from _typeshed import Incomplete

class ValidationError(ValueError):
    """Validation error.  If a rule converter raises this exception the rule
    does not match the current URL and the next URL is tried.
    """

class BaseConverter:
    """Base class for all converters.

    .. versionchanged:: 2.3
        ``part_isolating`` defaults to ``False`` if ``regex`` contains a ``/``.
    """
    regex: str
    weight: int
    part_isolating: bool
    def __init_subclass__(cls, **kwargs: t.Any) -> None: ...
    map: Incomplete
    def __init__(self, map: Map, *args: t.Any, **kwargs: t.Any) -> None: ...
    def to_python(self, value: str) -> t.Any: ...
    def to_url(self, value: t.Any) -> str: ...

class UnicodeConverter(BaseConverter):
    """This converter is the default converter and accepts any string but
    only one path segment.  Thus the string can not include a slash.

    This is the default validator.

    Example::

        Rule('/pages/<page>'),
        Rule('/<string(length=2):lang_code>')

    :param map: the :class:`Map`.
    :param minlength: the minimum length of the string.  Must be greater
                      or equal 1.
    :param maxlength: the maximum length of the string.
    :param length: the exact length of the string.
    """
    regex: Incomplete
    def __init__(self, map: Map, minlength: int = 1, maxlength: int | None = None, length: int | None = None) -> None: ...

class AnyConverter(BaseConverter):
    '''Matches one of the items provided.  Items can either be Python
    identifiers or strings::

        Rule(\'/<any(about, help, imprint, class, "foo,bar"):page_name>\')

    :param map: the :class:`Map`.
    :param items: this function accepts the possible items as positional
                  arguments.

    .. versionchanged:: 2.2
        Value is validated when building a URL.
    '''
    items: Incomplete
    regex: Incomplete
    def __init__(self, map: Map, *items: str) -> None: ...
    def to_url(self, value: t.Any) -> str: ...

class PathConverter(BaseConverter):
    """Like the default :class:`UnicodeConverter`, but it also matches
    slashes.  This is useful for wikis and similar applications::

        Rule('/<path:wikipage>')
        Rule('/<path:wikipage>/edit')

    :param map: the :class:`Map`.
    """
    part_isolating: bool
    regex: str
    weight: int

class NumberConverter(BaseConverter):
    """Baseclass for `IntegerConverter` and `FloatConverter`.

    :internal:
    """
    weight: int
    num_convert: t.Callable
    regex: Incomplete
    fixed_digits: Incomplete
    min: Incomplete
    max: Incomplete
    signed: Incomplete
    def __init__(self, map: Map, fixed_digits: int = 0, min: int | None = None, max: int | None = None, signed: bool = False) -> None: ...
    def to_python(self, value: str) -> t.Any: ...
    def to_url(self, value: t.Any) -> str: ...
    @property
    def signed_regex(self) -> str: ...

class IntegerConverter(NumberConverter):
    '''This converter only accepts integer values::

        Rule("/page/<int:page>")

    By default it only accepts unsigned, positive values. The ``signed``
    parameter will enable signed, negative values. ::

        Rule("/page/<int(signed=True):page>")

    :param map: The :class:`Map`.
    :param fixed_digits: The number of fixed digits in the URL. If you
        set this to ``4`` for example, the rule will only match if the
        URL looks like ``/0001/``. The default is variable length.
    :param min: The minimal value.
    :param max: The maximal value.
    :param signed: Allow signed (negative) values.

    .. versionadded:: 0.15
        The ``signed`` parameter.
    '''
    regex: str

class FloatConverter(NumberConverter):
    '''This converter only accepts floating point values::

        Rule("/probability/<float:probability>")

    By default it only accepts unsigned, positive values. The ``signed``
    parameter will enable signed, negative values. ::

        Rule("/offset/<float(signed=True):offset>")

    :param map: The :class:`Map`.
    :param min: The minimal value.
    :param max: The maximal value.
    :param signed: Allow signed (negative) values.

    .. versionadded:: 0.15
        The ``signed`` parameter.
    '''
    regex: str
    num_convert = float
    def __init__(self, map: Map, min: float | None = None, max: float | None = None, signed: bool = False) -> None: ...

class UUIDConverter(BaseConverter):
    """This converter only accepts UUID strings::

        Rule('/object/<uuid:identifier>')

    .. versionadded:: 0.10

    :param map: the :class:`Map`.
    """
    regex: str
    def to_python(self, value: str) -> uuid.UUID: ...
    def to_url(self, value: uuid.UUID) -> str: ...

DEFAULT_CONVERTERS: t.Mapping[str, type[BaseConverter]]
