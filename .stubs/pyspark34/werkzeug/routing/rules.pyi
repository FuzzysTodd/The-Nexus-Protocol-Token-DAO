import typing as t
from ..datastructures import iter_multi_items as iter_multi_items
from .converters import BaseConverter as BaseConverter, ValidationError as ValidationError
from .map import Map as Map
from _typeshed import Incomplete
from dataclasses import dataclass

class Weighting(t.NamedTuple):
    number_static_weights: int
    static_weights: list[tuple[int, int]]
    number_argument_weights: int
    argument_weights: list[int]

@dataclass
class RulePart:
    """A part of a rule.

    Rules can be represented by parts as delimited by `/` with
    instances of this class representing those parts. The *content* is
    either the raw content if *static* or a regex string to match
    against. The *weight* can be used to order parts when matching.

    """
    content: str
    final: bool
    static: bool
    suffixed: bool
    weight: Weighting
    def __init__(self, content, final, static, suffixed, weight) -> None: ...

def parse_converter_args(argstr: str) -> tuple[t.Tuple, dict[str, t.Any]]: ...

class RuleFactory:
    """As soon as you have more complex URL setups it's a good idea to use rule
    factories to avoid repetitive tasks.  Some of them are builtin, others can
    be added by subclassing `RuleFactory` and overriding `get_rules`.
    """
    def get_rules(self, map: Map) -> t.Iterable[Rule]:
        """Subclasses of `RuleFactory` have to override this method and return
        an iterable of rules."""

