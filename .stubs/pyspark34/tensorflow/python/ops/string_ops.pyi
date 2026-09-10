from tensorflow.python.ops.gen_string_ops import *
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_parsing_ops as gen_parsing_ops, gen_string_ops as gen_string_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def regex_full_match(input, pattern, name: Incomplete | None = None):
    """Match elements of `input` with regex `pattern`.

  Args:
    input: string `Tensor`, the source strings to process.
    pattern: string or scalar string `Tensor`, regular expression to use,
      see more details at https://github.com/google/re2/wiki/Syntax
    name: Name of the op.

  Returns:
    bool `Tensor` of the same shape as `input` with match results.
  """
def regex_replace(input, pattern, rewrite, replace_global: bool = True, name: Incomplete | None = None):
    '''Replace elements of `input` matching regex `pattern` with `rewrite`.

  >>> tf.strings.regex_replace("Text with tags.<br /><b>contains html</b>",
  ...                          "<[^>]+>", " ")
  <tf.Tensor: shape=(), dtype=string, numpy=b\'Text with tags.  contains html \'>

  Args:
    input: string `Tensor`, the source strings to process.
    pattern: string or scalar string `Tensor`, regular expression to use,
      see more details at https://github.com/google/re2/wiki/Syntax
    rewrite: string or scalar string `Tensor`, value to use in match
      replacement, supports backslash-escaped digits (\\1 to \\9) can be to insert
      text matching corresponding parenthesized group.
    replace_global: `bool`, if `True` replace all non-overlapping matches,
      else replace only the first match.
    name: A name for the operation (optional).

  Returns:
    string `Tensor` of the same shape as `input` with specified replacements.
  '''
def string_format(template, inputs, placeholder: str = '{}', summarize: int = 3, name: Incomplete | None = None):
    '''Formats a string template using a list of tensors.

  Formats a string template using a list of tensors, abbreviating tensors by
  only printing the first and last `summarize` elements of each dimension
  (recursively). If formatting only one tensor into a template, the tensor does
  not have to be wrapped in a list.

  Example:
    Formatting a single-tensor template:

    >>> tensor = tf.range(5)
    >>> tf.strings.format("tensor: {}, suffix", tensor)
    <tf.Tensor: shape=(), dtype=string, numpy=b\'tensor: [0 1 2 3 4], suffix\'>

    Formatting a multi-tensor template:

    >>> tensor_a = tf.range(2)
    >>> tensor_b = tf.range(1, 4, 2)
    >>> tf.strings.format("a: {}, b: {}, suffix", (tensor_a, tensor_b))
    <tf.Tensor: shape=(), dtype=string, numpy=b\'a: [0 1], b: [1 3], suffix\'>


  Args:
    template: A string template to format tensor values into.
    inputs: A list of `Tensor` objects, or a single Tensor.
      The list of tensors to format into the template string. If a solitary
      tensor is passed in, the input tensor will automatically be wrapped as a
      list.
    placeholder: An optional `string`. Defaults to `{}`.
      At each placeholder occurring in the template, a subsequent tensor
      will be inserted.
    summarize: An optional `int`. Defaults to `3`.
      When formatting the tensors, show the first and last `summarize`
      entries of each tensor dimension (recursively). If set to -1, all
      elements of the tensor will be shown.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`.

  Raises:
    ValueError: if the number of placeholders does not match the number of
      inputs.
  '''
def string_split(source, sep: Incomplete | None = None, skip_empty: bool = True, delimiter: Incomplete | None = None):
    """Split elements of `source` based on `delimiter` into a `SparseTensor`.

  Let N be the size of source (typically N will be the batch size). Split each
  element of `source` based on `delimiter` and return a `SparseTensor`
  containing the split tokens. Empty tokens are ignored.

  If `sep` is an empty string, each element of the `source` is split
  into individual strings, each containing one byte. (This includes splitting
  multibyte sequences of UTF-8.) If delimiter contains multiple bytes, it is
  treated as a set of delimiters with each considered a potential split point.

  For example:
  N = 2, source[0] is 'hello world' and source[1] is 'a b c', then the output
  will be

  st.indices = [0, 0;
                0, 1;
                1, 0;
                1, 1;
                1, 2]
  st.shape = [2, 3]
  st.values = ['hello', 'world', 'a', 'b', 'c']

  Args:
    source: `1-D` string `Tensor`, the strings to split.
    sep: `0-D` string `Tensor`, the delimiter character, the string should
      be length 0 or 1. Default is ' '.
    skip_empty: A `bool`. If `True`, skip the empty strings from the result.
    delimiter: deprecated alias for `sep`.

  Raises:
    ValueError: If delimiter is not a string.

  Returns:
    A `SparseTensor` of rank `2`, the strings split according to the delimiter.
    The first column of the indices corresponds to the row in `source` and the
    second column corresponds to the index of the split component in this row.
  """
