from pyspark.ml.param.shared import HasPredictionCol, Param
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaParams
from pyspark.sql import DataFrame
from typing import Any

__all__ = ['FPGrowth', 'FPGrowthModel', 'PrefixSpan']

class _FPGrowthParams(HasPredictionCol):
    """
    Params for :py:class:`FPGrowth` and :py:class:`FPGrowthModel`.

    .. versionadded:: 3.0.0
    """
    itemsCol: Param[str]
    minSupport: Param[float]
    numPartitions: Param[int]
    minConfidence: Param[float]
    def __init__(self, *args: Any) -> None: ...
    def getItemsCol(self) -> str:
        """
        Gets the value of itemsCol or its default value.
        """
    def getMinSupport(self) -> float:
        """
        Gets the value of minSupport or its default value.
        """
    def getNumPartitions(self) -> int:
        """
        Gets the value of :py:attr:`numPartitions` or its default value.
        """
    def getMinConfidence(self) -> float:
        """
        Gets the value of minConfidence or its default value.
        """

class FPGrowthModel(JavaModel, _FPGrowthParams, JavaMLWritable, JavaMLReadable['FPGrowthModel']):
    """
    Model fitted by FPGrowth.

    .. versionadded:: 2.2.0
    """
    def setItemsCol(self, value: str) -> FPGrowthModel:
        """
        Sets the value of :py:attr:`itemsCol`.
        """
    def setMinConfidence(self, value: float) -> FPGrowthModel:
        """
        Sets the value of :py:attr:`minConfidence`.
        """
    def setPredictionCol(self, value: str) -> FPGrowthModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    @property
    def freqItemsets(self) -> DataFrame:
        """
        DataFrame with two columns:
        * `items` - Itemset of the same type as the input column.
        * `freq`  - Frequency of the itemset (`LongType`).
        """
    @property
    def associationRules(self) -> DataFrame:
        """
        DataFrame with four columns:
        * `antecedent`  - Array of the same type as the input column.
        * `consequent`  - Array of the same type as the input column.
        * `confidence`  - Confidence for the rule (`DoubleType`).
        * `lift`        - Lift for the rule (`DoubleType`).
        """

