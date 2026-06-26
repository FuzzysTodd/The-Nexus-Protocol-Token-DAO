from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops, from_tensor_slices_op as from_tensor_slices_op, structured_function as structured_function
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class _TextLineDataset(dataset_ops.DatasetSource):
    """A `Dataset` comprising records from one or more text files."""
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `TextLineDataset`.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer. A value of 0 results in the default buffering values chosen
        based on the compression type.
      name: (Optional.) A name for the tf.data operation.
    '''
    @property
    def element_spec(self): ...

class TextLineDatasetV2(dataset_ops.DatasetSource):
    '''Creates a `Dataset` comprising lines from one or more text files.

  The `tf.data.TextLineDataset` loads text from text files and creates a dataset
  where each line of the files becomes an element of the dataset.

  For example, suppose we have 2 files "text_lines0.txt" and "text_lines1.txt"
  with the following lines:

  >>> with open(\'/tmp/text_lines0.txt\', \'w\') as f:
  ...   f.write(\'the cow\\n\')
  ...   f.write(\'jumped over\\n\')
  ...   f.write(\'the moon\\n\')
  >>> with open(\'/tmp/text_lines1.txt\', \'w\') as f:
  ...   f.write(\'jack and jill\\n\')
  ...   f.write(\'went up\\n\')
  ...   f.write(\'the hill\\n\')

  We can construct a TextLineDataset from them as follows:

  >>> dataset = tf.data.TextLineDataset([\'/tmp/text_lines0.txt\',
  ...                                    \'/tmp/text_lines1.txt\'])

  The elements of the dataset are expected to be:

  >>> for element in dataset.as_numpy_iterator():
  ...   print(element)
  b\'the cow\'
  b\'jumped over\'
  b\'the moon\'
  b\'jack and jill\'
  b\'went up\'
  b\'the hill\'
  '''
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `TextLineDataset`.

    The elements of the dataset will be the lines of the input files, using
    the newline character \'\\n\' to denote line splits. The newline characters
    will be stripped off of each element.

    Args:
      filenames: A `tf.data.Dataset` whose elements are `tf.string` scalars, a
        `tf.string` tensor, or a value that can be converted to a `tf.string`
        tensor (such as a list of Python strings).
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer. A value of 0 results in the default buffering values chosen
        based on the compression type.
      num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
        number of files to read in parallel. If greater than one, the records of
        files read in parallel are outputted in an interleaved order. If your
        input pipeline is I/O bottlenecked, consider setting this parameter to a
        value greater than one to parallelize the I/O. If `None`, files will be
        read sequentially.
      name: (Optional.) A name for the tf.data operation.
    '''
    @property
    def element_spec(self): ...

class TextLineDatasetV1(dataset_ops.DatasetV1Adapter):
    """A `Dataset` comprising lines from one or more text files."""
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

class _TFRecordDataset(dataset_ops.DatasetSource):
    """A `Dataset` comprising records from one or more TFRecord files."""
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `TFRecordDataset`.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes in the read buffer. 0 means no buffering.
      name: (Optional.) A name for the tf.data operation.
    '''
    @property
    def element_spec(self): ...

class ParallelInterleaveDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over its input and flattens the result."""
    def __init__(self, input_dataset, map_func, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, name: Incomplete | None = None) -> None:
        """See `tf.data.experimental.parallel_interleave()` for details."""
    @property
    def element_spec(self): ...

class TFRecordDatasetV2(dataset_ops.DatasetV2):
    '''A `Dataset` comprising records from one or more TFRecord files.

  This dataset loads TFRecords from the files as bytes, exactly as they were
  written.`TFRecordDataset` does not do any parsing or decoding on its own.
  Parsing and decoding can be done by applying `Dataset.map` transformations
  after the `TFRecordDataset`.

  A minimal example is given below:

  >>> import tempfile
  >>> example_path = os.path.join(tempfile.gettempdir(), "example.tfrecords")
  >>> np.random.seed(0)

  >>> # Write the records to a file.
  ... with tf.io.TFRecordWriter(example_path) as file_writer:
  ...   for _ in range(4):
  ...     x, y = np.random.random(), np.random.random()
  ...
  ...     record_bytes = tf.train.Example(features=tf.train.Features(feature={
  ...         "x": tf.train.Feature(float_list=tf.train.FloatList(value=[x])),
  ...         "y": tf.train.Feature(float_list=tf.train.FloatList(value=[y])),
  ...     })).SerializeToString()
  ...     file_writer.write(record_bytes)

  >>> # Read the data back out.
  >>> def decode_fn(record_bytes):
  ...   return tf.io.parse_single_example(
  ...       # Data
  ...       record_bytes,
  ...
  ...       # Schema
  ...       {"x": tf.io.FixedLenFeature([], dtype=tf.float32),
  ...        "y": tf.io.FixedLenFeature([], dtype=tf.float32)}
  ...   )

  >>> for batch in tf.data.TFRecordDataset([example_path]).map(decode_fn):
  ...   print("x = {x:.4f},  y = {y:.4f}".format(**batch))
  x = 0.5488,  y = 0.7152
  x = 0.6028,  y = 0.5449
  x = 0.4237,  y = 0.6459
  x = 0.4376,  y = 0.8918
  '''
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `TFRecordDataset` to read one or more TFRecord files.

    Each element of the dataset will contain a single TFRecord.

    Args:
      filenames: A `tf.string` tensor or `tf.data.Dataset` containing one or
        more filenames.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes in the read buffer. If your input pipeline is I/O bottlenecked,
        consider setting this parameter to a value 1-100 MBs. If `None`, a
        sensible default for both local and remote file systems is used.
      num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
        number of files to read in parallel. If greater than one, the records of
        files read in parallel are outputted in an interleaved order. If your
        input pipeline is I/O bottlenecked, consider setting this parameter to a
        value greater than one to parallelize the I/O. If `None`, files will be
        read sequentially.
      name: (Optional.) A name for the tf.data operation.

    Raises:
      TypeError: If any argument does not have the expected type.
      ValueError: If any argument does not have the expected shape.
    '''
    @property
    def element_spec(self): ...

class TFRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    """A `Dataset` comprising records from one or more TFRecord files."""
    def __init__(self, filenames, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

class _FixedLengthRecordDataset(dataset_ops.DatasetSource):
    """A `Dataset` of fixed-length records from one or more binary files."""
    def __init__(self, filenames, record_bytes, header_bytes: Incomplete | None = None, footer_bytes: Incomplete | None = None, buffer_size: Incomplete | None = None, compression_type: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `FixedLengthRecordDataset`.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      record_bytes: A `tf.int64` scalar representing the number of bytes in each
        record.
      header_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to skip at the start of a file.
      footer_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to ignore at the end of a file.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes to buffer when reading.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      name: (Optional.) A name for the tf.data operation.
    '''
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV2(dataset_ops.DatasetSource):
    '''A `Dataset` of fixed-length records from one or more binary files.

  The `tf.data.FixedLengthRecordDataset` reads fixed length records from binary
  files and creates a dataset where each record becomes an element of the
  dataset. The binary files can have a fixed length header and a fixed length
  footer, which will both be skipped.

  For example, suppose we have 2 files "fixed_length0.bin" and
  "fixed_length1.bin" with the following content:

  >>> with open(\'/tmp/fixed_length0.bin\', \'wb\') as f:
  ...   f.write(b\'HEADER012345FOOTER\')
  >>> with open(\'/tmp/fixed_length1.bin\', \'wb\') as f:
  ...   f.write(b\'HEADER6789abFOOTER\')

  We can construct a `FixedLengthRecordDataset` from them as follows:

  >>> dataset1 = tf.data.FixedLengthRecordDataset(
  ...     filenames=[\'/tmp/fixed_length0.bin\', \'/tmp/fixed_length1.bin\'],
  ...     record_bytes=2, header_bytes=6, footer_bytes=6)

  The elements of the dataset are:

  >>> for element in dataset1.as_numpy_iterator():
  ...   print(element)
  b\'01\'
  b\'23\'
  b\'45\'
  b\'67\'
  b\'89\'
  b\'ab\'
  '''
    def __init__(self, filenames, record_bytes, header_bytes: Incomplete | None = None, footer_bytes: Incomplete | None = None, buffer_size: Incomplete | None = None, compression_type: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None:
        '''Creates a `FixedLengthRecordDataset`.

    Args:
      filenames: A `tf.string` tensor or `tf.data.Dataset` containing one or
        more filenames.
      record_bytes: A `tf.int64` scalar representing the number of bytes in each
        record.
      header_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to skip at the start of a file.
      footer_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to ignore at the end of a file.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes to buffer when reading.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
        number of files to read in parallel. If greater than one, the records of
        files read in parallel are outputted in an interleaved order. If your
        input pipeline is I/O bottlenecked, consider setting this parameter to a
        value greater than one to parallelize the I/O. If `None`, files will be
        read sequentially.
      name: (Optional.) A name for the tf.data operation.
    '''
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    """A `Dataset` of fixed-length records from one or more binary files."""
    def __init__(self, filenames, record_bytes, header_bytes: Incomplete | None = None, footer_bytes: Incomplete | None = None, buffer_size: Incomplete | None = None, compression_type: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
FixedLengthRecordDataset = FixedLengthRecordDatasetV2
TFRecordDataset = TFRecordDatasetV2
TextLineDataset = TextLineDatasetV2
FixedLengthRecordDataset = FixedLengthRecordDatasetV1
TFRecordDataset = TFRecordDatasetV1
TextLineDataset = TextLineDatasetV1
