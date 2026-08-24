import typing as t
from ..datastructures import ImmutableDict as ImmutableDict, MultiDict as MultiDict
from ..exceptions import BadHost as BadHost, HTTPException as HTTPException, MethodNotAllowed as MethodNotAllowed, NotFound as NotFound
from ..wrappers.request import Request as Request
from ..wsgi import get_host as get_host
from .converters import BaseConverter as BaseConverter, DEFAULT_CONVERTERS as DEFAULT_CONVERTERS
from .exceptions import BuildError as BuildError, NoMatch as NoMatch, RequestAliasRedirect as RequestAliasRedirect, RequestPath as RequestPath, RequestRedirect as RequestRedirect, WebsocketMismatch as WebsocketMismatch
from .matcher import StateMachineMatcher as StateMachineMatcher
from .rules import Rule as Rule, RuleFactory as RuleFactory
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from threading import Lock

class Map:
    """The map class stores all the URL rules and some configuration
    parameters.  Some of the configuration values are only stored on the
    `Map` instance since those affect all rules, others are just defaults
    and can be overridden for each rule.  Note that you have to specify all
    arguments besides the `rules` as keyword arguments!

    :param rules: sequence of url rules for this map.
    :param default_subdomain: The default subdomain for rules without a
                              subdomain defined.
    :param strict_slashes: If a rule ends with a slash but the matched
        URL does not, redirect to the URL with a trailing slash.
    :param merge_slashes: Merge consecutive slashes when matching or
        building URLs. Matches will redirect to the normalized URL.
        Slashes in variable parts are not merged.
    :param redirect_defaults: This will redirect to the default rule if it
                              wasn't visited that way. This helps creating
                              unique URLs.
    :param converters: A dict of converters that adds additional converters
                       to the list of converters. If you redefine one
                       converter this will override the original one.
    :param sort_parameters: If set to `True` the url parameters are sorted.
                            See `url_encode` for more details.
    :param sort_key: The sort key function for `url_encode`.
    :param host_matching: if set to `True` it enables the host matching
                          feature and disables the subdomain one.  If
                          enabled the `host` parameter to rules is used
                          instead of the `subdomain` one.

    .. versionchanged:: 3.0
        The ``charset`` and ``encoding_errors`` parameters were removed.

    .. versionchanged:: 1.0
        If ``url_scheme`` is ``ws`` or ``wss``, only WebSocket rules will match.

    .. versionchanged:: 1.0
        The ``merge_slashes`` parameter was added.

    .. versionchanged:: 0.7
        The ``encoding_errors`` and ``host_matching`` parameters were added.

    .. versionchanged:: 0.5
        The ``sort_parameters`` and ``sort_key``  paramters were added.
    """
    default_converters: Incomplete
    lock_class = Lock
    default_subdomain: Incomplete
    strict_slashes: Incomplete
    merge_slashes: Incomplete
    redirect_defaults: Incomplete
    host_matching: Incomplete
    converters: Incomplete
    sort_parameters: Incomplete
    sort_key: Incomplete
    def __init__(self, rules: t.Iterable[RuleFactory] | None = None, default_subdomain: str = '', strict_slashes: bool = True, merge_slashes: bool = True, redirect_defaults: bool = True, converters: t.Mapping[str, type[BaseConverter]] | None = None, sort_parameters: bool = False, sort_key: t.Callable[[t.Any], t.Any] | None = None, host_matching: bool = False) -> None: ...
    def is_endpoint_expecting(self, endpoint: str, *arguments: str) -> bool:
        """Iterate over all rules and check if the endpoint expects
        the arguments provided.  This is for example useful if you have
        some URLs that expect a language code and others that do not and
        you want to wrap the builder a bit so that the current language
        code is automatically added if not provided but endpoints expect
        it.

        :param endpoint: the endpoint to check.
        :param arguments: this function accepts one or more arguments
                          as positional arguments.  Each one of them is
                          checked.
        """
    def iter_rules(self, endpoint: str | None = None) -> t.Iterator[Rule]:
        """Iterate over all rules or the rules of an endpoint.

        :param endpoint: if provided only the rules for that endpoint
                         are returned.
        :return: an iterator
        """
    def add(self, rulefactory: RuleFactory) -> None:
        """Add a new rule or factory to the map and bind it.  Requires that the
        rule is not bound to another map.

        :param rulefactory: a :class:`Rule` or :class:`RuleFactory`
        """
    def bind(self, server_name: str, script_name: str | None = None, subdomain: str | None = None, url_scheme: str = 'http', default_method: str = 'GET', path_info: str | None = None, query_args: t.Mapping[str, t.Any] | str | None = None) -> MapAdapter:
        """Return a new :class:`MapAdapter` with the details specified to the
        call.  Note that `script_name` will default to ``'/'`` if not further
        specified or `None`.  The `server_name` at least is a requirement
        because the HTTP RFC requires absolute URLs for redirects and so all
        redirect exceptions raised by Werkzeug will contain the full canonical
        URL.

        If no path_info is passed to :meth:`match` it will use the default path
        info passed to bind.  While this doesn't really make sense for
        manual bind calls, it's useful if you bind a map to a WSGI
        environment which already contains the path info.

        `subdomain` will default to the `default_subdomain` for this map if
        no defined. If there is no `default_subdomain` you cannot use the
        subdomain feature.

        .. versionchanged:: 1.0
            If ``url_scheme`` is ``ws`` or ``wss``, only WebSocket rules
            will match.

        .. versionchanged:: 0.15
            ``path_info`` defaults to ``'/'`` if ``None``.

        .. versionchanged:: 0.8
            ``query_args`` can be a string.

        .. versionchanged:: 0.7
            Added ``query_args``.
        """
    def bind_to_environ(self, environ: WSGIEnvironment | Request, server_name: str | None = None, subdomain: str | None = None) -> MapAdapter:
        """Like :meth:`bind` but you can pass it an WSGI environment and it
        will fetch the information from that dictionary.  Note that because of
        limitations in the protocol there is no way to get the current
        subdomain and real `server_name` from the environment.  If you don't
        provide it, Werkzeug will use `SERVER_NAME` and `SERVER_PORT` (or
        `HTTP_HOST` if provided) as used `server_name` with disabled subdomain
        feature.

        If `subdomain` is `None` but an environment and a server name is
        provided it will calculate the current subdomain automatically.
        Example: `server_name` is ``'example.com'`` and the `SERVER_NAME`
        in the wsgi `environ` is ``'staging.dev.example.com'`` the calculated
        subdomain will be ``'staging.dev'``.

        If the object passed as environ has an environ attribute, the value of
        this attribute is used instead.  This allows you to pass request
        objects.  Additionally `PATH_INFO` added as a default of the
        :class:`MapAdapter` so that you don't have to pass the path info to
        the match method.

        .. versionchanged:: 1.0.0
            If the passed server name specifies port 443, it will match
            if the incoming scheme is ``https`` without a port.

        .. versionchanged:: 1.0.0
            A warning is shown when the passed server name does not
            match the incoming WSGI server name.

        .. versionchanged:: 0.8
           This will no longer raise a ValueError when an unexpected server
           name was passed.

        .. versionchanged:: 0.5
            previously this method accepted a bogus `calculate_subdomain`
            parameter that did not have any effect.  It was removed because
            of that.

        :param environ: a WSGI environment.
        :param server_name: an optional server name hint (see above).
        :param subdomain: optionally the current subdomain (see above).
        """
    def update(self) -> None:
        """Called before matching and building to keep the compiled rules
        in the correct order after things changed.
        """

