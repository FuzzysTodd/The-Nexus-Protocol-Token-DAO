from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, templates as templates

class VariableAccessTransformer(converter.Base):
    '''Rewrites basic symbol reads.

  This transformer rewrites variable reads with a "read" operator which allows
  tracking activity.

  Example:

  For a basic statement:

      a = b + c

  This is translated to:

      a = ld(b) + ld(c)

  Augmented assignment operations also introduce a `ld` operator:

      a += b

  The assignment target also receives an operator to properly represent the
  read:

      a = ld(a)
      a += ld(b)
  '''
    def visit_Name(self, node): ...
    def visit_Delete(self, node): ...
    def visit_AugAssign(self, node): ...

def transform(node, ctx): ...