def string_split_v2(source, sep: Incomplete | None = None, maxsplit: int = -1):
    '''Split elements of `source` based on `sep` into a `SparseTensor`.

  Let N be the size of source (typically N will be the batch size). Split each
  element of `source` based on `sep` and return a `SparseTensor`
  containing the split tokens. Empty tokens are ignored.

  For example, N = 2, source[0] is \'hello world\' and source[1] is \'a b c\',
  then the output will be

  st.indices = [0, 0;
                0, 1;
                1, 0;
                1, 1;
                1, 2]
  st.shape = [2, 3]
  st.values = [\'hello\', \'world\', \'a\', \'b\', \'c\']

  If `sep` is given, consecutive delimiters are not grouped together and are
  deemed to delimit empty strings. For example, source of `"1<>2<><>3"` and
  sep of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
  string, consecutive whitespace are regarded as a single separator, and the
  result will contain no empty strings at the start or end if the string has
  leading or trailing whitespace.

  Note that the above mentioned behavior matches python\'s str.split.

  Args:
    source: `1-D` string `Tensor`, the strings to split.
    sep: `0-D` string `Tensor`, the delimiter character.
    maxsplit: An `int`. If `maxsplit > 0`, limit of the split of the result.

  Raises:
    ValueError: If sep is not a string.

  Returns:
    A `SparseTensor` of rank `2`, the strings split according to the delimiter.
    The first column of the indices corresponds to the row in `source` and the
    second column corresponds to the index of the split component in this row.
  '''
def reduce_join(inputs, axis: Incomplete | None = None, keep_dims: Incomplete | None = None, separator: str = '', name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keepdims: Incomplete | None = None): ...
def reduce_join_v2(inputs, axis: Incomplete | None = None, keepdims: bool = False, separator: str = '', name: Incomplete | None = None):
    '''Joins all strings into a single string, or joins along an axis.

  This is the reduction operation for the elementwise `tf.strings.join` op.

  >>> tf.strings.reduce_join([[\'abc\',\'123\'],
  ...                         [\'def\',\'456\']]).numpy()
  b\'abc123def456\'
  >>> tf.strings.reduce_join([[\'abc\',\'123\'],
  ...                         [\'def\',\'456\']], axis=-1).numpy()
  array([b\'abc123\', b\'def456\'], dtype=object)
  >>> tf.strings.reduce_join([[\'abc\',\'123\'],
  ...                         [\'def\',\'456\']],
  ...                        axis=-1,
  ...                        separator=" ").numpy()
  array([b\'abc 123\', b\'def 456\'], dtype=object)

  Args:
    inputs: A `tf.string` tensor.
    axis: Which axis to join along. The default behavior is to join all
      elements, producing a scalar.
    keepdims: If true, retains reduced dimensions with length 1.
    separator: a string added between each string being joined.
    name: A name for the operation (optional).

  Returns:
    A `tf.string` tensor.
  '''
def string_length(input, name: Incomplete | None = None, unit: str = 'BYTE'):
    '''Computes the length of each string given in the input tensor.

  >>> strings = tf.constant([\'Hello\',\'TensorFlow\', \'🙂\'])
  >>> tf.strings.length(strings).numpy() # default counts bytes
  array([ 5, 10, 4], dtype=int32)
  >>> tf.strings.length(strings, unit="UTF8_CHAR").numpy()
  array([ 5, 10, 1], dtype=int32)

  Args:
    input: A `Tensor` of type `string`. The strings for which to compute the
      length for each element.
    name: A name for the operation (optional).
    unit: An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to
      `"BYTE"`. The unit that is counted to compute string length.  One of:
        `"BYTE"` (for the number of bytes in each string) or `"UTF8_CHAR"` (for
        the number of UTF-8 encoded Unicode code points in each string). Results
        are undefined if `unit=UTF8_CHAR` and the `input` strings do not contain
        structurally valid UTF-8.

  Returns:
    A `Tensor` of type `int32`, containing the length of the input string in
    the same element of the input tensor.
  '''
