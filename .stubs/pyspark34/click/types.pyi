import os
import typing as t
from ._compat import open_stream as open_stream
from .core import Context as Context, Parameter as Parameter
from .exceptions import BadParameter as BadParameter
from .shell_completion import CompletionItem as CompletionItem
from .utils import LazyFile as LazyFile, format_filename as format_filename, safecall as safecall
from _typeshed import Incomplete

class ParamType:
    """Represents the type of a parameter. Validates and converts values
    from the command line or Python into the correct type.

    To implement a custom type, subclass and implement at least the
    following:

    -   The :attr:`name` class attribute must be set.
    -   Calling an instance of the type with ``None`` must return
        ``None``. This is already implemented by default.
    -   :meth:`convert` must convert string values to the correct type.
    -   :meth:`convert` must accept values that are already the correct
        type.
    -   It must be able to convert a value if the ``ctx`` and ``param``
        arguments are ``None``. This can occur when converting prompt
        input.
    """
    is_composite: t.ClassVar[bool]
    arity: t.ClassVar[int]
    name: str
    envvar_list_splitter: t.ClassVar[str | None]
    def to_info_dict(self) -> t.Dict[str, t.Any]:
        """Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionadded:: 8.0
        """
    def __call__(self, value: t.Any, param: Parameter | None = None, ctx: Context | None = None) -> t.Any: ...
    def get_metavar(self, param: Parameter) -> str | None:
        """Returns the metavar default for this param if it provides one."""
    def get_missing_message(self, param: Parameter) -> str | None:
        """Optionally might return extra information about a missing
        parameter.

        .. versionadded:: 2.0
        """
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any:
        """Convert the value to the correct type. This is not called if
        the value is ``None`` (the missing value).

        This must accept string values from the command line, as well as
        values that are already the correct type. It may also convert
        other compatible types.

        The ``param`` and ``ctx`` arguments may be ``None`` in certain
        situations, such as when converting prompt input.

        If the value cannot be converted, call :meth:`fail` with a
        descriptive message.

        :param value: The value to convert.
        :param param: The parameter that is using this type to convert
            its value. May be ``None``.
        :param ctx: The current context that arrived at this value. May
            be ``None``.
        """
    def split_envvar_value(self, rv: str) -> t.Sequence[str]:
        """Given a value from an environment variable this splits it up
        into small chunks depending on the defined envvar list splitter.

        If the splitter is set to `None`, which means that whitespace splits,
        then leading and trailing whitespace is ignored.  Otherwise, leading
        and trailing splitters usually lead to empty items being included.
        """
    def fail(self, message: str, param: Parameter | None = None, ctx: Context | None = None) -> t.NoReturn:
        """Helper method to fail with an invalid value message."""
    def shell_complete(self, ctx: Context, param: Parameter, incomplete: str) -> t.List['CompletionItem']:
        """Return a list of
        :class:`~click.shell_completion.CompletionItem` objects for the
        incomplete value. Most types do not provide completions, but
        some do, and this allows custom types to provide custom
        completions as well.

        :param ctx: Invocation context for this command.
        :param param: The parameter that is requesting completion.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class CompositeParamType(ParamType):
    is_composite: bool
    @property
    def arity(self) -> int: ...

class FuncParamType(ParamType):
    name: Incomplete
    func: Incomplete
    def __init__(self, func: t.Callable[[t.Any], t.Any]) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class UnprocessedParamType(ParamType):
    name: str
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class StringParamType(ParamType):
    name: str
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class Choice(ParamType):
    """The choice type allows a value to be checked against a fixed set
    of supported values. All of these values have to be strings.

    You should only pass a list or tuple of choices. Other iterables
    (like generators) may lead to surprising results.

    The resulting value will always be one of the originally passed choices
    regardless of ``case_sensitive`` or any ``ctx.token_normalize_func``
    being specified.

    See :ref:`choice-opts` for an example.

    :param case_sensitive: Set to false to make choices case
        insensitive. Defaults to true.
    """
    name: str
    choices: Incomplete
    case_sensitive: Incomplete
    def __init__(self, choices: t.Sequence[str], case_sensitive: bool = True) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def get_metavar(self, param: Parameter) -> str: ...
    def get_missing_message(self, param: Parameter) -> str: ...
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...
    def shell_complete(self, ctx: Context, param: Parameter, incomplete: str) -> t.List['CompletionItem']:
        """Complete choices that start with the incomplete value.

        :param ctx: Invocation context for this command.
        :param param: The parameter that is requesting completion.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class DateTime(ParamType):
    """The DateTime type converts date strings into `datetime` objects.

    The format strings which are checked are configurable, but default to some
    common (non-timezone aware) ISO 8601 formats.

    When specifying *DateTime* formats, you should only pass a list or a tuple.
    Other iterables, like generators, may lead to surprising results.

    The format strings are processed using ``datetime.strptime``, and this
    consequently defines the format strings which are allowed.

    Parsing is tried using each format, in order, and the first format which
    parses successfully is used.

    :param formats: A list or tuple of date format strings, in the order in
                    which they should be tried. Defaults to
                    ``'%Y-%m-%d'``, ``'%Y-%m-%dT%H:%M:%S'``,
                    ``'%Y-%m-%d %H:%M:%S'``.
    """
    name: str
    formats: Incomplete
    def __init__(self, formats: t.Sequence[str] | None = None) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def get_metavar(self, param: Parameter) -> str: ...
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class _NumberParamTypeBase(ParamType):
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class _NumberRangeBase(_NumberParamTypeBase):
    min: Incomplete
    max: Incomplete
    min_open: Incomplete
    max_open: Incomplete
    clamp: Incomplete
    def __init__(self, min: float | None = None, max: float | None = None, min_open: bool = False, max_open: bool = False, clamp: bool = False) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class IntParamType(_NumberParamTypeBase):
    name: str