class MapAdapter:
    """Returned by :meth:`Map.bind` or :meth:`Map.bind_to_environ` and does
    the URL matching and building based on runtime information.
    """
    map: Incomplete
    server_name: Incomplete
    script_name: Incomplete
    subdomain: Incomplete
    url_scheme: Incomplete
    path_info: Incomplete
    default_method: Incomplete
    query_args: Incomplete
    websocket: Incomplete
    def __init__(self, map: Map, server_name: str, script_name: str, subdomain: str | None, url_scheme: str, path_info: str, default_method: str, query_args: t.Mapping[str, t.Any] | str | None = None) -> None: ...
    def dispatch(self, view_func: t.Callable[[str, t.Mapping[str, t.Any]], WSGIApplication], path_info: str | None = None, method: str | None = None, catch_http_exceptions: bool = False) -> WSGIApplication:
        """Does the complete dispatching process.  `view_func` is called with
        the endpoint and a dict with the values for the view.  It should
        look up the view function, call it, and return a response object
        or WSGI application.  http exceptions are not caught by default
        so that applications can display nicer error messages by just
        catching them by hand.  If you want to stick with the default
        error messages you can pass it ``catch_http_exceptions=True`` and
        it will catch the http exceptions.

        Here a small example for the dispatch usage::

            from werkzeug.wrappers import Request, Response
            from werkzeug.wsgi import responder
            from werkzeug.routing import Map, Rule

            def on_index(request):
                return Response('Hello from the index')

            url_map = Map([Rule('/', endpoint='index')])
            views = {'index': on_index}

            @responder
            def application(environ, start_response):
                request = Request(environ)
                urls = url_map.bind_to_environ(environ)
                return urls.dispatch(lambda e, v: views[e](request, **v),
                                     catch_http_exceptions=True)

        Keep in mind that this method might return exception objects, too, so
        use :class:`Response.force_type` to get a response object.

        :param view_func: a function that is called with the endpoint as
                          first argument and the value dict as second.  Has
                          to dispatch to the actual view function with this
                          information.  (see above)
        :param path_info: the path info to use for matching.  Overrides the
                          path info specified on binding.
        :param method: the HTTP method used for matching.  Overrides the
                       method specified on binding.
        :param catch_http_exceptions: set to `True` to catch any of the
                                      werkzeug :class:`HTTPException`\\s.
        """
    @t.overload
    def match(self, path_info: str | None = None, method: str | None = None, return_rule: t.Literal[False] = False, query_args: t.Mapping[str, t.Any] | str | None = None, websocket: bool | None = None) -> tuple[str, t.Mapping[str, t.Any]]: ...
    @t.overload
    def match(self, path_info: str | None = None, method: str | None = None, return_rule: t.Literal[True] = True, query_args: t.Mapping[str, t.Any] | str | None = None, websocket: bool | None = None) -> tuple[Rule, t.Mapping[str, t.Any]]: ...
    def test(self, path_info: str | None = None, method: str | None = None) -> bool:
        """Test if a rule would match.  Works like `match` but returns `True`
        if the URL matches, or `False` if it does not exist.

        :param path_info: the path info to use for matching.  Overrides the
                          path info specified on binding.
        :param method: the HTTP method used for matching.  Overrides the
                       method specified on binding.
        """
    def allowed_methods(self, path_info: str | None = None) -> t.Iterable[str]:
        """Returns the valid methods that match for a given path.

        .. versionadded:: 0.7
        """
    def get_host(self, domain_part: str | None) -> str:
        """Figures out the full host name for the given domain part.  The
        domain part is a subdomain in case host matching is disabled or
        a full host name.
        """
    def get_default_redirect(self, rule: Rule, method: str, values: t.MutableMapping[str, t.Any], query_args: t.Mapping[str, t.Any] | str) -> str | None:
        """A helper that returns the URL to redirect to if it finds one.
        This is used for default redirecting only.

        :internal:
        """
    def encode_query_args(self, query_args: t.Mapping[str, t.Any] | str) -> str: ...
    def make_redirect_url(self, path_info: str, query_args: t.Mapping[str, t.Any] | str | None = None, domain_part: str | None = None) -> str:
        """Creates a redirect URL.

        :internal:
        """
    def make_alias_redirect_url(self, path: str, endpoint: str, values: t.Mapping[str, t.Any], method: str, query_args: t.Mapping[str, t.Any] | str) -> str:
        """Internally called to make an alias redirect URL."""
    def build(self, endpoint: str, values: t.Mapping[str, t.Any] | None = None, method: str | None = None, force_external: bool = False, append_unknown: bool = True, url_scheme: str | None = None) -> str:
        '''Building URLs works pretty much the other way round.  Instead of
        `match` you call `build` and pass it the endpoint and a dict of
        arguments for the placeholders.

        The `build` function also accepts an argument called `force_external`
        which, if you set it to `True` will force external URLs. Per default
        external URLs (include the server name) will only be used if the
        target URL is on a different subdomain.

        >>> m = Map([
        ...     Rule(\'/\', endpoint=\'index\'),
        ...     Rule(\'/downloads/\', endpoint=\'downloads/index\'),
        ...     Rule(\'/downloads/<int:id>\', endpoint=\'downloads/show\')
        ... ])
        >>> urls = m.bind("example.com", "/")
        >>> urls.build("index", {})
        \'/\'
        >>> urls.build("downloads/show", {\'id\': 42})
        \'/downloads/42\'
        >>> urls.build("downloads/show", {\'id\': 42}, force_external=True)
        \'http://example.com/downloads/42\'

        Because URLs cannot contain non ASCII data you will always get
        bytes back.  Non ASCII characters are urlencoded with the
        charset defined on the map instance.

        Additional values are converted to strings and appended to the URL as
        URL querystring parameters:

        >>> urls.build("index", {\'q\': \'My Searchstring\'})
        \'/?q=My+Searchstring\'

        When processing those additional values, lists are furthermore
        interpreted as multiple values (as per
        :py:class:`werkzeug.datastructures.MultiDict`):

        >>> urls.build("index", {\'q\': [\'a\', \'b\', \'c\']})
        \'/?q=a&q=b&q=c\'

        Passing a ``MultiDict`` will also add multiple values:

        >>> urls.build("index", MultiDict(((\'p\', \'z\'), (\'q\', \'a\'), (\'q\', \'b\'))))
        \'/?p=z&q=a&q=b\'

        If a rule does not exist when building a `BuildError` exception is
        raised.

        The build method accepts an argument called `method` which allows you
        to specify the method you want to have an URL built for if you have
        different methods for the same endpoint specified.

        :param endpoint: the endpoint of the URL to build.
        :param values: the values for the URL to build.  Unhandled values are
                       appended to the URL as query parameters.
        :param method: the HTTP method for the rule if there are different
                       URLs for different methods on the same endpoint.
        :param force_external: enforce full canonical external URLs. If the URL
                               scheme is not provided, this will generate
                               a protocol-relative URL.
        :param append_unknown: unknown parameters are appended to the generated
                               URL as query string argument.  Disable this
                               if you want the builder to ignore those.
        :param url_scheme: Scheme to use in place of the bound
            :attr:`url_scheme`.

        .. versionchanged:: 2.0
            Added the ``url_scheme`` parameter.

        .. versionadded:: 0.6
           Added the ``append_unknown`` parameter.
        '''
