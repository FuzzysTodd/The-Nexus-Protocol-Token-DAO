from tensorflow.python.ops.gen_io_ops import *
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.lib.io import python_io as python_io
from tensorflow.python.ops import gen_data_flow_ops as gen_data_flow_ops, gen_io_ops as gen_io_ops, gen_parsing_ops as gen_parsing_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def read_file(filename, name: Incomplete | None = None):
    '''Reads the contents of file.

  This operation returns a tensor with the entire contents of the input
  filename. It does not do any parsing, it just returns the contents as
  they are. Usually, this is the first step in the input pipeline.

  Example:

  >>> with open("/tmp/file.txt", "w") as f:
  ...   f.write("asdf")
  ...
  4
  >>> tf.io.read_file("/tmp/file.txt")
  <tf.Tensor: shape=(), dtype=string, numpy=b\'asdf\'>

  Example of using the op in a function to read an image, decode it and reshape
  the tensor containing the pixel data:

  >>> @tf.function
  ... def load_image(filename):
  ...   raw = tf.io.read_file(filename)
  ...   image = tf.image.decode_png(raw, channels=3)
  ...   # the `print` executes during tracing.
  ...   print("Initial shape: ", image.shape)
  ...   image.set_shape([28, 28, 3])
  ...   print("Final shape: ", image.shape)
  ...   return image

  Args:
    filename: string. filename to read from.
    name: string.  Optional name for the op.

  Returns:
    A tensor of dtype "string", with the file contents.
  '''
def serialize_tensor(tensor, name: Incomplete | None = None):
    '''Transforms a Tensor into a serialized TensorProto proto.

  This operation transforms data in a `tf.Tensor` into a `tf.Tensor` of type
  `tf.string` containing the data in a binary string format. This operation can
  transform scalar data and linear arrays, but it is most useful in converting
  multidimensional arrays into a format accepted by binary storage formats such
  as a `TFRecord` or `tf.train.Example`.

  See also:
  - `tf.io.parse_tensor`: inverse operation of `tf.io.serialize_tensor` that
  transforms a scalar string containing a serialized Tensor into a Tensor of a
  specified type.
  - `tf.ensure_shape`: `parse_tensor` cannot statically determine the shape of
  the parsed tensor. Use `tf.ensure_shape` to set the static shape when running
  under a `tf.function`
  - `.SerializeToString`, serializes a proto to a binary-string

  Example of serializing scalar data:

  >>> t = tf.constant(1)
  >>> tf.io.serialize_tensor(t)
  <tf.Tensor: shape=(), dtype=string, numpy=b\'\\x08...\\x00\'>

  Example of storing non-scalar data into a `tf.train.Example`:

  >>> t1 = [[1, 2]]
  >>> t2 = [[7, 8]]
  >>> nonscalar = tf.concat([t1, t2], 0)
  >>> nonscalar
  <tf.Tensor: shape=(2, 2), dtype=int32, numpy=
  array([[1, 2],
         [7, 8]], dtype=int32)>

  Serialize the data using `tf.io.serialize_tensor`.

  >>> serialized_nonscalar = tf.io.serialize_tensor(nonscalar)
  >>> serialized_nonscalar
  <tf.Tensor: shape=(), dtype=string, numpy=b\'\\x08...\\x00\'>

  Store the data in a `tf.train.Feature`.

  >>> feature_of_bytes = tf.train.Feature(
  ...   bytes_list=tf.train.BytesList(value=[serialized_nonscalar.numpy()]))
  >>> feature_of_bytes
  bytes_list {
    value: "\\010...\\000"
  }

  Put the `tf.train.Feature` message into a `tf.train.Example`.

  >>> features_for_example = {
  ...   \'feature0\': feature_of_bytes
  ... }
  >>> example_proto = tf.train.Example(
  ...   features=tf.train.Features(feature=features_for_example))
  >>> example_proto
  features {
    feature {
      key: "feature0"
      value {
        bytes_list {
          value: "\\010...\\000"
        }
      }
    }
  }

  Args:
    tensor: A `tf.Tensor`.
    name: string.  Optional name for the op.

  Returns:
    A Tensor of dtype string.
  '''

