from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def as_string(input, precision: int = -1, scientific: bool = False, shortest: bool = False, width: int = -1, fill: str = '', name: Incomplete | None = None):
    '''Converts each entry in the given tensor to strings.

  Supports many numeric types and boolean.

  For Unicode, see the
  [https://www.tensorflow.org/tutorials/representation/unicode](Working with Unicode text)
  tutorial.

  Examples:

  >>> tf.strings.as_string([3, 2])
  <tf.Tensor: shape=(2,), dtype=string, numpy=array([b\'3\', b\'2\'], dtype=object)>
  >>> tf.strings.as_string([3.1415926, 2.71828], precision=2).numpy()
  array([b\'3.14\', b\'2.72\'], dtype=object)

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `complex64`, `complex128`, `bool`, `variant`.
    precision: An optional `int`. Defaults to `-1`.
      The post-decimal precision to use for floating point numbers.
      Only used if precision > -1.
    scientific: An optional `bool`. Defaults to `False`.
      Use scientific notation for floating point numbers.
    shortest: An optional `bool`. Defaults to `False`.
      Use shortest representation (either scientific or standard) for
      floating point numbers.
    width: An optional `int`. Defaults to `-1`.
      Pad pre-decimal numbers to this width.
      Applies to both floating point and integer numbers.
      Only used if width > -1.
    fill: An optional `string`. Defaults to `""`.
      The value to pad if width > -1.  If empty, pads with spaces.
      Another typical value is \'0\'.  String cannot be longer than 1 character.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

AsString: Incomplete

def as_string_eager_fallback(input, precision, scientific, shortest, width, fill, name, ctx): ...
def decode_base64(input, name: Incomplete | None = None):
    """Decode web-safe base64-encoded strings.

  Input may or may not have padding at the end. See
  [EncodeBase64](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64)
  for padding. Web-safe means that input must use - and _ instead of + and /.

  Args:
    input: A `Tensor` of type `string`. Base64 strings to decode.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DecodeBase64: Incomplete

def decode_base64_eager_fallback(input, name, ctx): ...
def encode_base64(input, pad: bool = False, name: Incomplete | None = None):
    """Encode strings into web-safe base64 format.

  Refer to [this article](https://en.wikipedia.org/wiki/Base64) for more information on
  base64 format. Base64 strings may have padding with '=' at the
  end so that the encoded has length multiple of 4. See Padding section of the
  link above.

  Web-safe means that the encoder uses - and _ instead of + and /.

  Args:
    input: A `Tensor` of type `string`. Strings to be encoded.
    pad: An optional `bool`. Defaults to `False`.
      Bool whether padding is applied at the ends.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

EncodeBase64: Incomplete

def encode_base64_eager_fallback(input, pad, name, ctx): ...
def reduce_join(inputs, reduction_indices, keep_dims: bool = False, separator: str = '', name: Incomplete | None = None):
    '''Joins a string Tensor across the given dimensions.

  Computes the string join across dimensions in the given string Tensor of shape
  `[\\\\(d_0, d_1, ..., d_{n-1}\\\\)]`.  Returns a new Tensor created by joining the input
  strings with the given separator (default: empty string).  Negative indices are
  counted backwards from the end, with `-1` being equivalent to `n - 1`.  If
  indices are not specified, joins across all dimensions beginning from `n - 1`
  through `0`.

  For example:

  ```python
  # tensor `a` is [["a", "b"], ["c", "d"]]
  tf.reduce_join(a, 0) ==> ["ac", "bd"]
  tf.reduce_join(a, 1) ==> ["ab", "cd"]
  tf.reduce_join(a, -2) = tf.reduce_join(a, 0) ==> ["ac", "bd"]
  tf.reduce_join(a, -1) = tf.reduce_join(a, 1) ==> ["ab", "cd"]
  tf.reduce_join(a, 0, keep_dims=True) ==> [["ac", "bd"]]
  tf.reduce_join(a, 1, keep_dims=True) ==> [["ab"], ["cd"]]
  tf.reduce_join(a, 0, separator=".") ==> ["a.c", "b.d"]
  tf.reduce_join(a, [0, 1]) ==> "acbd"
  tf.reduce_join(a, [1, 0]) ==> "abcd"
  tf.reduce_join(a, []) ==> [["a", "b"], ["c", "d"]]
  tf.reduce_join(a) = tf.reduce_join(a, [1, 0]) ==> "abcd"
  ```

  Args:
    inputs: A `Tensor` of type `string`.
      The input to be joined.  All reduced indices must have non-zero size.
    reduction_indices: A `Tensor` of type `int32`.
      The dimensions to reduce over.  Dimensions are reduced in the
      order specified.  Omitting `reduction_indices` is equivalent to passing
      `[n-1, n-2, ..., 0]`.  Negative indices from `-n` to `-1` are supported.
    keep_dims: An optional `bool`. Defaults to `False`.
      If `True`, retain reduced dimensions with length `1`.
    separator: An optional `string`. Defaults to `""`.
      The separator to use when joining.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

