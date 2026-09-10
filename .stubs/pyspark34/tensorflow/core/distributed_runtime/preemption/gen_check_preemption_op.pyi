from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def check_preemption(preemption_key: str = 'TF_DEFAULT_PREEMPTION_NOTICE_KEY', name: Incomplete | None = None):
    '''Check if a preemption notice has been received in coordination service.

  Args:
    preemption_key: An optional `string`. Defaults to `"TF_DEFAULT_PREEMPTION_NOTICE_KEY"`.
      Key for preemption check in coordination service.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

CheckPreemption: Incomplete

def check_preemption_eager_fallback(preemption_key, name, ctx): ...
