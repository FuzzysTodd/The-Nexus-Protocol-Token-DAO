from . import helpers as helpers, presets as presets
from .common import normalize_url as normalize_url, utils as utils
from .parser_block import ParserBlock as ParserBlock
from .parser_core import ParserCore as ParserCore
from .parser_inline import ParserInline as ParserInline
from .renderer import RendererHTML as RendererHTML, RendererProtocol as RendererProtocol
from .rules_core.state_core import StateCore as StateCore
from .token import Token as Token
from .utils import EnvType as EnvType, OptionsDict as OptionsDict, OptionsType as OptionsType, PresetType as PresetType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Iterable, Mapping
from typing import Any, Literal, overload

class MarkdownIt:
    utils: Incomplete
    helpers: Incomplete
    inline: Incomplete
    block: Incomplete
    core: Incomplete
    renderer: Incomplete
    linkify: Incomplete
    def __init__(self, config: str | PresetType = 'commonmark', options_update: Mapping[str, Any] | None = None, *, renderer_cls: Callable[[MarkdownIt], RendererProtocol] = ...) -> None:
        '''Main parser class

        :param config: name of configuration to load or a pre-defined dictionary
        :param options_update: dictionary that will be merged into ``config["options"]``
        :param renderer_cls: the class to load as the renderer:
            ``self.renderer = renderer_cls(self)
        '''
    @overload
    def __getitem__(self, name: Literal['inline']) -> ParserInline: ...
    @overload
    def __getitem__(self, name: Literal['block']) -> ParserBlock: ...
    @overload
    def __getitem__(self, name: Literal['core']) -> ParserCore: ...
    @overload
    def __getitem__(self, name: Literal['renderer']) -> RendererProtocol: ...
    @overload
    def __getitem__(self, name: str) -> Any: ...
    options: Incomplete
    def set(self, options: OptionsType) -> None:
        """Set parser options (in the same format as in constructor).
        Probably, you will never need it, but you can change options after constructor call.

        __Note:__ To achieve the best possible performance, don't modify a
        `markdown-it` instance options on the fly. If you need multiple configurations
        it's best to create multiple instances and initialize each with separate config.
        """
    def configure(self, presets: str | PresetType, options_update: Mapping[str, Any] | None = None) -> MarkdownIt:
        """Batch load of all options and component settings.
        This is an internal method, and you probably will not need it.
        But if you will - see available presets and data structure
        [here](https://github.com/markdown-it/markdown-it/tree/master/lib/presets)

        We strongly recommend to use presets instead of direct config loads.
        That will give better compatibility with next versions.
        """
    def get_all_rules(self) -> dict[str, list[str]]:
        """Return the names of all active rules."""
    def get_active_rules(self) -> dict[str, list[str]]:
        """Return the names of all active rules."""
    def enable(self, names: str | Iterable[str], ignoreInvalid: bool = False) -> MarkdownIt:
        """Enable list or rules. (chainable)

        :param names: rule name or list of rule names to enable.
        :param ignoreInvalid: set `true` to ignore errors when rule not found.

        It will automatically find appropriate components,
        containing rules with given names. If rule not found, and `ignoreInvalid`
        not set - throws exception.

        Example::

            md = MarkdownIt().enable(['sub', 'sup']).disable('smartquotes')

        """
    def disable(self, names: str | Iterable[str], ignoreInvalid: bool = False) -> MarkdownIt:
        """The same as [[MarkdownIt.enable]], but turn specified rules off. (chainable)

        :param names: rule name or list of rule names to disable.
        :param ignoreInvalid: set `true` to ignore errors when rule not found.

        """
    def reset_rules(self) -> Generator[None, None, None]:
        """A context manager, that will reset the current enabled rules on exit."""
    def add_render_rule(self, name: str, function: Callable[..., Any], fmt: str = 'html') -> None:
        """Add a rule for rendering a particular Token type.

        Only applied when ``renderer.__output__ == fmt``
        """
    def use(self, plugin: Callable[..., None], *params: Any, **options: Any) -> MarkdownIt:
        """Load specified plugin with given params into current parser instance. (chainable)

        It's just a sugar to call `plugin(md, params)` with curring.

        Example::

            def func(tokens, idx):
                tokens[idx].content = tokens[idx].content.replace('foo', 'bar')
            md = MarkdownIt().use(plugin, 'foo_replace', 'text', func)

        """
    def parse(self, src: str, env: EnvType | None = None) -> list[Token]:
        '''Parse the source string to a token stream

        :param src: source string
        :param env: environment sandbox

        Parse input string and return list of block tokens (special token type
        "inline" will contain list of inline tokens).

        `env` is used to pass data between "distributed" rules and return additional
        metadata like reference info, needed for the renderer. It also can be used to
        inject data in specific cases. Usually, you will be ok to pass `{}`,
        and then pass updated object to renderer.
        '''
    def render(self, src: str, env: EnvType | None = None) -> Any:
        """Render markdown string into html. It does all magic for you :).

        :param src: source string
        :param env: environment sandbox
        :returns: The output of the loaded renderer

        `env` can be used to inject additional metadata (`{}` by default).
        But you will not need it with high probability. See also comment
        in [[MarkdownIt.parse]].
        """
    def parseInline(self, src: str, env: EnvType | None = None) -> list[Token]:
        """The same as [[MarkdownIt.parse]] but skip all block rules.

        :param src: source string
        :param env: environment sandbox

        It returns the
        block tokens list with the single `inline` element, containing parsed inline
        tokens in `children` property. Also updates `env` object.
        """
    def renderInline(self, src: str, env: EnvType | None = None) -> Any:
        """Similar to [[MarkdownIt.render]] but for single paragraph content.

        :param src: source string
        :param env: environment sandbox

        Similar to [[MarkdownIt.render]] but for single paragraph content. Result
        will NOT be wrapped into `<p>` tags.
        """
    def validateLink(self, url: str) -> bool:
        """Validate if the URL link is allowed in output.

        This validator can prohibit more than really needed to prevent XSS.
        It's a tradeoff to keep code simple and to be secure by default.

        Note: the url should be normalized at this point, and existing entities decoded.
        """
    def normalizeLink(self, url: str) -> str:
        """Normalize destination URLs in links

        ::

            [label]:   destination   'title'
                    ^^^^^^^^^^^
        """
    def normalizeLinkText(self, link: str) -> str:
        """Normalize autolink content

        ::

            <destination>
            ~~~~~~~~~~~
        """