class ReaderBase:
    """Base class for different Reader types, that produce a record every step.

  Conceptually, Readers convert string 'work units' into records (key,
  value pairs).  Typically the 'work units' are filenames and the
  records are extracted from the contents of those files.  We want a
  single record produced per step, but a work unit can correspond to
  many records.

  Therefore we introduce some decoupling using a queue.  The queue
  contains the work units and the Reader dequeues from the queue when
  it is asked to produce a record (via Read()) but it has finished the
  last work unit.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, reader_ref, supports_serialize: bool = False) -> None:
        """Creates a new ReaderBase.

    Args:
      reader_ref: The operation that implements the reader.
      supports_serialize: True if the reader implementation can
        serialize its state.

    Raises:
      RuntimeError: If eager execution is enabled.
    """
    @property
    def reader_ref(self):
        """Op that implements the reader."""
    def read(self, queue, name: Incomplete | None = None):
        """Returns the next record (key, value) pair produced by a reader.

    Will dequeue a work unit from queue if necessary (e.g. when the
    Reader needs to start reading from a new file since it has
    finished with the previous file).

    Args:
      queue: A Queue or a mutable string Tensor representing a handle
        to a Queue, with string work items.
      name: A name for the operation (optional).

    Returns:
      A tuple of Tensors (key, value).
      key: A string scalar Tensor.
      value: A string scalar Tensor.
    """
    def read_up_to(self, queue, num_records, name: Incomplete | None = None):
        """Returns up to num_records (key, value) pairs produced by a reader.

    Will dequeue a work unit from queue if necessary (e.g., when the
    Reader needs to start reading from a new file since it has
    finished with the previous file).
    It may return less than num_records even before the last batch.

    Args:
      queue: A Queue or a mutable string Tensor representing a handle
        to a Queue, with string work items.
      num_records: Number of records to read.
      name: A name for the operation (optional).

    Returns:
      A tuple of Tensors (keys, values).
      keys: A 1-D string Tensor.
      values: A 1-D string Tensor.
    """
    def num_records_produced(self, name: Incomplete | None = None):
        """Returns the number of records this reader has produced.

    This is the same as the number of Read executions that have
    succeeded.

    Args:
      name: A name for the operation (optional).

    Returns:
      An int64 Tensor.

    """
    def num_work_units_completed(self, name: Incomplete | None = None):
        """Returns the number of work units this reader has finished processing.

    Args:
      name: A name for the operation (optional).

    Returns:
      An int64 Tensor.
    """
    def serialize_state(self, name: Incomplete | None = None):
        """Produce a string tensor that encodes the state of a reader.

    Not all Readers support being serialized, so this can produce an
    Unimplemented error.

    Args:
      name: A name for the operation (optional).

    Returns:
      A string Tensor.
    """
    def restore_state(self, state, name: Incomplete | None = None):
        """Restore a reader to a previously saved state.

    Not all Readers support being restored, so this can produce an
    Unimplemented error.

    Args:
      state: A string Tensor.
        Result of a SerializeState of a Reader with matching type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
    @property
    def supports_serialize(self):
        """Whether the Reader implementation can serialize its state."""
    def reset(self, name: Incomplete | None = None):
        """Restore a reader to its initial clean state.

    Args:
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """

class WholeFileReader(ReaderBase):
    """A Reader that outputs the entire contents of a file as a value.

  To use, enqueue filenames in a Queue.  The output of Read will
  be a filename (key) and the contents of that file (value).

  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, name: Incomplete | None = None) -> None:
        """Create a WholeFileReader.

    Args:
      name: A name for the operation (optional).
    """

class TextLineReader(ReaderBase):
    """A Reader that outputs the lines of a file delimited by newlines.

  Newlines are stripped from the output.
  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, skip_header_lines: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Create a TextLineReader.

    Args:
      skip_header_lines: An optional int. Defaults to 0.  Number of lines
        to skip from the beginning of every file.
      name: A name for the operation (optional).
    """

class FixedLengthRecordReader(ReaderBase):
    """A Reader that outputs fixed-length records from a file.

  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, record_bytes, header_bytes: Incomplete | None = None, footer_bytes: Incomplete | None = None, hop_bytes: Incomplete | None = None, name: Incomplete | None = None, encoding: Incomplete | None = None) -> None:
        """Create a FixedLengthRecordReader.

    Args:
      record_bytes: An int.
      header_bytes: An optional int. Defaults to 0.
      footer_bytes: An optional int. Defaults to 0.
      hop_bytes: An optional int. Defaults to 0.
      name: A name for the operation (optional).
      encoding: The type of encoding for the file. Defaults to none.
    """

class TFRecordReader(ReaderBase):
    """A Reader that outputs the records from a TFRecords file.

  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, name: Incomplete | None = None, options: Incomplete | None = None) -> None:
        """Create a TFRecordReader.

    Args:
      name: A name for the operation (optional).
      options: A TFRecordOptions object (optional).
    """

class LMDBReader(ReaderBase):
    """A Reader that outputs the records from a LMDB file.

  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, name: Incomplete | None = None, options: Incomplete | None = None) -> None:
        """Create a LMDBReader.

    Args:
      name: A name for the operation (optional).
      options: A LMDBRecordOptions object (optional).
    """

class IdentityReader(ReaderBase):
    """A Reader that outputs the queued work as both the key and value.

  To use, enqueue strings in a Queue.  Read will take the front
  work string and output (work, work).

  See ReaderBase for supported methods.

  @compatibility(eager)
  Readers are not compatible with eager execution. Instead, please
  use `tf.data` to get data into your model.
  @end_compatibility
  """
    def __init__(self, name: Incomplete | None = None) -> None:
        """Create a IdentityReader.

    Args:
      name: A name for the operation (optional).
    """
