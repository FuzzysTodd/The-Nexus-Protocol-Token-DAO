from _typeshed import Incomplete
from tornado import escape as escape
from tornado.log import app_log as app_log
from tornado.util import ObjectDict as ObjectDict, exec_in as exec_in, unicode_type as unicode_type
from typing import Any, ContextManager, Dict, Iterable, List, TextIO

class _UnsetMarker: ...

def filter_whitespace(mode: str, text: str) -> str:
    """Transform whitespace in ``text`` according to ``mode``.

    Available modes are:

    * ``all``: Return all whitespace unmodified.
    * ``single``: Collapse consecutive whitespace with a single whitespace
      character, preserving newlines.
    * ``oneline``: Collapse all runs of whitespace into a single space
      character, removing all newlines in the process.

    .. versionadded:: 4.3
    """

class Template:
    """A compiled template.

    We compile into Python from the given template_string. You can generate
    the template from variables with generate().
    """
    name: Incomplete
    autoescape: Incomplete
    namespace: Incomplete
    file: Incomplete
    code: Incomplete
    loader: Incomplete
    compiled: Incomplete
    def __init__(self, template_string: str | bytes, name: str = '<string>', loader: BaseLoader | None = None, compress_whitespace: bool | _UnsetMarker = ..., autoescape: str | _UnsetMarker | None = ..., whitespace: str | None = None) -> None:
        '''Construct a Template.

        :arg str template_string: the contents of the template file.
        :arg str name: the filename from which the template was loaded
            (used for error message).
        :arg tornado.template.BaseLoader loader: the `~tornado.template.BaseLoader` responsible
            for this template, used to resolve ``{% include %}`` and ``{% extend %}`` directives.
        :arg bool compress_whitespace: Deprecated since Tornado 4.3.
            Equivalent to ``whitespace="single"`` if true and
            ``whitespace="all"`` if false.
        :arg str autoescape: The name of a function in the template
            namespace, or ``None`` to disable escaping by default.
        :arg str whitespace: A string specifying treatment of whitespace;
            see `filter_whitespace` for options.

        .. versionchanged:: 4.3
           Added ``whitespace`` parameter; deprecated ``compress_whitespace``.
        '''
    def generate(self, **kwargs: Any) -> bytes:
        """Generate this template with the given arguments."""

class BaseLoader:
    """Base class for template loaders.

    You must use a template loader to use template constructs like
    ``{% extends %}`` and ``{% include %}``. The loader caches all
    templates after they are loaded the first time.
    """
    autoescape: Incomplete
    namespace: Incomplete
    whitespace: Incomplete
    templates: Incomplete
    lock: Incomplete
    def __init__(self, autoescape: str = ..., namespace: Dict[str, Any] | None = None, whitespace: str | None = None) -> None:
        '''Construct a template loader.

        :arg str autoescape: The name of a function in the template
            namespace, such as "xhtml_escape", or ``None`` to disable
            autoescaping by default.
        :arg dict namespace: A dictionary to be added to the default template
            namespace, or ``None``.
        :arg str whitespace: A string specifying default behavior for
            whitespace in templates; see `filter_whitespace` for options.
            Default is "single" for files ending in ".html" and ".js" and
            "all" for other files.

        .. versionchanged:: 4.3
           Added ``whitespace`` parameter.
        '''
    def reset(self) -> None:
        """Resets the cache of compiled templates."""
    def resolve_path(self, name: str, parent_path: str | None = None) -> str:
        """Converts a possibly-relative path to absolute (used internally)."""
    def load(self, name: str, parent_path: str | None = None) -> Template:
        """Loads a template."""

class Loader(BaseLoader):
    """A template loader that loads from a single root directory."""
    root: Incomplete
    def __init__(self, root_directory: str, **kwargs: Any) -> None: ...
    def resolve_path(self, name: str, parent_path: str | None = None) -> str: ...

