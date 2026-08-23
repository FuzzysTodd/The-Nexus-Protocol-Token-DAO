import os
import typing
import typing as t
import typing_extensions as te
import weakref
from . import nodes as nodes
from .bccache import BytecodeCache as BytecodeCache
from .compiler import CodeGenerator as CodeGenerator, generate as generate
from .defaults import BLOCK_END_STRING as BLOCK_END_STRING, BLOCK_START_STRING as BLOCK_START_STRING, COMMENT_END_STRING as COMMENT_END_STRING, COMMENT_START_STRING as COMMENT_START_STRING, DEFAULT_FILTERS as DEFAULT_FILTERS, DEFAULT_NAMESPACE as DEFAULT_NAMESPACE, DEFAULT_POLICIES as DEFAULT_POLICIES, DEFAULT_TESTS as DEFAULT_TESTS, KEEP_TRAILING_NEWLINE as KEEP_TRAILING_NEWLINE, LINE_COMMENT_PREFIX as LINE_COMMENT_PREFIX, LINE_STATEMENT_PREFIX as LINE_STATEMENT_PREFIX, LSTRIP_BLOCKS as LSTRIP_BLOCKS, NEWLINE_SEQUENCE as NEWLINE_SEQUENCE, TRIM_BLOCKS as TRIM_BLOCKS, VARIABLE_END_STRING as VARIABLE_END_STRING, VARIABLE_START_STRING as VARIABLE_START_STRING
from .exceptions import TemplateNotFound as TemplateNotFound, TemplateRuntimeError as TemplateRuntimeError, TemplateSyntaxError as TemplateSyntaxError, TemplatesNotFound as TemplatesNotFound, UndefinedError as UndefinedError
from .ext import Extension as Extension
from .lexer import Lexer as Lexer, TokenStream as TokenStream, get_lexer as get_lexer
from .loaders import BaseLoader as BaseLoader
from .nodes import EvalContext as EvalContext
from .parser import Parser as Parser
from .runtime import Context as Context, Undefined as Undefined, new_context as new_context
from .utils import LRUCache as LRUCache, concat as concat, consume as consume, import_string as import_string, internalcode as internalcode, missing as missing
from _typeshed import Incomplete
from markupsafe import Markup
from types import CodeType

def get_spontaneous_environment(cls, *args: t.Any) -> _env_bound:
    """Return a new spontaneous environment. A spontaneous environment
    is used for templates created directly rather than through an
    existing environment.

    :param cls: Environment class to create.
    :param args: Positional arguments passed to environment.
    """
def create_cache(size: int) -> t.MutableMapping[t.Tuple[weakref.ref, str], 'Template'] | None:
    """Return the cache class for the given size."""
def copy_cache(cache: t.MutableMapping | None) -> t.MutableMapping[t.Tuple[weakref.ref, str], 'Template'] | None:
    """Create an empty copy of the given cache."""
def load_extensions(environment: Environment, extensions: t.Sequence[str | t.Type['Extension']]) -> t.Dict[str, 'Extension']:
    """Load the extensions from the list and bind it to the environment.
    Returns a dict of instantiated extensions.
    """