ReduceJoin: Incomplete

def reduce_join_eager_fallback(inputs, reduction_indices, keep_dims, separator, name, ctx): ...
def regex_full_match(input, pattern, name: Incomplete | None = None):
    '''Check if the input matches the regex pattern.

  The input is a string tensor of any shape. The pattern is a scalar
  string tensor which is applied to every element of the input tensor.
  The boolean values (True or False) of the output tensor indicate
  if the input matches the regex pattern provided.

  The pattern follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

  Examples:

  >>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*lib$")
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>
  >>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*TF$")
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>

  Args:
    input: A `Tensor` of type `string`.
      A string tensor of the text to be processed.
    pattern: A `Tensor` of type `string`.
      A scalar string tensor containing the regular expression to match the input.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  '''

RegexFullMatch: Incomplete

def regex_full_match_eager_fallback(input, pattern, name, ctx): ...
def regex_replace(input, pattern, rewrite, replace_global: bool = True, name: Incomplete | None = None):
    """Replaces matches of the `pattern` regular expression in `input` with the
replacement string provided in `rewrite`.

  It follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

  Args:
    input: A `Tensor` of type `string`. The text to be processed.
    pattern: A `Tensor` of type `string`.
      The regular expression to be matched in the `input` strings.
    rewrite: A `Tensor` of type `string`.
      The rewrite string to be substituted for the `pattern` expression where it is
      matched in the `input` strings.
    replace_global: An optional `bool`. Defaults to `True`.
      If True, the replacement is global (that is, all matches of the `pattern` regular
      expression in each input string are rewritten), otherwise the `rewrite`
      substitution is only made for the first `pattern` match.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

RegexReplace: Incomplete

def regex_replace_eager_fallback(input, pattern, rewrite, replace_global, name, ctx): ...
def static_regex_full_match(input, pattern, name: Incomplete | None = None):
    """Check if the input matches the regex pattern.

  The input is a string tensor of any shape. The pattern is the
  regular expression to be matched with every element of the input tensor.
  The boolean values (True or False) of the output tensor indicate
  if the input matches the regex pattern provided.

  The pattern follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

  Args:
    input: A `Tensor` of type `string`.
      A string tensor of the text to be processed.
    pattern: A `string`. The regular expression to match the input.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

StaticRegexFullMatch: Incomplete