class Subdomain(RuleFactory):
    """All URLs provided by this factory have the subdomain set to a
    specific domain. For example if you want to use the subdomain for
    the current language this can be a good setup::

        url_map = Map([
            Rule('/', endpoint='#select_language'),
            Subdomain('<string(length=2):lang_code>', [
                Rule('/', endpoint='index'),
                Rule('/about', endpoint='about'),
                Rule('/help', endpoint='help')
            ])
        ])

    All the rules except for the ``'#select_language'`` endpoint will now
    listen on a two letter long subdomain that holds the language code
    for the current request.
    """
    subdomain: Incomplete
    rules: Incomplete
    def __init__(self, subdomain: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class Submount(RuleFactory):
    """Like `Subdomain` but prefixes the URL rule with a given string::

        url_map = Map([
            Rule('/', endpoint='index'),
            Submount('/blog', [
                Rule('/', endpoint='blog/index'),
                Rule('/entry/<entry_slug>', endpoint='blog/show')
            ])
        ])

    Now the rule ``'blog/show'`` matches ``/blog/entry/<entry_slug>``.
    """
    path: Incomplete
    rules: Incomplete
    def __init__(self, path: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class EndpointPrefix(RuleFactory):
    """Prefixes all endpoints (which must be strings for this factory) with
    another string. This can be useful for sub applications::

        url_map = Map([
            Rule('/', endpoint='index'),
            EndpointPrefix('blog/', [Submount('/blog', [
                Rule('/', endpoint='index'),
                Rule('/entry/<entry_slug>', endpoint='show')
            ])])
        ])
    """
    prefix: Incomplete
    rules: Incomplete
    def __init__(self, prefix: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class RuleTemplate:
    """Returns copies of the rules wrapped and expands string templates in
    the endpoint, rule, defaults or subdomain sections.

    Here a small example for such a rule template::

        from werkzeug.routing import Map, Rule, RuleTemplate

        resource = RuleTemplate([
            Rule('/$name/', endpoint='$name.list'),
            Rule('/$name/<int:id>', endpoint='$name.show')
        ])

        url_map = Map([resource(name='user'), resource(name='page')])

    When a rule template is called the keyword arguments are used to
    replace the placeholders in all the string parameters.
    """
    rules: Incomplete
    def __init__(self, rules: t.Iterable[Rule]) -> None: ...
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> RuleTemplateFactory: ...

class RuleTemplateFactory(RuleFactory):
    """A factory that fills in template variables into rules.  Used by
    `RuleTemplate` internally.

    :internal:
    """
    rules: Incomplete
    context: Incomplete
    def __init__(self, rules: t.Iterable[RuleFactory], context: dict[str, t.Any]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class Rule(RuleFactory):
    """A Rule represents one URL pattern.  There are some options for `Rule`
    that change the way it behaves and are passed to the `Rule` constructor.
    Note that besides the rule-string all arguments *must* be keyword arguments
    in order to not break the application on Werkzeug upgrades.

    `string`
        Rule strings basically are just normal URL paths with placeholders in
        the format ``<converter(arguments):name>`` where the converter and the
        arguments are optional.  If no converter is defined the `default`
        converter is used which means `string` in the normal configuration.

        URL rules that end with a slash are branch URLs, others are leaves.
        If you have `strict_slashes` enabled (which is the default), all
        branch URLs that are matched without a trailing slash will trigger a
        redirect to the same URL with the missing slash appended.

        The converters are defined on the `Map`.

    `endpoint`
        The endpoint for this rule. This can be anything. A reference to a
        function, a string, a number etc.  The preferred way is using a string
        because the endpoint is used for URL generation.

    `defaults`
        An optional dict with defaults for other rules with the same endpoint.
        This is a bit tricky but useful if you want to have unique URLs::

            url_map = Map([
                Rule('/all/', defaults={'page': 1}, endpoint='all_entries'),
                Rule('/all/page/<int:page>', endpoint='all_entries')
            ])

        If a user now visits ``http://example.com/all/page/1`` they will be
        redirected to ``http://example.com/all/``.  If `redirect_defaults` is
        disabled on the `Map` instance this will only affect the URL
        generation.

    `subdomain`
        The subdomain rule string for this rule. If not specified the rule
        only matches for the `default_subdomain` of the map.  If the map is
        not bound to a subdomain this feature is disabled.

        Can be useful if you want to have user profiles on different subdomains
        and all subdomains are forwarded to your application::

            url_map = Map([
                Rule('/', subdomain='<username>', endpoint='user/homepage'),
                Rule('/stats', subdomain='<username>', endpoint='user/stats')
            ])

    `methods`
        A sequence of http methods this rule applies to.  If not specified, all
        methods are allowed. For example this can be useful if you want different
        endpoints for `POST` and `GET`.  If methods are defined and the path
        matches but the method matched against is not in this list or in the
        list of another rule for that path the error raised is of the type
        `MethodNotAllowed` rather than `NotFound`.  If `GET` is present in the
        list of methods and `HEAD` is not, `HEAD` is added automatically.

    `strict_slashes`
        Override the `Map` setting for `strict_slashes` only for this rule. If
        not specified the `Map` setting is used.

    `merge_slashes`
        Override :attr:`Map.merge_slashes` for this rule.

    `build_only`
        Set this to True and the rule will never match but will create a URL
        that can be build. This is useful if you have resources on a subdomain
        or folder that are not handled by the WSGI application (like static data)

    `redirect_to`
        If given this must be either a string or callable.  In case of a
        callable it's called with the url adapter that triggered the match and
        the values of the URL as keyword arguments and has to return the target
        for the redirect, otherwise it has to be a string with placeholders in
        rule syntax::

            def foo_with_slug(adapter, id):
                # ask the database for the slug for the old id.  this of
                # course has nothing to do with werkzeug.
                return f'foo/{Foo.get_slug_for_id(id)}'

            url_map = Map([
                Rule('/foo/<slug>', endpoint='foo'),
                Rule('/some/old/url/<slug>', redirect_to='foo/<slug>'),
                Rule('/other/old/url/<int:id>', redirect_to=foo_with_slug)
            ])

        When the rule is matched the routing system will raise a
        `RequestRedirect` exception with the target for the redirect.

        Keep in mind that the URL will be joined against the URL root of the
        script so don't use a leading slash on the target URL unless you
        really mean root of that domain.

    `alias`
        If enabled this rule serves as an alias for another rule with the same
        endpoint and arguments.

    `host`
        If provided and the URL map has host matching enabled this can be
        used to provide a match rule for the whole host.  This also means
        that the subdomain feature is disabled.

    `websocket`
        If ``True``, this rule is only matches for WebSocket (``ws://``,
        ``wss://``) requests. By default, rules will only match for HTTP
        requests.

    .. versionchanged:: 2.1
        Percent-encoded newlines (``%0a``), which are decoded by WSGI
        servers, are considered when routing instead of terminating the
        match early.

    .. versionadded:: 1.0
        Added ``websocket``.

    .. versionadded:: 1.0
        Added ``merge_slashes``.

    .. versionadded:: 0.7
        Added ``alias`` and ``host``.

    .. versionchanged:: 0.6.1
       ``HEAD`` is added to ``methods`` if ``GET`` is present.
    """
    rule: Incomplete
    is_leaf: Incomplete
    is_branch: Incomplete
    map: Incomplete
    strict_slashes: Incomplete
    merge_slashes: Incomplete
    subdomain: Incomplete
    host: Incomplete
    defaults: Incomplete
    build_only: Incomplete
    alias: Incomplete
    websocket: Incomplete
    methods: Incomplete
    endpoint: Incomplete
    redirect_to: Incomplete
    arguments: Incomplete
    def __init__(self, string: str, defaults: t.Mapping[str, t.Any] | None = None, subdomain: str | None = None, methods: t.Iterable[str] | None = None, build_only: bool = False, endpoint: str | None = None, strict_slashes: bool | None = None, merge_slashes: bool | None = None, redirect_to: str | t.Callable[..., str] | None = None, alias: bool = False, host: str | None = None, websocket: bool = False) -> None: ...
    def empty(self) -> Rule:
        """
        Return an unbound copy of this rule.

        This can be useful if want to reuse an already bound URL for another
        map.  See ``get_empty_kwargs`` to override what keyword arguments are
        provided to the new copy.
        """
    def get_empty_kwargs(self) -> t.Mapping[str, t.Any]:
        """
        Provides kwargs for instantiating empty copy with empty()

        Use this method to provide custom keyword arguments to the subclass of
        ``Rule`` when calling ``some_rule.empty()``.  Helpful when the subclass
        has custom keyword arguments that are needed at instantiation.

        Must return a ``dict`` that will be provided as kwargs to the new
        instance of ``Rule``, following the initial ``self.rule`` value which
        is always provided as the first, required positional argument.
        """
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...
    def refresh(self) -> None:
        """Rebinds and refreshes the URL.  Call this if you modified the
        rule in place.

        :internal:
        """
    def bind(self, map: Map, rebind: bool = False) -> None:
        """Bind the url to a map and create a regular expression based on
        the information from the rule itself and the defaults from the map.

        :internal:
        """
    def get_converter(self, variable_name: str, converter_name: str, args: t.Tuple, kwargs: t.Mapping[str, t.Any]) -> BaseConverter:
        """Looks up the converter for the given parameter.

        .. versionadded:: 0.9
        """
    def compile(self) -> None:
        """Compiles the regular expression and stores it."""
    def build(self, values: t.Mapping[str, t.Any], append_unknown: bool = True) -> tuple[str, str] | None:
        """Assembles the relative url for that rule and the subdomain.
        If building doesn't work for some reasons `None` is returned.

        :internal:
        """
    def provides_defaults_for(self, rule: Rule) -> bool:
        """Check if this rule has defaults for a given rule.

        :internal:
        """
    def suitable_for(self, values: t.Mapping[str, t.Any], method: str | None = None) -> bool:
        """Check if the dict of values has enough data for url generation.

        :internal:
        """
    def build_compare_key(self) -> tuple[int, int, int]:
        """The build compare key for sorting.

        :internal:
        """
    def __eq__(self, other: object) -> bool: ...
    __hash__: Incomplete