class Environment:
    """The core component of Jinja is the `Environment`.  It contains
    important shared variables like configuration, filters, tests,
    globals and others.  Instances of this class may be modified if
    they are not shared and if no template was loaded so far.
    Modifications on environments after the first template was loaded
    will lead to surprising effects and undefined behavior.

    Here are the possible initialization parameters:

        `block_start_string`
            The string marking the beginning of a block.  Defaults to ``'{%'``.

        `block_end_string`
            The string marking the end of a block.  Defaults to ``'%}'``.

        `variable_start_string`
            The string marking the beginning of a print statement.
            Defaults to ``'{{'``.

        `variable_end_string`
            The string marking the end of a print statement.  Defaults to
            ``'}}'``.

        `comment_start_string`
            The string marking the beginning of a comment.  Defaults to ``'{#'``.

        `comment_end_string`
            The string marking the end of a comment.  Defaults to ``'#}'``.

        `line_statement_prefix`
            If given and a string, this will be used as prefix for line based
            statements.  See also :ref:`line-statements`.

        `line_comment_prefix`
            If given and a string, this will be used as prefix for line based
            comments.  See also :ref:`line-statements`.

            .. versionadded:: 2.2

        `trim_blocks`
            If this is set to ``True`` the first newline after a block is
            removed (block, not variable tag!).  Defaults to `False`.

        `lstrip_blocks`
            If this is set to ``True`` leading spaces and tabs are stripped
            from the start of a line to a block.  Defaults to `False`.

        `newline_sequence`
            The sequence that starts a newline.  Must be one of ``'\\r'``,
            ``'\\n'`` or ``'\\r\\n'``.  The default is ``'\\n'`` which is a
            useful default for Linux and OS X systems as well as web
            applications.

        `keep_trailing_newline`
            Preserve the trailing newline when rendering templates.
            The default is ``False``, which causes a single newline,
            if present, to be stripped from the end of the template.

            .. versionadded:: 2.7

        `extensions`
            List of Jinja extensions to use.  This can either be import paths
            as strings or extension classes.  For more information have a
            look at :ref:`the extensions documentation <jinja-extensions>`.

        `optimized`
            should the optimizer be enabled?  Default is ``True``.

        `undefined`
            :class:`Undefined` or a subclass of it that is used to represent
            undefined values in the template.

        `finalize`
            A callable that can be used to process the result of a variable
            expression before it is output.  For example one can convert
            ``None`` implicitly into an empty string here.

        `autoescape`
            If set to ``True`` the XML/HTML autoescaping feature is enabled by
            default.  For more details about autoescaping see
            :class:`~markupsafe.Markup`.  As of Jinja 2.4 this can also
            be a callable that is passed the template name and has to
            return ``True`` or ``False`` depending on autoescape should be
            enabled by default.

            .. versionchanged:: 2.4
               `autoescape` can now be a function

        `loader`
            The template loader for this environment.

        `cache_size`
            The size of the cache.  Per default this is ``400`` which means
            that if more than 400 templates are loaded the loader will clean
            out the least recently used template.  If the cache size is set to
            ``0`` templates are recompiled all the time, if the cache size is
            ``-1`` the cache will not be cleaned.

            .. versionchanged:: 2.8
               The cache size was increased to 400 from a low 50.

        `auto_reload`
            Some loaders load templates from locations where the template
            sources may change (ie: file system or database).  If
            ``auto_reload`` is set to ``True`` (default) every time a template is
            requested the loader checks if the source changed and if yes, it
            will reload the template.  For higher performance it's possible to
            disable that.

        `bytecode_cache`
            If set to a bytecode cache object, this object will provide a
            cache for the internal Jinja bytecode so that templates don't
            have to be parsed if they were not changed.

            See :ref:`bytecode-cache` for more information.

        `enable_async`
            If set to true this enables async template execution which
            allows using async functions and generators.
    """
    sandboxed: bool
    overlayed: bool
    linked_to: Environment | None
    shared: bool
    code_generator_class: t.Type['CodeGenerator']
    concat: Incomplete
    context_class: t.Type[Context]
    template_class: t.Type['Template']
    block_start_string: Incomplete
    block_end_string: Incomplete
    variable_start_string: Incomplete
    variable_end_string: Incomplete
    comment_start_string: Incomplete
    comment_end_string: Incomplete
    line_statement_prefix: Incomplete
    line_comment_prefix: Incomplete
    trim_blocks: Incomplete
    lstrip_blocks: Incomplete
    newline_sequence: Incomplete
    keep_trailing_newline: Incomplete
    undefined: Incomplete
    optimized: Incomplete
    finalize: Incomplete
    autoescape: Incomplete
    filters: Incomplete
    tests: Incomplete
    globals: Incomplete
    loader: Incomplete
    cache: Incomplete
    bytecode_cache: Incomplete
    auto_reload: Incomplete
    policies: Incomplete
    extensions: Incomplete
    is_async: Incomplete
    def __init__(self, block_start_string: str = ..., block_end_string: str = ..., variable_start_string: str = ..., variable_end_string: str = ..., comment_start_string: str = ..., comment_end_string: str = ..., line_statement_prefix: str | None = ..., line_comment_prefix: str | None = ..., trim_blocks: bool = ..., lstrip_blocks: bool = ..., newline_sequence: te.Literal['\n', '\r\n', '\r'] = ..., keep_trailing_newline: bool = ..., extensions: t.Sequence[str | t.Type['Extension']] = (), optimized: bool = True, undefined: t.Type[Undefined] = ..., finalize: t.Callable[..., t.Any] | None = None, autoescape: bool | t.Callable[[str | None], bool] = False, loader: BaseLoader | None = None, cache_size: int = 400, auto_reload: bool = True, bytecode_cache: BytecodeCache | None = None, enable_async: bool = False) -> None: ...
    def add_extension(self, extension: str | t.Type['Extension']) -> None:
        """Adds an extension after the environment was created.

        .. versionadded:: 2.5
        """
    def extend(self, **attributes: t.Any) -> None:
        """Add the items to the instance of the environment if they do not exist
        yet.  This is used by :ref:`extensions <writing-extensions>` to register
        callbacks and configuration values without breaking inheritance.
        """
    def overlay(self, block_start_string: str = ..., block_end_string: str = ..., variable_start_string: str = ..., variable_end_string: str = ..., comment_start_string: str = ..., comment_end_string: str = ..., line_statement_prefix: str | None = ..., line_comment_prefix: str | None = ..., trim_blocks: bool = ..., lstrip_blocks: bool = ..., newline_sequence: te.Literal['\n', '\r\n', '\r'] = ..., keep_trailing_newline: bool = ..., extensions: t.Sequence[str | t.Type['Extension']] = ..., optimized: bool = ..., undefined: t.Type[Undefined] = ..., finalize: t.Callable[..., t.Any] | None = ..., autoescape: bool | t.Callable[[str | None], bool] = ..., loader: BaseLoader | None = ..., cache_size: int = ..., auto_reload: bool = ..., bytecode_cache: BytecodeCache | None = ..., enable_async: bool = False) -> Environment:
        """Create a new overlay environment that shares all the data with the
        current environment except for cache and the overridden attributes.
        Extensions cannot be removed for an overlayed environment.  An overlayed
        environment automatically gets all the extensions of the environment it
        is linked to plus optional extra extensions.

        Creating overlays should happen after the initial environment was set
        up completely.  Not all attributes are truly linked, some are just
        copied over so modifications on the original environment may not shine
        through.

        .. versionchanged:: 3.1.2
            Added the ``newline_sequence``,, ``keep_trailing_newline``,
            and ``enable_async`` parameters to match ``__init__``.
        """
    @property
    def lexer(self) -> Lexer:
        """The lexer for this environment."""
    def iter_extensions(self) -> t.Iterator['Extension']:
        """Iterates over the extensions by priority."""
    def getitem(self, obj: t.Any, argument: str | t.Any) -> t.Any | Undefined:
        """Get an item or attribute of an object but prefer the item."""
    def getattr(self, obj: t.Any, attribute: str) -> t.Any:
        """Get an item or attribute of an object but prefer the attribute.
        Unlike :meth:`getitem` the attribute *must* be a string.
        """
    def call_filter(self, name: str, value: t.Any, args: t.Sequence[t.Any] | None = None, kwargs: t.Mapping[str, t.Any] | None = None, context: Context | None = None, eval_ctx: EvalContext | None = None) -> t.Any:
        """Invoke a filter on a value the same way the compiler does.

        This might return a coroutine if the filter is running from an
        environment in async mode and the filter supports async
        execution. It's your responsibility to await this if needed.

        .. versionadded:: 2.7
        """
    def call_test(self, name: str, value: t.Any, args: t.Sequence[t.Any] | None = None, kwargs: t.Mapping[str, t.Any] | None = None, context: Context | None = None, eval_ctx: EvalContext | None = None) -> t.Any:
        """Invoke a test on a value the same way the compiler does.

        This might return a coroutine if the test is running from an
        environment in async mode and the test supports async execution.
        It's your responsibility to await this if needed.

        .. versionchanged:: 3.0
            Tests support ``@pass_context``, etc. decorators. Added
            the ``context`` and ``eval_ctx`` parameters.

        .. versionadded:: 2.7
        """
    def parse(self, source: str, name: str | None = None, filename: str | None = None) -> nodes.Template:
        """Parse the sourcecode and return the abstract syntax tree.  This
        tree of nodes is used by the compiler to convert the template into
        executable source- or bytecode.  This is useful for debugging or to
        extract information from templates.

        If you are :ref:`developing Jinja extensions <writing-extensions>`
        this gives you a good overview of the node tree generated.
        """
    def lex(self, source: str, name: str | None = None, filename: str | None = None) -> t.Iterator[t.Tuple[int, str, str]]:
        """Lex the given sourcecode and return a generator that yields
        tokens as tuples in the form ``(lineno, token_type, value)``.
        This can be useful for :ref:`extension development <writing-extensions>`
        and debugging templates.

        This does not perform preprocessing.  If you want the preprocessing
        of the extensions to be applied you have to filter source through
        the :meth:`preprocess` method.
        """
    def preprocess(self, source: str, name: str | None = None, filename: str | None = None) -> str:
        """Preprocesses the source with all extensions.  This is automatically
        called for all parsing and compiling methods but *not* for :meth:`lex`
        because there you usually only want the actual source tokenized.
        """
    @typing.overload
    def compile(self, source: str | nodes.Template, name: str | None = None, filename: str | None = None, raw: te.Literal[False] = False, defer_init: bool = False) -> CodeType: ...
    @typing.overload
    def compile(self, source: str | nodes.Template, name: str | None = None, filename: str | None = None, raw: te.Literal[True] = ..., defer_init: bool = False) -> str: ...
    def compile_expression(self, source: str, undefined_to_none: bool = True) -> TemplateExpression:
        '''A handy helper method that returns a callable that accepts keyword
        arguments that appear as variables in the expression.  If called it
        returns the result of the expression.

        This is useful if applications want to use the same rules as Jinja
        in template "configuration files" or similar situations.

        Example usage:

        >>> env = Environment()
        >>> expr = env.compile_expression(\'foo == 42\')
        >>> expr(foo=23)
        False
        >>> expr(foo=42)
        True

        Per default the return value is converted to `None` if the
        expression returns an undefined value.  This can be changed
        by setting `undefined_to_none` to `False`.

        >>> env.compile_expression(\'var\')() is None
        True
        >>> env.compile_expression(\'var\', undefined_to_none=False)()
        Undefined

        .. versionadded:: 2.1
        '''
    def compile_templates(self, target: str | os.PathLike, extensions: t.Collection[str] | None = None, filter_func: t.Callable[[str], bool] | None = None, zip: str | None = 'deflated', log_function: t.Callable[[str], None] | None = None, ignore_errors: bool = True) -> None:
        """Finds all the templates the loader can find, compiles them
        and stores them in `target`.  If `zip` is `None`, instead of in a
        zipfile, the templates will be stored in a directory.
        By default a deflate zip algorithm is used. To switch to
        the stored algorithm, `zip` can be set to ``'stored'``.

        `extensions` and `filter_func` are passed to :meth:`list_templates`.
        Each template returned will be compiled to the target folder or
        zipfile.

        By default template compilation errors are ignored.  In case a
        log function is provided, errors are logged.  If you want template
        syntax errors to abort the compilation you can set `ignore_errors`
        to `False` and you will get an exception on syntax errors.

        .. versionadded:: 2.4
        """
    def list_templates(self, extensions: t.Collection[str] | None = None, filter_func: t.Callable[[str], bool] | None = None) -> t.List[str]:
        """Returns a list of templates for this environment.  This requires
        that the loader supports the loader's
        :meth:`~BaseLoader.list_templates` method.

        If there are other files in the template folder besides the
        actual templates, the returned list can be filtered.  There are two
        ways: either `extensions` is set to a list of file extensions for
        templates, or a `filter_func` can be provided which is a callable that
        is passed a template name and should return `True` if it should end up
        in the result list.

        If the loader does not support that, a :exc:`TypeError` is raised.

        .. versionadded:: 2.4
        """
    def handle_exception(self, source: str | None = None) -> te.NoReturn:
        """Exception handling helper.  This is used internally to either raise
        rewritten exceptions or return a rendered traceback for the template.
        """
    def join_path(self, template: str, parent: str) -> str:
        """Join a template with the parent.  By default all the lookups are
        relative to the loader root so this method returns the `template`
        parameter unchanged, but if the paths should be relative to the
        parent template, this function can be used to calculate the real
        template name.

        Subclasses may override this method and implement template path
        joining here.
        """
    def get_template(self, name: str | Template, parent: str | None = None, globals: t.MutableMapping[str, t.Any] | None = None) -> Template:
        '''Load a template by name with :attr:`loader` and return a
        :class:`Template`. If the template does not exist a
        :exc:`TemplateNotFound` exception is raised.

        :param name: Name of the template to load. When loading
            templates from the filesystem, "/" is used as the path
            separator, even on Windows.
        :param parent: The name of the parent template importing this
            template. :meth:`join_path` can be used to implement name
            transformations with this.
        :param globals: Extend the environment :attr:`globals` with
            these extra variables available for all renders of this
            template. If the template has already been loaded and
            cached, its globals are updated with any new items.

        .. versionchanged:: 3.0
            If a template is loaded from cache, ``globals`` will update
            the template\'s globals instead of ignoring the new values.

        .. versionchanged:: 2.4
            If ``name`` is a :class:`Template` object it is returned
            unchanged.
        '''
    def select_template(self, names: t.Iterable[str | Template], parent: str | None = None, globals: t.MutableMapping[str, t.Any] | None = None) -> Template:
        """Like :meth:`get_template`, but tries loading multiple names.
        If none of the names can be loaded a :exc:`TemplatesNotFound`
        exception is raised.

        :param names: List of template names to try loading in order.
        :param parent: The name of the parent template importing this
            template. :meth:`join_path` can be used to implement name
            transformations with this.
        :param globals: Extend the environment :attr:`globals` with
            these extra variables available for all renders of this
            template. If the template has already been loaded and
            cached, its globals are updated with any new items.

        .. versionchanged:: 3.0
            If a template is loaded from cache, ``globals`` will update
            the template's globals instead of ignoring the new values.

        .. versionchanged:: 2.11
            If ``names`` is :class:`Undefined`, an :exc:`UndefinedError`
            is raised instead. If no templates were found and ``names``
            contains :class:`Undefined`, the message is more helpful.

        .. versionchanged:: 2.4
            If ``names`` contains a :class:`Template` object it is
            returned unchanged.

        .. versionadded:: 2.3
        """
    def get_or_select_template(self, template_name_or_list: str | Template | t.List[str | Template], parent: str | None = None, globals: t.MutableMapping[str, t.Any] | None = None) -> Template:
        """Use :meth:`select_template` if an iterable of template names
        is given, or :meth:`get_template` if one name is given.

        .. versionadded:: 2.3
        """
    def from_string(self, source: str | nodes.Template, globals: t.MutableMapping[str, t.Any] | None = None, template_class: t.Type['Template'] | None = None) -> Template:
        """Load a template from a source string without using
        :attr:`loader`.

        :param source: Jinja source to compile into a template.
        :param globals: Extend the environment :attr:`globals` with
            these extra variables available for all renders of this
            template. If the template has already been loaded and
            cached, its globals are updated with any new items.
        :param template_class: Return an instance of this
            :class:`Template` class.
        """
    def make_globals(self, d: t.MutableMapping[str, t.Any] | None) -> t.MutableMapping[str, t.Any]:
        """Make the globals map for a template. Any given template
        globals overlay the environment :attr:`globals`.

        Returns a :class:`collections.ChainMap`. This allows any changes
        to a template's globals to only affect that template, while
        changes to the environment's globals are still reflected.
        However, avoid modifying any globals after a template is loaded.

        :param d: Dict of template-specific globals.

        .. versionchanged:: 3.0
            Use :class:`collections.ChainMap` to always prevent mutating
            environment globals.
        """