def static_regex_full_match_eager_fallback(input, pattern, name, ctx): ...
def static_regex_replace(input, pattern, rewrite, replace_global: bool = True, name: Incomplete | None = None):
    """Replaces the match of pattern in input with rewrite.

  It follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

  Args:
    input: A `Tensor` of type `string`. The text to be processed.
    pattern: A `string`. The regular expression to match the input.
    rewrite: A `string`. The rewrite to be applied to the matched expression.
    replace_global: An optional `bool`. Defaults to `True`.
      If True, the replacement is global, otherwise the replacement
      is done only on the first match.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

StaticRegexReplace: Incomplete

def static_regex_replace_eager_fallback(input, pattern, rewrite, replace_global, name, ctx): ...
def string_format(inputs, template: str = '%s', placeholder: str = '%s', summarize: int = 3, name: Incomplete | None = None):
    '''Formats a string template using a list of tensors.

  Formats a string template using a list of tensors, pretty-printing tensor summaries.

  Args:
    inputs: A list of `Tensor` objects.
      The list of tensors to format into the placeholder string.
    template: An optional `string`. Defaults to `"%s"`.
      A string, the template to format tensor summaries into.
    placeholder: An optional `string`. Defaults to `"%s"`.
      A string, at each placeholder in the template a subsequent tensor summary will be inserted.
    summarize: An optional `int`. Defaults to `3`.
      When formatting the tensor summaries print the first and last summarize entries of each tensor dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

StringFormat: Incomplete

def string_format_eager_fallback(inputs, template, placeholder, summarize, name, ctx): ...
def string_join(inputs, separator: str = '', name: Incomplete | None = None):
    '''Joins the strings in the given list of string tensors into one tensor;

  with the given separator (default is an empty separator).

  Examples:

  >>> s = ["hello", "world", "tensorflow"]
  >>> tf.strings.join(s, " ")
  <tf.Tensor: shape=(), dtype=string, numpy=b\'hello world tensorflow\'>

  Args:
    inputs: A list of at least 1 `Tensor` objects with type `string`.
      A list of string tensors.  The tensors must all have the same shape,
      or be scalars.  Scalars may be mixed in; these will be broadcast to the shape
      of non-scalar inputs.
    separator: An optional `string`. Defaults to `""`.
      string, an optional join separator.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

StringJoin: Incomplete

def string_join_eager_fallback(inputs, separator, name, ctx): ...
def string_length(input, unit: str = 'BYTE', name: Incomplete | None = None):
    '''String lengths of `input`.

  Computes the length of each string given in the input tensor.

  >>> strings = tf.constant([\'Hello\',\'TensorFlow\', \'\\U0001F642\'])
  >>> tf.strings.length(strings).numpy() # default counts bytes
  array([ 5, 10, 4], dtype=int32)
  >>> tf.strings.length(strings, unit="UTF8_CHAR").numpy()
  array([ 5, 10, 1], dtype=int32)

  Args:
    input: A `Tensor` of type `string`.
      The strings for which to compute the length for each element.
    unit: An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
      The unit that is counted to compute string length.  One of: `"BYTE"` (for
      the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8
      encoded Unicode code points in each string).  Results are undefined
      if `unit=UTF8_CHAR` and the `input` strings do not contain structurally
      valid UTF-8.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  '''

StringLength: Incomplete

def string_length_eager_fallback(input, unit, name, ctx): ...
def string_lower(input, encoding: str = '', name: Incomplete | None = None):
    '''Converts all uppercase characters into their respective lowercase replacements.

  Example:

  >>> tf.strings.lower("CamelCase string and ALL CAPS")
  <tf.Tensor: shape=(), dtype=string, numpy=b\'camelcase string and all caps\'>

  Args:
    input: A `Tensor` of type `string`. The input to be lower-cased.
    encoding: An optional `string`. Defaults to `""`.
      Character encoding of `input`. Allowed values are \'\' and \'utf-8\'.
      Value \'\' is interpreted as ASCII.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

StringLower: Incomplete

def string_lower_eager_fallback(input, encoding, name, ctx): ...

class _StringNGramsOutput(NamedTuple):
    ngrams: Incomplete
    ngrams_splits: Incomplete

def string_n_grams(data, data_splits, separator, ngram_widths, left_pad, right_pad, pad_width, preserve_short_sequences, name: Incomplete | None = None):
    '''Creates ngrams from ragged string data.

  This op accepts a ragged tensor with 1 ragged dimension containing only
  strings and outputs a ragged tensor with 1 ragged dimension containing ngrams
  of that string, joined along the innermost axis.

  Args:
    data: A `Tensor` of type `string`.
      The values tensor of the ragged string tensor to make ngrams out of. Must be a
      1D string tensor.
    data_splits: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The splits tensor of the ragged string tensor to make ngrams out of.
    separator: A `string`.
      The string to append between elements of the token. Use "" for no separator.
    ngram_widths: A list of `ints`. The sizes of the ngrams to create.
    left_pad: A `string`.
      The string to use to pad the left side of the ngram sequence. Only used if
      pad_width != 0.
    right_pad: A `string`.
      The string to use to pad the right side of the ngram sequence. Only used if
      pad_width != 0.
    pad_width: An `int`.
      The number of padding elements to add to each side of each
      sequence. Note that padding will never be greater than \'ngram_widths\'-1
      regardless of this value. If `pad_width=-1`, then add `max(ngram_widths)-1`
      elements.
    preserve_short_sequences: A `bool`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (ngrams, ngrams_splits).

    ngrams: A `Tensor` of type `string`.
    ngrams_splits: A `Tensor`. Has the same type as `data_splits`.
  '''

StringNGrams: Incomplete

def string_n_grams_eager_fallback(data, data_splits, separator, ngram_widths, left_pad, right_pad, pad_width, preserve_short_sequences, name, ctx): ...

class _StringSplitOutput(NamedTuple):
    indices: Incomplete
    values: Incomplete
    shape: Incomplete

def string_split(input, delimiter, skip_empty: bool = True, name: Incomplete | None = None):
    """Split elements of `input` based on `delimiter` into a `SparseTensor`.

  Let N be the size of source (typically N will be the batch size). Split each
  element of `input` based on `delimiter` and return a `SparseTensor`
  containing the splitted tokens. Empty tokens are ignored.

  `delimiter` can be empty, or a string of split characters. If `delimiter` is an
   empty string, each element of `input` is split into individual single-byte
   character strings, including splitting of UTF-8 multibyte sequences. Otherwise
   every character of `delimiter` is a potential split point.

  For example:
    N = 2, input[0] is 'hello world' and input[1] is 'a b c', then the output
    will be

    indices = [0, 0;
               0, 1;
               1, 0;
               1, 1;
               1, 2]
    shape = [2, 3]
    values = ['hello', 'world', 'a', 'b', 'c']

  Args:
    input: A `Tensor` of type `string`. 1-D. Strings to split.
    delimiter: A `Tensor` of type `string`.
      0-D. Delimiter characters (bytes), or empty string.
    skip_empty: An optional `bool`. Defaults to `True`.
      A `bool`. If `True`, skip the empty strings from the result.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, values, shape).

    indices: A `Tensor` of type `int64`.
    values: A `Tensor` of type `string`.
    shape: A `Tensor` of type `int64`.
  """

StringSplit: Incomplete

def string_split_eager_fallback(input, delimiter, skip_empty, name, ctx): ...

class _StringSplitV2Output(NamedTuple):
    indices: Incomplete
    values: Incomplete
    shape: Incomplete

def string_split_v2(input, sep, maxsplit: int = -1, name: Incomplete | None = None):
    '''Split elements of `source` based on `sep` into a `SparseTensor`.

  Let N be the size of source (typically N will be the batch size). Split each
  element of `source` based on `sep` and return a `SparseTensor`
  containing the split tokens. Empty tokens are ignored.

  For example, N = 2, source[0] is \'hello world\' and source[1] is \'a b c\',
  then the output will be
  ```
  st.indices = [0, 0;
                0, 1;
                1, 0;
                1, 1;
                1, 2]
  st.shape = [2, 3]
  st.values = [\'hello\', \'world\', \'a\', \'b\', \'c\']
  ```

  If `sep` is given, consecutive delimiters are not grouped together and are
  deemed to delimit empty strings. For example, source of `"1<>2<><>3"` and
  sep of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
  string, consecutive whitespace are regarded as a single separator, and the
  result will contain no empty strings at the startor end if the string has
  leading or trailing whitespace.

  Note that the above mentioned behavior matches python\'s str.split.

  Args:
    input: A `Tensor` of type `string`.
      `1-D` string `Tensor`, the strings to split.
    sep: A `Tensor` of type `string`.
      `0-D` string `Tensor`, the delimiter character.
    maxsplit: An optional `int`. Defaults to `-1`.
      An `int`. If `maxsplit > 0`, limit of the split of the result.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, values, shape).

    indices: A `Tensor` of type `int64`.
    values: A `Tensor` of type `string`.
    shape: A `Tensor` of type `int64`.
  '''

StringSplitV2: Incomplete

def string_split_v2_eager_fallback(input, sep, maxsplit, name, ctx): ...
def string_strip(input, name: Incomplete | None = None):
    '''Strip leading and trailing whitespaces from the Tensor.

  Examples:

  >>> tf.strings.strip(["\\nTensorFlow", "     The python library    "]).numpy()
  array([b\'TensorFlow\', b\'The python library\'], dtype=object)

  Args:
    input: A `Tensor` of type `string`. A string `Tensor` of any shape.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

StringStrip: Incomplete

def string_strip_eager_fallback(input, name, ctx): ...
def string_to_hash_bucket(string_tensor, num_buckets, name: Incomplete | None = None):
    """Converts each string in the input Tensor to its hash mod by a number of buckets.

  The hash function is deterministic on the content of the string within the
  process.

  Note that the hash function may change from time to time.
  This functionality will be deprecated and it's recommended to use
  `tf.string_to_hash_bucket_fast()` or `tf.string_to_hash_bucket_strong()`.

  Args:
    string_tensor: A `Tensor` of type `string`.
    num_buckets: An `int` that is `>= 1`. The number of buckets.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

