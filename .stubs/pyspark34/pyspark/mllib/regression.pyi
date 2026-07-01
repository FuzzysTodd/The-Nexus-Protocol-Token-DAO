import numpy as np
from _typeshed import Incomplete
from pyspark.context import SparkContext
from pyspark.mllib._typing import VectorLike
from pyspark.mllib.linalg import Vector
from pyspark.mllib.util import Loader, Saveable
from pyspark.rdd import RDD
from pyspark.streaming.dstream import DStream
from typing import Iterable, Tuple, Type, TypeVar, overload

__all__ = ['LabeledPoint', 'LinearModel', 'LinearRegressionModel', 'LinearRegressionWithSGD', 'RidgeRegressionModel', 'RidgeRegressionWithSGD', 'LassoModel', 'LassoWithSGD', 'IsotonicRegressionModel', 'IsotonicRegression', 'StreamingLinearAlgorithm', 'StreamingLinearRegressionWithSGD']

LM = TypeVar('LM')
K = TypeVar('K')

class LabeledPoint:
    """
    Class that represents the features and labels of a data point.

    .. versionadded:: 1.0.0

    Parameters
    ----------
    label : int
        Label for this data point.
    features : :py:class:`pyspark.mllib.linalg.Vector` or convertible
        Vector of features for this point (NumPy array, list,
        pyspark.mllib.linalg.SparseVector, or scipy.sparse column matrix).

    Notes
    -----
    'label' and 'features' are accessible as class attributes.
    """
    label: Incomplete
    features: Incomplete
    def __init__(self, label: float, features: Iterable[float]) -> None: ...
    def __reduce__(self) -> Tuple[Type['LabeledPoint'], Tuple[float, Vector]]: ...

class LinearModel:
    """
    A linear model that has a vector of coefficients and an intercept.

    .. versionadded:: 0.9.0

    Parameters
    ----------
    weights : :py:class:`pyspark.mllib.linalg.Vector`
        Weights computed for every feature.
    intercept : float
      Intercept computed for this model.
    """
    def __init__(self, weights: Vector, intercept: float) -> None: ...
    @property
    def weights(self) -> Vector:
        """Weights computed for every feature."""
    @property
    def intercept(self) -> float:
        """Intercept computed for this model."""

class LinearRegressionModelBase(LinearModel):
    """A linear regression model.

    .. versionadded:: 0.9.0

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> lrmb = LinearRegressionModelBase(np.array([1.0, 2.0]), 0.1)
    >>> abs(lrmb.predict(np.array([-1.03, 7.777])) - 14.624) < 1e-6
    True
    >>> abs(lrmb.predict(SparseVector(2, {0: -1.03, 1: 7.777})) - 14.624) < 1e-6
    True
    """
    @overload
    def predict(self, x: VectorLike) -> float: ...
    @overload
    def predict(self, x: RDD['VectorLike']) -> RDD[float]: ...

class LinearRegressionModel(LinearRegressionModelBase):
    '''A linear regression model derived from a least-squares fit.

    .. versionadded:: 0.9.0

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> from pyspark.mllib.regression import LabeledPoint
    >>> data = [
    ...     LabeledPoint(0.0, [0.0]),
    ...     LabeledPoint(1.0, [1.0]),
    ...     LabeledPoint(3.0, [2.0]),
    ...     LabeledPoint(2.0, [3.0])
    ... ]
    >>> lrm = LinearRegressionWithSGD.train(sc.parallelize(data), iterations=10,
    ...     initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> abs(lrm.predict(sc.parallelize([[1.0]])).collect()[0] - 1) < 0.5
    True
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> lrm.save(sc, path)
    >>> sameModel = LinearRegressionModel.load(sc, path)
    >>> abs(sameModel.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(sameModel.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(sameModel.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> from shutil import rmtree
    >>> try:
    ...     rmtree(path)
    ... except BaseException:
    ...     pass
    >>> data = [
    ...     LabeledPoint(0.0, SparseVector(1, {0: 0.0})),
    ...     LabeledPoint(1.0, SparseVector(1, {0: 1.0})),
    ...     LabeledPoint(3.0, SparseVector(1, {0: 2.0})),
    ...     LabeledPoint(2.0, SparseVector(1, {0: 3.0}))
    ... ]
    >>> lrm = LinearRegressionWithSGD.train(sc.parallelize(data), iterations=10,
    ...     initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> lrm = LinearRegressionWithSGD.train(sc.parallelize(data), iterations=10, step=1.0,
    ...    miniBatchFraction=1.0, initialWeights=np.array([1.0]), regParam=0.1, regType="l2",
    ...    intercept=True, validateData=True)
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    '''
    def save(self, sc: SparkContext, path: str) -> None:
        """Save a LinearRegressionModel."""
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LinearRegressionModel:
        """Load a LinearRegressionModel."""

