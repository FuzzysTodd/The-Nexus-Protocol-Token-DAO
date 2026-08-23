from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno

class _Break:
    used: bool
    control_var_name: Incomplete
    def __init__(self) -> None: ...

class BreakTransformer(converter.Base):
    """Canonicalizes break statements into additional conditionals."""
    def visit_Break(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...

def transform(node, ctx): ...