class IntRange(_NumberRangeBase, IntParamType):
    """Restrict an :data:`click.INT` value to a range of accepted
    values. See :ref:`ranges`.

    If ``min`` or ``max`` are not passed, any value is accepted in that
    direction. If ``min_open`` or ``max_open`` are enabled, the
    corresponding boundary is not included in the range.

    If ``clamp`` is enabled, a value outside the range is clamped to the
    boundary instead of failing.

    .. versionchanged:: 8.0
        Added the ``min_open`` and ``max_open`` parameters.
    """
    name: str

class FloatParamType(_NumberParamTypeBase):
    name: str

class FloatRange(_NumberRangeBase, FloatParamType):
    """Restrict a :data:`click.FLOAT` value to a range of accepted
    values. See :ref:`ranges`.

    If ``min`` or ``max`` are not passed, any value is accepted in that
    direction. If ``min_open`` or ``max_open`` are enabled, the
    corresponding boundary is not included in the range.

    If ``clamp`` is enabled, a value outside the range is clamped to the
    boundary instead of failing. This is not supported if either
    boundary is marked ``open``.

    .. versionchanged:: 8.0
        Added the ``min_open`` and ``max_open`` parameters.
    """
    name: str
    def __init__(self, min: float | None = None, max: float | None = None, min_open: bool = False, max_open: bool = False, clamp: bool = False) -> None: ...

class BoolParamType(ParamType):
    name: str
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class UUIDParameterType(ParamType):
    name: str
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

