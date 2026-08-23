from _typeshed import Incomplete
from torch.utils.data.datapipes.datapipe import IterDataPipe, MapDataPipe
from typing import Iterator, List, TypeVar

__all__ = ['ShufflerIterDataPipe']

T_co = TypeVar('T_co', covariant=True)

class ShufflerIterDataPipe(IterDataPipe[T_co]):
    """
    Shuffle the input MapDataPipe via its indices (functional name: ``shuffle``).

    When it is used with :class:`~torch.utils.data.DataLoader`, the methods to
    set up random seed are different based on :attr:`num_workers`.

    For single-process mode (:attr:`num_workers == 0`), the random seed is set before
    the :class:`~torch.utils.data.DataLoader` in the main process. For multi-process
    mode (:attr:`num_worker > 0`), ``worker_init_fn`` is used to set up a random seed
    for each worker process.

    Args:
        datapipe: MapDataPipe being shuffled
        indices: a list of indices of the MapDataPipe. If not provided, we assume it uses 0-based indexing

    Example:
        >>> # xdoctest: +SKIP
        >>> from torchdata.datapipes.map import SequenceWrapper
        >>> dp = SequenceWrapper(range(10))
        >>> shuffle_dp = dp.shuffle().set_seed(0)
        >>> list(shuffle_dp)
        [7, 8, 1, 5, 3, 4, 2, 0, 9, 6]
        >>> list(shuffle_dp)
        [6, 1, 9, 5, 2, 4, 7, 3, 8, 0]
        >>> # Reset seed for Shuffler
        >>> shuffle_dp = shuffle_dp.set_seed(0)
        >>> list(shuffle_dp)
        [7, 8, 1, 5, 3, 4, 2, 0, 9, 6]

    Note:
        Even thought this ``shuffle`` operation takes a ``MapDataPipe`` as the input, it would return an
        ``IterDataPipe`` rather than a ``MapDataPipe``, because ``MapDataPipe`` should be non-sensitive to
        the order of data order for the sake of random reads, but ``IterDataPipe`` depends on the order
        of data during data-processing.
    """
    datapipe: MapDataPipe[T_co]
    indices: Incomplete
    def __init__(self, datapipe: MapDataPipe[T_co], *, indices: List | None = None) -> None: ...
    def set_shuffle(self, shuffle: bool = True): ...
    def set_seed(self, seed: int): ...
    def __iter__(self) -> Iterator[T_co]: ...
    def reset(self) -> None: ...
    def __len__(self) -> int: ...