class Template:
    """A compiled template that can be rendered.

    Use the methods on :class:`Environment` to create or load templates.
    The environment is used to configure how templates are compiled and
    behave.

    It is also possible to create a template object directly. This is
    not usually recommended. The constructor takes most of the same
    arguments as :class:`Environment`. All templates created with the
    same environment arguments share the same ephemeral ``Environment``
    instance behind the scenes.

    A template object should be considered immutable. Modifications on
    the object are not supported.
    """
    environment_class: t.Type[Environment]
    environment: Environment
    globals: t.MutableMapping[str, t.Any]
    name: str | None
    filename: str | None
    blocks: t.Dict[str, t.Callable[[Context], t.Iterator[str]]]
    root_render_func: t.Callable[[Context], t.Iterator[str]]
    def __new__(cls, source: str | nodes.Template, block_start_string: str = ..., block_end_string: str = ..., variable_start_string: str = ..., variable_end_string: str = ..., comment_start_string: str = ..., comment_end_string: str = ..., line_statement_prefix: str | None = ..., line_comment_prefix: str | None = ..., trim_blocks: bool = ..., lstrip_blocks: bool = ..., newline_sequence: te.Literal['\n', '\r\n', '\r'] = ..., keep_trailing_newline: bool = ..., extensions: t.Sequence[str | t.Type['Extension']] = (), optimized: bool = True, undefined: t.Type[Undefined] = ..., finalize: t.Callable[..., t.Any] | None = None, autoescape: bool | t.Callable[[str | None], bool] = False, enable_async: bool = False) -> t.Any: ...
    @classmethod
    def from_code(cls, environment: Environment, code: CodeType, globals: t.MutableMapping[str, t.Any], uptodate: t.Callable[[], bool] | None = None) -> Template:
        """Creates a template object from compiled code and the globals.  This
        is used by the loaders and environment to create a template object.
        """
    @classmethod
    def from_module_dict(cls, environment: Environment, module_dict: t.MutableMapping[str, t.Any], globals: t.MutableMapping[str, t.Any]) -> Template:
        """Creates a template object from a module.  This is used by the
        module loader to create a template object.

        .. versionadded:: 2.4
        """
    def render(self, *args: t.Any, **kwargs: t.Any) -> str:
        """This method accepts the same arguments as the `dict` constructor:
        A dict, a dict subclass or some keyword arguments.  If no arguments
        are given the context will be empty.  These two calls do the same::

            template.render(knights='that say nih')
            template.render({'knights': 'that say nih'})

        This will return the rendered template as a string.
        """
    async def render_async(self, *args: t.Any, **kwargs: t.Any) -> str:
        """This works similar to :meth:`render` but returns a coroutine
        that when awaited returns the entire rendered template string.  This
        requires the async feature to be enabled.

        Example usage::

            await template.render_async(knights='that say nih; asynchronously')
        """
    def stream(self, *args: t.Any, **kwargs: t.Any) -> TemplateStream:
        """Works exactly like :meth:`generate` but returns a
        :class:`TemplateStream`.
        """
    def generate(self, *args: t.Any, **kwargs: t.Any) -> t.Iterator[str]:
        """For very large templates it can be useful to not render the whole
        template at once but evaluate each statement after another and yield
        piece for piece.  This method basically does exactly that and returns
        a generator that yields one item after another as strings.

        It accepts the same arguments as :meth:`render`.
        """
    async def generate_async(self, *args: t.Any, **kwargs: t.Any) -> t.AsyncIterator[str]:
        """An async version of :meth:`generate`.  Works very similarly but
        returns an async iterator instead.
        """
    def new_context(self, vars: t.Dict[str, t.Any] | None = None, shared: bool = False, locals: t.Mapping[str, t.Any] | None = None) -> Context:
        """Create a new :class:`Context` for this template.  The vars
        provided will be passed to the template.  Per default the globals
        are added to the context.  If shared is set to `True` the data
        is passed as is to the context without adding the globals.

        `locals` can be a dict of local variables for internal usage.
        """
    def make_module(self, vars: t.Dict[str, t.Any] | None = None, shared: bool = False, locals: t.Mapping[str, t.Any] | None = None) -> TemplateModule:
        """This method works like the :attr:`module` attribute when called
        without arguments but it will evaluate the template on every call
        rather than caching it.  It's also possible to provide
        a dict which is then used as context.  The arguments are the same
        as for the :meth:`new_context` method.
        """
    async def make_module_async(self, vars: t.Dict[str, t.Any] | None = None, shared: bool = False, locals: t.Mapping[str, t.Any] | None = None) -> TemplateModule:
        """As template module creation can invoke template code for
        asynchronous executions this method must be used instead of the
        normal :meth:`make_module` one.  Likewise the module attribute
        becomes unavailable in async mode.
        """
    @property
    def module(self) -> TemplateModule:
        """The template as module.  This is used for imports in the
        template runtime but is also useful if one wants to access
        exported template variables from the Python layer:

        >>> t = Template('{% macro foo() %}42{% endmacro %}23')
        >>> str(t.module)
        '23'
        >>> t.module.foo() == u'42'
        True

        This attribute is not available if async mode is enabled.
        """
    def get_corresponding_lineno(self, lineno: int) -> int:
        """Return the source line number of a line number in the
        generated bytecode as they are not in sync.
        """
    @property
    def is_up_to_date(self) -> bool:
        """If this variable is `False` there is a newer version available."""
    @property
    def debug_info(self) -> t.List[t.Tuple[int, int]]:
        """The debug info mapping."""

