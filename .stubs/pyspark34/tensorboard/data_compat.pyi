from tensorboard.compat.proto import event_pb2 as event_pb2, summary_pb2 as summary_pb2
from tensorboard.util import tensor_util as tensor_util

def migrate_event(event): ...
def migrate_value(value):
    '''Convert `value` to a new-style value, if necessary and possible.

    An "old-style" value is a value that uses any `value` field other than
    the `tensor` field. A "new-style" value is a value that uses the
    `tensor` field. TensorBoard continues to support old-style values on
    disk; this method converts them to new-style values so that further
    code need only deal with one data format.

    Arguments:
      value: A `Summary.Value` object. This argument is not modified.

    Returns:
      If the `value` is an old-style value for which there is a new-style
      equivalent, the result is the new-style value. Otherwise---if the
      value is already new-style or does not yet have a new-style
      equivalent---the value will be returned unchanged.

    :type value: Summary.Value
    :rtype: Summary.Value
    '''
def make_summary(tag, metadata, data): ...
