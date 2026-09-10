from pyspark.ml.param import Param
from pyspark.ml.param.shared import HasBlockSize, HasCheckpointInterval, HasMaxIter, HasPredictionCol, HasRegParam, HasSeed
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel
from pyspark.sql import DataFrame
from typing import Any

__all__ = ['ALS', 'ALSModel']

class _ALSModelParams(HasPredictionCol, HasBlockSize):
    """
    Params for :py:class:`ALS` and :py:class:`ALSModel`.

    .. versionadded:: 3.0.0
    """
    userCol: Param[str]
    itemCol: Param[str]
    coldStartStrategy: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getUserCol(self) -> str:
        """
        Gets the value of userCol or its default value.
        """
    def getItemCol(self) -> str:
        """
        Gets the value of itemCol or its default value.
        """
    def getColdStartStrategy(self) -> str:
        """
        Gets the value of coldStartStrategy or its default value.
        """

class _ALSParams(_ALSModelParams, HasMaxIter, HasRegParam, HasCheckpointInterval, HasSeed):
    """
    Params for :py:class:`ALS`.

    .. versionadded:: 3.0.0
    """
    rank: Param[int]
    numUserBlocks: Param[int]
    numItemBlocks: Param[int]
    implicitPrefs: Param[bool]
    alpha: Param[float]
    ratingCol: Param[str]
    nonnegative: Param[bool]
    intermediateStorageLevel: Param[str]
    finalStorageLevel: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getRank(self) -> int:
        """
        Gets the value of rank or its default value.
        """
    def getNumUserBlocks(self) -> int:
        """
        Gets the value of numUserBlocks or its default value.
        """
    def getNumItemBlocks(self) -> int:
        """
        Gets the value of numItemBlocks or its default value.
        """
    def getImplicitPrefs(self) -> bool:
        """
        Gets the value of implicitPrefs or its default value.
        """
    def getAlpha(self) -> float:
        """
        Gets the value of alpha or its default value.
        """
    def getRatingCol(self) -> str:
        """
        Gets the value of ratingCol or its default value.
        """
    def getNonnegative(self) -> bool:
        """
        Gets the value of nonnegative or its default value.
        """
    def getIntermediateStorageLevel(self) -> str:
        """
        Gets the value of intermediateStorageLevel or its default value.
        """
    def getFinalStorageLevel(self) -> str:
        """
        Gets the value of finalStorageLevel or its default value.
        """