class DictLoader(BaseLoader):
    """A template loader that loads from a dictionary."""
    dict: Incomplete
    def __init__(self, dict: Dict[str, str], **kwargs: Any) -> None: ...
    def resolve_path(self, name: str, parent_path: str | None = None) -> str: ...

class _Node:
    def each_child(self) -> Iterable['_Node']: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def find_named_blocks(self, loader: BaseLoader | None, named_blocks: Dict[str, '_NamedBlock']) -> None: ...

class _File(_Node):
    template: Incomplete
    body: Incomplete
    line: int
    def __init__(self, template: Template, body: _ChunkList) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def each_child(self) -> Iterable['_Node']: ...

class _ChunkList(_Node):
    chunks: Incomplete
    def __init__(self, chunks: List[_Node]) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def each_child(self) -> Iterable['_Node']: ...

class _NamedBlock(_Node):
    name: Incomplete
    body: Incomplete
    template: Incomplete
    line: Incomplete
    def __init__(self, name: str, body: _Node, template: Template, line: int) -> None: ...
    def each_child(self) -> Iterable['_Node']: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def find_named_blocks(self, loader: BaseLoader | None, named_blocks: Dict[str, '_NamedBlock']) -> None: ...

class _ExtendsBlock(_Node):
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class _IncludeBlock(_Node):
    name: Incomplete
    template_name: Incomplete
    line: Incomplete
    def __init__(self, name: str, reader: _TemplateReader, line: int) -> None: ...
    def find_named_blocks(self, loader: BaseLoader | None, named_blocks: Dict[str, _NamedBlock]) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _ApplyBlock(_Node):
    method: Incomplete
    line: Incomplete
    body: Incomplete
    def __init__(self, method: str, line: int, body: _Node) -> None: ...
    def each_child(self) -> Iterable['_Node']: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _ControlBlock(_Node):
    statement: Incomplete
    line: Incomplete
    body: Incomplete
    def __init__(self, statement: str, line: int, body: _Node) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _IntermediateControlBlock(_Node):
    statement: Incomplete
    line: Incomplete
    def __init__(self, statement: str, line: int) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Statement(_Node):
    statement: Incomplete
    line: Incomplete
    def __init__(self, statement: str, line: int) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Expression(_Node):
    expression: Incomplete
    line: Incomplete
    raw: Incomplete
    def __init__(self, expression: str, line: int, raw: bool = False) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Module(_Expression):
    def __init__(self, expression: str, line: int) -> None: ...

class _Text(_Node):
    value: Incomplete
    line: Incomplete
    whitespace: Incomplete
    def __init__(self, value: str, line: int, whitespace: str) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class ParseError(Exception):
    """Raised for template syntax errors.

    ``ParseError`` instances have ``filename`` and ``lineno`` attributes
    indicating the position of the error.

    .. versionchanged:: 4.3
       Added ``filename`` and ``lineno`` attributes.
    """
    message: Incomplete
    filename: Incomplete
    lineno: Incomplete
    def __init__(self, message: str, filename: str | None = None, lineno: int = 0) -> None: ...

class _CodeWriter:
    file: Incomplete
    named_blocks: Incomplete
    loader: Incomplete
    current_template: Incomplete
    apply_counter: int
    include_stack: Incomplete
    def __init__(self, file: TextIO, named_blocks: Dict[str, _NamedBlock], loader: BaseLoader | None, current_template: Template) -> None: ...
    def indent_size(self) -> int: ...
    def indent(self) -> ContextManager: ...
    def include(self, template: Template, line: int) -> ContextManager: ...
    def write_line(self, line: str, line_number: int, indent: int | None = None) -> None: ...

class _TemplateReader:
    name: Incomplete
    text: Incomplete
    whitespace: Incomplete
    line: int
    pos: int
    def __init__(self, name: str, text: str, whitespace: str) -> None: ...
    def find(self, needle: str, start: int = 0, end: int | None = None) -> int: ...
    def consume(self, count: int | None = None) -> str: ...
    def remaining(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: int | slice) -> str: ...
    def raise_parse_error(self, msg: str) -> None: ...
