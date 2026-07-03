import typing as t
from . import nodes as nodes
from .compiler import CodeGenerator as CodeGenerator, Frame as Frame
from .environment import Environment as Environment
from _typeshed import Incomplete

class TrackingCodeGenerator(CodeGenerator):
    """We abuse the code generator for introspection."""
    undeclared_identifiers: Incomplete
    def __init__(self, environment: Environment) -> None: ...
    def write(self, x: str) -> None:
        """Don't write."""
    def enter_frame(self, frame: Frame) -> None:
        """Remember all undeclared identifiers."""

def find_undeclared_variables(ast: nodes.Template) -> t.Set[str]:
    """Returns a set of all variables in the AST that will be looked up from
    the context at runtime.  Because at compile time it's not known which
    variables will be used depending on the path the execution takes at
    runtime, all variables are returned.

    >>> from jinja2 import Environment, meta
    >>> env = Environment()
    >>> ast = env.parse('{% set foo = 42 %}{{ bar + foo }}')
    >>> meta.find_undeclared_variables(ast) == {'bar'}
    True

    .. admonition:: Implementation

       Internally the code generator is used for finding undeclared variables.
       This is good to know because the code generator might raise a
       :exc:`TemplateAssertionError` during compilation and as a matter of
       fact this function can currently raise that exception as well.
    """
def find_referenced_templates(ast: nodes.Template) -> t.Iterator[str | None]:
    '''Finds all the referenced templates from the AST.  This will return an
    iterator over all the hardcoded template extensions, inclusions and
    imports.  If dynamic inheritance or inclusion is used, `None` will be
    yielded.

    >>> from jinja2 import Environment, meta
    >>> env = Environment()
    >>> ast = env.parse(\'{% extends "layout.html" %}{% include helper %}\')
    >>> list(meta.find_referenced_templates(ast))
    [\'layout.html\', None]

    This function is useful for dependency tracking.  For example if you want
    to rebuild parts of the website after a layout template has changed.
    '''