StringToHashBucket: Incomplete

def string_to_hash_bucket_eager_fallback(string_tensor, num_buckets, name, ctx): ...
def string_to_hash_bucket_fast(input, num_buckets, name: Incomplete | None = None):
    '''Converts each string in the input Tensor to its hash mod by a number of buckets.

  The hash function is deterministic on the content of the string within the
  process and will never change. However, it is not suitable for cryptography.
  This function may be used when CPU time is scarce and inputs are trusted or
  unimportant. There is a risk of adversaries constructing inputs that all hash
  to the same bucket. To prevent this problem, use a strong hash function with
  `tf.string_to_hash_bucket_strong`.

  Examples:

  >>> tf.strings.to_hash_bucket_fast(["Hello", "TensorFlow", "2.x"], 3).numpy()
  array([0, 2, 2])

  Args:
    input: A `Tensor` of type `string`. The strings to assign a hash bucket.
    num_buckets: An `int` that is `>= 1`. The number of buckets.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  '''

StringToHashBucketFast: Incomplete

def string_to_hash_bucket_fast_eager_fallback(input, num_buckets, name, ctx): ...
def string_to_hash_bucket_strong(input, num_buckets, key, name: Incomplete | None = None):
    '''Converts each string in the input Tensor to its hash mod by a number of buckets.

  The hash function is deterministic on the content of the string within the
  process. The hash function is a keyed hash function, where attribute `key`
  defines the key of the hash function. `key` is an array of 2 elements.

  A strong hash is important when inputs may be malicious, e.g. URLs with
  additional components. Adversaries could try to make their inputs hash to the
  same bucket for a denial-of-service attack or to skew the results. A strong
  hash can be used to make it difficult to find inputs with a skewed hash value
  distribution over buckets. This requires that the hash function is
  seeded by a high-entropy (random) "key" unknown to the adversary.

  The additional robustness comes at a cost of roughly 4x higher compute
  time than `tf.string_to_hash_bucket_fast`.

  Examples:

  >>> tf.strings.to_hash_bucket_strong(["Hello", "TF"], 3, [1, 2]).numpy()
  array([2, 0])

  Args:
    input: A `Tensor` of type `string`. The strings to assign a hash bucket.
    num_buckets: An `int` that is `>= 1`. The number of buckets.
    key: A list of `ints`.
      The key used to seed the hash function, passed as a list of two uint64
      elements.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  '''

