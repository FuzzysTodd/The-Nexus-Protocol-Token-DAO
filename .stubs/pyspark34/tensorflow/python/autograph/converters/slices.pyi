from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.lang import directives as directives
from tensorflow.python.autograph.pyct import templates as templates

class SliceTransformer(converter.Base):
    """Converts slicing operations to their TF counterpart.

  Currently, relying on the default slice operator that Tensor uses is
  insufficient, because TensorArray and tensor lists use dedicated index read
  and write functions.
  """
    def visit_Assign(self, node): ...
    def visit_Subscript(self, node): ...

def transform(node, ctx): ...
