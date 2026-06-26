import numpy as np
import pyarrow as pa
from . import config as config
from .arrow_dataset import Dataset as Dataset, DatasetInfoMixin as DatasetInfoMixin
from .features import Features as Features
from .features.features import FeatureType as FeatureType, cast_to_python_objects as cast_to_python_objects
from .formatting import PythonFormatter as PythonFormatter, TensorFormatter as TensorFormatter, get_format_type_from_alias as get_format_type_from_alias, get_formatter as get_formatter
from .info import DatasetInfo as DatasetInfo
from .splits import NamedSplit as NamedSplit
from .table import cast_table_to_features as cast_table_to_features, read_schema_from_file as read_schema_from_file, table_cast as table_cast
from .utils.logging import get_logger as get_logger
from .utils.py_utils import Literal as Literal
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Callable, Dict, Iterator, List, Tuple

logger: Incomplete
Key = int | str

def identity_func(x): ...
def add_column_fn(example: Dict, idx: int, name: str, column: List[Dict]): ...

class _HasNextIterator(Iterator):
    """Iterator with an hasnext() function. Taken from https://stackoverflow.com/questions/1966591/has-next-in-python-iterators."""
    it: Incomplete
    def __init__(self, it) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def hasnext(self): ...

class _BaseExamplesIterable:
    """Base class for the examples iterable used by an IterableDataset"""
    iter_arrow: Incomplete
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[Tuple[Key, dict]]:
        """An examples iterable should yield tuples (example_key, example) of type (int/str, dict)"""
    def shuffle_data_sources(self, generator: np.random.Generator) -> _BaseExamplesIterable:
        """
        Either shuffle the shards/sources of the dataset, or propagate the shuffling to the underlying iterable.
        If the order of the shards must stay fixed (when using .skip or .take for example), then this method returns self.
        """
    def shard_data_sources(self, worker_id: int, num_workers: int) -> _BaseExamplesIterable:
        """Either keep only the requested shard, or propagate the request to the underlying iterable."""
    def split_shard_indices_by_worker(self, worker_id: int, num_workers: int) -> List[int]: ...
    @property
    def n_shards(self) -> int: ...

class ExamplesIterable(_BaseExamplesIterable):
    generate_examples_fn: Incomplete
    kwargs: Incomplete
    def __init__(self, generate_examples_fn: Callable[..., Tuple[Key, dict]], kwargs: dict) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> ExamplesIterable: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> ExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class ShuffledDataSourcesExamplesIterable(ExamplesIterable):
    generator: Incomplete
    def __init__(self, generate_examples_fn: Callable[..., Tuple[Key, dict]], kwargs: dict, generator: np.random.Generator) -> None: ...
    def __iter__(self):
        """Shuffle the kwargs order to shuffle shards"""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> ExamplesIterable:
        """Keep only the requested shard."""

class ArrowExamplesIterable(_BaseExamplesIterable):
    generate_tables_fn: Incomplete
    kwargs: Incomplete
    iter_arrow: Incomplete
    def __init__(self, generate_tables_fn: Callable[..., Tuple[Key, pa.Table]], kwargs: dict) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> ArrowExamplesIterable: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> ArrowExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class ShuffledDataSourcesArrowExamplesIterable(ArrowExamplesIterable):
    generator: Incomplete
    def __init__(self, generate_tables_fn: Callable[..., Tuple[Key, pa.Table]], kwargs: dict, generator: np.random.Generator) -> None: ...
    def __iter__(self):
        """Shuffle the kwargs order to shuffle shards"""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> ArrowExamplesIterable:
        """Keep only the requested shard."""

class SelectColumnsIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    column_names: Incomplete
    iter_arrow: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, column_names: List[str]) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> SelectColumnsIterable: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> SelectColumnsIterable: ...
    @property
    def n_shards(self) -> int: ...

class StepExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    step: Incomplete
    offset: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, step: int, offset: int) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> StepExamplesIterable: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> StepExamplesIterable: ...
    @property
    def n_shards(self) -> int: ...

class CyclingMultiSourcesExamplesIterable(_BaseExamplesIterable):
    ex_iterables: Incomplete
    stopping_strategy: Incomplete
    bool_strategy_func: Incomplete
    def __init__(self, ex_iterables: List[_BaseExamplesIterable], stopping_strategy: Literal['first_exhausted', 'all_exhausted'] = 'first_exhausted') -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> CyclingMultiSourcesExamplesIterable:
        """Shuffle each underlying examples iterable."""
    @property
    def n_shards(self) -> int: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> CyclingMultiSourcesExamplesIterable:
        """Either keep only the requested shard, or propagate the request to the underlying iterable."""

