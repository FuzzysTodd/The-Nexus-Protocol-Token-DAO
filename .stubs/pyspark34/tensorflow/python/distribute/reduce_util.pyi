import enum
from tensorflow.python.ops import variable_scope as variable_scope
from tensorflow.python.util.tf_export import tf_export as tf_export

class ReduceOp(enum.Enum):
    '''Indicates how a set of values should be reduced.

  * `SUM`: Add all the values.
  * `MEAN`: Take the arithmetic mean ("average") of the values.
  '''
    SUM: str
    MEAN: str
    @staticmethod
    def from_variable_aggregation(aggregation): ...