class ALS(JavaEstimator['ALSModel'], _ALSParams, JavaMLWritable, JavaMLReadable['ALS']):
    '''
    Alternating Least Squares (ALS) matrix factorization.

    ALS attempts to estimate the ratings matrix `R` as the product of
    two lower-rank matrices, `X` and `Y`, i.e. `X * Yt = R`. Typically
    these approximations are called \'factor\' matrices. The general
    approach is iterative. During each iteration, one of the factor
    matrices is held constant, while the other is solved for using least
    squares. The newly-solved factor matrix is then held constant while
    solving for the other factor matrix.

    This is a blocked implementation of the ALS factorization algorithm
    that groups the two sets of factors (referred to as "users" and
    "products") into blocks and reduces communication by only sending
    one copy of each user vector to each product block on each
    iteration, and only for the product blocks that need that user\'s
    feature vector. This is achieved by pre-computing some information
    about the ratings matrix to determine the "out-links" of each user
    (which blocks of products it will contribute to) and "in-link"
    information for each product (which of the feature vectors it
    receives from each user block it will depend on). This allows us to
    send only an array of feature vectors between each user block and
    product block, and have the product block find the users\' ratings
    and update the products based on these messages.

    For implicit preference data, the algorithm used is based on
    `"Collaborative Filtering for Implicit Feedback Datasets",
    <https://doi.org/10.1109/ICDM.2008.22>`_, adapted for the blocked
    approach used here.

    Essentially instead of finding the low-rank approximations to the
    rating matrix `R`, this finds the approximations for a preference
    matrix `P` where the elements of `P` are 1 if r > 0 and 0 if r <= 0.
    The ratings then act as \'confidence\' values related to strength of
    indicated user preferences rather than explicit ratings given to
    items.

    .. versionadded:: 1.4.0

    Notes
    -----
    The input rating dataframe to the ALS implementation should be deterministic.
    Nondeterministic data can cause failure during fitting ALS model.
    For example, an order-sensitive operation like sampling after a repartition makes
    dataframe output nondeterministic, like `df.repartition(2).sample(False, 0.5, 1618)`.
    Checkpointing sampled dataframe or adding a sort before sampling can help make the
    dataframe deterministic.

    Examples
    --------
    >>> df = spark.createDataFrame(
    ...     [(0, 0, 4.0), (0, 1, 2.0), (1, 1, 3.0), (1, 2, 4.0), (2, 1, 1.0), (2, 2, 5.0)],
    ...     ["user", "item", "rating"])
    >>> als = ALS(rank=10, seed=0)
    >>> als.setMaxIter(5)
    ALS...
    >>> als.getMaxIter()
    5
    >>> als.setRegParam(0.1)
    ALS...
    >>> als.getRegParam()
    0.1
    >>> als.clear(als.regParam)
    >>> model = als.fit(df)
    >>> model.getBlockSize()
    4096
    >>> model.getUserCol()
    \'user\'
    >>> model.setUserCol("user")
    ALSModel...
    >>> model.getItemCol()
    \'item\'
    >>> model.setPredictionCol("newPrediction")
    ALS...
    >>> model.rank
    10
    >>> model.userFactors.orderBy("id").collect()
    [Row(id=0, features=[...]), Row(id=1, ...), Row(id=2, ...)]
    >>> test = spark.createDataFrame([(0, 2), (1, 0), (2, 0)], ["user", "item"])
    >>> predictions = sorted(model.transform(test).collect(), key=lambda r: r[0])
    >>> predictions[0]
    Row(user=0, item=2, newPrediction=0.6929...)
    >>> predictions[1]
    Row(user=1, item=0, newPrediction=3.47356...)
    >>> predictions[2]
    Row(user=2, item=0, newPrediction=-0.899198...)
    >>> user_recs = model.recommendForAllUsers(3)
    >>> user_recs.where(user_recs.user == 0)        .select("recommendations.item", "recommendations.rating").collect()
    [Row(item=[0, 1, 2], rating=[3.910..., 1.997..., 0.692...])]
    >>> item_recs = model.recommendForAllItems(3)
    >>> item_recs.where(item_recs.item == 2)        .select("recommendations.user", "recommendations.rating").collect()
    [Row(user=[2, 1, 0], rating=[4.892..., 3.991..., 0.692...])]
    >>> user_subset = df.where(df.user == 2)
    >>> user_subset_recs = model.recommendForUserSubset(user_subset, 3)
    >>> user_subset_recs.select("recommendations.item", "recommendations.rating").first()
    Row(item=[2, 1, 0], rating=[4.892..., 1.076..., -0.899...])
    >>> item_subset = df.where(df.item == 0)
    >>> item_subset_recs = model.recommendForItemSubset(item_subset, 3)
    >>> item_subset_recs.select("recommendations.user", "recommendations.rating").first()
    Row(user=[0, 1, 2], rating=[3.910..., 3.473..., -0.899...])
    >>> als_path = temp_path + "/als"
    >>> als.save(als_path)
    >>> als2 = ALS.load(als_path)
    >>> als.getMaxIter()
    5
    >>> model_path = temp_path + "/als_model"
    >>> model.save(model_path)
    >>> model2 = ALSModel.load(model_path)
    >>> model.rank == model2.rank
    True
    >>> sorted(model.userFactors.collect()) == sorted(model2.userFactors.collect())
    True
    >>> sorted(model.itemFactors.collect()) == sorted(model2.itemFactors.collect())
    True
    >>> model.transform(test).take(1) == model2.transform(test).take(1)
    True
    '''
    def __init__(self, *, rank: int = 10, maxIter: int = 10, regParam: float = 0.1, numUserBlocks: int = 10, numItemBlocks: int = 10, implicitPrefs: bool = False, alpha: float = 1.0, userCol: str = 'user', itemCol: str = 'item', seed: int | None = None, ratingCol: str = 'rating', nonnegative: bool = False, checkpointInterval: int = 10, intermediateStorageLevel: str = 'MEMORY_AND_DISK', finalStorageLevel: str = 'MEMORY_AND_DISK', coldStartStrategy: str = 'nan', blockSize: int = 4096) -> None:
        '''
        __init__(self, \\*, rank=10, maxIter=10, regParam=0.1, numUserBlocks=10,
                 numItemBlocks=10, implicitPrefs=False, alpha=1.0, userCol="user", itemCol="item",                  seed=None, ratingCol="rating", nonnegative=False, checkpointInterval=10,                  intermediateStorageLevel="MEMORY_AND_DISK",                  finalStorageLevel="MEMORY_AND_DISK", coldStartStrategy="nan", blockSize=4096)
        '''
    def setParams(self, *, rank: int = 10, maxIter: int = 10, regParam: float = 0.1, numUserBlocks: int = 10, numItemBlocks: int = 10, implicitPrefs: bool = False, alpha: float = 1.0, userCol: str = 'user', itemCol: str = 'item', seed: int | None = None, ratingCol: str = 'rating', nonnegative: bool = False, checkpointInterval: int = 10, intermediateStorageLevel: str = 'MEMORY_AND_DISK', finalStorageLevel: str = 'MEMORY_AND_DISK', coldStartStrategy: str = 'nan', blockSize: int = 4096) -> ALS:
        '''
        setParams(self, \\*, rank=10, maxIter=10, regParam=0.1, numUserBlocks=10,                  numItemBlocks=10, implicitPrefs=False, alpha=1.0, userCol="user", itemCol="item",                  seed=None, ratingCol="rating", nonnegative=False, checkpointInterval=10,                  intermediateStorageLevel="MEMORY_AND_DISK",                  finalStorageLevel="MEMORY_AND_DISK", coldStartStrategy="nan", blockSize=4096)
        Sets params for ALS.
        '''
    def setRank(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`rank`.
        """
    def setNumUserBlocks(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`numUserBlocks`.
        """
    def setNumItemBlocks(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`numItemBlocks`.
        """
    def setNumBlocks(self, value: int) -> ALS:
        """
        Sets both :py:attr:`numUserBlocks` and :py:attr:`numItemBlocks` to the specific value.
        """
    def setImplicitPrefs(self, value: bool) -> ALS:
        """
        Sets the value of :py:attr:`implicitPrefs`.
        """
    def setAlpha(self, value: float) -> ALS:
        """
        Sets the value of :py:attr:`alpha`.
        """
    def setUserCol(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`userCol`.
        """
    def setItemCol(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`itemCol`.
        """
    def setRatingCol(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`ratingCol`.
        """
    def setNonnegative(self, value: bool) -> ALS:
        """
        Sets the value of :py:attr:`nonnegative`.
        """
    def setIntermediateStorageLevel(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`intermediateStorageLevel`.
        """
    def setFinalStorageLevel(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`finalStorageLevel`.
        """
    def setColdStartStrategy(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`coldStartStrategy`.
        """
    def setMaxIter(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setRegParam(self, value: float) -> ALS:
        """
        Sets the value of :py:attr:`regParam`.
        """
    def setPredictionCol(self, value: str) -> ALS:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setCheckpointInterval(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setBlockSize(self, value: int) -> ALS:
        """
        Sets the value of :py:attr:`blockSize`.
        """

class ALSModel(JavaModel, _ALSModelParams, JavaMLWritable, JavaMLReadable['ALSModel']):
    """
    Model fitted by ALS.

    .. versionadded:: 1.4.0
    """
    def setUserCol(self, value: str) -> ALSModel:
        """
        Sets the value of :py:attr:`userCol`.
        """
    def setItemCol(self, value: str) -> ALSModel:
        """
        Sets the value of :py:attr:`itemCol`.
        """
    def setColdStartStrategy(self, value: str) -> ALSModel:
        """
        Sets the value of :py:attr:`coldStartStrategy`.
        """
    def setPredictionCol(self, value: str) -> ALSModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setBlockSize(self, value: int) -> ALSModel:
        """
        Sets the value of :py:attr:`blockSize`.
        """
    @property
    def rank(self) -> int:
        """rank of the matrix factorization model"""
    @property
    def userFactors(self) -> DataFrame:
        """
        a DataFrame that stores user factors in two columns: `id` and
        `features`
        """
    @property
    def itemFactors(self) -> DataFrame:
        """
        a DataFrame that stores item factors in two columns: `id` and
        `features`
        """
    def recommendForAllUsers(self, numItems: int) -> DataFrame:
        """
        Returns top `numItems` items recommended for each user, for all users.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        numItems : int
            max number of recommendations for each user

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            a DataFrame of (userCol, recommendations), where recommendations are
            stored as an array of (itemCol, rating) Rows.
        """
    def recommendForAllItems(self, numUsers: int) -> DataFrame:
        """
        Returns top `numUsers` users recommended for each item, for all items.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        numUsers : int
            max number of recommendations for each item

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            a DataFrame of (itemCol, recommendations), where recommendations are
            stored as an array of (userCol, rating) Rows.
        """
    def recommendForUserSubset(self, dataset: DataFrame, numItems: int) -> DataFrame:
        """
        Returns top `numItems` items recommended for each user id in the input data set. Note that
        if there are duplicate ids in the input dataset, only one set of recommendations per unique
        id will be returned.

        .. versionadded:: 2.3.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            a DataFrame containing a column of user ids. The column name must match `userCol`.
        numItems : int
            max number of recommendations for each user

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            a DataFrame of (userCol, recommendations), where recommendations are
            stored as an array of (itemCol, rating) Rows.
        """
    def recommendForItemSubset(self, dataset: DataFrame, numUsers: int) -> DataFrame:
        """
        Returns top `numUsers` users recommended for each item id in the input data set. Note that
        if there are duplicate ids in the input dataset, only one set of recommendations per unique
        id will be returned.

        .. versionadded:: 2.3.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            a DataFrame containing a column of item ids. The column name must match `itemCol`.
        numUsers : int
            max number of recommendations for each item

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            a DataFrame of (itemCol, recommendations), where recommendations are
            stored as an array of (userCol, rating) Rows.
        """