class LinearRegressionWithSGD:
    """
    Train a linear regression model with no regularization using Stochastic Gradient Descent.

    .. versionadded:: 0.9.0
    .. deprecated:: 2.0.0
        Use :py:class:`pyspark.ml.regression.LinearRegression`.
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, step: float = 1.0, miniBatchFraction: float = 1.0, initialWeights: VectorLike | None = None, regParam: float = 0.0, regType: str | None = None, intercept: bool = False, validateData: bool = True, convergenceTol: float = 0.001) -> LinearRegressionModel:
        '''
        Train a linear regression model using Stochastic Gradient
        Descent (SGD). This solves the least squares regression
        formulation

            f(weights) = 1/(2n) ||A weights - y||^2

        which is the mean squared error. Here the data matrix has n rows,
        and the input RDD holds the set of rows of A, each with its
        corresponding right hand side label y.
        See also the documentation for the precise formulation.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of LabeledPoint.
        iterations : int, optional
            The number of iterations.
            (default: 100)
        step : float, optional
            The step parameter used in SGD.
            (default: 1.0)
        miniBatchFraction : float, optional
            Fraction of data to be used for each SGD iteration.
            (default: 1.0)
        initialWeights : :py:class:`pyspark.mllib.linalg.Vector` or convertible, optional
            The initial weights.
            (default: None)
        regParam : float, optional
            The regularizer parameter.
            (default: 0.0)
        regType : str, optional
            The type of regularizer used for training our model.
            Supported values:

            - "l1" for using L1 regularization
            - "l2" for using L2 regularization
            - None for no regularization (default)

        intercept : bool, optional
            Boolean parameter which indicates the use or not of the
            augmented representation for training data (i.e., whether bias
            features are activated or not).
            (default: False)
        validateData : bool, optional
            Boolean parameter which indicates if the algorithm should
            validate data before training.
            (default: True)
        convergenceTol : float, optional
            A condition which decides iteration termination.
            (default: 0.001)
        '''

class LassoModel(LinearRegressionModelBase):
    """A linear regression model derived from a least-squares fit with
    an l_1 penalty term.

    .. versionadded:: 0.9.0

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> from pyspark.mllib.regression import LabeledPoint
    >>> data = [
    ...     LabeledPoint(0.0, [0.0]),
    ...     LabeledPoint(1.0, [1.0]),
    ...     LabeledPoint(3.0, [2.0]),
    ...     LabeledPoint(2.0, [3.0])
    ... ]
    >>> lrm = LassoWithSGD.train(
    ...     sc.parallelize(data), iterations=10, initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> abs(lrm.predict(sc.parallelize([[1.0]])).collect()[0] - 1) < 0.5
    True
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> lrm.save(sc, path)
    >>> sameModel = LassoModel.load(sc, path)
    >>> abs(sameModel.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(sameModel.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(sameModel.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> from shutil import rmtree
    >>> try:
    ...    rmtree(path)
    ... except BaseException:
    ...    pass
    >>> data = [
    ...     LabeledPoint(0.0, SparseVector(1, {0: 0.0})),
    ...     LabeledPoint(1.0, SparseVector(1, {0: 1.0})),
    ...     LabeledPoint(3.0, SparseVector(1, {0: 2.0})),
    ...     LabeledPoint(2.0, SparseVector(1, {0: 3.0}))
    ... ]
    >>> lrm = LinearRegressionWithSGD.train(sc.parallelize(data), iterations=10,
    ...     initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> lrm = LassoWithSGD.train(sc.parallelize(data), iterations=10, step=1.0,
    ...     regParam=0.01, miniBatchFraction=1.0, initialWeights=np.array([1.0]), intercept=True,
    ...     validateData=True)
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    """
    def save(self, sc: SparkContext, path: str) -> None:
        """Save a LassoModel."""
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LassoModel:
        """Load a LassoModel."""

class LassoWithSGD:
    """
    Train a regression model with L1-regularization using Stochastic Gradient Descent.

    .. versionadded:: 0.9.0
    .. deprecated:: 2.0.0
        Use :py:class:`pyspark.ml.regression.LinearRegression` with elasticNetParam = 1.0.
        Note the default regParam is 0.01 for LassoWithSGD, but is 0.0 for LinearRegression.
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, step: float = 1.0, regParam: float = 0.01, miniBatchFraction: float = 1.0, initialWeights: VectorLike | None = None, intercept: bool = False, validateData: bool = True, convergenceTol: float = 0.001) -> LassoModel:
        """
        Train a regression model with L1-regularization using Stochastic
        Gradient Descent. This solves the l1-regularized least squares
        regression formulation

            f(weights) = 1/(2n) ||A weights - y||^2  + regParam ||weights||_1

        Here the data matrix has n rows, and the input RDD holds the set
        of rows of A, each with its corresponding right hand side label y.
        See also the documentation for the precise formulation.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of LabeledPoint.
        iterations : int, optional
            The number of iterations.
            (default: 100)
        step : float, optional
            The step parameter used in SGD.
            (default: 1.0)
        regParam : float, optional
            The regularizer parameter.
            (default: 0.01)
        miniBatchFraction : float, optional
            Fraction of data to be used for each SGD iteration.
            (default: 1.0)
        initialWeights : :py:class:`pyspark.mllib.linalg.Vector` or convertible, optional
            The initial weights.
            (default: None)
        intercept : bool, optional
            Boolean parameter which indicates the use or not of the
            augmented representation for training data (i.e. whether bias
            features are activated or not).
            (default: False)
        validateData : bool, optional
            Boolean parameter which indicates if the algorithm should
            validate data before training.
            (default: True)
        convergenceTol : float, optional
            A condition which decides iteration termination.
            (default: 0.001)
        """

class RidgeRegressionModel(LinearRegressionModelBase):
    """A linear regression model derived from a least-squares fit with
    an l_2 penalty term.

    .. versionadded:: 0.9.0

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> from pyspark.mllib.regression import LabeledPoint
    >>> data = [
    ...     LabeledPoint(0.0, [0.0]),
    ...     LabeledPoint(1.0, [1.0]),
    ...     LabeledPoint(3.0, [2.0]),
    ...     LabeledPoint(2.0, [3.0])
    ... ]
    >>> lrm = RidgeRegressionWithSGD.train(sc.parallelize(data), iterations=10,
    ...     initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> abs(lrm.predict(sc.parallelize([[1.0]])).collect()[0] - 1) < 0.5
    True
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> lrm.save(sc, path)
    >>> sameModel = RidgeRegressionModel.load(sc, path)
    >>> abs(sameModel.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(sameModel.predict(np.array([1.0])) - 1) < 0.5
    True
    >>> abs(sameModel.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> from shutil import rmtree
    >>> try:
    ...    rmtree(path)
    ... except BaseException:
    ...    pass
    >>> data = [
    ...     LabeledPoint(0.0, SparseVector(1, {0: 0.0})),
    ...     LabeledPoint(1.0, SparseVector(1, {0: 1.0})),
    ...     LabeledPoint(3.0, SparseVector(1, {0: 2.0})),
    ...     LabeledPoint(2.0, SparseVector(1, {0: 3.0}))
    ... ]
    >>> lrm = LinearRegressionWithSGD.train(sc.parallelize(data), iterations=10,
    ...     initialWeights=np.array([1.0]))
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    >>> lrm = RidgeRegressionWithSGD.train(sc.parallelize(data), iterations=10, step=1.0,
    ...     regParam=0.01, miniBatchFraction=1.0, initialWeights=np.array([1.0]), intercept=True,
    ...     validateData=True)
    >>> abs(lrm.predict(np.array([0.0])) - 0) < 0.5
    True
    >>> abs(lrm.predict(SparseVector(1, {0: 1.0})) - 1) < 0.5
    True
    """
    def save(self, sc: SparkContext, path: str) -> None:
        """Save a RidgeRegressionMode."""
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> RidgeRegressionModel:
        """Load a RidgeRegressionMode."""

class RidgeRegressionWithSGD:
    """
    Train a regression model with L2-regularization using Stochastic Gradient Descent.

    .. versionadded:: 0.9.0
    .. deprecated:: 2.0.0
        Use :py:class:`pyspark.ml.regression.LinearRegression` with elasticNetParam = 0.0.
        Note the default regParam is 0.01 for RidgeRegressionWithSGD, but is 0.0 for
        LinearRegression.
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, step: float = 1.0, regParam: float = 0.01, miniBatchFraction: float = 1.0, initialWeights: VectorLike | None = None, intercept: bool = False, validateData: bool = True, convergenceTol: float = 0.001) -> RidgeRegressionModel:
        """
        Train a regression model with L2-regularization using Stochastic
        Gradient Descent. This solves the l2-regularized least squares
        regression formulation

            f(weights) = 1/(2n) ||A weights - y||^2 + regParam/2 ||weights||^2

        Here the data matrix has n rows, and the input RDD holds the set
        of rows of A, each with its corresponding right hand side label y.
        See also the documentation for the precise formulation.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of LabeledPoint.
        iterations : int, optional
            The number of iterations.
            (default: 100)
        step : float, optional
            The step parameter used in SGD.
            (default: 1.0)
        regParam : float, optional
            The regularizer parameter.
            (default: 0.01)
        miniBatchFraction : float, optional
            Fraction of data to be used for each SGD iteration.
            (default: 1.0)
        initialWeights : :py:class:`pyspark.mllib.linalg.Vector` or convertible, optional
            The initial weights.
            (default: None)
        intercept : bool, optional
            Boolean parameter which indicates the use or not of the
            augmented representation for training data (i.e. whether bias
            features are activated or not).
            (default: False)
        validateData : bool, optional
            Boolean parameter which indicates if the algorithm should
            validate data before training.
            (default: True)
        convergenceTol : float, optional
            A condition which decides iteration termination.
            (default: 0.001)
        """

class IsotonicRegressionModel(Saveable, Loader['IsotonicRegressionModel']):
    """
    Regression model for isotonic regression.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    boundaries : ndarray
        Array of boundaries for which predictions are known. Boundaries
        must be sorted in increasing order.
    predictions : ndarray
        Array of predictions associated to the boundaries at the same
        index. Results of isotonic regression and therefore monotone.
    isotonic : true
        Indicates whether this is isotonic or antitonic.

    Examples
    --------
    >>> data = [(1, 0, 1), (2, 1, 1), (3, 2, 1), (1, 3, 1), (6, 4, 1), (17, 5, 1), (16, 6, 1)]
    >>> irm = IsotonicRegression.train(sc.parallelize(data))
    >>> irm.predict(3)
    2.0
    >>> irm.predict(5)
    16.5
    >>> irm.predict(sc.parallelize([3, 5])).collect()
    [2.0, 16.5]
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> irm.save(sc, path)
    >>> sameModel = IsotonicRegressionModel.load(sc, path)
    >>> sameModel.predict(3)
    2.0
    >>> sameModel.predict(5)
    16.5
    >>> from shutil import rmtree
    >>> try:
    ...     rmtree(path)
    ... except OSError:
    ...     pass
    """
    boundaries: Incomplete
    predictions: Incomplete
    isotonic: Incomplete
    def __init__(self, boundaries: np.ndarray, predictions: np.ndarray, isotonic: bool) -> None: ...
    @overload
    def predict(self, x: float) -> np.float64: ...
    @overload
    def predict(self, x: VectorLike) -> np.ndarray: ...
    @overload
    def predict(self, x: RDD[float]) -> RDD[np.float64]: ...
    @overload
    def predict(self, x: RDD['VectorLike']) -> RDD[np.ndarray]: ...
    def save(self, sc: SparkContext, path: str) -> None:
        """Save an IsotonicRegressionModel."""
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> IsotonicRegressionModel:
        """Load an IsotonicRegressionModel."""

class IsotonicRegression:
    '''
    Isotonic regression.
    Currently implemented using parallelized pool adjacent violators
    algorithm. Only univariate (single feature) algorithm supported.

    .. versionadded:: 1.4.0

    Notes
    -----
    Sequential PAV implementation based on
    Tibshirani, Ryan J., Holger Hoefling, and Robert Tibshirani (2011) [1]_

    Sequential PAV parallelization based on
    Kearsley, Anthony J., Richard A. Tapia, and Michael W. Trosset (1996) [2]_

    See also
    `Isotonic regression (Wikipedia) <http://en.wikipedia.org/wiki/Isotonic_regression>`_.

    .. [1] Tibshirani, Ryan J., Holger Hoefling, and Robert Tibshirani.
        "Nearly-isotonic regression." Technometrics 53.1 (2011): 54-61.
        Available from http://www.stat.cmu.edu/~ryantibs/papers/neariso.pdf
    .. [2] Kearsley, Anthony J., Richard A. Tapia, and Michael W. Trosset
        "An approach to parallelizing isotonic regression."
        Applied Mathematics and Parallel Computing. Physica-Verlag HD, 1996. 141-147.
        Available from http://softlib.rice.edu/pub/CRPC-TRs/reports/CRPC-TR96640.pdf
    '''
    @classmethod
    def train(cls, data: RDD['VectorLike'], isotonic: bool = True) -> IsotonicRegressionModel:
        """
        Train an isotonic regression model on the given data.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            RDD of (label, feature, weight) tuples.
        isotonic : bool, optional
            Whether this is isotonic (which is default) or antitonic.
            (default: True)
        """

class StreamingLinearAlgorithm:
    """
    Base class that has to be inherited by any StreamingLinearAlgorithm.

    Prevents reimplementation of methods predictOn and predictOnValues.

    .. versionadded:: 1.5.0
    """
    def __init__(self, model: LinearModel | None) -> None: ...
    def latestModel(self) -> LinearModel | None:
        """
        Returns the latest model.
        """
    def predictOn(self, dstream: DStream[VectorLike]) -> DStream[float]:
        """
        Use the model to make predictions on batches of data from a
        DStream.

        .. versionadded:: 1.5.0

        Returns
        -------
        :py:class:`pyspark.streaming.DStream`
            DStream containing predictions.
        """
    def predictOnValues(self, dstream: DStream[Tuple[K, VectorLike]]) -> DStream[Tuple[K, float]]:
        """
        Use the model to make predictions on the values of a DStream and
        carry over its keys.

        .. versionadded:: 1.5.0

        Returns
        -------
        :py:class:`pyspark.streaming.DStream`
            DStream containing predictions.
        """

class StreamingLinearRegressionWithSGD(StreamingLinearAlgorithm):
    """
    Train or predict a linear regression model on streaming data.
    Training uses Stochastic Gradient Descent to update the model
    based on each new batch of incoming data from a DStream
    (see `LinearRegressionWithSGD` for model equation).

    Each batch of data is assumed to be an RDD of LabeledPoints.
    The number of data points per batch can vary, but the number
    of features must be constant. An initial weight vector must
    be provided.

    .. versionadded:: 1.5.0

    Parameters
    ----------
    stepSize : float, optional
        Step size for each iteration of gradient descent.
        (default: 0.1)
    numIterations : int, optional
        Number of iterations run for each batch of data.
        (default: 50)
    miniBatchFraction : float, optional
        Fraction of each batch of data to use for updates.
        (default: 1.0)
    convergenceTol : float, optional
        Value used to determine when to terminate iterations.
        (default: 0.001)
    """
    stepSize: Incomplete
    numIterations: Incomplete
    miniBatchFraction: Incomplete
    convergenceTol: Incomplete
    def __init__(self, stepSize: float = 0.1, numIterations: int = 50, miniBatchFraction: float = 1.0, convergenceTol: float = 0.001) -> None: ...
    def setInitialWeights(self, initialWeights: VectorLike) -> StreamingLinearRegressionWithSGD:
        """
        Set the initial value of weights.

        This must be set before running trainOn and predictOn
        """
    def trainOn(self, dstream: DStream[LabeledPoint]) -> None:
        """Train the model on the incoming dstream."""