def string_length_v2(input, unit: str = 'BYTE', name: Incomplete | None = None): ...
def substr_deprecated(input, pos, len, name: Incomplete | None = None, unit: str = 'BYTE'): ...
def substr(input, pos, len, name: Incomplete | None = None, unit: str = 'BYTE'): ...
def substr_v2(input, pos, len, unit: str = 'BYTE', name: Incomplete | None = None): ...
def string_to_number(input, out_type=..., name: Incomplete | None = None):
    '''Converts each string in the input Tensor to the specified numeric type.

  (Note that int32 overflow results in an error while float overflow
  results in a rounded value.)

  Examples:

  >>> tf.strings.to_number("1.55")
  <tf.Tensor: shape=(), dtype=float32, numpy=1.55>
  >>> tf.strings.to_number("3", tf.int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=3>

  Args:
    input: A `Tensor` of type `string`.
    out_type: An optional `tf.DType` from: `tf.float32, tf.float64, tf.int32,
      tf.int64`. Defaults to `tf.float32`.
      The numeric type to interpret each string in `string_tensor` as.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  '''
def string_to_number_v1(string_tensor: Incomplete | None = None, out_type=..., name: Incomplete | None = None, input: Incomplete | None = None): ...
def string_to_hash_bucket(input, num_buckets, name: Incomplete | None = None):
    '''Converts each string in the input Tensor to its hash mod by a number of buckets.

  The hash function is deterministic on the content of the string within the
  process.

  Note that the hash function may change from time to time.
  This functionality will be deprecated and it\'s recommended to use
  `tf.strings.to_hash_bucket_fast()` or `tf.strings.to_hash_bucket_strong()`.

  Examples:

  >>> tf.strings.to_hash_bucket(["Hello", "TensorFlow", "2.x"], 3)
  <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 0, 1])>

  Args:
    input: A `Tensor` of type `string`.
    num_buckets: An `int` that is `>= 1`. The number of buckets.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  '''
def string_to_hash_bucket_v1(string_tensor: Incomplete | None = None, num_buckets: Incomplete | None = None, name: Incomplete | None = None, input: Incomplete | None = None): ...
def string_join(inputs, separator: str = '', name: Incomplete | None = None):
    '''Perform element-wise concatenation of a list of string tensors.

  Given a list of string tensors of same shape, performs element-wise
  concatenation of the strings of the same index in all tensors.


  >>> tf.strings.join([\'abc\',\'def\']).numpy()
  b\'abcdef\'
  >>> tf.strings.join([[\'abc\',\'123\'],
  ...                  [\'def\',\'456\'],
  ...                  [\'ghi\',\'789\']]).numpy()
  array([b\'abcdefghi\', b\'123456789\'], dtype=object)
  >>> tf.strings.join([[\'abc\',\'123\'],
  ...                  [\'def\',\'456\']],
  ...                  separator=" ").numpy()
  array([b\'abc def\', b\'123 456\'], dtype=object)

  The reduction version of this elementwise operation is
  `tf.strings.reduce_join`

  Args:
    inputs: A list of `tf.Tensor` objects of same size and `tf.string` dtype.
    separator: A string added between each string being joined.
    name: A name for the operation (optional).

  Returns:
    A `tf.string` tensor.
  '''
def unsorted_segment_join(inputs, segment_ids, num_segments, separator: str = '', name: Incomplete | None = None):
    '''Joins the elements of `inputs` based on `segment_ids`.

  Computes the string join along segments of a tensor.

  Given `segment_ids` with rank `N` and `data` with rank `N+M`:

  ```
  output[i, k1...kM] = strings.join([data[j1...jN, k1...kM])
  ```

  where the join is over all `[j1...jN]` such that `segment_ids[j1...jN] = i`.

  Strings are joined in row-major order.

  For example:

  >>> inputs = [\'this\', \'a\', \'test\', \'is\']
  >>> segment_ids = [0, 1, 1, 0]
  >>> num_segments = 2
  >>> separator = \' \'
  >>> tf.strings.unsorted_segment_join(inputs, segment_ids, num_segments,
  ...                                  separator).numpy()
  array([b\'this is\', b\'a test\'], dtype=object)

  >>> inputs = [[\'Y\', \'q\', \'c\'], [\'Y\', \'6\', \'6\'], [\'p\', \'G\', \'a\']]
  >>> segment_ids = [1, 0, 1]
  >>> num_segments = 2
  >>> tf.strings.unsorted_segment_join(inputs, segment_ids, num_segments,
  ...                                  separator=\':\').numpy()
  array([[b\'Y\', b\'6\', b\'6\'],
         [b\'Y:p\', b\'q:G\', b\'c:a\']], dtype=object)

  Args:
    inputs: A list of `tf.Tensor` objects of type `tf.string`.
    segment_ids: A tensor whose shape is a prefix of `inputs.shape` and whose
      type must be `tf.int32` or `tf.int64`. Negative segment ids are not
      supported.
    num_segments: A scalar of type `tf.int32` or `tf.int64`. Must be
      non-negative and larger than any segment id.
    separator: The separator to use when joining. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `tf.string` tensor representing the concatenated values, using the given
    separator.
  '''
