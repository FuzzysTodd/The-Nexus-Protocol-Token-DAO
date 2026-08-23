from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity, annos as annos

class _Function:
    context_name: Incomplete
    def __init__(self) -> None: ...

class FunctionTransformer(converter.Base):
    """Wraps function bodies around autograph-specific boilerplate."""
    def visit_Lambda(self, node): ...
    def visit_FunctionDef(self, node): ...

def transform(node, ctx): ...
