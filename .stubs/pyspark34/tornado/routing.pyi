from _typeshed import Incomplete
from tornado import httputil as httputil
from tornado.escape import url_escape as url_escape, url_unescape as url_unescape, utf8 as utf8
from tornado.log import app_log as app_log
from tornado.util import basestring_type as basestring_type, import_object as import_object, re_unescape as re_unescape, unicode_type as unicode_type
from typing import Any, Awaitable, Dict, Pattern

class Router(httputil.HTTPServerConnectionDelegate):
    """Abstract router interface."""
    def find_handler(self, request: httputil.HTTPServerRequest, **kwargs: Any) -> httputil.HTTPMessageDelegate | None:
        """Must be implemented to return an appropriate instance of `~.httputil.HTTPMessageDelegate`
        that can serve the request.
        Routing implementations may pass additional kwargs to extend the routing logic.

        :arg httputil.HTTPServerRequest request: current HTTP request.
        :arg kwargs: additional keyword arguments passed by routing implementation.
        :returns: an instance of `~.httputil.HTTPMessageDelegate` that will be used to
            process the request.
        """
    def start_request(self, server_conn: object, request_conn: httputil.HTTPConnection) -> httputil.HTTPMessageDelegate: ...

class ReversibleRouter(Router):
    """Abstract router interface for routers that can handle named routes
    and support reversing them to original urls.
    """
    def reverse_url(self, name: str, *args: Any) -> str | None:
        """Returns url string for a given route name and arguments
        or ``None`` if no match is found.

        :arg str name: route name.
        :arg args: url parameters.
        :returns: parametrized url string for a given route name (or ``None``).
        """

class _RoutingDelegate(httputil.HTTPMessageDelegate):
    server_conn: Incomplete
    request_conn: Incomplete
    delegate: Incomplete
    router: Incomplete
    def __init__(self, router: Router, server_conn: object, request_conn: httputil.HTTPConnection) -> None: ...
    def headers_received(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders) -> Awaitable[None] | None: ...
    def data_received(self, chunk: bytes) -> Awaitable[None] | None: ...
    def finish(self) -> None: ...
    def on_connection_close(self) -> None: ...

class _DefaultMessageDelegate(httputil.HTTPMessageDelegate):
    connection: Incomplete
    def __init__(self, connection: httputil.HTTPConnection) -> None: ...
    def finish(self) -> None: ...

class RuleRouter(Router):
    """Rule-based router implementation."""
    rules: Incomplete
    def __init__(self, rules: _RuleList | None = None) -> None:
        '''Constructs a router from an ordered list of rules::

            RuleRouter([
                Rule(PathMatches("/handler"), Target),
                # ... more rules
            ])

        You can also omit explicit `Rule` constructor and use tuples of arguments::

            RuleRouter([
                (PathMatches("/handler"), Target),
            ])

        `PathMatches` is a default matcher, so the example above can be simplified::

            RuleRouter([
                ("/handler", Target),
            ])

        In the examples above, ``Target`` can be a nested `Router` instance, an instance of
        `~.httputil.HTTPServerConnectionDelegate` or an old-style callable,
        accepting a request argument.

        :arg rules: a list of `Rule` instances or tuples of `Rule`
            constructor arguments.
        '''
    def add_rules(self, rules: _RuleList) -> None:
        """Appends new rules to the router.

        :arg rules: a list of Rule instances (or tuples of arguments, which are
            passed to Rule constructor).
        """
    def process_rule(self, rule: Rule) -> Rule:
        """Override this method for additional preprocessing of each rule.

        :arg Rule rule: a rule to be processed.
        :returns: the same or modified Rule instance.
        """
    def find_handler(self, request: httputil.HTTPServerRequest, **kwargs: Any) -> httputil.HTTPMessageDelegate | None: ...
    def get_target_delegate(self, target: Any, request: httputil.HTTPServerRequest, **target_params: Any) -> httputil.HTTPMessageDelegate | None:
        """Returns an instance of `~.httputil.HTTPMessageDelegate` for a
        Rule's target. This method is called by `~.find_handler` and can be
        extended to provide additional target types.

        :arg target: a Rule's target.
        :arg httputil.HTTPServerRequest request: current request.
        :arg target_params: additional parameters that can be useful
            for `~.httputil.HTTPMessageDelegate` creation.
        """

