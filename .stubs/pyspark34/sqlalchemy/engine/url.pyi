from .. import exc as exc, util as util
from ..dialects import plugins as plugins, registry as registry
from .interfaces import Dialect as Dialect
from typing import Any, Dict, Iterable, List, Mapping, NamedTuple, Sequence, Tuple, Type

class URL(NamedTuple):
    """
    Represent the components of a URL used to connect to a database.

    URLs are typically constructed from a fully formatted URL string, where the
    :func:`.make_url` function is used internally by the
    :func:`_sa.create_engine` function in order to parse the URL string into
    its individual components, which are then used to construct a new
    :class:`.URL` object. When parsing from a formatted URL string, the parsing
    format generally follows
    `RFC-1738 <https://www.ietf.org/rfc/rfc1738.txt>`_, with some exceptions.

    A :class:`_engine.URL` object may also be produced directly, either by
    using the :func:`.make_url` function with a fully formed URL string, or
    by using the :meth:`_engine.URL.create` constructor in order
    to construct a :class:`_engine.URL` programmatically given individual
    fields. The resulting :class:`.URL` object may be passed directly to
    :func:`_sa.create_engine` in place of a string argument, which will bypass
    the usage of :func:`.make_url` within the engine's creation process.

    .. versionchanged:: 1.4

        The :class:`_engine.URL` object is now an immutable object.  To
        create a URL, use the :func:`_engine.make_url` or
        :meth:`_engine.URL.create` function / method.  To modify
        a :class:`_engine.URL`, use methods like
        :meth:`_engine.URL.set` and
        :meth:`_engine.URL.update_query_dict` to return a new
        :class:`_engine.URL` object with modifications.   See notes for this
        change at :ref:`change_5526`.

    .. seealso::

        :ref:`database_urls`

    :class:`_engine.URL` contains the following attributes:

    * :attr:`_engine.URL.drivername`: database backend and driver name, such as
      ``postgresql+psycopg2``
    * :attr:`_engine.URL.username`: username string
    * :attr:`_engine.URL.password`: password string
    * :attr:`_engine.URL.host`: string hostname
    * :attr:`_engine.URL.port`: integer port number
    * :attr:`_engine.URL.database`: string database name
    * :attr:`_engine.URL.query`: an immutable mapping representing the query
      string.  contains strings for keys and either strings or tuples of
      strings for values.


    """
    drivername: str
    username: str | None
    password: str | None
    host: str | None
    port: int | None
    database: str | None
    query: util.immutabledict[str, Tuple[str, ...] | str]
    @classmethod
    def create(cls, drivername: str, username: str | None = None, password: str | None = None, host: str | None = None, port: int | None = None, database: str | None = None, query: Mapping[str, Sequence[str] | str] = ...) -> URL:
        """Create a new :class:`_engine.URL` object.

        .. seealso::

            :ref:`database_urls`

        :param drivername: the name of the database backend. This name will
          correspond to a module in sqlalchemy/databases or a third party
          plug-in.
        :param username: The user name.
        :param password: database password.  Is typically a string, but may
          also be an object that can be stringified with ``str()``.

          .. note::  A password-producing object will be stringified only
             **once** per :class:`_engine.Engine` object.  For dynamic password
             generation per connect, see :ref:`engines_dynamic_tokens`.

        :param host: The name of the host.
        :param port: The port number.
        :param database: The database name.
        :param query: A dictionary of string keys to string values to be passed
          to the dialect and/or the DBAPI upon connect.   To specify non-string
          parameters to a Python DBAPI directly, use the
          :paramref:`_sa.create_engine.connect_args` parameter to
          :func:`_sa.create_engine`.   See also
          :attr:`_engine.URL.normalized_query` for a dictionary that is
          consistently string->list of string.
        :return: new :class:`_engine.URL` object.

        .. versionadded:: 1.4

            The :class:`_engine.URL` object is now an **immutable named
            tuple**.  In addition, the ``query`` dictionary is also immutable.
            To create a URL, use the :func:`_engine.url.make_url` or
            :meth:`_engine.URL.create` function/ method.  To modify a
            :class:`_engine.URL`, use the :meth:`_engine.URL.set` and
            :meth:`_engine.URL.update_query` methods.

        """
    def set(self, drivername: str | None = None, username: str | None = None, password: str | None = None, host: str | None = None, port: int | None = None, database: str | None = None, query: Mapping[str, Sequence[str] | str] | None = None) -> URL:
        """return a new :class:`_engine.URL` object with modifications.

        Values are used if they are non-None.  To set a value to ``None``
        explicitly, use the :meth:`_engine.URL._replace` method adapted
        from ``namedtuple``.

        :param drivername: new drivername
        :param username: new username
        :param password: new password
        :param host: new hostname
        :param port: new port
        :param query: new query parameters, passed a dict of string keys
         referring to string or sequence of string values.  Fully
         replaces the previous list of arguments.

        :return: new :class:`_engine.URL` object.

        .. versionadded:: 1.4

        .. seealso::

            :meth:`_engine.URL.update_query_dict`

        """
    def update_query_string(self, query_string: str, append: bool = False) -> URL:
        '''Return a new :class:`_engine.URL` object with the :attr:`_engine.URL.query`
        parameter dictionary updated by the given query string.

        E.g.::

            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_string("alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt")
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'

        :param query_string: a URL escaped query string, not including the
         question mark.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_dict`

        '''
    def update_query_pairs(self, key_value_pairs: Iterable[Tuple[str, str | List[str]]], append: bool = False) -> URL:
        '''Return a new :class:`_engine.URL` object with the
        :attr:`_engine.URL.query`
        parameter dictionary updated by the given sequence of key/value pairs

        E.g.::

            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_pairs([("alt_host", "host1"), ("alt_host", "host2"), ("ssl_cipher", "/path/to/crt")])
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'

        :param key_value_pairs: A sequence of tuples containing two strings
         each.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.difference_update_query`

            :meth:`_engine.URL.set`

        '''
    def update_query_dict(self, query_parameters: Mapping[str, str | List[str]], append: bool = False) -> URL:
        '''Return a new :class:`_engine.URL` object with the
        :attr:`_engine.URL.query` parameter dictionary updated by the given
        dictionary.

        The dictionary typically contains string keys and string values.
        In order to represent a query parameter that is expressed multiple
        times, pass a sequence of string values.

        E.g.::


            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_dict({"alt_host": ["host1", "host2"], "ssl_cipher": "/path/to/crt"})
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'


        :param query_parameters: A dictionary with string keys and values
         that are either strings, or sequences of strings.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.


        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_string`

            :meth:`_engine.URL.update_query_pairs`

            :meth:`_engine.URL.difference_update_query`

            :meth:`_engine.URL.set`

        '''
    def difference_update_query(self, names: Iterable[str]) -> URL:
        """
        Remove the given names from the :attr:`_engine.URL.query` dictionary,
        returning the new :class:`_engine.URL`.

        E.g.::

            url = url.difference_update_query(['foo', 'bar'])

        Equivalent to using :meth:`_engine.URL.set` as follows::

            url = url.set(
                query={
                    key: url.query[key]
                    for key in set(url.query).difference(['foo', 'bar'])
                }
            )

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_dict`

            :meth:`_engine.URL.set`

        """
    @property
    def normalized_query(self) -> Mapping[str, Sequence[str]]:
        '''Return the :attr:`_engine.URL.query` dictionary with values normalized
        into sequences.

        As the :attr:`_engine.URL.query` dictionary may contain either
        string values or sequences of string values to differentiate between
        parameters that are specified multiple times in the query string,
        code that needs to handle multiple parameters generically will wish
        to use this attribute so that all parameters present are presented
        as sequences.   Inspiration is from Python\'s ``urllib.parse.parse_qs``
        function.  E.g.::


            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt")
            >>> url.query
            immutabledict({\'alt_host\': (\'host1\', \'host2\'), \'ssl_cipher\': \'/path/to/crt\'})
            >>> url.normalized_query
            immutabledict({\'alt_host\': (\'host1\', \'host2\'), \'ssl_cipher\': (\'/path/to/crt\',)})

        '''
    def __to_string__(self, hide_password: bool = True) -> str:
        """Render this :class:`_engine.URL` object as a string.

        :param hide_password: Defaults to True.   The password is not shown
         in the string unless this is set to False.

        """
    def render_as_string(self, hide_password: bool = True) -> str:
        """Render this :class:`_engine.URL` object as a string.

        This method is used when the ``__str__()`` or ``__repr__()``
        methods are used.   The method directly includes additional options.

        :param hide_password: Defaults to True.   The password is not shown
         in the string unless this is set to False.

        """
    def __copy__(self) -> URL: ...
    def __deepcopy__(self, memo: Any) -> URL: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def get_backend_name(self) -> str:
        """Return the backend name.

        This is the name that corresponds to the database backend in
        use, and is the portion of the :attr:`_engine.URL.drivername`
        that is to the left of the plus sign.

        """
    def get_driver_name(self) -> str:
        """Return the backend name.

        This is the name that corresponds to the DBAPI driver in
        use, and is the portion of the :attr:`_engine.URL.drivername`
        that is to the right of the plus sign.

        If the :attr:`_engine.URL.drivername` does not include a plus sign,
        then the default :class:`_engine.Dialect` for this :class:`_engine.URL`
        is imported in order to get the driver name.

        """
    def get_dialect(self, _is_async: bool = False) -> Type[Dialect]:
        """Return the SQLAlchemy :class:`_engine.Dialect` class corresponding
        to this URL's driver name.

        """
    def translate_connect_args(self, names: List[str] | None = None, **kw: Any) -> Dict[str, Any]:
        """Translate url attributes into a dictionary of connection arguments.

        Returns attributes of this url (`host`, `database`, `username`,
        `password`, `port`) as a plain dictionary.  The attribute names are
        used as the keys by default.  Unset or false attributes are omitted
        from the final dictionary.

        :param \\**kw: Optional, alternate key names for url attributes.

        :param names: Deprecated.  Same purpose as the keyword-based alternate
            names, but correlates the name to the original positionally.
        """

def make_url(name_or_url: str | URL) -> URL:
    '''Given a string, produce a new URL instance.

    The format of the URL generally follows `RFC-1738
    <https://www.ietf.org/rfc/rfc1738.txt>`_, with some exceptions, including
    that underscores, and not dashes or periods, are accepted within the
    "scheme" portion.

    If a :class:`.URL` object is passed, it is returned as is.

    .. seealso::

        :ref:`database_urls`

    '''
