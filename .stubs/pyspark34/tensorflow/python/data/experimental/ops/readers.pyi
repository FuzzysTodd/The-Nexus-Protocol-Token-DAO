from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import error_ops as error_ops, parsing_ops as parsing_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, map_op as map_op
from tensorflow.python.data.util import convert as convert, nest as nest
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, io_ops as io_ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util.tf_export import tf_export as tf_export

def make_tf_record_dataset(file_pattern, batch_size, parser_fn: Incomplete | None = None, num_epochs: Incomplete | None = None, shuffle: bool = True, shuffle_buffer_size: Incomplete | None = None, shuffle_seed: Incomplete | None = None, prefetch_buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, num_parallel_parser_calls: Incomplete | None = None, drop_final_batch: bool = False):
    """Reads and optionally parses TFRecord files into a dataset.

  Provides common functionality such as batching, optional parsing, shuffling,
  and performant defaults.

  Args:
    file_pattern: List of files or patterns of TFRecord file paths.
      See `tf.io.gfile.glob` for pattern rules.
    batch_size: An int representing the number of records to combine
      in a single batch.
    parser_fn: (Optional.) A function accepting string input to parse
      and process the record contents. This function must map records
      to components of a fixed shape, so they may be batched. By
      default, uses the record contents unmodified.
    num_epochs: (Optional.) An int specifying the number of times this
      dataset is repeated.  If None (the default), cycles through the
      dataset forever.
    shuffle: (Optional.) A bool that indicates whether the input
      should be shuffled. Defaults to `True`.
    shuffle_buffer_size: (Optional.) Buffer size to use for
      shuffling. A large buffer size ensures better shuffling, but
      increases memory usage and startup time.
    shuffle_seed: (Optional.) Randomization seed to use for shuffling.
    prefetch_buffer_size: (Optional.) An int specifying the number of
      feature batches to prefetch for performance improvement.
      Defaults to auto-tune. Set to 0 to disable prefetching.
    num_parallel_reads: (Optional.) Number of threads used to read
      records from files. By default or if set to a value >1, the
      results will be interleaved. Defaults to `24`.
    num_parallel_parser_calls: (Optional.) Number of parallel
      records to parse in parallel. Defaults to `batch_size`.
    drop_final_batch: (Optional.) Whether the last batch should be
      dropped in case its size is smaller than `batch_size`; the
      default behavior is not to drop the smaller batch.

  Returns:
    A dataset, where each element matches the output of `parser_fn`
    except it will have an additional leading `batch-size` dimension,
    or a `batch_size`-length 1-D tensor of strings if `parser_fn` is
    unspecified.
  """