StringToHashBucketStrong: Incomplete

def string_to_hash_bucket_strong_eager_fallback(input, num_buckets, key, name, ctx): ...
def string_upper(input, encoding: str = '', name: Incomplete | None = None):
    '''Converts all lowercase characters into their respective uppercase replacements.

  Example:

  >>> tf.strings.upper("CamelCase string and ALL CAPS")
  <tf.Tensor: shape=(), dtype=string, numpy=b\'CAMELCASE STRING AND ALL CAPS\'>

  Args:
    input: A `Tensor` of type `string`. The input to be upper-cased.
    encoding: An optional `string`. Defaults to `""`.
      Character encoding of `input`. Allowed values are \'\' and \'utf-8\'.
      Value \'\' is interpreted as ASCII.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

StringUpper: Incomplete

def string_upper_eager_fallback(input, encoding, name, ctx): ...
def substr(input, pos, len, unit: str = 'BYTE', name: Incomplete | None = None):
    '''Return substrings from `Tensor` of strings.

  For each string in the input `Tensor`, creates a substring starting at index
  `pos` with a total length of `len`.

  If `len` defines a substring that would extend beyond the length of the input
  string, or if `len` is negative, then as many characters as possible are used.

  A negative `pos` indicates distance within the string backwards from the end.

  If `pos` specifies an index which is out of range for any of the input strings,
  then an `InvalidArgumentError` is thrown.

  `pos` and `len` must have the same shape, otherwise a `ValueError` is thrown on
  Op creation.

  *NOTE*: `Substr` supports broadcasting up to two dimensions. More about
  broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  ---

  Examples

  Using scalar `pos` and `len`:

  ```python
  input = [b\'Hello\', b\'World\']
  position = 1
  length = 3

  output = [b\'ell\', b\'orl\']
  ```

  Using `pos` and `len` with same shape as `input`:

  ```python
  input = [[b\'ten\', b\'eleven\', b\'twelve\'],
           [b\'thirteen\', b\'fourteen\', b\'fifteen\'],
           [b\'sixteen\', b\'seventeen\', b\'eighteen\']]
  position = [[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]]
  length =   [[2, 3, 4],
              [4, 3, 2],
              [5, 5, 5]]

  output = [[b\'en\', b\'eve\', b\'lve\'],
            [b\'hirt\', b\'urt\', b\'te\'],
            [b\'ixtee\', b\'vente\', b\'hteen\']]
  ```

  Broadcasting `pos` and `len` onto `input`:

  ```
  input = [[b\'ten\', b\'eleven\', b\'twelve\'],
           [b\'thirteen\', b\'fourteen\', b\'fifteen\'],
           [b\'sixteen\', b\'seventeen\', b\'eighteen\'],
           [b\'nineteen\', b\'twenty\', b\'twentyone\']]
  position = [1, 2, 3]
  length =   [1, 2, 3]

  output = [[b\'e\', b\'ev\', b\'lve\'],
            [b\'h\', b\'ur\', b\'tee\'],
            [b\'i\', b\'ve\', b\'hte\'],
            [b\'i\', b\'en\', b\'nty\']]
  ```

  Broadcasting `input` onto `pos` and `len`:

  ```
  input = b\'thirteen\'
  position = [1, 5, 7]
  length =   [3, 2, 1]

  output = [b\'hir\', b\'ee\', b\'n\']
  ```

  Raises:

    * `ValueError`: If the first argument cannot be converted to a
       Tensor of `dtype string`.
    * `InvalidArgumentError`: If indices are out of range.
    * `ValueError`: If `pos` and `len` are not the same shape.

  Args:
    input: A `Tensor` of type `string`. Tensor of strings
    pos: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Scalar defining the position of first character in each substring
    len: A `Tensor`. Must have the same type as `pos`.
      Scalar defining the number of characters to include in each substring
    unit: An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
      The unit that is used to create the substring.  One of: `"BYTE"` (for
      defining position and length by bytes) or `"UTF8_CHAR"` (for the UTF-8
      encoded Unicode code points).  The default is `"BYTE"`. Results are undefined if
      `unit=UTF8_CHAR` and the `input` strings do not contain structurally valid
      UTF-8.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

