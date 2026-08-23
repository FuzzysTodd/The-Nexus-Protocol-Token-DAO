import abc
import typing as t
import typing_extensions as te
from . import defaults as defaults, nodes as nodes
from .environment import Environment as Environment
from .exceptions import TemplateAssertionError as TemplateAssertionError, TemplateSyntaxError as TemplateSyntaxError
from .lexer import Token as Token, TokenStream as TokenStream
from .parser import Parser as Parser
from .runtime import Context as Context, Undefined as Undefined, concat as concat
from .utils import import_string as import_string, pass_context as pass_context
from _typeshed import Incomplete

class _TranslationsBasic(te.Protocol):
    def gettext(self, message: str) -> str: ...
    def ngettext(self, singular: str, plural: str, n: int) -> str: ...

class _TranslationsContext(_TranslationsBasic, metaclass=abc.ABCMeta):
    def pgettext(self, context: str, message: str) -> str: ...
    def npgettext(self, context: str, singular: str, plural: str, n: int) -> str: ...

GETTEXT_FUNCTIONS: t.Tuple[str, ...]

class Extension:
    """Extensions can be used to add extra functionality to the Jinja template
    system at the parser level.  Custom extensions are bound to an environment
    but may not store environment specific data on `self`.  The reason for
    this is that an extension can be bound to another environment (for
    overlays) by creating a copy and reassigning the `environment` attribute.

    As extensions are created by the environment they cannot accept any
    arguments for configuration.  One may want to work around that by using
    a factory function, but that is not possible as extensions are identified
    by their import name.  The correct way to configure the extension is
    storing the configuration values on the environment.  Because this way the
    environment ends up acting as central configuration storage the
    attributes may clash which is why extensions have to ensure that the names
    they choose for configuration are not too generic.  ``prefix`` for example
    is a terrible name, ``fragment_cache_prefix`` on the other hand is a good
    name as includes the name of the extension (fragment cache).
    """
    identifier: t.ClassVar[str]
    def __init_subclass__(cls) -> None: ...
    tags: t.Set[str]
    priority: int
    environment: Incomplete
    def __init__(self, environment: Environment) -> None: ...
    def bind(self, environment: Environment) -> Extension:
        """Create a copy of this extension bound to another environment."""
    def preprocess(self, source: str, name: str | None, filename: str | None = None) -> str:
        """This method is called before the actual lexing and can be used to
        preprocess the source.  The `filename` is optional.  The return value
        must be the preprocessed source.
        """
    def filter_stream(self, stream: TokenStream) -> TokenStream | t.Iterable['Token']:
        """It's passed a :class:`~jinja2.lexer.TokenStream` that can be used
        to filter tokens returned.  This method has to return an iterable of
        :class:`~jinja2.lexer.Token`\\s, but it doesn't have to return a
        :class:`~jinja2.lexer.TokenStream`.
        """
    def parse(self, parser: Parser) -> nodes.Node | t.List[nodes.Node]:
        """If any of the :attr:`tags` matched this method is called with the
        parser as first argument.  The token the parser stream is pointing at
        is the name token that matched.  This method has to return one or a
        list of multiple nodes.
        """
    def attr(self, name: str, lineno: int | None = None) -> nodes.ExtensionAttribute:
        """Return an attribute node for the current extension.  This is useful
        to pass constants on extensions to generated template code.

        ::

            self.attr('_my_attribute', lineno=lineno)
        """
    def call_method(self, name: str, args: t.List[nodes.Expr] | None = None, kwargs: t.List[nodes.Keyword] | None = None, dyn_args: nodes.Expr | None = None, dyn_kwargs: nodes.Expr | None = None, lineno: int | None = None) -> nodes.Call:
        """Call a method of the extension.  This is a shortcut for
        :meth:`attr` + :class:`jinja2.nodes.Call`.
        """

class InternationalizationExtension(Extension):
    """This extension adds gettext support to Jinja."""
    tags: Incomplete
    def __init__(self, environment: Environment) -> None: ...
    def parse(self, parser: Parser) -> nodes.Node | t.List[nodes.Node]:
        """Parse a translatable tag."""

class ExprStmtExtension(Extension):
    """Adds a `do` tag to Jinja that works like the print statement just
    that it doesn't print the return value.
    """
    tags: Incomplete
    def parse(self, parser: Parser) -> nodes.ExprStmt: ...

class LoopControlExtension(Extension):
    """Adds break and continue to the template engine."""
    tags: Incomplete
    def parse(self, parser: Parser) -> nodes.Break | nodes.Continue: ...