class TemplateModule:
    """Represents an imported template.  All the exported names of the
    template are available as attributes on this object.  Additionally
    converting it into a string renders the contents.
    """
    def __init__(self, template: Template, context: Context, body_stream: t.Iterable[str] | None = None) -> None: ...
    def __html__(self) -> Markup: ...

class TemplateExpression:
    """The :meth:`jinja2.Environment.compile_expression` method returns an
    instance of this object.  It encapsulates the expression-like access
    to the template with an expression it wraps.
    """
    def __init__(self, template: Template, undefined_to_none: bool) -> None: ...
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any | None: ...

class TemplateStream:
    """A template stream works pretty much like an ordinary python generator
    but it can buffer multiple items to reduce the number of total iterations.
    Per default the output is unbuffered which means that for every unbuffered
    instruction in the template one string is yielded.

    If buffering is enabled with a buffer size of 5, five items are combined
    into a new string.  This is mainly useful if you are streaming
    big templates to a client via WSGI which flushes after each iteration.
    """
    def __init__(self, gen: t.Iterator[str]) -> None: ...
    def dump(self, fp: str | t.IO, encoding: str | None = None, errors: str | None = 'strict') -> None:
        """Dump the complete stream into a file or file-like object.
        Per default strings are written, if you want to encode
        before writing specify an `encoding`.

        Example usage::

            Template('Hello {{ name }}!').stream(name='foo').dump('hello.html')
        """
    buffered: bool
    def disable_buffering(self) -> None:
        """Disable the output buffering."""
    def enable_buffering(self, size: int = 5) -> None:
        """Enable buffering.  Buffer `size` items before yielding them."""
    def __iter__(self) -> TemplateStream: ...
    def __next__(self) -> str: ...