class VerticallyConcatenatedMultiSourcesExamplesIterable(_BaseExamplesIterable):
    """
    VerticallyConcatenatedMultiSourcesExamplesIterable simply chains the input iterables.
    It doesn't require the examples iterables to always yield the same columns.
    Instead, this is handled by the `IterableDataset` class or `TypedExamplesIterable`.

    For information, `IterableDataset` merges the features of all the datasets to concatenate into one.
    We use `IterableDataset._resolve_features` to obtain the features of all the datasets to concatenate.

    Then for each example, `IterableDataset` and `TypedExamplesIterable` automatically fill missing columns with None.
    This is done with `_apply_feature_types_on_example`.
    """
    ex_iterables: Incomplete
    iter_arrow: Incomplete
    def __init__(self, ex_iterables: List[_BaseExamplesIterable]) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> VerticallyConcatenatedMultiSourcesExamplesIterable:
        """Shuffle the list of examples iterable, as well as each underlying examples iterable."""
    @property
    def n_shards(self) -> int: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> VerticallyConcatenatedMultiSourcesExamplesIterable:
        """Either keep only the requested shard, or propagate the request to the underlying iterable."""

class HorizontallyConcatenatedMultiSourcesExamplesIterable(_BaseExamplesIterable):
    """
    HorizontallyConcatenatedMultiSourcesExamplesIterable merges examples together for the input list of iterables.
    It also checks that there are no duplicate columns (otherwise we don't know which one to keep).
    This check is done once when yielding the first example.

    However it doesn't fill missing columns with None.
    Instead, this is handled by the `IterableDataset` class or `TypedExamplesIterable`.

    For information, `IterableDataset` merges the features of all the datasets to concatenate into one.
    We use `IterableDataset._resolve_features` to obtain the features of all the datasets to concatenate.

    Then for each example, `IterableDataset` and `TypedExamplesIterable` automatically fill missing columns with None.
    This is done with `_apply_feature_types_on_example`.
    """
    ex_iterables: Incomplete
    def __init__(self, ex_iterables: List[_BaseExamplesIterable]) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> HorizontallyConcatenatedMultiSourcesExamplesIterable:
        """Doesn't shuffle the wrapped examples iterable since it would break the alignment between them."""
    @property
    def n_shards(self) -> int: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> HorizontallyConcatenatedMultiSourcesExamplesIterable:
        """Either keep only the requested shard, or propagate the request to the underlying iterable."""

class RandomlyCyclingMultiSourcesExamplesIterable(CyclingMultiSourcesExamplesIterable):
    generator: Incomplete
    probabilities: Incomplete
    def __init__(self, ex_iterables: List[_BaseExamplesIterable], generator: np.random.Generator, probabilities: List[float] | None = None, stopping_strategy: Literal['first_exhausted', 'all_exhausted'] = 'first_exhausted') -> None: ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> RandomlyCyclingMultiSourcesExamplesIterable:
        """Shuffle the data sources of each wrapped examples iterable."""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> RandomlyCyclingMultiSourcesExamplesIterable:
        """Either keep only the requested shard, or propagate the request to the underlying iterable."""

class MappedExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    function: Incomplete
    batched: Incomplete
    batch_size: Incomplete
    drop_last_batch: Incomplete
    remove_columns: Incomplete
    with_indices: Incomplete
    input_columns: Incomplete
    fn_kwargs: Incomplete
    formatting: Incomplete
    iter_arrow: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, function: Callable, with_indices: bool = False, input_columns: List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, drop_last_batch: bool = False, remove_columns: List[str] | None = None, fn_kwargs: dict | None = None, formatting: FormattingConfig | None = None, format_type: str = 'deprecated') -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> MappedExamplesIterable:
        """Shuffle the wrapped examples iterable."""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> MappedExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class FilteredExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    function: Incomplete
    batched: Incomplete
    batch_size: Incomplete
    with_indices: Incomplete
    input_columns: Incomplete
    fn_kwargs: Incomplete
    formatting: Incomplete
    iter_arrow: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, function: Callable, with_indices: bool = False, input_columns: List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, fn_kwargs: dict | None = None, formatting: FormattingConfig | None = None, format_type: str = 'deprecated') -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, seed: int | None) -> FilteredExamplesIterable:
        """Shuffle the wrapped examples iterable."""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> FilteredExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class BufferShuffledExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    buffer_size: Incomplete
    generator: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, buffer_size: int, generator: np.random.Generator) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> BufferShuffledExamplesIterable:
        """Shuffle the wrapped examples iterable as well as the shuffling buffer."""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> BufferShuffledExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class SkipExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    n: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, n: int) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> SkipExamplesIterable:
        """Doesn't shuffle the wrapped examples iterable since it would skip examples from other shards instead."""
    @property
    def n_shards(self) -> int: ...

class TakeExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    n: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, n: int) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> TakeExamplesIterable:
        """Doesn't shuffle the wrapped examples iterable since it would take examples from other shards instead."""
    @staticmethod
    def split_number(num, n): ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> TakeExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

class TypedExamplesIterable(_BaseExamplesIterable):
    ex_iterable: Incomplete
    features: Incomplete
    token_per_repo_id: Incomplete
    iter_arrow: Incomplete
    def __init__(self, ex_iterable: _BaseExamplesIterable, features: Features, token_per_repo_id: Dict[str, str | bool | None]) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> TypedExamplesIterable:
        """Shuffle the wrapped examples iterable."""
    def shard_data_sources(self, worker_id: int, num_workers: int) -> TypedExamplesIterable:
        """Keep only the requested shard."""
    @property
    def n_shards(self) -> int: ...

@dataclass
class FormattingConfig:
    format_type: str | None
    def __post_init__(self) -> None: ...
    def __init__(self, format_type) -> None: ...

@dataclass
class ShufflingConfig:
    generator: np.random.Generator
    def __init__(self, generator, _original_seed) -> None: ...

@dataclass
class DistributedConfig:
    rank: int
    world_size: int
    def __init__(self, rank, world_size) -> None: ...

class IterableDataset(DatasetInfoMixin):
    """A Dataset backed by an iterable."""
    def __init__(self, ex_iterable: _BaseExamplesIterable, info: DatasetInfo | None = None, split: NamedSplit | None = None, formatting: FormattingConfig | None = None, shuffling: ShufflingConfig | None = None, distributed: DistributedConfig | None = None, token_per_repo_id: Dict[str, str | bool | None] | None = None, format_type: str = 'deprecated') -> None: ...
    @property
    def n_shards(self) -> int: ...
    def __iter__(self): ...
    def iter(self, batch_size: int, drop_last_batch: bool = False):
        """Iterate through the batches of size `batch_size`.

        Args:
            batch_size (:obj:`int`): size of each batch to yield.
            drop_last_batch (:obj:`bool`, default `False`): Whether a last batch smaller than the batch_size should be
                dropped
        """
    @staticmethod
    def from_generator(generator: Callable, features: Features | None = None, gen_kwargs: dict | None = None) -> IterableDataset:
        '''Create an Iterable Dataset from a generator.

        Args:
            generator (`Callable`):
                A generator function that `yields` examples.
            features (`Features`, *optional*):
                Dataset features.
            gen_kwargs(`dict`, *optional*):
                Keyword arguments to be passed to the `generator` callable.
                You can define a sharded iterable dataset by passing the list of shards in `gen_kwargs`.
                This can be used to improve shuffling and when iterating over the dataset with multiple workers.

        Returns:
            `IterableDataset`

        Example:

        ```py
        >>> def gen():
        ...     yield {"text": "Good", "label": 0}
        ...     yield {"text": "Bad", "label": 1}
        ...
        >>> ds = IterableDataset.from_generator(gen)
        ```

        ```py
        >>> def gen(shards):
        ...     for shard in shards:
        ...         with open(shard) as f:
        ...             for line in f:
        ...                 yield {"line": line}
        ...
        >>> shards = [f"data{i}.txt" for i in range(32)]
        >>> ds = IterableDataset.from_generator(gen, gen_kwargs={"shards": shards})
        >>> ds = ds.shuffle(seed=42, buffer_size=10_000)  # shuffles the shards order + uses a shuffle buffer
        >>> from torch.utils.data import DataLoader
        >>> dataloader = DataLoader(ds.with_format("torch"), num_workers=4)  # give each worker a subset of 32/4=8 shards
        ```
        '''
    @staticmethod
    def from_spark(df: pyspark.sql.DataFrame, split: NamedSplit | None = None, features: Features | None = None, **kwargs) -> IterableDataset:
        '''Create an IterableDataset from Spark DataFrame. The dataset is streamed to the driver in batches.

        Args:
            df (`pyspark.sql.DataFrame`):
                The DataFrame containing the desired data.
            split (`NamedSplit`, *optional*):
                Split name to be assigned to the dataset.
            features (`Features`, *optional*):
                Dataset features.

        Returns:
            [`IterableDataset`]

        Example:

        ```py
        >>> df = spark.createDataFrame(
        >>>     data=[[1, "Elia"], [2, "Teo"], [3, "Fang"]],
        >>>     columns=["id", "name"],
        >>> )
        >>> ds = IterableDataset.from_spark(df)
        ```
        '''
    @staticmethod
    def from_file(filename: str) -> IterableDataset:
        """Instantiate a IterableDataset from Arrow table at filename.

        Args:
            filename (`str`):
                File name of the dataset.

        Returns:
            [`IterableDataset`]
        """
    def with_format(self, type: str | None = None) -> IterableDataset:
        '''
        Return a dataset with the specified format.
        Supported formats: "arrow", or None for regular python objects.
        The other formats are currently not implemented.

        Args:

            type (`str`, optional, default None): if set to "torch", the returned dataset
                will be a subclass of torch.utils.data.IterableDataset to be used in a DataLoader
        '''
    def map(self, function: Callable | None = None, with_indices: bool = False, input_columns: str | List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, drop_last_batch: bool = False, remove_columns: str | List[str] | None = None, features: Features | None = None, fn_kwargs: dict | None = None) -> IterableDataset:
        '''
        Apply a function to all the examples in the iterable dataset (individually or in batches) and update them.
        If your function returns a column that already exists, then it overwrites it.
        The function is applied on-the-fly on the examples when iterating over the dataset.

        You can specify whether the function should be batched or not with the `batched` parameter:

        - If batched is `False`, then the function takes 1 example in and should return 1 example.
          An example is a dictionary, e.g. `{"text": "Hello there !"}`.
        - If batched is `True` and `batch_size` is 1, then the function takes a batch of 1 example as input and can return a batch with 1 or more examples.
          A batch is a dictionary, e.g. a batch of 1 example is {"text": ["Hello there !"]}.
        - If batched is `True` and `batch_size` is `n` > 1, then the function takes a batch of `n` examples as input and can return a batch with `n` examples, or with an arbitrary number of examples.
          Note that the last batch may have less than `n` examples.
          A batch is a dictionary, e.g. a batch of `n` examples is `{"text": ["Hello there !"] * n}`.

        Args:
            function (`Callable`, *optional*, defaults to `None`):
                Function applied on-the-fly on the examples when you iterate on the dataset.
                It must have one of the following signatures:

                - `function(example: Dict[str, Any]) -> Dict[str, Any]` if `batched=False` and `with_indices=False`
                - `function(example: Dict[str, Any], idx: int) -> Dict[str, Any]` if `batched=False` and `with_indices=True`
                - `function(batch: Dict[str, List]) -> Dict[str, List]` if `batched=True` and `with_indices=False`
                - `function(batch: Dict[str, List], indices: List[int]) -> Dict[str, List]` if `batched=True` and `with_indices=True`

                For advanced usage, the function can also return a `pyarrow.Table`.
                Moreover if your function returns nothing (`None`), then `map` will run your function and return the dataset unchanged.
                If no function is provided, default to identity function: `lambda x: x`.
            with_indices (`bool`, defaults to `False`):
                Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx[, rank]): ...`.
            input_columns (`Optional[Union[str, List[str]]]`, defaults to `None`):
                The columns to be passed into `function`
                as positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
            batched (`bool`, defaults to `False`):
                Provide batch of examples to `function`.
            batch_size (`int`, *optional*, defaults to `1000`):
                Number of examples per batch provided to `function` if `batched=True`.
                `batch_size <= 0` or `batch_size == None` then provide the full dataset as a single batch to `function`.
            drop_last_batch (`bool`, defaults to `False`):
                Whether a last batch smaller than the batch_size should be
                dropped instead of being processed by the function.
            remove_columns (`[List[str]]`, *optional*, defaults to `None`):
                Remove a selection of columns while doing the mapping.
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
                columns with names in `remove_columns`, these columns will be kept.
            features (`[Features]`, *optional*, defaults to `None`):
                Feature types of the resulting dataset.
            fn_kwargs (`Dict`, *optional*, default `None`):
                Keyword arguments to be passed to `function`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> def add_prefix(example):
        ...     example["text"] = "Review: " + example["text"]
        ...     return example
        >>> ds = ds.map(add_prefix)
        >>> list(ds.take(3))
        [{\'label\': 1,
         \'text\': \'Review: the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'},
         {\'label\': 1,
         \'text\': \'Review: the gorgeously elaborate continuation of " the lord of the rings " trilogy is so huge that a column of words cannot adequately describe co-writer/director peter jackson\'s expanded vision of j . r . r . tolkien\'s middle-earth .\'},
         {\'label\': 1, \'text\': \'Review: effective but too-tepid biopic\'}]
        ```
        '''
    def filter(self, function: Callable | None = None, with_indices: bool = False, input_columns: str | List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, fn_kwargs: dict | None = None) -> IterableDataset:
        '''Apply a filter function to all the elements so that the dataset only includes examples according to the filter function.
        The filtering is done on-the-fly when iterating over the dataset.

        Args:
            function (`Callable`):
                Callable with one of the following signatures:

                - `function(example: Dict[str, Any]) -> bool` if `with_indices=False, batched=False`
                - `function(example: Dict[str, Any], indices: int) -> bool` if `with_indices=True, batched=False`
                - `function(example: Dict[str, List]) -> List[bool]` if `with_indices=False, batched=True`
                - `function(example: Dict[str, List], indices: List[int]) -> List[bool]` if `with_indices=True, batched=True`

                If no function is provided, defaults to an always True function: `lambda x: True`.
            with_indices (`bool`, defaults to `False`):
                Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
            input_columns (`str` or `List[str]`, *optional*):
                The columns to be passed into `function` as
                positional arguments. If `None`, a dict mapping to all formatted columns is passed as one argument.
            batched (`bool`, defaults to `False`):
                Provide batch of examples to `function`.
            batch_size (`int`, *optional*, default `1000`):
                Number of examples per batch provided to `function` if `batched=True`.
            fn_kwargs (`Dict`, *optional*, default `None`):
                Keyword arguments to be passed to `function`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> ds = ds.filter(lambda x: x["label"] == 0)
        >>> list(ds.take(3))
        [{\'label\': 0, \'movie_review\': \'simplistic , silly and tedious .\'},
         {\'label\': 0,
         \'movie_review\': "it\'s so laddish and juvenile , only teenage boys could possibly find it funny ."},
         {\'label\': 0,
         \'movie_review\': \'exploitative and largely devoid of the depth or sophistication that would make watching such a graphic treatment of the crimes bearable .\'}]
        ```
        '''
    def shuffle(self, seed: Incomplete | None = None, generator: np.random.Generator | None = None, buffer_size: int = 1000) -> IterableDataset:
        '''
        Randomly shuffles the elements of this dataset.

        This dataset fills a buffer with `buffer_size` elements, then randomly samples elements from this buffer,
        replacing the selected elements with new elements. For perfect shuffling, a buffer size greater than or
        equal to the full size of the dataset is required.

        For instance, if your dataset contains 10,000 elements but `buffer_size` is set to 1000, then `shuffle` will
        initially select a random element from only the first 1000 elements in the buffer. Once an element is
        selected, its space in the buffer is replaced by the next (i.e. 1,001-st) element,
        maintaining the 1000 element buffer.

        If the dataset is made of several shards, it also does shuffle the order of the shards.
        However if the order has been fixed by using [`~datasets.IterableDataset.skip`] or [`~datasets.IterableDataset.take`]
        then the order of the shards is kept unchanged.

        Args:
            seed (`int`, *optional*, defaults to `None`):
                Random seed that will be used to shuffle the dataset.
                It is used to sample from the shuffle buffe and also to shuffle the data shards.
            generator (`numpy.random.Generator`, *optional*):
                Numpy random Generator to use to compute the permutation of the dataset rows.
                If `generator=None` (default), uses `np.random.default_rng` (the default BitGenerator (PCG64) of NumPy).
            buffer_size (`int`, defaults to `1000`):
                Size of the buffer.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> list(ds.take(3))
        [{\'label\': 1,
         \'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'},
         {\'label\': 1,
         \'text\': \'the gorgeously elaborate continuation of " the lord of the rings " trilogy is so huge that a column of words cannot adequately describe co-writer/director peter jackson\'s expanded vision of j . r . r . tolkien\'s middle-earth .\'},
         {\'label\': 1, \'text\': \'effective but too-tepid biopic\'}]
        >>> shuffled_ds = ds.shuffle(seed=42)
        >>> list(shuffled_ds.take(3))
        [{\'label\': 1,
         \'text\': "a sports movie with action that\'s exciting on the field and a story you care about off it ."},
         {\'label\': 1,
         \'text\': \'at its best , the good girl is a refreshingly adult take on adultery . . .\'},
         {\'label\': 1,
         \'text\': "sam jones became a very lucky filmmaker the day wilco got dropped from their record label , proving that one man\'s ruin may be another\'s fortune ."}]
        ```
        '''
    def set_epoch(self, epoch: int): ...
    def skip(self, n) -> IterableDataset:
        '''
        Create a new [`IterableDataset`] that skips the first `n` elements.

        Args:
            n (`int`):
                Number of elements to skip.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> list(ds.take(3))
        [{\'label\': 1,
         \'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'},
         {\'label\': 1,
         \'text\': \'the gorgeously elaborate continuation of " the lord of the rings " trilogy is so huge that a column of words cannot adequately describe co-writer/director peter jackson\'s expanded vision of j . r . r . tolkien\'s middle-earth .\'},
         {\'label\': 1, \'text\': \'effective but too-tepid biopic\'}]
        >>> ds = ds.skip(1)
        >>> list(ds.take(3))
        [{\'label\': 1,
         \'text\': \'the gorgeously elaborate continuation of " the lord of the rings " trilogy is so huge that a column of words cannot adequately describe co-writer/director peter jackson\'s expanded vision of j . r . r . tolkien\'s middle-earth .\'},
         {\'label\': 1, \'text\': \'effective but too-tepid biopic\'},
         {\'label\': 1,
         \'text\': \'if you sometimes like to go to the movies to have fun , wasabi is a good place to start .\'}]
        ```
        '''
    def take(self, n) -> IterableDataset:
        '''
        Create a new [`IterableDataset`] with only the first `n` elements.

        Args:
            n (`int`):
                Number of elements to take.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> small_ds = ds.take(2)
        >>> list(small_ds)
        [{\'label\': 1,
         \'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'},
         {\'label\': 1,
         \'text\': \'the gorgeously elaborate continuation of " the lord of the rings " trilogy is so huge that a column of words cannot adequately describe co-writer/director peter jackson\'s expanded vision of j . r . r . tolkien\'s middle-earth .\'}]
        ```
        '''
    @property
    def column_names(self) -> List[str] | None:
        '''Names of the columns in the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation", streaming=True)
        >>> ds.column_names
        [\'text\', \'label\']
        ```
        '''
    def add_column(self, name: str, column: list | np.array) -> IterableDataset:
        """Add column to Dataset.

        Args:
            name (str): Column name.
            column (list or np.array): Column data to be added.

        Returns:
            `IterableDataset`
        """
    def rename_column(self, original_column_name: str, new_column_name: str) -> IterableDataset:
        '''
        Rename a column in the dataset, and move the features associated to the original column under the new column
        name.

        Args:
            original_column_name (`str`):
                Name of the column to rename.
            new_column_name (`str`):
                New name for the column.

        Returns:
            `IterableDataset`: A copy of the dataset with a renamed column.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> next(iter(ds))
        {\'label\': 1,
         \'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'}
        >>> ds = ds.rename_column("text", "movie_review")
        >>> next(iter(ds))
        {\'label\': 1,
         \'movie_review\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'}
        ```
        '''
    def rename_columns(self, column_mapping: Dict[str, str]) -> IterableDataset:
        """
        Rename several columns in the dataset, and move the features associated to the original columns under
        the new column names.

        Args:
            column_mapping (`Dict[str, str]`): A mapping of columns to rename to their new names

        Returns:
            `IterableDataset`: A copy of the dataset with renamed columns
        """
    def remove_columns(self, column_names: str | List[str]) -> IterableDataset:
        '''
        Remove one or several column(s) in the dataset and the features associated to them.
        The removal is done on-the-fly on the examples when iterating over the dataset.


        Args:
            column_names (`Union[str, List[str]]`):
                Name of the column(s) to remove.

        Returns:
            `IterableDataset`: A copy of the dataset object without the columns to remove.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> next(iter(ds))
        {\'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\', \'label\': 1}
        >>> ds = ds.remove_columns("label")
        >>> next(iter(ds))
        {\'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'}
        ```
        '''
    def select_columns(self, column_names: str | List[str]) -> IterableDataset:
        '''Select one or several column(s) in the dataset and the features
        associated to them. The selection is done on-the-fly on the examples
        when iterating over the dataset.


        Args:
            column_names (`Union[str, List[str]]`):
                Name of the column(s) to select.

        Returns:
            `IterableDataset`: A copy of the dataset object with selected columns.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> next(iter(ds))
        {\'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\', \'label\': 1}
        >>> ds = ds.select_columns("text")
        >>> next(iter(ds))
        {\'text\': \'the rock is destined to be the 21st century\'s new " conan " and that he\'s going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal .\'}
        ```
        '''
    def cast_column(self, column: str, feature: FeatureType) -> IterableDataset:
        '''Cast column to feature for decoding.

        Args:
            column (`str`):
                Column name.
            feature (`Feature`):
                Target feature.

        Returns:
            `IterableDataset`

        Example:

        ```py
        >>> from datasets import load_dataset, Audio
        >>> ds = load_dataset("PolyAI/minds14", name="en-US", split="train", streaming=True)
        >>> ds.features
        {\'audio\': Audio(sampling_rate=8000, mono=True, decode=True, id=None),
         \'english_transcription\': Value(dtype=\'string\', id=None),
         \'intent_class\': ClassLabel(num_classes=14, names=[\'abroad\', \'address\', \'app_error\', \'atm_limit\', \'balance\', \'business_loan\',  \'card_issues\', \'cash_deposit\', \'direct_debit\', \'freeze\', \'high_value_payment\', \'joint_account\', \'latest_transactions\', \'pay_bill\'], id=None),
         \'lang_id\': ClassLabel(num_classes=14, names=[\'cs-CZ\', \'de-DE\', \'en-AU\', \'en-GB\', \'en-US\', \'es-ES\', \'fr-FR\', \'it-IT\', \'ko-KR\',  \'nl-NL\', \'pl-PL\', \'pt-PT\', \'ru-RU\', \'zh-CN\'], id=None),
         \'path\': Value(dtype=\'string\', id=None),
         \'transcription\': Value(dtype=\'string\', id=None)}
        >>> ds = ds.cast_column("audio", Audio(sampling_rate=16000))
        >>> ds.features
        {\'audio\': Audio(sampling_rate=16000, mono=True, decode=True, id=None),
         \'english_transcription\': Value(dtype=\'string\', id=None),
         \'intent_class\': ClassLabel(num_classes=14, names=[\'abroad\', \'address\', \'app_error\', \'atm_limit\', \'balance\', \'business_loan\',  \'card_issues\', \'cash_deposit\', \'direct_debit\', \'freeze\', \'high_value_payment\', \'joint_account\', \'latest_transactions\', \'pay_bill\'], id=None),
         \'lang_id\': ClassLabel(num_classes=14, names=[\'cs-CZ\', \'de-DE\', \'en-AU\', \'en-GB\', \'en-US\', \'es-ES\', \'fr-FR\', \'it-IT\', \'ko-KR\',  \'nl-NL\', \'pl-PL\', \'pt-PT\', \'ru-RU\', \'zh-CN\'], id=None),
         \'path\': Value(dtype=\'string\', id=None),
         \'transcription\': Value(dtype=\'string\', id=None)}
        ```
        '''
    def cast(self, features: Features) -> IterableDataset:
        '''
        Cast the dataset to a new set of features.

        Args:
            features ([`Features`]):
                New features to cast the dataset to.
                The name of the fields in the features must match the current column names.
                The type of the data must also be convertible from one type to the other.
                For non-trivial conversion, e.g. `string` <-> `ClassLabel` you should use [`~Dataset.map`] to update the Dataset.

        Returns:
            `IterableDataset`: A copy of the dataset with casted features.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train", streaming=True)
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None),
         \'text\': Value(dtype=\'string\', id=None)}
        >>> new_features = ds.features.copy()
        >>> new_features["label"] = ClassLabel(names=["bad", "good"])
        >>> new_features["text"] = Value("large_string")
        >>> ds = ds.cast(new_features)
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'bad\', \'good\'], id=None),
         \'text\': Value(dtype=\'large_string\', id=None)}
        ```
        '''