Substr: Incomplete

def substr_eager_fallback(input, pos, len, unit, name, ctx): ...

class _UnicodeDecodeOutput(NamedTuple):
    row_splits: Incomplete
    char_values: Incomplete

def unicode_decode(input, input_encoding, errors: str = 'replace', replacement_char: int = 65533, replace_control_characters: bool = False, Tsplits=..., name: Incomplete | None = None):
    '''Decodes each string in `input` into a sequence of Unicode code points.

  The character codepoints for all strings are returned using a single vector
  `char_values`, with strings expanded to characters in row-major order.

  The `row_splits` tensor indicates where the codepoints for
  each input string begin and end within the `char_values` tensor.
  In particular, the values for the `i`th
  string (in row-major order) are stored in the slice
  `[row_splits[i]:row_splits[i+1]]`. Thus:

  * `char_values[row_splits[i]+j]` is the Unicode codepoint for the `j`th
    character in the `i`th string (in row-major order).
  * `row_splits[i+1] - row_splits[i]` is the number of characters in the `i`th
    string (in row-major order).

  Args:
    input: A `Tensor` of type `string`.
      The text to be decoded. Can have any shape. Note that the output is flattened
      to a vector of char values.
    input_encoding: A `string`.
      Text encoding of the input strings. This is any of the encodings supported
      by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`.
    errors: An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`.
      Error handling policy when there is invalid formatting found in the input.
      The value of \'strict\' will cause the operation to produce a InvalidArgument
      error on any invalid input formatting. A value of \'replace\' (the default) will
      cause the operation to replace any invalid formatting in the input with the
      `replacement_char` codepoint. A value of \'ignore\' will cause the operation to
      skip any invalid formatting in the input and produce no corresponding output
      character.
    replacement_char: An optional `int`. Defaults to `65533`.
      The replacement character codepoint to be used in place of any invalid
      formatting in the input when `errors=\'replace\'`. Any valid unicode codepoint may
      be used. The default value is the default unicode replacement character is
      0xFFFD or U+65533.)
    replace_control_characters: An optional `bool`. Defaults to `False`.
      Whether to replace the C0 control characters (00-1F) with the
      `replacement_char`. Default is false.
    Tsplits: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (row_splits, char_values).

    row_splits: A `Tensor` of type `Tsplits`.
    char_values: A `Tensor` of type `int32`.
  '''

UnicodeDecode: Incomplete

def unicode_decode_eager_fallback(input, input_encoding, errors, replacement_char, replace_control_characters, Tsplits, name, ctx): ...

class _UnicodeDecodeWithOffsetsOutput(NamedTuple):
    row_splits: Incomplete
    char_values: Incomplete
    char_to_byte_starts: Incomplete