def make_csv_dataset_v2(file_pattern, batch_size, column_names: Incomplete | None = None, column_defaults: Incomplete | None = None, label_name: Incomplete | None = None, select_columns: Incomplete | None = None, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', header: bool = True, num_epochs: Incomplete | None = None, shuffle: bool = True, shuffle_buffer_size: int = 10000, shuffle_seed: Incomplete | None = None, prefetch_buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, sloppy: bool = False, num_rows_for_inference: int = 100, compression_type: Incomplete | None = None, ignore_errors: bool = False, encoding: str = 'utf-8'):
    '''Reads CSV files into a dataset.

  Reads CSV files into a dataset, where each element of the dataset is a
  (features, labels) tuple that corresponds to a batch of CSV rows. The features
  dictionary maps feature column names to `Tensor`s containing the corresponding
  feature data, and labels is a `Tensor` containing the batch\'s label data.

  By default, the first rows of the CSV files are expected to be headers listing
  the column names. If the first rows are not headers, set `header=False` and
  provide the column names with the `column_names` argument.

  By default, the dataset is repeated indefinitely, reshuffling the order each
  time. This behavior can be modified by setting the `num_epochs` and `shuffle`
  arguments.

  For example, suppose you have a CSV file containing

  | Feature_A | Feature_B |
  | --------- | --------- |
  | 1         | "a"       |
  | 2         | "b"       |
  | 3         | "c"       |
  | 4         | "d"       |

  ```
  # No label column specified
  dataset = tf.data.experimental.make_csv_dataset(filename, batch_size=2)
  iterator = dataset.as_numpy_iterator()
  print(dict(next(iterator)))
  # prints a dictionary of batched features:
  # OrderedDict([(\'Feature_A\', array([1, 4], dtype=int32)),
  #              (\'Feature_B\', array([b\'a\', b\'d\'], dtype=object))])
  ```

  ```
  # Set Feature_B as label column
  dataset = tf.data.experimental.make_csv_dataset(
      filename, batch_size=2, label_name="Feature_B")
  iterator = dataset.as_numpy_iterator()
  print(next(iterator))
  # prints (features, labels) tuple:
  # (OrderedDict([(\'Feature_A\', array([1, 2], dtype=int32))]),
  #  array([b\'a\', b\'b\'], dtype=object))
  ```

  See the
  [Load CSV data guide](https://www.tensorflow.org/tutorials/load_data/csv) for
  more examples of using `make_csv_dataset` to read CSV data.

  Args:
    file_pattern: List of files or patterns of file paths containing CSV
      records. See `tf.io.gfile.glob` for pattern rules.
    batch_size: An int representing the number of records to combine
      in a single batch.
    column_names: An optional list of strings that corresponds to the CSV
      columns, in order. One per column of the input record. If this is not
      provided, infers the column names from the first row of the records.
      These names will be the keys of the features dict of each dataset element.
    column_defaults: A optional list of default values for the CSV fields. One
      item per selected column of the input record. Each item in the list is
      either a valid CSV dtype (float32, float64, int32, int64, or string), or a
      `Tensor` with one of the aforementioned types. The tensor can either be
      a scalar default value (if the column is optional), or an empty tensor (if
      the column is required). If a dtype is provided instead of a tensor, the
      column is also treated as required. If this list is not provided, tries
      to infer types based on reading the first num_rows_for_inference rows of
      files specified, and assumes all columns are optional, defaulting to `0`
      for numeric values and `""` for string values. If both this and
      `select_columns` are specified, these must have the same lengths, and
      `column_defaults` is assumed to be sorted in order of increasing column
      index.
    label_name: A optional string corresponding to the label column. If
      provided, the data for this column is returned as a separate `Tensor` from
      the features dictionary, so that the dataset complies with the format
      expected by a `tf.Estimator.train` or `tf.Estimator.evaluate` input
      function.
    select_columns: An optional list of integer indices or string column
      names, that specifies a subset of columns of CSV data to select. If
      column names are provided, these must correspond to names provided in
      `column_names` or inferred from the file header lines. When this argument
      is specified, only a subset of CSV columns will be parsed and returned,
      corresponding to the columns specified. Using this results in faster
      parsing and lower memory usage. If both this and `column_defaults` are
      specified, these must have the same lengths, and `column_defaults` is
      assumed to be sorted in order of increasing column index.
    field_delim: An optional `string`. Defaults to `","`. Char delimiter to
      separate fields in a record.
    use_quote_delim: An optional bool. Defaults to `True`. If false, treats
      double quotation marks as regular characters inside of the string fields.
    na_value: Additional string to recognize as NA/NaN.
    header: A bool that indicates whether the first rows of provided CSV files
      correspond to header lines with column names, and should not be included
      in the data.
    num_epochs: An int specifying the number of times this dataset is repeated.
      If None, cycles through the dataset forever.
    shuffle: A bool that indicates whether the input should be shuffled.
    shuffle_buffer_size: Buffer size to use for shuffling. A large buffer size
      ensures better shuffling, but increases memory usage and startup time.
    shuffle_seed: Randomization seed to use for shuffling.
    prefetch_buffer_size: An int specifying the number of feature
      batches to prefetch for performance improvement. Recommended value is the
      number of batches consumed per training step. Defaults to auto-tune.
    num_parallel_reads: Number of threads used to read CSV records from files.
      If >1, the results will be interleaved. Defaults to `1`.
    sloppy: If `True`, reading performance will be improved at
      the cost of non-deterministic ordering. If `False`, the order of elements
      produced is deterministic prior to shuffling (elements are still
      randomized if `shuffle=True`. Note that if the seed is set, then order
      of elements after shuffling is deterministic). Defaults to `False`.
    num_rows_for_inference: Number of rows of a file to use for type inference
      if record_defaults is not provided. If None, reads all the rows of all
      the files. Defaults to 100.
    compression_type: (Optional.) A `tf.string` scalar evaluating to one of
      `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no compression.
    ignore_errors: (Optional.) If `True`, ignores errors with CSV file parsing,
      such as malformed data or empty lines, and moves on to the next valid
      CSV record. Otherwise, the dataset raises an error and stops processing
      when encountering any invalid records. Defaults to `False`.
    encoding: Encoding to use when reading. Defaults to `UTF-8`.

  Returns:
    A dataset, where each element is a (features, labels) tuple that corresponds
    to a batch of `batch_size` CSV rows. The features dictionary maps feature
    column names to `Tensor`s containing the corresponding column data, and
    labels is a `Tensor` containing the column data for the label column
    specified by `label_name`.

  Raises:
    ValueError: If any of the arguments is malformed.
  '''
def make_csv_dataset_v1(file_pattern, batch_size, column_names: Incomplete | None = None, column_defaults: Incomplete | None = None, label_name: Incomplete | None = None, select_columns: Incomplete | None = None, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', header: bool = True, num_epochs: Incomplete | None = None, shuffle: bool = True, shuffle_buffer_size: int = 10000, shuffle_seed: Incomplete | None = None, prefetch_buffer_size: Incomplete | None = None, num_parallel_reads: Incomplete | None = None, sloppy: bool = False, num_rows_for_inference: int = 100, compression_type: Incomplete | None = None, ignore_errors: bool = False, encoding: str = 'utf-8'): ...

class CsvDatasetV2(dataset_ops.DatasetSource):
    '''A Dataset comprising lines from one or more CSV files.

  The `tf.data.experimental.CsvDataset` class provides a minimal CSV Dataset
  interface. There is also a richer `tf.data.experimental.make_csv_dataset`
  function which provides additional convenience features such as column header
  parsing, column type-inference, automatic shuffling, and file interleaving.

  The elements of this dataset correspond to records from the file(s).
  RFC 4180 format is expected for CSV files
  (https://tools.ietf.org/html/rfc4180)
  Note that we allow leading and trailing spaces for int or float fields.

  For example, suppose we have a file \'my_file0.csv\' with four CSV columns of
  different data types:

  >>> with open(\'/tmp/my_file0.csv\', \'w\') as f:
  ...   f.write(\'abcdefg,4.28E10,5.55E6,12\\n\')
  ...   f.write(\'hijklmn,-5.3E14,,2\\n\')

  We can construct a CsvDataset from it as follows:

  >>> dataset = tf.data.experimental.CsvDataset(
  ...   "/tmp/my_file0.csv",
  ...   [tf.float32,  # Required field, use dtype or empty tensor
  ...    tf.constant([0.0], dtype=tf.float32),  # Optional field, default to 0.0
  ...    tf.int32,  # Required field, use dtype or empty tensor
  ...   ],
  ...   select_cols=[1,2,3]  # Only parse last three columns
  ... )

  The expected output of its iterations is:

  >>> for element in dataset.as_numpy_iterator():
  ...   print(element)
  (4.28e10, 5.55e6, 12)
  (-5.3e14, 0.0, 2)

  See
  https://www.tensorflow.org/tutorials/load_data/csv#tfdataexperimentalcsvdataset
  for more in-depth example usage.
  '''
    def __init__(self, filenames, record_defaults, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, header: bool = False, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', select_cols: Incomplete | None = None, exclude_cols: Incomplete | None = None) -> None:
        '''Creates a `CsvDataset` by reading and decoding CSV files.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      record_defaults: A list of default values for the CSV fields. Each item in
        the list is either a valid CSV `DType` (float32, float64, int32, int64,
        string), or a `Tensor` object with one of the above types. One per
        column of CSV data, with either a scalar `Tensor` default value for the
        column if it is optional, or `DType` or empty `Tensor` if required. If
        both this and `select_columns` are specified, these must have the same
        lengths, and `column_defaults` is assumed to be sorted in order of
        increasing column index. If both this and \'exclude_cols\' are specified,
        the sum of lengths of record_defaults and exclude_cols should equal
        the total number of columns in the CSV file.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no
        compression.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer while reading files. Defaults to 4MB.
      header: (Optional.) A `tf.bool` scalar indicating whether the CSV file(s)
        have header line(s) that should be skipped when parsing. Defaults to
        `False`.
      field_delim: (Optional.) A `tf.string` scalar containing the delimiter
        character that separates fields in a record. Defaults to `","`.
      use_quote_delim: (Optional.) A `tf.bool` scalar. If `False`, treats
        double quotation marks as regular characters inside of string fields
        (ignoring RFC 4180, Section 2, Bullet 5). Defaults to `True`.
      na_value: (Optional.) A `tf.string` scalar indicating a value that will
        be treated as NA/NaN.
      select_cols: (Optional.) A sorted list of column indices to select from
        the input data. If specified, only this subset of columns will be
        parsed. Defaults to parsing all columns. At most one of `select_cols`
        and `exclude_cols` can be specified.
      exclude_cols: (Optional.) A sorted list of column indices to exclude from
        the input data. If specified, only the complement of this set of column
        will be parsed. Defaults to parsing all columns. At most one of
        `select_cols` and `exclude_cols` can be specified.

    Raises:
       InvalidArgumentError: If exclude_cols is not None and
           len(exclude_cols) + len(record_defaults) does not match the total
           number of columns in the file(s)


    '''
    @property
    def element_spec(self): ...

class CsvDatasetV1(dataset_ops.DatasetV1Adapter):
    """A Dataset comprising lines from one or more CSV files."""
    def __init__(self, filenames, record_defaults, compression_type: Incomplete | None = None, buffer_size: Incomplete | None = None, header: bool = False, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', select_cols: Incomplete | None = None) -> None:
        '''Creates a `CsvDataset` by reading and decoding CSV files.

    The elements of this dataset correspond to records from the file(s).
    RFC 4180 format is expected for CSV files
    (https://tools.ietf.org/html/rfc4180)
    Note that we allow leading and trailing spaces with int or float field.


    For example, suppose we have a file \'my_file0.csv\' with four CSV columns of
    different data types:
    ```
    abcdefg,4.28E10,5.55E6,12
    hijklmn,-5.3E14,,2
    ```

    We can construct a CsvDataset from it as follows:

    ```python
     dataset = tf.data.experimental.CsvDataset(
        "my_file*.csv",
        [tf.float32,  # Required field, use dtype or empty tensor
         tf.constant([0.0], dtype=tf.float32),  # Optional field, default to 0.0
         tf.int32,  # Required field, use dtype or empty tensor
         ],
        select_cols=[1,2,3]  # Only parse last three columns
    )
    ```

    The expected output of its iterations is:

    ```python
    for element in dataset:
      print(element)

    >> (4.28e10, 5.55e6, 12)
    >> (-5.3e14, 0.0, 2)
    ```

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      record_defaults: A list of default values for the CSV fields. Each item in
        the list is either a valid CSV `DType` (float32, float64, int32, int64,
        string), or a `Tensor` object with one of the above types. One per
        column of CSV data, with either a scalar `Tensor` default value for the
        column if it is optional, or `DType` or empty `Tensor` if required. If
        both this and `select_columns` are specified, these must have the same
        lengths, and `column_defaults` is assumed to be sorted in order of
        increasing column index. If both this and \'exclude_cols\' are specified,
        the sum of lengths of record_defaults and exclude_cols should equal the
        total number of columns in the CSV file.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no
        compression.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer while reading files. Defaults to 4MB.
      header: (Optional.) A `tf.bool` scalar indicating whether the CSV file(s)
        have header line(s) that should be skipped when parsing. Defaults to
        `False`.
      field_delim: (Optional.) A `tf.string` scalar containing the delimiter
        character that separates fields in a record. Defaults to `","`.
      use_quote_delim: (Optional.) A `tf.bool` scalar. If `False`, treats double
        quotation marks as regular characters inside of string fields (ignoring
        RFC 4180, Section 2, Bullet 5). Defaults to `True`.
      na_value: (Optional.) A `tf.string` scalar indicating a value that will be
        treated as NA/NaN.
      select_cols: (Optional.) A sorted list of column indices to select from
        the input data. If specified, only this subset of columns will be
        parsed. Defaults to parsing all columns. At most one of `select_cols`
        and `exclude_cols` can be specified.
    '''

def make_batched_features_dataset_v2(file_pattern, batch_size, features, reader: Incomplete | None = None, label_key: Incomplete | None = None, reader_args: Incomplete | None = None, num_epochs: Incomplete | None = None, shuffle: bool = True, shuffle_buffer_size: int = 10000, shuffle_seed: Incomplete | None = None, prefetch_buffer_size: Incomplete | None = None, reader_num_threads: Incomplete | None = None, parser_num_threads: Incomplete | None = None, sloppy_ordering: bool = False, drop_final_batch: bool = False):
    '''Returns a `Dataset` of feature dictionaries from `Example` protos.

  If label_key argument is provided, returns a `Dataset` of tuple
  comprising of feature dictionaries and label.

  Example:

  ```
  serialized_examples = [
    features {
      feature { key: "age" value { int64_list { value: [ 0 ] } } }
      feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
      feature { key: "kws" value { bytes_list { value: [ "code", "art" ] } } }
    },
    features {
      feature { key: "age" value { int64_list { value: [] } } }
      feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
      feature { key: "kws" value { bytes_list { value: [ "sports" ] } } }
    }
  ]
  ```

  We can use arguments:

  ```
  features: {
    "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
    "gender": FixedLenFeature([], dtype=tf.string),
    "kws": VarLenFeature(dtype=tf.string),
  }
  ```

  And the expected output is:

  ```python
  {
    "age": [[0], [-1]],
    "gender": [["f"], ["f"]],
    "kws": SparseTensor(
      indices=[[0, 0], [0, 1], [1, 0]],
      values=["code", "art", "sports"]
      dense_shape=[2, 2]),
  }
  ```

  Args:
    file_pattern: List of files or patterns of file paths containing
      `Example` records. See `tf.io.gfile.glob` for pattern rules.
    batch_size: An int representing the number of records to combine
      in a single batch.
    features: A `dict` mapping feature keys to `FixedLenFeature` or
      `VarLenFeature` values. See `tf.io.parse_example`.
    reader: A function or class that can be
      called with a `filenames` tensor and (optional) `reader_args` and returns
      a `Dataset` of `Example` tensors. Defaults to `tf.data.TFRecordDataset`.
    label_key: (Optional) A string corresponding to the key labels are stored in
      `tf.Examples`. If provided, it must be one of the `features` key,
      otherwise results in `ValueError`.
    reader_args: Additional arguments to pass to the reader class.
    num_epochs: Integer specifying the number of times to read through the
      dataset. If None, cycles through the dataset forever. Defaults to `None`.
    shuffle: A boolean, indicates whether the input should be shuffled. Defaults
      to `True`.
    shuffle_buffer_size: Buffer size of the ShuffleDataset. A large capacity
      ensures better shuffling but would increase memory usage and startup time.
    shuffle_seed: Randomization seed to use for shuffling.
    prefetch_buffer_size: Number of feature batches to prefetch in order to
      improve performance. Recommended value is the number of batches consumed
      per training step. Defaults to auto-tune.
    reader_num_threads: Number of threads used to read `Example` records. If >1,
      the results will be interleaved. Defaults to `1`.
    parser_num_threads: Number of threads to use for parsing `Example` tensors
      into a dictionary of `Feature` tensors. Defaults to `2`.
    sloppy_ordering: If `True`, reading performance will be improved at
      the cost of non-deterministic ordering. If `False`, the order of elements
      produced is deterministic prior to shuffling (elements are still
      randomized if `shuffle=True`. Note that if the seed is set, then order
      of elements after shuffling is deterministic). Defaults to `False`.
    drop_final_batch: If `True`, and the batch size does not evenly divide the
      input dataset size, the final smaller batch will be dropped. Defaults to
      `False`.

  Returns:
    A dataset of `dict` elements, (or a tuple of `dict` elements and label).
    Each `dict` maps feature keys to `Tensor` or `SparseTensor` objects.

  Raises:
    TypeError: If `reader` is of the wrong type.
    ValueError: If `label_key` is not one of the `features` keys.
  '''
def make_batched_features_dataset_v1(file_pattern, batch_size, features, reader: Incomplete | None = None, label_key: Incomplete | None = None, reader_args: Incomplete | None = None, num_epochs: Incomplete | None = None, shuffle: bool = True, shuffle_buffer_size: int = 10000, shuffle_seed: Incomplete | None = None, prefetch_buffer_size: Incomplete | None = None, reader_num_threads: Incomplete | None = None, parser_num_threads: Incomplete | None = None, sloppy_ordering: bool = False, drop_final_batch: bool = False): ...

class SqlDatasetV2(dataset_ops.DatasetSource):
    '''A `Dataset` consisting of the results from a SQL query.

  `SqlDataset` allows a user to read data from the result set of a SQL query.
  For example:

  ```python
  dataset = tf.data.experimental.SqlDataset("sqlite", "/foo/bar.sqlite3",
                                            "SELECT name, age FROM people",
                                            (tf.string, tf.int32))
  # Prints the rows of the result set of the above query.
  for element in dataset:
    print(element)
  ```
  '''
    def __init__(self, driver_name, data_source_name, query, output_types) -> None:
        """Creates a `SqlDataset`.

    Args:
      driver_name: A 0-D `tf.string` tensor containing the database type.
        Currently, the only supported value is 'sqlite'.
      data_source_name: A 0-D `tf.string` tensor containing a connection string
        to connect to the database.
      query: A 0-D `tf.string` tensor containing the SQL query to execute.
      output_types: A tuple of `tf.DType` objects representing the types of the
        columns returned by `query`.
    """
    @property
    def element_spec(self): ...

class SqlDatasetV1(dataset_ops.DatasetV1Adapter):
    """A `Dataset` consisting of the results from a SQL query."""
    def __init__(self, driver_name, data_source_name, query, output_types) -> None: ...
CsvDataset = CsvDatasetV2
SqlDataset = SqlDatasetV2
make_batched_features_dataset = make_batched_features_dataset_v2
make_csv_dataset = make_csv_dataset_v2
CsvDataset = CsvDatasetV1
SqlDataset = SqlDatasetV1
make_batched_features_dataset = make_batched_features_dataset_v1
make_csv_dataset = make_csv_dataset_v1
