from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import templates as templates

class AssertTransformer(converter.Base):
    """Transforms Assert nodes to Call so they can be handled as functions."""
    def visit_Assert(self, node): ...

def transform(node, ctx): ...
