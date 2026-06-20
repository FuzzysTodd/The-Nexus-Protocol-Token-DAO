from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def anonymous_iterator(output_types, output_shapes, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousIterator: Incomplete

def anonymous_iterator_eager_fallback(output_types, output_shapes, name, ctx): ...

class _AnonymousIteratorV2Output(NamedTuple):
    handle: Incomplete
    deleter: Incomplete

def anonymous_iterator_v2(output_types, output_shapes, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (handle, deleter).

    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

AnonymousIteratorV2: Incomplete

def anonymous_iterator_v2_eager_fallback(output_types, output_shapes, name, ctx): ...
def anonymous_iterator_v3(output_types, output_shapes, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousIteratorV3: Incomplete

def anonymous_iterator_v3_eager_fallback(output_types, output_shapes, name, ctx): ...

class _AnonymousMemoryCacheOutput(NamedTuple):
    handle: Incomplete
    deleter: Incomplete

def anonymous_memory_cache(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (handle, deleter).

    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

AnonymousMemoryCache: Incomplete

def anonymous_memory_cache_eager_fallback(name, ctx): ...

class _AnonymousMultiDeviceIteratorOutput(NamedTuple):
    handle: Incomplete
    deleter: Incomplete

def anonymous_multi_device_iterator(devices, output_types, output_shapes, name: Incomplete | None = None):
    """A container for a multi device iterator resource.

  Args:
    devices: A list of `strings` that has length `>= 1`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (handle, deleter).

    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

AnonymousMultiDeviceIterator: Incomplete

def anonymous_multi_device_iterator_eager_fallback(devices, output_types, output_shapes, name, ctx): ...
def anonymous_multi_device_iterator_v3(devices, output_types, output_shapes, name: Incomplete | None = None):
    """A container for a multi device iterator resource.

  Args:
    devices: A list of `strings` that has length `>= 1`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousMultiDeviceIteratorV3: Incomplete

def anonymous_multi_device_iterator_v3_eager_fallback(devices, output_types, output_shapes, name, ctx): ...

class _AnonymousRandomSeedGeneratorOutput(NamedTuple):
    handle: Incomplete
    deleter: Incomplete

def anonymous_random_seed_generator(seed, seed2, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    seed: A `Tensor` of type `int64`.
    seed2: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (handle, deleter).

    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

AnonymousRandomSeedGenerator: Incomplete

def anonymous_random_seed_generator_eager_fallback(seed, seed2, name, ctx): ...

class _AnonymousSeedGeneratorOutput(NamedTuple):
    handle: Incomplete
    deleter: Incomplete

def anonymous_seed_generator(seed, seed2, reshuffle, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    seed: A `Tensor` of type `int64`.
    seed2: A `Tensor` of type `int64`.
    reshuffle: A `Tensor` of type `bool`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (handle, deleter).

    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

AnonymousSeedGenerator: Incomplete

def anonymous_seed_generator_eager_fallback(seed, seed2, reshuffle, name, ctx): ...
def batch_dataset(input_dataset, batch_size, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that batches `batch_size` elements from `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

BatchDataset: Incomplete

def batch_dataset_eager_fallback(input_dataset, batch_size, output_types, output_shapes, metadata, name, ctx): ...
def batch_dataset_v2(input_dataset, batch_size, drop_remainder, output_types, output_shapes, parallel_copy: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that batches `batch_size` elements from `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a batch.
    drop_remainder: A `Tensor` of type `bool`.
      A scalar representing whether the last batch should be dropped in case its size
      is smaller than desired.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    parallel_copy: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

BatchDatasetV2: Incomplete

def batch_dataset_v2_eager_fallback(input_dataset, batch_size, drop_remainder, output_types, output_shapes, parallel_copy, metadata, name, ctx): ...
def cache_dataset(input_dataset, filename, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that caches elements from `input_dataset`.

  A CacheDataset will iterate over the input_dataset, and store tensors. If the
  cache already exists, the cache will be used. If the cache is inappropriate
  (e.g. cannot be opened, contains tensors of the wrong shape / size), an error
  will the returned when used.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    filename: A `Tensor` of type `string`.
      A path on the filesystem where we should cache the dataset. Note: this
      will be a directory.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

CacheDataset: Incomplete

def cache_dataset_eager_fallback(input_dataset, filename, output_types, output_shapes, metadata, name, ctx): ...
def cache_dataset_v2(input_dataset, filename, cache, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    filename: A `Tensor` of type `string`.
    cache: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

CacheDatasetV2: Incomplete

def cache_dataset_v2_eager_fallback(input_dataset, filename, cache, output_types, output_shapes, metadata, name, ctx): ...
def concatenate_dataset(input_dataset, another_dataset, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that concatenates `input_dataset` with `another_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    another_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ConcatenateDataset: Incomplete

def concatenate_dataset_eager_fallback(input_dataset, another_dataset, output_types, output_shapes, metadata, name, ctx): ...
def dataset_cardinality(input_dataset, name: Incomplete | None = None):
    """Returns the cardinality of `input_dataset`.

  Returns the cardinality of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to return cardinality for.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

DatasetCardinality: Incomplete

def dataset_cardinality_eager_fallback(input_dataset, name, ctx): ...
def dataset_to_graph(input_dataset, stateful_whitelist=[], allow_stateful: bool = False, strip_device_assignment: bool = False, name: Incomplete | None = None):
    """Returns a serialized GraphDef representing `input_dataset`.

  Returns a graph representation for `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to return the graph representation for.
    stateful_whitelist: An optional list of `strings`. Defaults to `[]`.
    allow_stateful: An optional `bool`. Defaults to `False`.
    strip_device_assignment: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DatasetToGraph: Incomplete

def dataset_to_graph_eager_fallback(input_dataset, stateful_whitelist, allow_stateful, strip_device_assignment, name, ctx): ...
def dataset_to_graph_v2(input_dataset, external_state_policy: int = 0, strip_device_assignment: bool = False, name: Incomplete | None = None):
    """Returns a serialized GraphDef representing `input_dataset`.

  Returns a graph representation for `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to return the graph representation for.
    external_state_policy: An optional `int`. Defaults to `0`.
    strip_device_assignment: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DatasetToGraphV2: Incomplete

def dataset_to_graph_v2_eager_fallback(input_dataset, external_state_policy, strip_device_assignment, name, ctx): ...
def dataset_to_single_element(dataset, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Outputs the single element from the given dataset.

  Args:
    dataset: A `Tensor` of type `variant`.
      A handle to a dataset that contains a single element.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  '''

DatasetToSingleElement: Incomplete

def dataset_to_single_element_eager_fallback(dataset, output_types, output_shapes, metadata, name, ctx): ...
def delete_iterator(handle, deleter, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    handle: A `Tensor` of type `resource`. A handle to the iterator to delete.
    deleter: A `Tensor` of type `variant`. A variant deleter.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteIterator: Incomplete

def delete_iterator_eager_fallback(handle, deleter, name, ctx): ...
def delete_memory_cache(handle, deleter, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteMemoryCache: Incomplete

def delete_memory_cache_eager_fallback(handle, deleter, name, ctx): ...
def delete_multi_device_iterator(multi_device_iterator, iterators, deleter, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    multi_device_iterator: A `Tensor` of type `resource`.
      A handle to the multi device iterator to delete.
    iterators: A list of `Tensor` objects with type `resource`.
      A list of iterator handles (unused). This is added so that automatic control dependencies get added during function tracing that ensure this op runs after all the dependent iterators are deleted.
    deleter: A `Tensor` of type `variant`. A variant deleter.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteMultiDeviceIterator: Incomplete

def delete_multi_device_iterator_eager_fallback(multi_device_iterator, iterators, deleter, name, ctx): ...
def delete_random_seed_generator(handle, deleter, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteRandomSeedGenerator: Incomplete

def delete_random_seed_generator_eager_fallback(handle, deleter, name, ctx): ...
def delete_seed_generator(handle, deleter, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteSeedGenerator: Incomplete

def delete_seed_generator_eager_fallback(handle, deleter, name, ctx): ...
def deserialize_iterator(resource_handle, serialized, name: Incomplete | None = None):
    """Converts the given variant tensor to an iterator and stores it in the given resource.

  Args:
    resource_handle: A `Tensor` of type `resource`.
      A handle to an iterator resource.
    serialized: A `Tensor` of type `variant`.
      A variant tensor storing the state of the iterator contained in the
      resource.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeserializeIterator: Incomplete

def deserialize_iterator_eager_fallback(resource_handle, serialized, name, ctx): ...
def dummy_memory_cache(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

DummyMemoryCache: Incomplete

def dummy_memory_cache_eager_fallback(name, ctx): ...
def dummy_seed_generator(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

DummySeedGenerator: Incomplete

def dummy_seed_generator_eager_fallback(name, ctx): ...
def filter_by_last_component_dataset(input_dataset, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset containing elements of first component of `input_dataset` having true in the last component.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

FilterByLastComponentDataset: Incomplete

def filter_by_last_component_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def filter_dataset(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset containing elements of `input_dataset` matching `predicate`.

  The `predicate` function must return a scalar boolean and accept the
  following arguments:

  * One tensor for each component of an element of `input_dataset`.
  * One tensor for each value in `other_arguments`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `predicate`.
    predicate: A function decorated with @Defun.
      A function returning a scalar boolean.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

FilterDataset: Incomplete

def filter_dataset_eager_fallback(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata, name, ctx): ...
def finalize_dataset(input_dataset, output_types, output_shapes, has_captured_ref: bool = False, name: Incomplete | None = None):
    """Creates a dataset by applying `tf.data.Options` to `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    has_captured_ref: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

FinalizeDataset: Incomplete

def finalize_dataset_eager_fallback(input_dataset, output_types, output_shapes, has_captured_ref, name, ctx): ...
def fixed_length_record_dataset(filenames, header_bytes, record_bytes, footer_bytes, buffer_size, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits the records from one or more binary files.

  Args:
    filenames: A `Tensor` of type `string`.
      A scalar or a vector containing the name(s) of the file(s) to be
      read.
    header_bytes: A `Tensor` of type `int64`.
      A scalar representing the number of bytes to skip at the
      beginning of a file.
    record_bytes: A `Tensor` of type `int64`.
      A scalar representing the number of bytes in each record.
    footer_bytes: A `Tensor` of type `int64`.
      A scalar representing the number of bytes to skip at the end
      of a file.
    buffer_size: A `Tensor` of type `int64`.
      A scalar representing the number of bytes to buffer. Must be > 0.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

FixedLengthRecordDataset: Incomplete

def fixed_length_record_dataset_eager_fallback(filenames, header_bytes, record_bytes, footer_bytes, buffer_size, metadata, name, ctx): ...
def fixed_length_record_dataset_v2(filenames, header_bytes, record_bytes, footer_bytes, buffer_size, compression_type, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    header_bytes: A `Tensor` of type `int64`.
    record_bytes: A `Tensor` of type `int64`.
    footer_bytes: A `Tensor` of type `int64`.
    buffer_size: A `Tensor` of type `int64`.
    compression_type: A `Tensor` of type `string`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

FixedLengthRecordDatasetV2: Incomplete

def fixed_length_record_dataset_v2_eager_fallback(filenames, header_bytes, record_bytes, footer_bytes, buffer_size, compression_type, metadata, name, ctx): ...
def flat_map_dataset(input_dataset, other_arguments, f, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Unlike MapDataset, the `f` in FlatMapDataset is expected to return a
  Dataset variant, and FlatMapDataset will flatten successive results
  into a single Dataset.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

FlatMapDataset: Incomplete

def flat_map_dataset_eager_fallback(input_dataset, other_arguments, f, output_types, output_shapes, metadata, name, ctx): ...
def generator_dataset(init_func_other_args, next_func_other_args, finalize_func_other_args, init_func, next_func, finalize_func, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that invokes a function to generate elements.

  Args:
    init_func_other_args: A list of `Tensor` objects.
    next_func_other_args: A list of `Tensor` objects.
    finalize_func_other_args: A list of `Tensor` objects.
    init_func: A function decorated with @Defun.
    next_func: A function decorated with @Defun.
    finalize_func: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

GeneratorDataset: Incomplete

def generator_dataset_eager_fallback(init_func_other_args, next_func_other_args, finalize_func_other_args, init_func, next_func, finalize_func, output_types, output_shapes, metadata, name, ctx): ...
def get_options(input_dataset, name: Incomplete | None = None):
    """Returns the `tf.data.Options` attached to `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

GetOptions: Incomplete

def get_options_eager_fallback(input_dataset, name, ctx): ...
def interleave_dataset(input_dataset, other_arguments, cycle_length, block_length, f, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Unlike MapDataset, the `f` in InterleaveDataset is expected to return
  a Dataset variant, and InterleaveDataset will flatten successive
  results into a single Dataset. Unlike FlatMapDataset,
  InterleaveDataset will interleave sequences of up to `block_length`
  consecutive elements from `cycle_length` input elements.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    cycle_length: A `Tensor` of type `int64`.
    block_length: A `Tensor` of type `int64`.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

InterleaveDataset: Incomplete

def interleave_dataset_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, f, output_types, output_shapes, metadata, name, ctx): ...
def iterator(shared_name, container, output_types, output_shapes, name: Incomplete | None = None):
    """A container for an iterator resource.

  Args:
    shared_name: A `string`.
    container: A `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

Iterator: Incomplete

def iterator_eager_fallback(shared_name, container, output_types, output_shapes, name, ctx): ...
def iterator_from_string_handle(string_handle, output_types=[], output_shapes=[], name: Incomplete | None = None):
    """Converts the given string representing a handle to an iterator to a resource.

  Args:
    string_handle: A `Tensor` of type `string`.
      A string representation of the given handle.
    output_types: An optional list of `tf.DTypes`. Defaults to `[]`.
      If specified, defines the type of each tuple component in an
      element produced by the resulting iterator.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      If specified, defines the shape of each tuple component in an
      element produced by the resulting iterator.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

IteratorFromStringHandle: Incomplete

def iterator_from_string_handle_eager_fallback(string_handle, output_types, output_shapes, name, ctx): ...
def iterator_from_string_handle_v2(string_handle, output_types=[], output_shapes=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    string_handle: A `Tensor` of type `string`.
    output_types: An optional list of `tf.DTypes`. Defaults to `[]`.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

IteratorFromStringHandleV2: Incomplete

def iterator_from_string_handle_v2_eager_fallback(string_handle, output_types, output_shapes, name, ctx): ...
def iterator_get_next(iterator, output_types, output_shapes, name: Incomplete | None = None):
    """Gets the next output from the given iterator .

  Args:
    iterator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

IteratorGetNext: Incomplete

def iterator_get_next_eager_fallback(iterator, output_types, output_shapes, name, ctx): ...
def iterator_get_next_as_optional(iterator, output_types, output_shapes, name: Incomplete | None = None):
    """Gets the next output from the given iterator as an Optional variant.

  Args:
    iterator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

IteratorGetNextAsOptional: Incomplete

def iterator_get_next_as_optional_eager_fallback(iterator, output_types, output_shapes, name, ctx): ...
def iterator_get_next_sync(iterator, output_types, output_shapes, name: Incomplete | None = None):
    """Gets the next output from the given iterator.

  This operation is a synchronous version IteratorGetNext. It should only be used
  in situations where the iterator does not block the calling thread, or where
  the calling thread is not a member of the thread pool used to execute parallel
  operations (e.g. in eager mode).

  Args:
    iterator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

IteratorGetNextSync: Incomplete

def iterator_get_next_sync_eager_fallback(iterator, output_types, output_shapes, name, ctx): ...
def iterator_to_string_handle(resource_handle, name: Incomplete | None = None):
    """Converts the given `resource_handle` representing an iterator to a string.

  Args:
    resource_handle: A `Tensor` of type `resource`.
      A handle to an iterator resource.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

IteratorToStringHandle: Incomplete

def iterator_to_string_handle_eager_fallback(resource_handle, name, ctx): ...
def iterator_v2(shared_name, container, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    shared_name: A `string`.
    container: A `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

IteratorV2: Incomplete

def iterator_v2_eager_fallback(shared_name, container, output_types, output_shapes, name, ctx): ...
def make_iterator(dataset, iterator, name: Incomplete | None = None):
    """Makes a new iterator from the given `dataset` and stores it in `iterator`.

  This operation may be executed multiple times. Each execution will reset the
  iterator in `iterator` to the first element of `dataset`.

  Args:
    dataset: A `Tensor` of type `variant`.
    iterator: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

MakeIterator: Incomplete

def make_iterator_eager_fallback(dataset, iterator, name, ctx): ...
def map_dataset(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism: bool = True, preserve_cardinality: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_inter_op_parallelism: An optional `bool`. Defaults to `True`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

MapDataset: Incomplete

def map_dataset_eager_fallback(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism, preserve_cardinality, metadata, name, ctx): ...
def map_defun(arguments, captured_inputs, output_types, output_shapes, f, max_intra_op_parallelism: int = 1, name: Incomplete | None = None):
    """  Maps a function on the list of tensors unpacked from arguments on dimension 0.
  The function given by `f` is assumed to be stateless, and is executed
  concurrently on all the slices; up to batch_size (i.e. the size of the 0th
  dimension of each argument) functions will be scheduled at once.

  The `max_intra_op_parallelism` attr, which defaults to 1, can be used to
  limit the intra op parallelism. To limit inter-op parallelism, a user can
  set a private threadpool on the dataset using `tf.data.Options`'s
  `ThreadingOptions`.

  Note that this op is not exposed to users directly, but is invoked in tf.data
  rewrites.

  Args:
    arguments: A list of `Tensor` objects.
          A list of tensors whose types are `Targuments`, corresponding to the inputs
          the function should be mapped over.
    captured_inputs: A list of `Tensor` objects.
          A list of tensors whose types are `Tcaptured`, corresponding to the captured
          inputs of the defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      A list of types.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      A list of shapes.
    f: A function decorated with @Defun.
    max_intra_op_parallelism: An optional `int`. Defaults to `1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

MapDefun: Incomplete

def map_defun_eager_fallback(arguments, captured_inputs, output_types, output_shapes, f, max_intra_op_parallelism, name, ctx): ...
def model_dataset(input_dataset, output_types, output_shapes, algorithm: int = 0, cpu_budget: int = 0, ram_budget: int = 0, name: Incomplete | None = None):
    """Identity transformation that models performance.

  Identity transformation that models performance.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    algorithm: An optional `int`. Defaults to `0`.
    cpu_budget: An optional `int`. Defaults to `0`.
    ram_budget: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ModelDataset: Incomplete

def model_dataset_eager_fallback(input_dataset, output_types, output_shapes, algorithm, cpu_budget, ram_budget, name, ctx): ...
def multi_device_iterator(devices, shared_name, container, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a MultiDeviceIterator resource.

  Args:
    devices: A list of `strings` that has length `>= 1`.
      A list of devices the iterator works across.
    shared_name: A `string`.
      If non-empty, this resource will be shared under the given name
      across multiple sessions.
    container: A `string`.
      If non-empty, this resource is placed in the given container.
      Otherwise, a default container is used.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      The list of shapes being produced.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

MultiDeviceIterator: Incomplete

def multi_device_iterator_eager_fallback(devices, shared_name, container, output_types, output_shapes, name, ctx): ...
def multi_device_iterator_from_string_handle(string_handle, output_types=[], output_shapes=[], name: Incomplete | None = None):
    """Generates a MultiDeviceIterator resource from its provided string handle.

  Args:
    string_handle: A `Tensor` of type `string`.
      String representing the resource.
    output_types: An optional list of `tf.DTypes`. Defaults to `[]`.
      The type list for the return values.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      The list of shapes being produced.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

MultiDeviceIteratorFromStringHandle: Incomplete

def multi_device_iterator_from_string_handle_eager_fallback(string_handle, output_types, output_shapes, name, ctx): ...
def multi_device_iterator_get_next_from_shard(multi_device_iterator, shard_num, incarnation_id, output_types, output_shapes, name: Incomplete | None = None):
    """Gets next element for the provided shard number.

  Args:
    multi_device_iterator: A `Tensor` of type `resource`.
      A MultiDeviceIterator resource.
    shard_num: A `Tensor` of type `int32`.
      Integer representing which shard to fetch data for.
    incarnation_id: A `Tensor` of type `int64`.
      Which incarnation of the MultiDeviceIterator is running.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      The list of shapes being produced.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

MultiDeviceIteratorGetNextFromShard: Incomplete

def multi_device_iterator_get_next_from_shard_eager_fallback(multi_device_iterator, shard_num, incarnation_id, output_types, output_shapes, name, ctx): ...
def multi_device_iterator_init(dataset, multi_device_iterator, max_buffer_size, name: Incomplete | None = None):
    """Initializes the multi device iterator with the given dataset.

  Args:
    dataset: A `Tensor` of type `variant`. Dataset to be iterated upon.
    multi_device_iterator: A `Tensor` of type `resource`.
      A MultiDeviceIteratorResource.
    max_buffer_size: A `Tensor` of type `int64`.
      The maximum size of the host side per device buffer to keep.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

MultiDeviceIteratorInit: Incomplete

def multi_device_iterator_init_eager_fallback(dataset, multi_device_iterator, max_buffer_size, name, ctx): ...
def multi_device_iterator_to_string_handle(multi_device_iterator, name: Incomplete | None = None):
    """Produces a string handle for the given MultiDeviceIterator.

  Args:
    multi_device_iterator: A `Tensor` of type `resource`.
      A MultiDeviceIterator resource.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

MultiDeviceIteratorToStringHandle: Incomplete

def multi_device_iterator_to_string_handle_eager_fallback(multi_device_iterator, name, ctx): ...
def one_shot_iterator(dataset_factory, output_types, output_shapes, container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Makes a "one-shot" iterator that can be iterated only once.

  A one-shot iterator bundles the logic for defining the dataset and
  the state of the iterator in a single op, which allows simple input
  pipelines to be defined without an additional initialization
  ("MakeIterator") step.

  One-shot iterators have the following limitations:

  * They do not support parameterization: all logic for creating the underlying
    dataset must be bundled in the `dataset_factory` function.
  * They are not resettable. Once a one-shot iterator reaches the end of its
    underlying dataset, subsequent "IteratorGetNext" operations on that
    iterator will always produce an `OutOfRange` error.

  For greater flexibility, use "Iterator" and "MakeIterator" to define
  an iterator using an arbitrary subgraph, which may capture tensors
  (including fed values) as parameters, and which may be reset multiple
  times by rerunning "MakeIterator".

  Args:
    dataset_factory: A function decorated with @Defun.
      A function of type `() -> DT_VARIANT`, where the returned
      DT_VARIANT is a dataset.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

OneShotIterator: Incomplete

def one_shot_iterator_eager_fallback(dataset_factory, output_types, output_shapes, container, shared_name, name, ctx): ...
def optimize_dataset(input_dataset, optimizations, output_types, output_shapes, optimization_configs=[], name: Incomplete | None = None):
    """Creates a dataset by applying optimizations to `input_dataset`.

  Creates a dataset by applying optimizations to `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    optimizations: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying optimizations to use.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    optimization_configs: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

OptimizeDataset: Incomplete

def optimize_dataset_eager_fallback(input_dataset, optimizations, output_types, output_shapes, optimization_configs, name, ctx): ...
def optimize_dataset_v2(input_dataset, optimizations_enabled, optimizations_disabled, optimizations_default, output_types, output_shapes, optimization_configs=[], name: Incomplete | None = None):
    """Creates a dataset by applying related optimizations to `input_dataset`.

  Creates a dataset by applying related optimizations to `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    optimizations_enabled: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying user enabled optimizations.
    optimizations_disabled: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying user disabled optimizations.
    optimizations_default: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying optimizations by default.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    optimization_configs: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

OptimizeDatasetV2: Incomplete

def optimize_dataset_v2_eager_fallback(input_dataset, optimizations_enabled, optimizations_disabled, optimizations_default, output_types, output_shapes, optimization_configs, name, ctx): ...
def options_dataset(input_dataset, serialized_options, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset by attaching tf.data.Options to `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    serialized_options: A `string`.
      A `tf.string` scalar `tf.Tensor` of serialized `tf.data.Options` protocol buffer.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

OptionsDataset: Incomplete

def options_dataset_eager_fallback(input_dataset, serialized_options, output_types, output_shapes, metadata, name, ctx): ...
def padded_batch_dataset(input_dataset, batch_size, padded_shapes, padding_values, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that batches and pads `batch_size` elements from the input.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch.
    padded_shapes: A list of at least 1 `Tensor` objects with type `int64`.
      A list of int64 tensors representing the desired padded shapes
      of the corresponding output components. These shapes may be partially
      specified, using `-1` to indicate that a particular dimension should be
      padded to the maximum size of all batch elements.
    padding_values: A list of `Tensor` objects.
      A list of scalars containing the padding value to use for
      each of the outputs.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

PaddedBatchDataset: Incomplete

def padded_batch_dataset_eager_fallback(input_dataset, batch_size, padded_shapes, padding_values, output_shapes, metadata, name, ctx): ...
def padded_batch_dataset_v2(input_dataset, batch_size, padded_shapes, padding_values, drop_remainder, output_shapes, parallel_copy: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that batches and pads `batch_size` elements from the input.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch.
    padded_shapes: A list of at least 1 `Tensor` objects with type `int64`.
      A list of int64 tensors representing the desired padded shapes
      of the corresponding output components. These shapes may be partially
      specified, using `-1` to indicate that a particular dimension should be
      padded to the maximum size of all batch elements.
    padding_values: A list of `Tensor` objects.
      A list of scalars containing the padding value to use for
      each of the outputs.
    drop_remainder: A `Tensor` of type `bool`.
      A scalar representing whether the last batch should be dropped in case its size
      is smaller than desired.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    parallel_copy: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

PaddedBatchDatasetV2: Incomplete

def padded_batch_dataset_v2_eager_fallback(input_dataset, batch_size, padded_shapes, padding_values, drop_remainder, output_shapes, parallel_copy, metadata, name, ctx): ...
def parallel_batch_dataset(input_dataset, batch_size, num_parallel_calls, drop_remainder, output_types, output_shapes, parallel_copy: bool = False, deterministic: str = 'default', metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    batch_size: A `Tensor` of type `int64`.
    num_parallel_calls: A `Tensor` of type `int64`.
    drop_remainder: A `Tensor` of type `bool`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    parallel_copy: An optional `bool`. Defaults to `False`.
    deterministic: An optional `string`. Defaults to `"default"`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelBatchDataset: Incomplete

def parallel_batch_dataset_eager_fallback(input_dataset, batch_size, num_parallel_calls, drop_remainder, output_types, output_shapes, parallel_copy, deterministic, metadata, name, ctx): ...
def parallel_filter_dataset(input_dataset, other_arguments, num_parallel_calls, predicate, output_types, output_shapes, deterministic: str = 'default', metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset containing elements of `input_dataset` matching `predicate`.

  The `predicate` function must return a scalar boolean and accept the
  following arguments:

  * One tensor for each component of an element of `input_dataset`.
  * One tensor for each value in `other_arguments`.

  Unlike a "FilterDataset", which applies `predicate` sequentially, this dataset
  invokes up to `num_parallel_calls` copies of `predicate` in parallel.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `predicate`.
    num_parallel_calls: A `Tensor` of type `int64`.
      The number of concurrent invocations of `predicate` that process
      elements from `input_dataset` in parallel.
    predicate: A function decorated with @Defun.
      A function returning a scalar boolean.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    deterministic: An optional `string`. Defaults to `"default"`.
      A string indicating the op-level determinism to use. Deterministic controls
      whether the interleave is allowed to return elements out of order if the next
      element to be returned isn\'t available, but a later element is. Options are
      "true", "false", and "default". "default" indicates that determinism should be
      decided by the `experimental_deterministic` parameter of `tf.data.Options`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelFilterDataset: Incomplete

def parallel_filter_dataset_eager_fallback(input_dataset, other_arguments, num_parallel_calls, predicate, output_types, output_shapes, deterministic, metadata, name, ctx): ...
def parallel_interleave_dataset_v2(input_dataset, other_arguments, cycle_length, block_length, num_parallel_calls, f, output_types, output_shapes, sloppy: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, except that the
  dataset will fetch records from the interleaved datasets in parallel.

  The `tf.data` Python API creates instances of this op from
  `Dataset.interleave()` when the `num_parallel_calls` parameter of that method
  is set to any value other than `None`.

  By default, the output of this dataset will be deterministic, which may result
  in the dataset blocking if the next data item to be returned isn\'t available.
  In order to avoid head-of-line blocking, one can set the
  `experimental_deterministic` parameter of `tf.data.Options` to `False`,
  which can improve performance at the expense of non-determinism.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      Dataset that produces a stream of arguments for the function `f`.
    other_arguments: A list of `Tensor` objects.
      Additional arguments to pass to `f` beyond those produced by `input_dataset`.
      Evaluated once when the dataset is instantiated.
    cycle_length: A `Tensor` of type `int64`.
      Number of datasets (each created by applying `f` to the elements of
      `input_dataset`) among which the `ParallelInterleaveDatasetV2` will cycle in a
      round-robin fashion.
    block_length: A `Tensor` of type `int64`.
      Number of elements at a time to produce from each interleaved invocation of a
      dataset returned by `f`.
    num_parallel_calls: A `Tensor` of type `int64`.
      Determines the number of threads that should be used for fetching data from
      input datasets in parallel. The Python API `tf.data.experimental.AUTOTUNE`
      constant can be used to indicate that the level of parallelism should be autotuned.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    sloppy: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelInterleaveDatasetV2: Incomplete

def parallel_interleave_dataset_v2_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, num_parallel_calls, f, output_types, output_shapes, sloppy, metadata, name, ctx): ...
def parallel_interleave_dataset_v3(input_dataset, other_arguments, cycle_length, block_length, num_parallel_calls, f, output_types, output_shapes, deterministic: str = 'default', metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, except that the
  dataset will fetch records from the interleaved datasets in parallel.

  The `tf.data` Python API creates instances of this op from
  `Dataset.interleave()` when the `num_parallel_calls` parameter of that method
  is set to any value other than `None`.

  By default, the output of this dataset will be deterministic, which may result
  in the dataset blocking if the next data item to be returned isn\'t available.
  In order to avoid head-of-line blocking, one can either set the `deterministic`
  attribute to "false", or leave it as "default" and set the
  `experimental_deterministic` parameter of `tf.data.Options` to `False`.
  This can improve performance at the expense of non-determinism.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      Dataset that produces a stream of arguments for the function `f`.
    other_arguments: A list of `Tensor` objects.
      Additional arguments to pass to `f` beyond those produced by `input_dataset`.
      Evaluated once when the dataset is instantiated.
    cycle_length: A `Tensor` of type `int64`.
      Number of datasets (each created by applying `f` to the elements of
      `input_dataset`) among which the `ParallelInterleaveDatasetV2` will cycle in a
      round-robin fashion.
    block_length: A `Tensor` of type `int64`.
      Number of elements at a time to produce from each interleaved invocation of a
      dataset returned by `f`.
    num_parallel_calls: A `Tensor` of type `int64`.
      Determines the number of threads that should be used for fetching data from
      input datasets in parallel. The Python API `tf.data.experimental.AUTOTUNE`
      constant can be used to indicate that the level of parallelism should be autotuned.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    deterministic: An optional `string`. Defaults to `"default"`.
      A string indicating the op-level determinism to use. Deterministic controls
      whether the interleave is allowed to return elements out of order if the next
      element to be returned isn\'t available, but a later element is. Options are
      "true", "false", and "default". "default" indicates that determinism should be
      decided by the `experimental_deterministic` parameter of `tf.data.Options`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelInterleaveDatasetV3: Incomplete

def parallel_interleave_dataset_v3_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, num_parallel_calls, f, output_types, output_shapes, deterministic, metadata, name, ctx): ...
def parallel_interleave_dataset_v4(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, num_parallel_calls, f, output_types, output_shapes, deterministic: str = 'default', metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, except that the
  dataset will fetch records from the interleaved datasets in parallel.

  The `tf.data` Python API creates instances of this op from
  `Dataset.interleave()` when the `num_parallel_calls` parameter of that method
  is set to any value other than `None`.

  By default, the output of this dataset will be deterministic, which may result
  in the dataset blocking if the next data item to be returned isn\'t available.
  In order to avoid head-of-line blocking, one can either set the `deterministic`
  attribute to "false", or leave it as "default" and set the
  `experimental_deterministic` parameter of `tf.data.Options` to `False`.
  This can improve performance at the expense of non-determinism.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      Dataset that produces a stream of arguments for the function `f`.
    other_arguments: A list of `Tensor` objects.
      Additional arguments to pass to `f` beyond those produced by `input_dataset`.
      Evaluated once when the dataset is instantiated.
    cycle_length: A `Tensor` of type `int64`.
      Number of datasets (each created by applying `f` to the elements of
      `input_dataset`) among which the `ParallelInterleaveDatasetV2` will cycle in a
      round-robin fashion.
    block_length: A `Tensor` of type `int64`.
      Number of elements at a time to produce from each interleaved invocation of a
      dataset returned by `f`.
    buffer_output_elements: A `Tensor` of type `int64`.
      The number of elements each iterator being interleaved should buffer (similar
      to the `.prefetch()` transformation for each interleaved iterator).
    prefetch_input_elements: A `Tensor` of type `int64`.
      Determines the number of iterators to prefetch, allowing buffers to warm up and
      data to be pre-fetched without blocking the main thread.
    num_parallel_calls: A `Tensor` of type `int64`.
      Determines the number of threads that should be used for fetching data from
      input datasets in parallel. The Python API `tf.data.experimental.AUTOTUNE`
      constant can be used to indicate that the level of parallelism should be autotuned.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    deterministic: An optional `string`. Defaults to `"default"`.
      A string indicating the op-level determinism to use. Deterministic controls
      whether the interleave is allowed to return elements out of order if the next
      element to be returned isn\'t available, but a later element is. Options are
      "true", "false", and "default". "default" indicates that determinism should be
      decided by the `experimental_deterministic` parameter of `tf.data.Options`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelInterleaveDatasetV4: Incomplete

def parallel_interleave_dataset_v4_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, num_parallel_calls, f, output_types, output_shapes, deterministic, metadata, name, ctx): ...
def parallel_map_dataset(input_dataset, other_arguments, num_parallel_calls, f, output_types, output_shapes, use_inter_op_parallelism: bool = True, sloppy: bool = False, preserve_cardinality: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
  to `num_parallel_calls` copies of `f` in parallel.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    num_parallel_calls: A `Tensor` of type `int32`.
      The number of concurrent invocations of `f` that process
      elements from `input_dataset` in parallel.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_inter_op_parallelism: An optional `bool`. Defaults to `True`.
    sloppy: An optional `bool`. Defaults to `False`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelMapDataset: Incomplete

def parallel_map_dataset_eager_fallback(input_dataset, other_arguments, num_parallel_calls, f, output_types, output_shapes, use_inter_op_parallelism, sloppy, preserve_cardinality, metadata, name, ctx): ...
def parallel_map_dataset_v2(input_dataset, other_arguments, num_parallel_calls, f, output_types, output_shapes, use_inter_op_parallelism: bool = True, deterministic: str = 'default', preserve_cardinality: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
  to `num_parallel_calls` copies of `f` in parallel.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    num_parallel_calls: A `Tensor` of type `int64`.
      The number of concurrent invocations of `f` that process
      elements from `input_dataset` in parallel.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_inter_op_parallelism: An optional `bool`. Defaults to `True`.
    deterministic: An optional `string`. Defaults to `"default"`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelMapDatasetV2: Incomplete

def parallel_map_dataset_v2_eager_fallback(input_dataset, other_arguments, num_parallel_calls, f, output_types, output_shapes, use_inter_op_parallelism, deterministic, preserve_cardinality, metadata, name, ctx): ...
def prefetch_dataset(input_dataset, buffer_size, output_types, output_shapes, slack_period: int = 0, legacy_autotune: bool = True, buffer_size_min: int = 0, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that asynchronously prefetches elements from `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
      The maximum number of elements to buffer in an iterator over
      this dataset.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    slack_period: An optional `int`. Defaults to `0`.
    legacy_autotune: An optional `bool`. Defaults to `True`.
    buffer_size_min: An optional `int`. Defaults to `0`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

PrefetchDataset: Incomplete

def prefetch_dataset_eager_fallback(input_dataset, buffer_size, output_types, output_shapes, slack_period, legacy_autotune, buffer_size_min, metadata, name, ctx): ...
def range_dataset(start, stop, step, output_types, output_shapes, metadata: str = '', replicate_on_split: bool = False, name: Incomplete | None = None):
    '''Creates a dataset with a range of values. Corresponds to python\'s xrange.

  Args:
    start: A `Tensor` of type `int64`.
      corresponds to start in python\'s xrange().
    stop: A `Tensor` of type `int64`.
      corresponds to stop in python\'s xrange().
    step: A `Tensor` of type `int64`.
      corresponds to step in python\'s xrange().
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    replicate_on_split: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

RangeDataset: Incomplete

def range_dataset_eager_fallback(start, stop, step, output_types, output_shapes, metadata, replicate_on_split, name, ctx): ...
def reduce_dataset(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''Reduces the input dataset to a singleton using a reduce function.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    initial_state: A list of `Tensor` objects.
      A nested structure of tensors, representing the initial state of the
      transformation.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
      A function that maps `(old_state, input_element)` to `new_state`. It must take
      two arguments and return a nested structures of tensors. The structure of
      `new_state` must match the structure of `initial_state`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_inter_op_parallelism: An optional `bool`. Defaults to `True`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  '''

ReduceDataset: Incomplete

def reduce_dataset_eager_fallback(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism, metadata, name, ctx): ...
def repeat_dataset(input_dataset, count, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits the outputs of `input_dataset` `count` times.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    count: A `Tensor` of type `int64`.
      A scalar representing the number of times that `input_dataset` should
      be repeated. A value of `-1` indicates that it should be repeated infinitely.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

RepeatDataset: Incomplete

def repeat_dataset_eager_fallback(input_dataset, count, output_types, output_shapes, metadata, name, ctx): ...
def rewrite_dataset(input_dataset, rewrite_name, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    rewrite_name: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

RewriteDataset: Incomplete

def rewrite_dataset_eager_fallback(input_dataset, rewrite_name, output_types, output_shapes, name, ctx): ...
def serialize_iterator(resource_handle, external_state_policy: int = 0, name: Incomplete | None = None):
    """Converts the given `resource_handle` representing an iterator to a variant tensor.

  Args:
    resource_handle: A `Tensor` of type `resource`.
      A handle to an iterator resource.
    external_state_policy: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SerializeIterator: Incomplete

def serialize_iterator_eager_fallback(resource_handle, external_state_policy, name, ctx): ...
def shard_dataset(input_dataset, num_shards, index, output_types, output_shapes, require_non_empty: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_shards: A `Tensor` of type `int64`.
      An integer representing the number of shards operating in parallel.
    index: A `Tensor` of type `int64`.
      An integer representing the current worker index.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    require_non_empty: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShardDataset: Incomplete

def shard_dataset_eager_fallback(input_dataset, num_shards, index, output_types, output_shapes, require_non_empty, metadata, name, ctx): ...
def shuffle_and_repeat_dataset(input_dataset, buffer_size, seed, seed2, count, output_types, output_shapes, reshuffle_each_iteration: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that shuffles and repeats elements from `input_dataset`

  pseudorandomly.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
      The number of output elements to buffer in an iterator over
      this dataset. Compare with the `min_after_dequeue` attr when creating a
      `RandomShuffleQueue`.
    seed: A `Tensor` of type `int64`.
      A scalar seed for the random number generator. If either `seed` or
      `seed2` is set to be non-zero, the random number generator is seeded
      by the given seed.  Otherwise, a random seed is used.
    seed2: A `Tensor` of type `int64`.
      A second scalar seed to avoid seed collision.
    count: A `Tensor` of type `int64`.
      A scalar representing the number of times the underlying dataset
      should be repeated. The default is `-1`, which results in infinite repetition.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reshuffle_each_iteration: An optional `bool`. Defaults to `True`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShuffleAndRepeatDataset: Incomplete

def shuffle_and_repeat_dataset_eager_fallback(input_dataset, buffer_size, seed, seed2, count, output_types, output_shapes, reshuffle_each_iteration, metadata, name, ctx): ...
def shuffle_and_repeat_dataset_v2(input_dataset, buffer_size, seed, seed2, count, seed_generator, output_types, output_shapes, reshuffle_each_iteration: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
    seed: A `Tensor` of type `int64`.
    seed2: A `Tensor` of type `int64`.
    count: A `Tensor` of type `int64`.
    seed_generator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reshuffle_each_iteration: An optional `bool`. Defaults to `True`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShuffleAndRepeatDatasetV2: Incomplete

def shuffle_and_repeat_dataset_v2_eager_fallback(input_dataset, buffer_size, seed, seed2, count, seed_generator, output_types, output_shapes, reshuffle_each_iteration, metadata, name, ctx): ...
def shuffle_dataset(input_dataset, buffer_size, seed, seed2, output_types, output_shapes, reshuffle_each_iteration: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that shuffles elements from `input_dataset` pseudorandomly.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
      The number of output elements to buffer in an iterator over
      this dataset. Compare with the `min_after_dequeue` attr when creating a
      `RandomShuffleQueue`.
    seed: A `Tensor` of type `int64`.
      A scalar seed for the random number generator. If either `seed` or
      `seed2` is set to be non-zero, the random number generator is seeded
      by the given seed.  Otherwise, a random seed is used.
    seed2: A `Tensor` of type `int64`.
      A second scalar seed to avoid seed collision.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reshuffle_each_iteration: An optional `bool`. Defaults to `True`.
      If true, each iterator over this dataset will be given
      a different pseudorandomly generated seed, based on a sequence seeded by the
      `seed` and `seed2` inputs. If false, each iterator will be given the same
      seed, and repeated iteration over this dataset will yield the exact same
      sequence of results.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShuffleDataset: Incomplete

def shuffle_dataset_eager_fallback(input_dataset, buffer_size, seed, seed2, output_types, output_shapes, reshuffle_each_iteration, metadata, name, ctx): ...
def shuffle_dataset_v2(input_dataset, buffer_size, seed_generator, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
    seed_generator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShuffleDatasetV2: Incomplete

def shuffle_dataset_v2_eager_fallback(input_dataset, buffer_size, seed_generator, output_types, output_shapes, metadata, name, ctx): ...
def shuffle_dataset_v3(input_dataset, buffer_size, seed, seed2, seed_generator, output_types, output_shapes, reshuffle_each_iteration: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    buffer_size: A `Tensor` of type `int64`.
    seed: A `Tensor` of type `int64`.
    seed2: A `Tensor` of type `int64`.
    seed_generator: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reshuffle_each_iteration: An optional `bool`. Defaults to `True`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ShuffleDatasetV3: Incomplete

def shuffle_dataset_v3_eager_fallback(input_dataset, buffer_size, seed, seed2, seed_generator, output_types, output_shapes, reshuffle_each_iteration, metadata, name, ctx): ...
def skip_dataset(input_dataset, count, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that skips `count` elements from the `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    count: A `Tensor` of type `int64`.
      A scalar representing the number of elements from the `input_dataset`
      that should be skipped.  If count is -1, skips everything.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

SkipDataset: Incomplete

def skip_dataset_eager_fallback(input_dataset, count, output_types, output_shapes, metadata, name, ctx): ...
def sparse_tensor_slice_dataset(indices, values, dense_shape, name: Incomplete | None = None):
    """Creates a dataset that splits a SparseTensor into elements row-wise.

  Args:
    indices: A `Tensor` of type `int64`.
    values: A `Tensor`.
    dense_shape: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SparseTensorSliceDataset: Incomplete

def sparse_tensor_slice_dataset_eager_fallback(indices, values, dense_shape, name, ctx): ...
def tf_record_dataset(filenames, compression_type, buffer_size, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits the records from one or more TFRecord files.

  Args:
    filenames: A `Tensor` of type `string`.
      A scalar or vector containing the name(s) of the file(s) to be
      read.
    compression_type: A `Tensor` of type `string`.
      A scalar containing either (i) the empty string (no
      compression), (ii) "ZLIB", or (iii) "GZIP".
    buffer_size: A `Tensor` of type `int64`.
      A scalar representing the number of bytes to buffer. A value of
      0 means no buffering will be performed.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TFRecordDataset: Incomplete

def tf_record_dataset_eager_fallback(filenames, compression_type, buffer_size, metadata, name, ctx): ...
def take_dataset(input_dataset, count, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that contains `count` elements from the `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    count: A `Tensor` of type `int64`.
      A scalar representing the number of elements from the `input_dataset`
      that should be taken. A value of `-1` indicates that all of `input_dataset`
      is taken.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TakeDataset: Incomplete

def take_dataset_eager_fallback(input_dataset, count, output_types, output_shapes, metadata, name, ctx): ...
def tensor_dataset(components, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits `components` as a tuple of tensors once.

  Args:
    components: A list of `Tensor` objects.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TensorDataset: Incomplete

def tensor_dataset_eager_fallback(components, output_shapes, metadata, name, ctx): ...
def tensor_slice_dataset(components, output_shapes, is_files: bool = False, metadata: str = '', replicate_on_split: bool = False, name: Incomplete | None = None):
    '''Creates a dataset that emits each dim-0 slice of `components` once.

  Args:
    components: A list of `Tensor` objects.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    is_files: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    replicate_on_split: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TensorSliceDataset: Incomplete

def tensor_slice_dataset_eager_fallback(components, output_shapes, is_files, metadata, replicate_on_split, name, ctx): ...
def text_line_dataset(filenames, compression_type, buffer_size, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits the lines of one or more text files.

  Args:
    filenames: A `Tensor` of type `string`.
      A scalar or a vector containing the name(s) of the file(s) to be
      read.
    compression_type: A `Tensor` of type `string`.
      A scalar containing either (i) the empty string (no
      compression), (ii) "ZLIB", or (iii) "GZIP".
    buffer_size: A `Tensor` of type `int64`.
      A scalar containing the number of bytes to buffer.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TextLineDataset: Incomplete

def text_line_dataset_eager_fallback(filenames, compression_type, buffer_size, metadata, name, ctx): ...
def unwrap_dataset_variant(input_handle, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_handle: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

UnwrapDatasetVariant: Incomplete

def unwrap_dataset_variant_eager_fallback(input_handle, name, ctx): ...
def window_dataset(input_dataset, size, shift, stride, drop_remainder, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''  Combines (nests of) input elements into a dataset of (nests of) windows.

  A "window" is a finite dataset of flat elements of size `size` (or possibly
  fewer if there are not enough input elements to fill the window and
  `drop_remainder` evaluates to false).

  The `shift` argument determines the number of input elements by which
  the window moves on each iteration.  The first element in the `k`th window
  will be element

  ```
  1 + (k-1) * shift
  ```

  of the input dataset. In particular, the first element of the first window
  will always be the first element of the input dataset.  

  If the `stride` parameter is greater than 1, then each window will skip
  `(stride - 1)` input elements between each element that appears in the
  window. Output windows will still contain `size` elements regardless of
  the value of `stride`.

  The `stride` argument determines the stride of the input elements, and the
  `shift` argument determines the shift of the window.

  For example, letting `{...}` to represent a Dataset:

  - `tf.data.Dataset.range(7).window(2)` produces
    `{{0, 1}, {2, 3}, {4, 5}, {6}}`
  - `tf.data.Dataset.range(7).window(3, 2, 1, True)` produces
    `{{0, 1, 2}, {2, 3, 4}, {4, 5, 6}}`
  - `tf.data.Dataset.range(7).window(3, 1, 2, True)` produces
    `{{0, 2, 4}, {1, 3, 5}, {2, 4, 6}}`

  Note that when the `window` transformation is applied to a dataset of
  nested elements, it produces a dataset of nested windows.

  For example:

  - `tf.data.Dataset.from_tensor_slices((range(4), range(4))).window(2)`
    produces `{({0, 1}, {0, 1}), ({2, 3}, {2, 3})}`
  - `tf.data.Dataset.from_tensor_slices({"a": range(4)}).window(2)`
    produces `{{"a": {0, 1}}, {"a": {2, 3}}}`

  Args:
    input_dataset: A `Tensor` of type `variant`.
    size: A `Tensor` of type `int64`.
      An integer scalar, representing the number of elements
      of the input dataset to combine into a window. Must be positive.
    shift: A `Tensor` of type `int64`.
      An integer scalar, representing the number of input elements
      by which the window moves in each iteration.  Defaults to `size`.
      Must be positive.
    stride: A `Tensor` of type `int64`.
      An integer scalar, representing the stride of the input elements
      in the sliding window. Must be positive. The default value of 1 means
      "retain every input element".
    drop_remainder: A `Tensor` of type `bool`.
      A Boolean scalar, representing whether the last window should be
      dropped if its size is smaller than `window_size`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

WindowDataset: Incomplete

def window_dataset_eager_fallback(input_dataset, size, shift, stride, drop_remainder, output_types, output_shapes, metadata, name, ctx): ...
def window_op(inputs, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    inputs: A list of `Tensor` objects.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

WindowOp: Incomplete

def window_op_eager_fallback(inputs, output_types, output_shapes, name, ctx): ...
def wrap_dataset_variant(input_handle, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_handle: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

WrapDatasetVariant: Incomplete

def wrap_dataset_variant_eager_fallback(input_handle, name, ctx): ...
def zip_dataset(input_datasets, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that zips together `input_datasets`.

  The elements of the resulting dataset are created by zipping corresponding
  elements from each of the input datasets.

  The size of the resulting dataset will match the size of the smallest input
  dataset, and no error will be raised if input datasets have different sizes.

  Args:
    input_datasets: A list of at least 1 `Tensor` objects with type `variant`.
      List of `N` variant Tensors representing datasets to be zipped together.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ZipDataset: Incomplete

def zip_dataset_eager_fallback(input_datasets, output_types, output_shapes, metadata, name, ctx): ...