class FPGrowth(JavaEstimator[FPGrowthModel], _FPGrowthParams, JavaMLWritable, JavaMLReadable['FPGrowth']):
    '''
    A parallel FP-growth algorithm to mine frequent itemsets.

    .. versionadded:: 2.2.0

    Notes
    -----

    The algorithm is described in
    Li et al., PFP: Parallel FP-Growth for Query Recommendation [1]_.
    PFP distributes computation in such a way that each worker executes an
    independent group of mining tasks. The FP-Growth algorithm is described in
    Han et al., Mining frequent patterns without candidate generation [2]_

    NULL values in the feature column are ignored during `fit()`.

    Internally `transform` `collects` and `broadcasts` association rules.


    .. [1] Haoyuan Li, Yi Wang, Dong Zhang, Ming Zhang, and Edward Y. Chang. 2008.
        Pfp: parallel fp-growth for query recommendation.
        In Proceedings of the 2008 ACM conference on Recommender systems (RecSys \'08).
        Association for Computing Machinery, New York, NY, USA, 107-114.
        DOI: https://doi.org/10.1145/1454008.1454027
    .. [2] Jiawei Han, Jian Pei, and Yiwen Yin. 2000.
        Mining frequent patterns without candidate generation.
        SIGMOD Rec. 29, 2 (June 2000), 1-12.
        DOI: https://doi.org/10.1145/335191.335372


    Examples
    --------
    >>> from pyspark.sql.functions import split
    >>> data = (spark.read
    ...     .text("data/mllib/sample_fpgrowth.txt")
    ...     .select(split("value", "\\s+").alias("items")))
    >>> data.show(truncate=False)
    +------------------------+
    |items                   |
    +------------------------+
    |[r, z, h, k, p]         |
    |[z, y, x, w, v, u, t, s]|
    |[s, x, o, n, r]         |
    |[x, z, y, m, t, s, q, e]|
    |[z]                     |
    |[x, z, y, r, q, t, p]   |
    +------------------------+
    ...
    >>> fp = FPGrowth(minSupport=0.2, minConfidence=0.7)
    >>> fpm = fp.fit(data)
    >>> fpm.setPredictionCol("newPrediction")
    FPGrowthModel...
    >>> fpm.freqItemsets.sort("items").show(5)
    +---------+----+
    |    items|freq|
    +---------+----+
    |      [p]|   2|
    |   [p, r]|   2|
    |[p, r, z]|   2|
    |   [p, z]|   2|
    |      [q]|   2|
    +---------+----+
    only showing top 5 rows
    ...
    >>> fpm.associationRules.sort("antecedent", "consequent").show(5)
    +----------+----------+----------+----+------------------+
    |antecedent|consequent|confidence|lift|           support|
    +----------+----------+----------+----+------------------+
    |       [p]|       [r]|       1.0| 2.0|0.3333333333333333|
    |       [p]|       [z]|       1.0| 1.2|0.3333333333333333|
    |    [p, r]|       [z]|       1.0| 1.2|0.3333333333333333|
    |    [p, z]|       [r]|       1.0| 2.0|0.3333333333333333|
    |       [q]|       [t]|       1.0| 2.0|0.3333333333333333|
    +----------+----------+----------+----+------------------+
    only showing top 5 rows
    ...
    >>> new_data = spark.createDataFrame([(["t", "s"], )], ["items"])
    >>> sorted(fpm.transform(new_data).first().newPrediction)
    [\'x\', \'y\', \'z\']
    >>> model_path = temp_path + "/fpm_model"
    >>> fpm.save(model_path)
    >>> model2 = FPGrowthModel.load(model_path)
    >>> fpm.transform(data).take(1) == model2.transform(data).take(1)
    True
    '''
    def __init__(self, *, minSupport: float = 0.3, minConfidence: float = 0.8, itemsCol: str = 'items', predictionCol: str = 'prediction', numPartitions: int | None = None) -> None:
        '''
        __init__(self, \\*, minSupport=0.3, minConfidence=0.8, itemsCol="items",                  predictionCol="prediction", numPartitions=None)
        '''
    def setParams(self, *, minSupport: float = 0.3, minConfidence: float = 0.8, itemsCol: str = 'items', predictionCol: str = 'prediction', numPartitions: int | None = None) -> FPGrowth:
        '''
        setParams(self, \\*, minSupport=0.3, minConfidence=0.8, itemsCol="items",                   predictionCol="prediction", numPartitions=None)
        '''
    def setItemsCol(self, value: str) -> FPGrowth:
        """
        Sets the value of :py:attr:`itemsCol`.
        """
    def setMinSupport(self, value: float) -> FPGrowth:
        """
        Sets the value of :py:attr:`minSupport`.
        """
    def setNumPartitions(self, value: int) -> FPGrowth:
        """
        Sets the value of :py:attr:`numPartitions`.
        """
    def setMinConfidence(self, value: float) -> FPGrowth:
        """
        Sets the value of :py:attr:`minConfidence`.
        """
    def setPredictionCol(self, value: str) -> FPGrowth:
        """
        Sets the value of :py:attr:`predictionCol`.
        """

