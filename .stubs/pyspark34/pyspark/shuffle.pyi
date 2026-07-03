from _typeshed import Incomplete
from pyspark.serializers import AutoBatchedSerializer as AutoBatchedSerializer, BatchedSerializer as BatchedSerializer, CPickleSerializer as CPickleSerializer, CompressedSerializer as CompressedSerializer, FlattenedValuesSerializer as FlattenedValuesSerializer
from pyspark.util import fail_on_stopiteration as fail_on_stopiteration

process: Incomplete

def get_used_memory():
    """Return the used memory in MiB"""

MemoryBytesSpilled: int
DiskBytesSpilled: int

class Aggregator:
    """
    Aggregator has tree functions to merge values into combiner.

    createCombiner:  (value) -> combiner
    mergeValue:      (combine, value) -> combiner
    mergeCombiners:  (combiner, combiner) -> combiner
    """
    createCombiner: Incomplete
    mergeValue: Incomplete
    mergeCombiners: Incomplete
    def __init__(self, createCombiner, mergeValue, mergeCombiners) -> None: ...

class SimpleAggregator(Aggregator):
    """
    SimpleAggregator is useful for the cases that combiners have
    same type with values
    """
    def __init__(self, combiner) -> None: ...

class Merger:
    """
    Merge shuffled data together by aggregator
    """
    agg: Incomplete
    def __init__(self, aggregator) -> None: ...
    def mergeValues(self, iterator) -> None:
        """Combine the items by creator and combiner"""
    def mergeCombiners(self, iterator) -> None:
        """Merge the combined items by mergeCombiner"""
    def items(self) -> None:
        """Return the merged items ad iterator"""

class ExternalMerger(Merger):
    """
    External merger will dump the aggregated data into disks when
    memory usage goes above the limit, then merge them together.

    This class works as follows:

    - It repeatedly combine the items and save them in one dict in
      memory.

    - When the used memory goes above memory limit, it will split
      the combined data into partitions by hash code, dump them
      into disk, one file per partition.

    - Then it goes through the rest of the iterator, combine items
      into different dict by hash. Until the used memory goes over
      memory limit, it dump all the dicts into disks, one file per
      dict. Repeat this again until combine all the items.

    - Before return any items, it will load each partition and
      combine them separately. Yield them before loading next
      partition.

    - During loading a partition, if the memory goes over limit,
      it will partition the loaded data and dump them into disks
      and load them partition by partition again.

    `data` and `pdata` are used to hold the merged items in memory.
    At first, all the data are merged into `data`. Once the used
    memory goes over limit, the items in `data` are dumped into
    disks, `data` will be cleared, all rest of items will be merged
    into `pdata` and then dumped into disks. Before returning, all
    the items in `pdata` will be dumped into disks.

    Finally, if any items were spilled into disks, each partition
    will be merged into `data` and be yielded, then cleared.

    Examples
    --------
    >>> agg = SimpleAggregator(lambda x, y: x + y)
    >>> merger = ExternalMerger(agg, 10)
    >>> N = 10000
    >>> merger.mergeValues(zip(range(N), range(N)))
    >>> assert merger.spills > 0
    >>> sum(v for k,v in merger.items())
    49995000

    >>> merger = ExternalMerger(agg, 10)
    >>> merger.mergeCombiners(zip(range(N), range(N)))
    >>> assert merger.spills > 0
    >>> sum(v for k,v in merger.items())
    49995000
    """
    MAX_TOTAL_PARTITIONS: int
    memory_limit: Incomplete
    serializer: Incomplete
    localdirs: Incomplete
    partitions: Incomplete
    batch: Incomplete
    scale: Incomplete
    data: Incomplete
    pdata: Incomplete
    spills: int
    def __init__(self, aggregator, memory_limit: int = 512, serializer: Incomplete | None = None, localdirs: Incomplete | None = None, scale: int = 1, partitions: int = 59, batch: int = 1000) -> None: ...
    def mergeValues(self, iterator) -> None:
        """Combine the items by creator and combiner"""
    def mergeCombiners(self, iterator, limit: Incomplete | None = None) -> None:
        """Merge (K,V) pair by mergeCombiner"""
    def items(self):
        """Return all merged items as iterator"""