def unicode_decode_with_offsets(input, input_encoding, errors: str = 'replace', replacement_char: int = 65533, replace_control_characters: bool = False, Tsplits=..., name: Incomplete | None = None):
    '''Decodes each string in `input` into a sequence of Unicode code points.

  The character codepoints for all strings are returned using a single vector
  `char_values`, with strings expanded to characters in row-major order.
  Similarly, the character start byte offsets are returned using a single vector
  `char_to_byte_starts`, with strings expanded in row-major order.

  The `row_splits` tensor indicates where the codepoints and start offsets for
  each input string begin and end within the `char_values` and
  `char_to_byte_starts` tensors.  In particular, the values for the `i`th
  string (in row-major order) are stored in the slice
  `[row_splits[i]:row_splits[i+1]]`. Thus:

  * `char_values[row_splits[i]+j]` is the Unicode codepoint for the `j`th
    character in the `i`th string (in row-major order).
  * `char_to_bytes_starts[row_splits[i]+j]` is the start byte offset for the `j`th
    character in the `i`th string (in row-major order).
  * `row_splits[i+1] - row_splits[i]` is the number of characters in the `i`th
    string (in row-major order).

  Args:
    input: A `Tensor` of type `string`.
      The text to be decoded. Can have any shape. Note that the output is flattened
      to a vector of char values.
    input_encoding: A `string`.
      Text encoding of the input strings. This is any of the encodings supported
      by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`.
    errors: An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`.
      Error handling policy when there is invalid formatting found in the input.
      The value of \'strict\' will cause the operation to produce a InvalidArgument
      error on any invalid input formatting. A value of \'replace\' (the default) will
      cause the operation to replace any invalid formatting in the input with the
      `replacement_char` codepoint. A value of \'ignore\' will cause the operation to
      skip any invalid formatting in the input and produce no corresponding output
      character.
    replacement_char: An optional `int`. Defaults to `65533`.
      The replacement character codepoint to be used in place of any invalid
      formatting in the input when `errors=\'replace\'`. Any valid unicode codepoint may
      be used. The default value is the default unicode replacement character is
      0xFFFD or U+65533.)
    replace_control_characters: An optional `bool`. Defaults to `False`.
      Whether to replace the C0 control characters (00-1F) with the
      `replacement_char`. Default is false.
    Tsplits: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (row_splits, char_values, char_to_byte_starts).

    row_splits: A `Tensor` of type `Tsplits`.
    char_values: A `Tensor` of type `int32`.
    char_to_byte_starts: A `Tensor` of type `int64`.
  '''

UnicodeDecodeWithOffsets: Incomplete

