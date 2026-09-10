import typing_extensions as te
from ..http import dump_header as dump_header, parse_dict_header as parse_dict_header, quote_header_value as quote_header_value
from .structures import CallbackDict as CallbackDict
from _typeshed import Incomplete

class Authorization:
    '''Represents the parts of an ``Authorization`` request header.

    :attr:`.Request.authorization` returns an instance if the header is set.

    An instance can be used with the test :class:`.Client` request methods\' ``auth``
    parameter to send the header in test requests.

    Depending on the auth scheme, either :attr:`parameters` or :attr:`token` will be
    set. The ``Basic`` scheme\'s token is decoded into the ``username`` and ``password``
    parameters.

    For convenience, ``auth["key"]`` and ``auth.key`` both access the key in the
    :attr:`parameters` dict, along with ``auth.get("key")`` and ``"key" in auth``.

    .. versionchanged:: 2.3
        The ``token`` parameter and attribute was added to support auth schemes that use
        a token instead of parameters, such as ``Bearer``.

    .. versionchanged:: 2.3
        The object is no longer a ``dict``.

    .. versionchanged:: 0.5
        The object is an immutable dict.
    '''
    type: Incomplete
    parameters: Incomplete
    token: Incomplete
    def __init__(self, auth_type: str, data: dict[str, str | None] | None = None, token: str | None = None) -> None: ...
    def __getattr__(self, name: str) -> str | None: ...
    def __getitem__(self, name: str) -> str | None: ...
    def get(self, key: str, default: str | None = None) -> str | None: ...
    def __contains__(self, key: str) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def from_header(cls, value: str | None) -> te.Self | None:
        """Parse an ``Authorization`` header value and return an instance, or ``None``
        if the value is empty.

        :param value: The header value to parse.

        .. versionadded:: 2.3
        """
    def to_header(self) -> str:
        """Produce an ``Authorization`` header value representing this data.

        .. versionadded:: 2.0
        """

class WWWAuthenticate:
    '''Represents the parts of a ``WWW-Authenticate`` response header.

    Set :attr:`.Response.www_authenticate` to an instance of list of instances to set
    values for this header in the response. Modifying this instance will modify the
    header value.

    Depending on the auth scheme, either :attr:`parameters` or :attr:`token` should be
    set. The ``Basic`` scheme will encode ``username`` and ``password`` parameters to a
    token.

    For convenience, ``auth["key"]`` and ``auth.key`` both act on the :attr:`parameters`
    dict, and can be used to get, set, or delete parameters. ``auth.get("key")`` and
    ``"key" in auth`` are also provided.

    .. versionchanged:: 2.3
        The ``token`` parameter and attribute was added to support auth schemes that use
        a token instead of parameters, such as ``Bearer``.

    .. versionchanged:: 2.3
        The object is no longer a ``dict``.

    .. versionchanged:: 2.3
        The ``on_update`` parameter was removed.
    '''
    def __init__(self, auth_type: str, values: dict[str, str | None] | None = None, token: str | None = None) -> None: ...
    @property
    def type(self) -> str:
        """The authorization scheme, like ``basic``, ``digest``, or ``bearer``."""
    @type.setter
    def type(self, value: str) -> None: ...
    @property
    def parameters(self) -> dict[str, str | None]:
        """A dict of parameters for the header. Only one of this or :attr:`token` should
        have a value for a given scheme.
        """
    @parameters.setter
    def parameters(self, value: dict[str, str]) -> None: ...
    @property
    def token(self) -> str | None:
        """A dict of parameters for the header. Only one of this or :attr:`token` should
        have a value for a given scheme.
        """
    @token.setter
    def token(self, value: str | None) -> None:
        """A token for the header. Only one of this or :attr:`parameters` should have a
        value for a given scheme.

        .. versionadded:: 2.3
        """
    def __getitem__(self, key: str) -> str | None: ...
    def __setitem__(self, key: str, value: str | None) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __getattr__(self, name: str) -> str | None: ...
    def __setattr__(self, name: str, value: str | None) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def get(self, key: str, default: str | None = None) -> str | None: ...
    @classmethod
    def from_header(cls, value: str | None) -> te.Self | None:
        """Parse a ``WWW-Authenticate`` header value and return an instance, or ``None``
        if the value is empty.

        :param value: The header value to parse.

        .. versionadded:: 2.3
        """
    def to_header(self) -> str:
        """Produce a ``WWW-Authenticate`` header value representing this data."""
