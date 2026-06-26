from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import parser as parser, templates as templates

SAFE_BOOLEAN_OPERAND: str
LOGICAL_OPERATORS: Incomplete
EQUALITY_OPERATORS: Incomplete

class LogicalExpressionTransformer(converter.Base):
    """Converts logical expressions to corresponding TF calls."""
    def visit_Compare(self, node): ...
    def visit_UnaryOp(self, node): ...
    def visit_BoolOp(self, node): ...

def transform(node, ctx): ...
