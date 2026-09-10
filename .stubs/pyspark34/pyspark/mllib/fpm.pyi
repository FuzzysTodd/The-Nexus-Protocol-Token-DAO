from pyspark import SparkContext
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.util import JavaLoader, JavaSaveable
from pyspark.rdd import RDD
from typing import Any, Generic, List, NamedTuple, TypeVar

__all__ = ['FPGrowth', 'FPGrowthModel', 'PrefixSpan', 'PrefixSpanModel']

T = TypeVar('T')

class FPGrowthModel(JavaModelWrapper, JavaSaveable, JavaLoader['FPGrowthModel']):
    '''
    A FP-Growth model for mining frequent itemsets
    using the Parallel FP-Growth algorithm.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> data = [["a", "b", "c"], ["a", "b", "d", "e"], ["a", "c", "e"], ["a", "c", "f"]]
    >>> rdd = sc.parallelize(data, 2)
    >>> model = FPGrowth.train(rdd, 0.6, 2)
    >>> sorted(model.freqItemsets().collect())
    [FreqItemset(items=[\'a\'], freq=4), FreqItemset(items=[\'c\'], freq=3), ...
    >>> model_path = temp_path + "/fpm"
    >>> model.save(sc, model_path)
    >>> sameModel = FPGrowthModel.load(sc, model_path)
    >>> sorted(model.freqItemsets().collect()) == sorted(sameModel.freqItemsets().collect())
    True
    '''
    def freqItemsets(self) -> RDD['FPGrowth.FreqItemset']:
        """
        Returns the frequent itemsets of this model.
        """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> FPGrowthModel:
        """
        Load a model from the given path.
        """

class FPGrowth:
    """
    A Parallel FP-growth algorithm to mine frequent itemsets.

    .. versionadded:: 1.4.0
    """
    @classmethod
    def train(cls, data: RDD[List[T]], minSupport: float = 0.3, numPartitions: int = -1) -> FPGrowthModel:
        """
        Computes an FP-Growth model that contains frequent itemsets.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The input data set, each element contains a transaction.
        minSupport : float, optional
            The minimal support level.
            (default: 0.3)
        numPartitions : int, optional
            The number of partitions used by parallel FP-growth. A value
            of -1 will use the same number as input data.
            (default: -1)
        """
    class FreqItemset(NamedTuple):
        """
        Represents an (items, freq) tuple.

        .. versionadded:: 1.4.0
        """
        items: List[Any]
        freq: int

class PrefixSpanModel(JavaModelWrapper, Generic[T]):
    '''
    Model fitted by PrefixSpan

    .. versionadded:: 1.6.0

    Examples
    --------
    >>> data = [
    ...    [["a", "b"], ["c"]],
    ...    [["a"], ["c", "b"], ["a", "b"]],
    ...    [["a", "b"], ["e"]],
    ...    [["f"]]]
    >>> rdd = sc.parallelize(data, 2)
    >>> model = PrefixSpan.train(rdd)
    >>> sorted(model.freqSequences().collect())
    [FreqSequence(sequence=[[\'a\']], freq=3), FreqSequence(sequence=[[\'a\'], [\'a\']], freq=1), ...
    '''
    def freqSequences(self) -> RDD['PrefixSpan.FreqSequence']:
        """Gets frequent sequences"""

class PrefixSpan:
    '''
    A parallel PrefixSpan algorithm to mine frequent sequential patterns.
    The PrefixSpan algorithm is described in Jian Pei et al (2001) [1]_

    .. versionadded:: 1.6.0

    .. [1] Jian Pei et al.,
        "PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth,"
        Proceedings 17th International Conference on Data Engineering, Heidelberg,
        Germany, 2001, pp. 215-224,
        doi: https://doi.org/10.1109/ICDE.2001.914830
    '''
    @classmethod
    def train(cls, data: RDD[List[List[T]]], minSupport: float = 0.1, maxPatternLength: int = 10, maxLocalProjDBSize: int = 32000000) -> PrefixSpanModel[T]:
        """
        Finds the complete set of frequent sequential patterns in the
        input sequences of itemsets.

        .. versionadded:: 1.6.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The input data set, each element contains a sequence of
            itemsets.
        minSupport : float, optional
            The minimal support level of the sequential pattern, any
            pattern that appears more than (minSupport *
            size-of-the-dataset) times will be output.
            (default: 0.1)
        maxPatternLength : int, optional
            The maximal length of the sequential pattern, any pattern
            that appears less than maxPatternLength will be output.
            (default: 10)
        maxLocalProjDBSize : int, optional
            The maximum number of items (including delimiters used in the
            internal storage format) allowed in a projected database before
            local processing. If a projected database exceeds this size,
            another iteration of distributed prefix growth is run.
            (default: 32000000)
        """
    class FreqSequence(NamedTuple):
        """
        Represents a (sequence, freq) tuple.

        .. versionadded:: 1.6.0
        """
        sequence: List[List[Any]]
        freq: int