class DebugExtension(Extension):
    """A ``{% debug %}`` tag that dumps the available variables,
    filters, and tests.

    .. code-block:: html+jinja

        <pre>{% debug %}</pre>

    .. code-block:: text

        {'context': {'cycler': <class 'jinja2.utils.Cycler'>,
                     ...,
                     'namespace': <class 'jinja2.utils.Namespace'>},
         'filters': ['abs', 'attr', 'batch', 'capitalize', 'center', 'count', 'd',
                     ..., 'urlencode', 'urlize', 'wordcount', 'wordwrap', 'xmlattr'],
         'tests': ['!=', '<', '<=', '==', '>', '>=', 'callable', 'defined',
                   ..., 'odd', 'sameas', 'sequence', 'string', 'undefined', 'upper']}

    .. versionadded:: 2.11.0
    """
    tags: Incomplete
    def parse(self, parser: Parser) -> nodes.Output: ...

def extract_from_ast(ast: nodes.Template, gettext_functions: t.Sequence[str] = ..., babel_style: bool = True) -> t.Iterator[t.Tuple[int, str, str | None | t.Tuple[str | None, ...]]]:
    '''Extract localizable strings from the given template node.  Per
    default this function returns matches in babel style that means non string
    parameters as well as keyword arguments are returned as `None`.  This
    allows Babel to figure out what you really meant if you are using
    gettext functions that allow keyword arguments for placeholder expansion.
    If you don\'t want that behavior set the `babel_style` parameter to `False`
    which causes only strings to be returned and parameters are always stored
    in tuples.  As a consequence invalid gettext calls (calls without a single
    string parameter or string parameters after non-string parameters) are
    skipped.

    This example explains the behavior:

    >>> from jinja2 import Environment
    >>> env = Environment()
    >>> node = env.parse(\'{{ (_("foo"), _(), ngettext("foo", "bar", 42)) }}\')
    >>> list(extract_from_ast(node))
    [(1, \'_\', \'foo\'), (1, \'_\', ()), (1, \'ngettext\', (\'foo\', \'bar\', None))]
    >>> list(extract_from_ast(node, babel_style=False))
    [(1, \'_\', (\'foo\',)), (1, \'ngettext\', (\'foo\', \'bar\'))]

    For every string found this function yields a ``(lineno, function,
    message)`` tuple, where:

    * ``lineno`` is the number of the line on which the string was found,
    * ``function`` is the name of the ``gettext`` function used (if the
      string was extracted from embedded Python code), and
    *   ``message`` is the string, or a tuple of strings for functions
         with multiple string arguments.

    This extraction function operates on the AST and is because of that unable
    to extract any comments.  For comment support you have to use the babel
    extraction interface or extract comments yourself.
    '''

class _CommentFinder:
    """Helper class to find comments in a token stream.  Can only
    find comments for gettext calls forwards.  Once the comment
    from line 4 is found, a comment for line 1 will not return a
    usable value.
    """
    tokens: Incomplete
    comment_tags: Incomplete
    offset: int
    last_lineno: int
    def __init__(self, tokens: t.Sequence[t.Tuple[int, str, str]], comment_tags: t.Sequence[str]) -> None: ...
    def find_backwards(self, offset: int) -> t.List[str]: ...
    def find_comments(self, lineno: int) -> t.List[str]: ...

def babel_extract(fileobj: t.BinaryIO, keywords: t.Sequence[str], comment_tags: t.Sequence[str], options: t.Dict[str, t.Any]) -> t.Iterator[t.Tuple[int, str, str | None | t.Tuple[str | None, ...], t.List[str]]]:
    """Babel extraction method for Jinja templates.

    .. versionchanged:: 2.3
       Basic support for translation comments was added.  If `comment_tags`
       is now set to a list of keywords for extraction, the extractor will
       try to find the best preceding comment that begins with one of the
       keywords.  For best results, make sure to not have more than one
       gettext call in one line of code and the matching comment in the
       same line or the line before.

    .. versionchanged:: 2.5.1
       The `newstyle_gettext` flag can be set to `True` to enable newstyle
       gettext calls.

    .. versionchanged:: 2.7
       A `silent` option can now be provided.  If set to `False` template
       syntax errors are propagated instead of being ignored.

    :param fileobj: the file-like object the messages should be extracted from
    :param keywords: a list of keywords (i.e. function names) that should be
                     recognized as translation functions
    :param comment_tags: a list of translator tags to search for and include
                         in the results.
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)`` tuples.
             (comments will be empty currently)
    """
i18n = InternationalizationExtension
do = ExprStmtExtension
loopcontrols = LoopControlExtension
debug = DebugExtension
