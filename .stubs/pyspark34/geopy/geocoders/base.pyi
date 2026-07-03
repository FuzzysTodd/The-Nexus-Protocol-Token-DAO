from _typeshed import Incomplete

__all__ = ['Geocoder', 'options']

class options:
    '''The `options` object contains default configuration values for
    geocoders, e.g. `timeout` and `User-Agent`.
    Instead of passing a custom value to each geocoder individually, you can
    override a default value in this object.

    Please note that not all geocoders use all attributes of this object.
    For example, some geocoders don\'t respect the ``default_scheme``
    attribute. Refer to the specific geocoder\'s initializer doc for a list
    of parameters which that geocoder accepts.

    Example for overriding default ``timeout`` and ``user_agent``::

        >>> import geopy.geocoders
        >>> from geopy.geocoders import Nominatim
        >>> geopy.geocoders.options.default_user_agent = \'my_app/1\'
        >>> geopy.geocoders.options.default_timeout = 7
        >>> geolocator = Nominatim()
        >>> print(geolocator.headers)
        {\'User-Agent\': \'my_app/1\'}
        >>> print(geolocator.timeout)
        7

    Attributes:
        default_adapter_factory
            A callable which returns a :class:`geopy.adapters.BaseAdapter`
            instance. Adapters are different implementations of HTTP clients.
            See :mod:`geopy.adapters` for more info.

            This callable accepts two keyword args: ``proxies`` and ``ssl_context``.
            A class might be specified as this callable as well.

            Example::

                import geopy.geocoders
                geopy.geocoders.options.default_adapter_factory = geopy.adapters.URLLibAdapter

                geopy.geocoders.options.default_adapter_factory = (
                    lambda proxies, ssl_context: MyAdapter(
                        proxies=proxies, ssl_context=ssl_context, my_custom_arg=42
                    )
                )

            If `requests <https://requests.readthedocs.io>`_ package is
            installed, the default adapter is
            :class:`geopy.adapters.RequestsAdapter`. Otherwise it is
            :class:`geopy.adapters.URLLibAdapter`.

            .. versionadded:: 2.0

        default_proxies
            Tunnel requests through HTTP proxy.

            By default the system proxies are respected (e.g.
            `HTTP_PROXY` and `HTTPS_PROXY` env vars or platform-specific
            proxy settings, such as macOS or Windows native
            preferences -- see :func:`urllib.request.getproxies` for
            more details). The `proxies` value for using system proxies
            is ``None``.

            To disable system proxies and issue requests directly,
            explicitly pass an empty dict as a value for `proxies`: ``{}``.

            To use a custom HTTP proxy location, pass a string.
            Valid examples are:

            - ``"192.0.2.0:8080"``
            - ``"john:passw0rd@192.0.2.0:8080"``
            - ``"http://john:passw0rd@192.0.2.0:8080"``

            Please note:

            - Scheme part (``http://``) of the proxy is ignored.
            - Only `http` proxy is supported. Even if the proxy scheme
              is `https`, it will be ignored, and the connection between
              client and proxy would still be unencrypted.
              However, `https` requests via `http` proxy are still
              supported (via `HTTP CONNECT` method).


            Raw urllib-style `proxies` dict might be provided instead of
            a string:

            - ``{"https": "192.0.2.0:8080"}`` -- means that HTTP proxy
              would be used only for requests having `https` scheme.
              String `proxies` value is automatically used for both
              schemes, and is provided as a shorthand for the urllib-style
              `proxies` dict.

            For more information, see
            documentation on :func:`urllib.request.getproxies`.

        default_scheme
            Use ``\'https\'`` or ``\'http\'`` as the API URL\'s scheme.

        default_ssl_context
            An :class:`ssl.SSLContext` instance with custom TLS
            verification settings. Pass ``None`` to use the interpreter\'s
            defaults (that is to use the system\'s trusted CA certificates).

            To use the CA bundle used by `requests` library::

                import ssl
                import certifi
                import geopy.geocoders
                ctx = ssl.create_default_context(cafile=certifi.where())
                geopy.geocoders.options.default_ssl_context = ctx

            To disable TLS certificate verification completely::

                import ssl
                import geopy.geocoders
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                geopy.geocoders.options.default_ssl_context = ctx

            See docs for the :class:`ssl.SSLContext` class for more examples.

        default_timeout
            Time, in seconds, to wait for the geocoding service to respond
            before raising a :class:`geopy.exc.GeocoderTimedOut` exception.
            Pass `None` to disable timeout.

        default_user_agent
            User-Agent header to send with the requests to geocoder API.
    '''
    default_adapter_factory: Incomplete
    default_proxies: Incomplete
    default_scheme: str
    default_ssl_context: Incomplete
    default_timeout: int
    default_user_agent: Incomplete

class Geocoder:
    """
    Template object for geocoders.
    """
    scheme: Incomplete
    timeout: Incomplete
    proxies: Incomplete
    headers: Incomplete
    ssl_context: Incomplete
    adapter: Incomplete
    def __init__(self, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None: ...
    def __enter__(self):
        """Context manager for synchronous adapters. At exit all
        open connections will be closed.

        In synchronous mode context manager usage is not required,
        and connections will be automatically closed by garbage collection.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    async def __aenter__(self):
        """Context manager for asynchronous adapters. At exit all
        open connections will be closed.

        In asynchronous mode context manager usage is not required,
        however, it is strongly advised to avoid warnings about
        resources leaks.
        """
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