class PrefixSpan(JavaParams):
    '''
    A parallel PrefixSpan algorithm to mine frequent sequential patterns.
    The PrefixSpan algorithm is described in J. Pei, et al., PrefixSpan: Mining Sequential Patterns
    Efficiently by Prefix-Projected Pattern Growth
    (see `here <https://doi.org/10.1109/ICDE.2001.914830">`_).
    This class is not yet an Estimator/Transformer, use :py:func:`findFrequentSequentialPatterns`
    method to run the PrefixSpan algorithm.

    .. versionadded:: 2.4.0

    Notes
    -----
    See `Sequential Pattern Mining (Wikipedia)       <https://en.wikipedia.org/wiki/Sequential_Pattern_Mining>`_

    Examples
    --------
    >>> from pyspark.ml.fpm import PrefixSpan
    >>> from pyspark.sql import Row
    >>> df = sc.parallelize([Row(sequence=[[1, 2], [3]]),
    ...                      Row(sequence=[[1], [3, 2], [1, 2]]),
    ...                      Row(sequence=[[1, 2], [5]]),
    ...                      Row(sequence=[[6]])]).toDF()
    >>> prefixSpan = PrefixSpan()
    >>> prefixSpan.getMaxLocalProjDBSize()
    32000000
    >>> prefixSpan.getSequenceCol()
    \'sequence\'
    >>> prefixSpan.setMinSupport(0.5)
    PrefixSpan...
    >>> prefixSpan.setMaxPatternLength(5)
    PrefixSpan...
    >>> prefixSpan.findFrequentSequentialPatterns(df).sort("sequence").show(truncate=False)
    +----------+----+
    |sequence  |freq|
    +----------+----+
    |[[1]]     |3   |
    |[[1], [3]]|2   |
    |[[2]]     |3   |
    |[[2, 1]]  |3   |
    |[[3]]     |2   |
    +----------+----+
    ...
    '''
    minSupport: Param[float]
    maxPatternLength: Param[int]
    maxLocalProjDBSize: Param[int]
    sequenceCol: Param[str]
    def __init__(self, *, minSupport: float = 0.1, maxPatternLength: int = 10, maxLocalProjDBSize: int = 32000000, sequenceCol: str = 'sequence') -> None:
        '''
        __init__(self, \\*, minSupport=0.1, maxPatternLength=10, maxLocalProjDBSize=32000000,                  sequenceCol="sequence")
        '''
    def setParams(self, *, minSupport: float = 0.1, maxPatternLength: int = 10, maxLocalProjDBSize: int = 32000000, sequenceCol: str = 'sequence') -> PrefixSpan:
        '''
        setParams(self, \\*, minSupport=0.1, maxPatternLength=10, maxLocalProjDBSize=32000000,                   sequenceCol="sequence")
        '''
    def setMinSupport(self, value: float) -> PrefixSpan:
        """
        Sets the value of :py:attr:`minSupport`.
        """
    def getMinSupport(self) -> float:
        """
        Gets the value of minSupport or its default value.
        """
    def setMaxPatternLength(self, value: int) -> PrefixSpan:
        """
        Sets the value of :py:attr:`maxPatternLength`.
        """
    def getMaxPatternLength(self) -> int:
        """
        Gets the value of maxPatternLength or its default value.
        """
    def setMaxLocalProjDBSize(self, value: int) -> PrefixSpan:
        """
        Sets the value of :py:attr:`maxLocalProjDBSize`.
        """
    def getMaxLocalProjDBSize(self) -> int:
        """
        Gets the value of maxLocalProjDBSize or its default value.
        """
    def setSequenceCol(self, value: str) -> PrefixSpan:
        """
        Sets the value of :py:attr:`sequenceCol`.
        """
    def getSequenceCol(self) -> str:
        """
        Gets the value of sequenceCol or its default value.
        """
    def findFrequentSequentialPatterns(self, dataset: DataFrame) -> DataFrame:
        """
        Finds the complete set of frequent sequential patterns in the input sequences of itemsets.

        .. versionadded:: 2.4.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            A dataframe containing a sequence column which is
            `ArrayType(ArrayType(T))` type, T is the item type for the input dataset.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            A `DataFrame` that contains columns of sequence and corresponding frequency.
            The schema of it will be:

            - `sequence: ArrayType(ArrayType(T))` (T is the item type)
            - `freq: Long`
        """
