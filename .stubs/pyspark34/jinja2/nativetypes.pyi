import typing as t
from . import nodes as nodes
from .compiler import CodeGenerator as CodeGenerator, Frame as Frame, has_safe_repr as has_safe_repr
from .environment import Environment as Environment, Template as Template
from _typeshed import Incomplete

def native_concat(values: t.Iterable[t.Any]) -> t.Any | None:
    """Return a native Python type from the list of compiled nodes. If
    the result is a single node, its value is returned. Otherwise, the
    nodes are concatenated as strings. If the result can be parsed with
    :func:`ast.literal_eval`, the parsed value is returned. Otherwise,
    the string is returned.

    :param values: Iterable of outputs to concatenate.
    """

class NativeCodeGenerator(CodeGenerator):
    """A code generator which renders Python types by not adding
    ``str()`` around output nodes.
    """

class NativeEnvironment(Environment):
    """An environment that renders templates to native Python types."""
    code_generator_class = NativeCodeGenerator
    concat: Incomplete

class NativeTemplate(Template):
    environment_class = NativeEnvironment
    def render(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Render the template to produce a native Python type. If the
        result is a single node, its value is returned. Otherwise, the
        nodes are concatenated as strings. If the result can be parsed
        with :func:`ast.literal_eval`, the parsed value is returned.
        Otherwise, the string is returned.
        """
    async def render_async(self, *args: t.Any, **kwargs: t.Any) -> t.Any: ...
