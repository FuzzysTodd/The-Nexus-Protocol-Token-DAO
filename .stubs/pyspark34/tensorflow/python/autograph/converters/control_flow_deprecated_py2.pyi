from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.lang import directives as directives
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, cfg as cfg, parser as parser, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity, annos as annos, liveness as liveness, reaching_definitions as reaching_definitions, reaching_fndefs as reaching_fndefs

class ControlFlowTransformer(converter.Base):
    """Transforms control flow structures like loops an conditionals."""
    def visit_If(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...

class AnnotatedDef(reaching_definitions.Definition):
    directives: Incomplete
    def __init__(self) -> None: ...

def transform(node, ctx): ...