class ReversibleRuleRouter(ReversibleRouter, RuleRouter):
    """A rule-based router that implements ``reverse_url`` method.

    Each rule added to this router may have a ``name`` attribute that can be
    used to reconstruct an original uri. The actual reconstruction takes place
    in a rule's matcher (see `Matcher.reverse`).
    """
    named_rules: Incomplete
    def __init__(self, rules: _RuleList | None = None) -> None: ...
    def process_rule(self, rule: Rule) -> Rule: ...
    def reverse_url(self, name: str, *args: Any) -> str | None: ...

class Rule:
    """A routing rule."""
    matcher: Incomplete
    target: Incomplete
    target_kwargs: Incomplete
    name: Incomplete
    def __init__(self, matcher: Matcher, target: Any, target_kwargs: Dict[str, Any] | None = None, name: str | None = None) -> None:
        """Constructs a Rule instance.

        :arg Matcher matcher: a `Matcher` instance used for determining
            whether the rule should be considered a match for a specific
            request.
        :arg target: a Rule's target (typically a ``RequestHandler`` or
            `~.httputil.HTTPServerConnectionDelegate` subclass or even a nested `Router`,
            depending on routing implementation).
        :arg dict target_kwargs: a dict of parameters that can be useful
            at the moment of target instantiation (for example, ``status_code``
            for a ``RequestHandler`` subclass). They end up in
            ``target_params['target_kwargs']`` of `RuleRouter.get_target_delegate`
            method.
        :arg str name: the name of the rule that can be used to find it
            in `ReversibleRouter.reverse_url` implementation.
        """
    def reverse(self, *args: Any) -> str | None: ...

class Matcher:
    """Represents a matcher for request features."""
    def match(self, request: httputil.HTTPServerRequest) -> Dict[str, Any] | None:
        """Matches current instance against the request.

        :arg httputil.HTTPServerRequest request: current HTTP request
        :returns: a dict of parameters to be passed to the target handler
            (for example, ``handler_kwargs``, ``path_args``, ``path_kwargs``
            can be passed for proper `~.web.RequestHandler` instantiation).
            An empty dict is a valid (and common) return value to indicate a match
            when the argument-passing features are not used.
            ``None`` must be returned to indicate that there is no match."""
    def reverse(self, *args: Any) -> str | None:
        """Reconstructs full url from matcher instance and additional arguments."""

class AnyMatches(Matcher):
    """Matches any request."""
    def match(self, request: httputil.HTTPServerRequest) -> Dict[str, Any] | None: ...

class HostMatches(Matcher):
    """Matches requests from hosts specified by ``host_pattern`` regex."""
    host_pattern: Incomplete
    def __init__(self, host_pattern: str | Pattern) -> None: ...
    def match(self, request: httputil.HTTPServerRequest) -> Dict[str, Any] | None: ...

class DefaultHostMatches(Matcher):
    """Matches requests from host that is equal to application's default_host.
    Always returns no match if ``X-Real-Ip`` header is present.
    """
    application: Incomplete
    host_pattern: Incomplete
    def __init__(self, application: Any, host_pattern: Pattern) -> None: ...
    def match(self, request: httputil.HTTPServerRequest) -> Dict[str, Any] | None: ...

class PathMatches(Matcher):
    """Matches requests with paths specified by ``path_pattern`` regex."""
    regex: Incomplete
    def __init__(self, path_pattern: str | Pattern) -> None: ...
    def match(self, request: httputil.HTTPServerRequest) -> Dict[str, Any] | None: ...
    def reverse(self, *args: Any) -> str | None: ...

class URLSpec(Rule):
    """Specifies mappings between URLs and handlers.

    .. versionchanged: 4.5
       `URLSpec` is now a subclass of a `Rule` with `PathMatches` matcher and is preserved for
       backwards compatibility.
    """
    regex: Incomplete
    handler_class: Incomplete
    kwargs: Incomplete
    def __init__(self, pattern: str | Pattern, handler: Any, kwargs: Dict[str, Any] | None = None, name: str | None = None) -> None:
        """Parameters:

        * ``pattern``: Regular expression to be matched. Any capturing
          groups in the regex will be passed in to the handler's
          get/post/etc methods as arguments (by keyword if named, by
          position if unnamed. Named and unnamed capturing groups
          may not be mixed in the same rule).

        * ``handler``: `~.web.RequestHandler` subclass to be invoked.

        * ``kwargs`` (optional): A dictionary of additional arguments
          to be passed to the handler's constructor.

        * ``name`` (optional): A name for this handler.  Used by
          `~.web.Application.reverse_url`.

        """
