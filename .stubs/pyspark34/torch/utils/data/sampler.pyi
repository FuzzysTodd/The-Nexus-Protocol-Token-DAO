from _typeshed import Incomplete
from torch import Tensor
from typing import Generic, Iterable, Iterator, List, Sequence, Sized, TypeVar

__all__ = ['BatchSampler', 'RandomSampler', 'Sampler', 'SequentialSampler', 'SubsetRandomSampler', 'WeightedRandomSampler']

T_co = TypeVar('T_co', covariant=True)

class Sampler(Generic[T_co]):
    """Base class for all Samplers.

    Every Sampler subclass has to provide an :meth:`__iter__` method, providing a
    way to iterate over indices of dataset elements, and a :meth:`__len__` method
    that returns the length of the returned iterators.

    .. note:: The :meth:`__len__` method isn't strictly required by
              :class:`~torch.utils.data.DataLoader`, but is expected in any
              calculation involving the length of a :class:`~torch.utils.data.DataLoader`.
    """
    def __init__(self, data_source: Sized | None) -> None: ...
    def __iter__(self) -> Iterator[T_co]: ...

class SequentialSampler(Sampler[int]):
    """Samples elements sequentially, always in the same order.

    Args:
        data_source (Dataset): dataset to sample from
    """
    data_source: Sized
    def __init__(self, data_source: Sized) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

class RandomSampler(Sampler[int]):
    """Samples elements randomly. If without replacement, then sample from a shuffled dataset.
    If with replacement, then user can specify :attr:`num_samples` to draw.

    Args:
        data_source (Dataset): dataset to sample from
        replacement (bool): samples are drawn on-demand with replacement if ``True``, default=``False``
        num_samples (int): number of samples to draw, default=`len(dataset)`.
        generator (Generator): Generator used in sampling.
    """
    data_source: Sized
    replacement: bool
    generator: Incomplete
    def __init__(self, data_source: Sized, replacement: bool = False, num_samples: int | None = None, generator: Incomplete | None = None) -> None: ...
    @property
    def num_samples(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

class SubsetRandomSampler(Sampler[int]):
    """Samples elements randomly from a given list of indices, without replacement.

    Args:
        indices (sequence): a sequence of indices
        generator (Generator): Generator used in sampling.
    """
    indices: Sequence[int]
    generator: Incomplete
    def __init__(self, indices: Sequence[int], generator: Incomplete | None = None) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

class WeightedRandomSampler(Sampler[int]):
    '''Samples elements from ``[0,..,len(weights)-1]`` with given probabilities (weights).

    Args:
        weights (sequence)   : a sequence of weights, not necessary summing up to one
        num_samples (int): number of samples to draw
        replacement (bool): if ``True``, samples are drawn with replacement.
            If not, they are drawn without replacement, which means that when a
            sample index is drawn for a row, it cannot be drawn again for that row.
        generator (Generator): Generator used in sampling.

    Example:
        >>> # xdoctest: +IGNORE_WANT("non-deterministic")
        >>> list(WeightedRandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], 5, replacement=True))
        [4, 4, 1, 4, 5]
        >>> list(WeightedRandomSampler([0.9, 0.4, 0.05, 0.2, 0.3, 0.1], 5, replacement=False))
        [0, 1, 4, 3, 2]
    '''
    weights: Tensor
    num_samples: int
    replacement: bool
    generator: Incomplete
    def __init__(self, weights: Sequence[float], num_samples: int, replacement: bool = True, generator: Incomplete | None = None) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

class BatchSampler(Sampler[List[int]]):
    """Wraps another sampler to yield a mini-batch of indices.

    Args:
        sampler (Sampler or Iterable): Base sampler. Can be any iterable object
        batch_size (int): Size of mini-batch.
        drop_last (bool): If ``True``, the sampler will drop the last batch if
            its size would be less than ``batch_size``

    Example:
        >>> list(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=False))
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
        >>> list(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=True))
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    """
    sampler: Incomplete
    batch_size: Incomplete
    drop_last: Incomplete
    def __init__(self, sampler: Sampler[int] | Iterable[int], batch_size: int, drop_last: bool) -> None: ...
    def __iter__(self) -> Iterator[List[int]]: ...
    def __len__(self) -> int: ...