class File(ParamType):
    """Declares a parameter to be a file for reading or writing.  The file
    is automatically closed once the context tears down (after the command
    finished working).

    Files can be opened for reading or writing.  The special value ``-``
    indicates stdin or stdout depending on the mode.

    By default, the file is opened for reading text data, but it can also be
    opened in binary mode or for writing.  The encoding parameter can be used
    to force a specific encoding.

    The `lazy` flag controls if the file should be opened immediately or upon
    first IO. The default is to be non-lazy for standard input and output
    streams as well as files opened for reading, `lazy` otherwise. When opening a
    file lazily for reading, it is still opened temporarily for validation, but
    will not be held open until first IO. lazy is mainly useful when opening
    for writing to avoid creating the file until it is needed.

    Starting with Click 2.0, files can also be opened atomically in which
    case all writes go into a separate file in the same folder and upon
    completion the file will be moved over to the original location.  This
    is useful if a file regularly read by other users is modified.

    See :ref:`file-args` for more information.
    """
    name: str
    envvar_list_splitter: t.ClassVar[str]
    mode: Incomplete
    encoding: Incomplete
    errors: Incomplete
    lazy: Incomplete
    atomic: Incomplete
    def __init__(self, mode: str = 'r', encoding: str | None = None, errors: str | None = 'strict', lazy: bool | None = None, atomic: bool = False) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def resolve_lazy_flag(self, value: str | os.PathLike[str]) -> bool: ...
    def convert(self, value: str | os.PathLike[str] | t.IO[t.Any], param: Parameter | None, ctx: Context | None) -> t.IO[t.Any]: ...
    def shell_complete(self, ctx: Context, param: Parameter, incomplete: str) -> t.List['CompletionItem']:
        """Return a special completion marker that tells the completion
        system to use the shell to provide file path completions.

        :param ctx: Invocation context for this command.
        :param param: The parameter that is requesting completion.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class Path(ParamType):
    """The ``Path`` type is similar to the :class:`File` type, but
    returns the filename instead of an open file. Various checks can be
    enabled to validate the type of file and permissions.

    :param exists: The file or directory needs to exist for the value to
        be valid. If this is not set to ``True``, and the file does not
        exist, then all further checks are silently skipped.
    :param file_okay: Allow a file as a value.
    :param dir_okay: Allow a directory as a value.
    :param readable: if true, a readable check is performed.
    :param writable: if true, a writable check is performed.
    :param executable: if true, an executable check is performed.
    :param resolve_path: Make the value absolute and resolve any
        symlinks. A ``~`` is not expanded, as this is supposed to be
        done by the shell only.
    :param allow_dash: Allow a single dash as a value, which indicates
        a standard stream (but does not open it). Use
        :func:`~click.open_file` to handle opening this value.
    :param path_type: Convert the incoming path value to this type. If
        ``None``, keep Python's default, which is ``str``. Useful to
        convert to :class:`pathlib.Path`.

    .. versionchanged:: 8.1
        Added the ``executable`` parameter.

    .. versionchanged:: 8.0
        Allow passing ``path_type=pathlib.Path``.

    .. versionchanged:: 6.0
        Added the ``allow_dash`` parameter.
    """
    envvar_list_splitter: t.ClassVar[str]
    exists: Incomplete
    file_okay: Incomplete
    dir_okay: Incomplete
    readable: Incomplete
    writable: Incomplete
    executable: Incomplete
    resolve_path: Incomplete
    allow_dash: Incomplete
    type: Incomplete
    name: Incomplete
    def __init__(self, exists: bool = False, file_okay: bool = True, dir_okay: bool = True, writable: bool = False, readable: bool = True, resolve_path: bool = False, allow_dash: bool = False, path_type: t.Type[t.Any] | None = None, executable: bool = False) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    def coerce_path_result(self, value: str | os.PathLike[str]) -> str | bytes | os.PathLike[str]: ...
    def convert(self, value: str | os.PathLike[str], param: Parameter | None, ctx: Context | None) -> str | bytes | os.PathLike[str]: ...
    def shell_complete(self, ctx: Context, param: Parameter, incomplete: str) -> t.List['CompletionItem']:
        """Return a special completion marker that tells the completion
        system to use the shell to provide path completions for only
        directories or any paths.

        :param ctx: Invocation context for this command.
        :param param: The parameter that is requesting completion.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        """

class Tuple(CompositeParamType):
    """The default behavior of Click is to apply a type on a value directly.
    This works well in most cases, except for when `nargs` is set to a fixed
    count and different types should be used for different items.  In this
    case the :class:`Tuple` type can be used.  This type can only be used
    if `nargs` is set to a fixed number.

    For more information see :ref:`tuple-type`.

    This can be selected by using a Python tuple literal as a type.

    :param types: a list of types that should be used for the tuple items.
    """
    types: Incomplete
    def __init__(self, types: t.Sequence[t.Type[t.Any] | ParamType]) -> None: ...
    def to_info_dict(self) -> t.Dict[str, t.Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def arity(self) -> int: ...
    def convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> t.Any: ...

def convert_type(ty: t.Any | None, default: t.Any | None = None) -> ParamType:
    """Find the most appropriate :class:`ParamType` for the given Python
    type. If the type isn't provided, it can be inferred from a default
    value.
    """

UNPROCESSED: Incomplete
STRING: Incomplete
INT: Incomplete
FLOAT: Incomplete
BOOL: Incomplete
UUID: Incomplete