class ExternalSorter:
    """
    ExternalSorter will divide the elements into chunks, sort them in
    memory and dump them into disks, finally merge them back.

    The spilling will only happen when the used memory goes above
    the limit.

    Examples
    --------
    >>> sorter = ExternalSorter(1)  # 1M
    >>> import random
    >>> l = list(range(1024))
    >>> random.shuffle(l)
    >>> sorted(l) == list(sorter.sorted(l))
    True
    >>> sorted(l) == list(sorter.sorted(l, key=lambda x: -x, reverse=True))
    True
    """
    memory_limit: Incomplete
    local_dirs: Incomplete
    serializer: Incomplete
    def __init__(self, memory_limit, serializer: Incomplete | None = None) -> None: ...
    def sorted(self, iterator, key: Incomplete | None = None, reverse: bool = False):
        """
        Sort the elements in iterator, do external sort when the memory
        goes above the limit.
        """

class ExternalList:
    """
    ExternalList can have many items which cannot be hold in memory in
    the same time.

    Examples
    --------
    >>> l = ExternalList(list(range(100)))
    >>> len(l)
    100
    >>> l.append(10)
    >>> len(l)
    101
    >>> for i in range(20240):
    ...     l.append(i)
    >>> len(l)
    20341
    >>> import pickle
    >>> l2 = pickle.loads(pickle.dumps(l))
    >>> len(l2)
    20341
    >>> list(l2)[100]
    10
    """
    LIMIT: int
    values: Incomplete
    count: Incomplete
    def __init__(self, values) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def append(self, value) -> None: ...
    def __del__(self) -> None: ...

class ExternalListOfList(ExternalList):
    """
    An external list for list.

    Examples
    --------
    >>> l = ExternalListOfList([[i, i] for i in range(100)])
    >>> len(l)
    200
    >>> l.append(range(10))
    >>> len(l)
    210
    >>> len(list(l))
    210
    """
    count: Incomplete
    def __init__(self, values) -> None: ...
    def append(self, value) -> None: ...
    def __iter__(self): ...

class GroupByKey:
    """
    Group a sorted iterator as [(k1, it1), (k2, it2), ...]

    Examples
    --------
    >>> k = [i // 3 for i in range(6)]
    >>> v = [[i] for i in range(6)]
    >>> g = GroupByKey(zip(k, v))
    >>> [(k, list(it)) for k, it in g]
    [(0, [0, 1, 2]), (1, [3, 4, 5])]
    """
    iterator: Incomplete
    def __init__(self, iterator) -> None: ...
    def __iter__(self): ...

class ExternalGroupBy(ExternalMerger):
    """
    Group by the items by key. If any partition of them can not been
    hold in memory, it will do sort based group by.

    This class works as follows:

    - It repeatedly group the items by key and save them in one dict in
      memory.

    - When the used memory goes above memory limit, it will split
      the combined data into partitions by hash code, dump them
      into disk, one file per partition. If the number of keys
      in one partitions is smaller than 1000, it will sort them
      by key before dumping into disk.

    - Then it goes through the rest of the iterator, group items
      by key into different dict by hash. Until the used memory goes over
      memory limit, it dump all the dicts into disks, one file per
      dict. Repeat this again until combine all the items. It
      also will try to sort the items by key in each partition
      before dumping into disks.

    - It will yield the grouped items partitions by partitions.
      If the data in one partitions can be hold in memory, then it
      will load and combine them in memory and yield.

    - If the dataset in one partition cannot be hold in memory,
      it will sort them first. If all the files are already sorted,
      it merge them by heap.merge(), so it will do external sort
      for all the files.

    - After sorting, `GroupByKey` class will put all the continuous
      items with the same key as a group, yield the values as
      an iterator.
    """
    SORT_KEY_LIMIT: int
    def flattened_serializer(self): ...
