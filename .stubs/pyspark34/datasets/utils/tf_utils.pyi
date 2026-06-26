from .. import config as config
from _typeshed import Incomplete

def minimal_tf_collate_fn(features): ...
def minimal_tf_collate_fn_with_renaming(features): ...
def is_numeric_pa_type(pa_type): ...
def is_numeric_feature(feature): ...
def np_get_batch(indices, dataset, cols_to_retain, collate_fn, collate_fn_args, columns_to_np_types, return_dict: bool = False): ...
def dataset_to_tf(dataset, cols_to_retain, collate_fn, collate_fn_args, columns_to_np_types, output_signature, shuffle, batch_size, drop_remainder):
    """Create a tf.data.Dataset from the underlying Dataset. This is a single-process method - the multiprocess
    equivalent is multiprocess_dataset_to_tf.

    Args:
        dataset (`Dataset`): Dataset to wrap with tf.data.Dataset.
        cols_to_retain (`List[str]`): Dataset column(s) to load in the
            tf.data.Dataset. It is acceptable to include column names that are created by the `collate_fn` and
            that do not exist in the original dataset.
        collate_fn(`Callable`): A function or callable object (such as a `DataCollator`) that will collate
            lists of samples into a batch.
        collate_fn_args (`Dict`): A  `dict` of keyword arguments to be passed to the
            `collate_fn`. Can be empty.
        columns_to_np_types (`Dict[str, np.dtype]`): A `dict` mapping column names to numpy dtypes.
        output_signature (`Dict[str, tf.TensorSpec]`): A `dict` mapping column names to
            `tf.TensorSpec` objects.
        shuffle(`bool`): Shuffle the dataset order when loading. Recommended True for training, False for
            validation/evaluation.
        batch_size (`int`, default `None`): Size of batches to load from the dataset. Defaults to `None`, which implies that
            the dataset won't be batched, but the returned dataset can be batched later with `tf_dataset.batch(batch_size)`.
        drop_remainder(`bool`, default `None`): Drop the last incomplete batch when loading. If not provided,
            defaults to the same setting as shuffle.

    Returns:
        `tf.data.Dataset`
    """

class SharedMemoryContext:
    created_shms: Incomplete
    opened_shms: Incomplete
    def __init__(self) -> None: ...
    def get_shm(self, name, size, create): ...
    def get_array(self, name, shape, dtype, create): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class NumpyMultiprocessingGenerator:
    dataset: Incomplete
    cols_to_retain: Incomplete
    collate_fn: Incomplete
    collate_fn_args: Incomplete
    string_columns: Incomplete
    columns_to_np_types: Incomplete
    output_signature: Incomplete
    shuffle: Incomplete
    batch_size: Incomplete
    drop_remainder: Incomplete
    num_workers: Incomplete
    columns_to_ranks: Incomplete
    def __init__(self, dataset, cols_to_retain, collate_fn, collate_fn_args, columns_to_np_types, output_signature, shuffle, batch_size, drop_remainder, num_workers) -> None: ...
    def __iter__(self): ...
    def __call__(self): ...
    @staticmethod
    def worker_loop(dataset, cols_to_retain, collate_fn, collate_fn_args, columns_to_np_types, columns_to_ranks, string_columns, indices, extra_batch, worker_name, array_ready_event, array_loaded_event) -> None: ...
    @staticmethod
    def distribute_batches(dataset, batch_size, drop_remainder, num_workers, shuffle): ...

def multiprocess_dataset_to_tf(dataset, cols_to_retain, collate_fn, collate_fn_args, columns_to_np_types, output_signature, shuffle, batch_size, drop_remainder, num_workers):
    """Create a tf.data.Dataset from the underlying Dataset. This is a multi-process method - the single-process
    equivalent is dataset_to_tf.

    Args:
        dataset (`Dataset`): Dataset to wrap with tf.data.Dataset.
        cols_to_retain (`List[str]`): Dataset column(s) to load in the
            tf.data.Dataset. It is acceptable to include column names that are created by the `collate_fn` and
            that do not exist in the original dataset.
        collate_fn(`Callable`): A function or callable object (such as a `DataCollator`) that will collate
            lists of samples into a batch.
        collate_fn_args (`Dict`): A  `dict` of keyword arguments to be passed to the
            `collate_fn`. Can be empty.
        columns_to_np_types (`Dict[str, np.dtype]`): A `dict` mapping column names to numpy dtypes.
        output_signature (`Dict[str, tf.TensorSpec]`): A `dict` mapping column names to
            `tf.TensorSpec` objects.
        shuffle(`bool`): Shuffle the dataset order when loading. Recommended True for training, False for
            validation/evaluation.
        batch_size (`int`, default `None`): Size of batches to load from the dataset. Defaults to `None`, which implies that
            the dataset won't be batched, but the returned dataset can be batched later with `tf_dataset.batch(batch_size)`.
        drop_remainder(`bool`, default `None`): Drop the last incomplete batch when loading. If not provided,
            defaults to the same setting as shuffle.
        num_workers (`int`): Number of workers to use for loading the dataset. Should be >= 1.

    Returns:
        `tf.data.Dataset`
    """