def unicode_decode_with_offsets_eager_fallback(input, input_encoding, errors, replacement_char, replace_control_characters, Tsplits, name, ctx): ...
def unicode_encode(input_values, input_splits, output_encoding, errors: str = 'replace', replacement_char: int = 65533, name: Incomplete | None = None):
    '''Encode a tensor of ints into unicode strings.

  Returns a vector of strings, where `output[i]` is constructed by encoding the
  Unicode codepoints in `input_values[input_splits[i]:input_splits[i+1]]`
  using `output_encoding`.

  ---

  Example:

  ```
  input_values = [72, 101, 108, 108, 111, 87, 111, 114, 108, 100]
  input_splits = [0, 5, 10]
  output_encoding = \'UTF-8\'

  output = [\'Hello\', \'World\']
  ```

  Args:
    input_values: A `Tensor` of type `int32`.
      A 1D tensor containing the unicode codepoints that should be encoded.
    input_splits: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1D tensor specifying how the unicode codepoints should be split into strings.
      In particular, `output[i]` is constructed by encoding the codepoints in the
      slice `input_values[input_splits[i]:input_splits[i+1]]`.
    output_encoding: A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`.
      Unicode encoding of the output strings. Valid encodings are: `"UTF-8",
      "UTF-16-BE", and "UTF-32-BE"`.
    errors: An optional `string` from: `"ignore", "replace", "strict"`. Defaults to `"replace"`.
      Error handling policy when there is invalid formatting found in the input.
      The value of \'strict\' will cause the operation to produce a InvalidArgument
      error on any invalid input formatting. A value of \'replace\' (the default) will
      cause the operation to replace any invalid formatting in the input with the
      `replacement_char` codepoint. A value of \'ignore\' will cause the operation to
      skip any invalid formatting in the input and produce no corresponding output
      character.
    replacement_char: An optional `int`. Defaults to `65533`.
      The replacement character codepoint to be used in place of any invalid
      formatting in the input when `errors=\'replace\'`. Any valid unicode codepoint may
      be used. The default value is the default unicode replacement character is
      0xFFFD (U+65533).
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

UnicodeEncode: Incomplete

def unicode_encode_eager_fallback(input_values, input_splits, output_encoding, errors, replacement_char, name, ctx): ...
def unicode_script(input, name: Incomplete | None = None):
    """Determine the script codes of a given tensor of Unicode integer code points.

  This operation converts Unicode code points to script codes corresponding to
  each code point. Script codes correspond to International Components for
  Unicode (ICU) UScriptCode values.

  See
  [ICU project docs](http://icu-project.org/apiref/icu4c/uscript_8h.html)
  for more details on script codes.

  For an example, see the unicode strings guide on [unicode scripts]
  (https://www.tensorflow.org/tutorials/load_data/unicode#representing_unicode).

  Returns -1 (USCRIPT_INVALID_CODE) for invalid codepoints. Output shape will
  match input shape.

  Examples:

  >>> tf.strings.unicode_script([1, 31, 38])
  <tf.Tensor: shape=(3,), dtype=int32, numpy=array([0, 0, 0], dtype=int32)>

  Args:
    input: A `Tensor` of type `int32`. A Tensor of int32 Unicode code points.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

UnicodeScript: Incomplete

def unicode_script_eager_fallback(input, name, ctx): ...
def unicode_transcode(input, input_encoding, output_encoding, errors: str = 'replace', replacement_char: int = 65533, replace_control_characters: bool = False, name: Incomplete | None = None):
    '''Transcode the input text from a source encoding to a destination encoding.

  The input is a string tensor of any shape. The output is a string tensor of
  the same shape containing the transcoded strings. Output strings are always
  valid unicode. If the input contains invalid encoding positions, the
  `errors` attribute sets the policy for how to deal with them. If the default
  error-handling policy is used, invalid formatting will be substituted in the
  output by the `replacement_char`. If the errors policy is to `ignore`, any
  invalid encoding positions in the input are skipped and not included in the
  output. If it set to `strict` then any invalid formatting will result in an
  InvalidArgument error.

  This operation can be used with `output_encoding = input_encoding` to enforce
  correct formatting for inputs even if they are already in the desired encoding.

  If the input is prefixed by a Byte Order Mark needed to determine encoding
  (e.g. if the encoding is UTF-16 and the BOM indicates big-endian), then that
  BOM will be consumed and not emitted into the output. If the input encoding
  is marked with an explicit endianness (e.g. UTF-16-BE), then the BOM is
  interpreted as a non-breaking-space and is preserved in the output (including
  always for UTF-8).

  The end result is that if the input is marked as an explicit endianness the
  transcoding is faithful to all codepoints in the source. If it is not marked
  with an explicit endianness, the BOM is not considered part of the string itself
  but as metadata, and so is not preserved in the output.

  Examples:

  >>> tf.strings.unicode_transcode(["Hello", "TensorFlow", "2.x"], "UTF-8", "UTF-16-BE")
  <tf.Tensor: shape=(3,), dtype=string, numpy=
  array([b\'\\x00H\\x00e\\x00l\\x00l\\x00o\',
         b\'\\x00T\\x00e\\x00n\\x00s\\x00o\\x00r\\x00F\\x00l\\x00o\\x00w\',
         b\'\\x002\\x00.\\x00x\'], dtype=object)>
  >>> tf.strings.unicode_transcode(["A", "B", "C"], "US ASCII", "UTF-8").numpy()
  array([b\'A\', b\'B\', b\'C\'], dtype=object)

  Args:
    input: A `Tensor` of type `string`.
      The text to be processed. Can have any shape.
    input_encoding: A `string`.
      Text encoding of the input strings. This is any of the encodings supported
      by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`.
    output_encoding: A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`.
      The unicode encoding to use in the output. Must be one of
      `"UTF-8", "UTF-16-BE", "UTF-32-BE"`. Multi-byte encodings will be big-endian.
    errors: An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`.
      Error handling policy when there is invalid formatting found in the input.
      The value of \'strict\' will cause the operation to produce a InvalidArgument
      error on any invalid input formatting. A value of \'replace\' (the default) will
      cause the operation to replace any invalid formatting in the input with the
      `replacement_char` codepoint. A value of \'ignore\' will cause the operation to
      skip any invalid formatting in the input and produce no corresponding output
      character.
    replacement_char: An optional `int`. Defaults to `65533`.
      The replacement character codepoint to be used in place of any invalid
      formatting in the input when `errors=\'replace\'`. Any valid unicode codepoint may
      be used. The default value is the default unicode replacement character is
      0xFFFD or U+65533.)

      Note that for UTF-8, passing a replacement character expressible in 1 byte, such
      as \' \', will preserve string alignment to the source since invalid bytes will be
      replaced with a 1-byte replacement. For UTF-16-BE and UTF-16-LE, any 1 or 2 byte
      replacement character will preserve byte alignment to the source.
    replace_control_characters: An optional `bool`. Defaults to `False`.
      Whether to replace the C0 control characters (00-1F) with the
      `replacement_char`. Default is false.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

UnicodeTranscode: Incomplete

def unicode_transcode_eager_fallback(input, input_encoding, output_encoding, errors, replacement_char, replace_control_characters, name, ctx): ...
def unsorted_segment_join(inputs, segment_ids, num_segments, separator: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    inputs: A `Tensor` of type `string`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    separator: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

UnsortedSegmentJoin: Incomplete

def unsorted_segment_join_eager_fallback(inputs, segment_ids, num_segments, separator, name, ctx): ...
