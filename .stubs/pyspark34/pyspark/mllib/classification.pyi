import numpy
from _typeshed import Incomplete
from pyspark import RDD, SparkContext
from pyspark.mllib._typing import VectorLike
from pyspark.mllib.linalg import Vector
from pyspark.mllib.regression import LabeledPoint, LinearModel, StreamingLinearAlgorithm
from pyspark.mllib.util import Loader, Saveable
from pyspark.streaming.dstream import DStream
from typing import overload

__all__ = ['LogisticRegressionModel', 'LogisticRegressionWithSGD', 'LogisticRegressionWithLBFGS', 'SVMModel', 'SVMWithSGD', 'NaiveBayesModel', 'NaiveBayes', 'StreamingLogisticRegressionWithSGD']

class LinearClassificationModel(LinearModel):
    """
    A private abstract class representing a multiclass classification
    model. The categories are represented by int values: 0, 1, 2, etc.
    """
    def __init__(self, weights: Vector, intercept: float) -> None: ...
    def setThreshold(self, value: float) -> None:
        """
        Sets the threshold that separates positive predictions from
        negative predictions. An example with prediction score greater
        than or equal to this threshold is identified as a positive,
        and negative otherwise. It is used for binary classification
        only.
        """
    @property
    def threshold(self) -> float | None:
        """
        Returns the threshold (if any) used for converting raw
        prediction scores into 0/1 predictions. It is used for
        binary classification only.
        """
    def clearThreshold(self) -> None:
        """
        Clears the threshold so that `predict` will output raw
        prediction scores. It is used for binary classification only.
        """
    @overload
    def predict(self, test: VectorLike) -> int | float: ...
    @overload
    def predict(self, test: RDD['VectorLike']) -> RDD[int | float]: ...

class LogisticRegressionModel(LinearClassificationModel):
    """
    Classification model trained using Multinomial/Binary Logistic
    Regression.

    .. versionadded:: 0.9.0

    Parameters
    ----------
    weights : :py:class:`pyspark.mllib.linalg.Vector`
        Weights computed for every feature.
    intercept : float
        Intercept computed for this model. (Only used in Binary Logistic
        Regression. In Multinomial Logistic Regression, the intercepts will
        not be a single value, so the intercepts will be part of the
        weights.)
    numFeatures : int
        The dimension of the features.
    numClasses : int
        The number of possible outcomes for k classes classification problem
        in Multinomial Logistic Regression. By default, it is binary
        logistic regression so numClasses will be set to 2.

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> data = [
    ...     LabeledPoint(0.0, [0.0, 1.0]),
    ...     LabeledPoint(1.0, [1.0, 0.0]),
    ... ]
    >>> lrm = LogisticRegressionWithSGD.train(sc.parallelize(data), iterations=10)
    >>> lrm.predict([1.0, 0.0])
    1
    >>> lrm.predict([0.0, 1.0])
    0
    >>> lrm.predict(sc.parallelize([[1.0, 0.0], [0.0, 1.0]])).collect()
    [1, 0]
    >>> lrm.clearThreshold()
    >>> lrm.predict([0.0, 1.0])
    0.279...

    >>> sparse_data = [
    ...     LabeledPoint(0.0, SparseVector(2, {0: 0.0})),
    ...     LabeledPoint(1.0, SparseVector(2, {1: 1.0})),
    ...     LabeledPoint(0.0, SparseVector(2, {0: 1.0})),
    ...     LabeledPoint(1.0, SparseVector(2, {1: 2.0}))
    ... ]
    >>> lrm = LogisticRegressionWithSGD.train(sc.parallelize(sparse_data), iterations=10)
    >>> lrm.predict(numpy.array([0.0, 1.0]))
    1
    >>> lrm.predict(numpy.array([1.0, 0.0]))
    0
    >>> lrm.predict(SparseVector(2, {1: 1.0}))
    1
    >>> lrm.predict(SparseVector(2, {0: 1.0}))
    0
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> lrm.save(sc, path)
    >>> sameModel = LogisticRegressionModel.load(sc, path)
    >>> sameModel.predict(numpy.array([0.0, 1.0]))
    1
    >>> sameModel.predict(SparseVector(2, {0: 1.0}))
    0
    >>> from shutil import rmtree
    >>> try:
    ...    rmtree(path)
    ... except BaseException:
    ...    pass
    >>> multi_class_data = [
    ...     LabeledPoint(0.0, [0.0, 1.0, 0.0]),
    ...     LabeledPoint(1.0, [1.0, 0.0, 0.0]),
    ...     LabeledPoint(2.0, [0.0, 0.0, 1.0])
    ... ]
    >>> data = sc.parallelize(multi_class_data)
    >>> mcm = LogisticRegressionWithLBFGS.train(data, iterations=10, numClasses=3)
    >>> mcm.predict([0.0, 0.5, 0.0])
    0
    >>> mcm.predict([0.8, 0.0, 0.0])
    1
    >>> mcm.predict([0.0, 0.0, 0.3])
    2
    """
    def __init__(self, weights: Vector, intercept: float, numFeatures: int, numClasses: int) -> None: ...
    @property
    def numFeatures(self) -> int:
        """
        Dimension of the features.
        """
    @property
    def numClasses(self) -> int:
        """
        Number of possible outcomes for k classes classification problem
        in Multinomial Logistic Regression.
        """
    @overload
    def predict(self, x: VectorLike) -> int | float: ...
    @overload
    def predict(self, x: RDD['VectorLike']) -> RDD[int | float]: ...
    def save(self, sc: SparkContext, path: str) -> None:
        """
        Save this model to the given path.
        """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LogisticRegressionModel:
        """
        Load a model from the given path.
        """

class LogisticRegressionWithSGD:
    """
    Train a classification model for Binary Logistic Regression using Stochastic Gradient Descent.

    .. versionadded:: 0.9.0
    .. deprecated:: 2.0.0
        Use ml.classification.LogisticRegression or LogisticRegressionWithLBFGS.
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, step: float = 1.0, miniBatchFraction: float = 1.0, initialWeights: VectorLike | None = None, regParam: float = 0.01, regType: str = 'l2', intercept: bool = False, validateData: bool = True, convergenceTol: float = 0.001) -> LogisticRegressionModel:
        '''
        Train a logistic regression model on the given data.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of :py:class:`pyspark.mllib.regression.LabeledPoint`.
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
            (default: 0.01)
        regType : str, optional
            The type of regularizer used for training our model.
            Supported values:

            - "l1" for using L1 regularization
            - "l2" for using L2 regularization (default)
            - None for no regularization

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

class LogisticRegressionWithLBFGS:
    """
    Train a classification model for Multinomial/Binary Logistic Regression
    using Limited-memory BFGS.

    Standard feature scaling and L2 regularization are used by default.
    .. versionadded:: 1.2.0
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, initialWeights: VectorLike | None = None, regParam: float = 0.0, regType: str = 'l2', intercept: bool = False, corrections: int = 10, tolerance: float = 1e-06, validateData: bool = True, numClasses: int = 2) -> LogisticRegressionModel:
        '''
        Train a logistic regression model on the given data.

        .. versionadded:: 1.2.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of :py:class:`pyspark.mllib.regression.LabeledPoint`.
        iterations : int, optional
            The number of iterations.
            (default: 100)
        initialWeights : :py:class:`pyspark.mllib.linalg.Vector` or convertible, optional
            The initial weights.
            (default: None)
        regParam : float, optional
            The regularizer parameter.
            (default: 0.01)
        regType : str, optional
            The type of regularizer used for training our model.
            Supported values:

            - "l1" for using L1 regularization
            - "l2" for using L2 regularization (default)
            - None for no regularization

        intercept : bool, optional
            Boolean parameter which indicates the use or not of the
            augmented representation for training data (i.e., whether bias
            features are activated or not).
            (default: False)
        corrections : int, optional
            The number of corrections used in the LBFGS update.
            If a known updater is used for binary classification,
            it calls the ml implementation and this parameter will
            have no effect. (default: 10)
        tolerance : float, optional
            The convergence tolerance of iterations for L-BFGS.
            (default: 1e-6)
        validateData : bool, optional
            Boolean parameter which indicates if the algorithm should
            validate data before training.
            (default: True)
        numClasses : int, optional
            The number of classes (i.e., outcomes) a label can take in
            Multinomial Logistic Regression.
            (default: 2)

        Examples
        --------
        >>> data = [
        ...     LabeledPoint(0.0, [0.0, 1.0]),
        ...     LabeledPoint(1.0, [1.0, 0.0]),
        ... ]
        >>> lrm = LogisticRegressionWithLBFGS.train(sc.parallelize(data), iterations=10)
        >>> lrm.predict([1.0, 0.0])
        1
        >>> lrm.predict([0.0, 1.0])
        0
        '''

class SVMModel(LinearClassificationModel):
    """
    Model for Support Vector Machines (SVMs).

    .. versionadded:: 0.9.0

    Parameters
    ----------
    weights : :py:class:`pyspark.mllib.linalg.Vector`
        Weights computed for every feature.
    intercept : float
        Intercept computed for this model.

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> data = [
    ...     LabeledPoint(0.0, [0.0]),
    ...     LabeledPoint(1.0, [1.0]),
    ...     LabeledPoint(1.0, [2.0]),
    ...     LabeledPoint(1.0, [3.0])
    ... ]
    >>> svm = SVMWithSGD.train(sc.parallelize(data), iterations=10)
    >>> svm.predict([1.0])
    1
    >>> svm.predict(sc.parallelize([[1.0]])).collect()
    [1]
    >>> svm.clearThreshold()
    >>> svm.predict(numpy.array([1.0]))
    1.44...

    >>> sparse_data = [
    ...     LabeledPoint(0.0, SparseVector(2, {0: -1.0})),
    ...     LabeledPoint(1.0, SparseVector(2, {1: 1.0})),
    ...     LabeledPoint(0.0, SparseVector(2, {0: 0.0})),
    ...     LabeledPoint(1.0, SparseVector(2, {1: 2.0}))
    ... ]
    >>> svm = SVMWithSGD.train(sc.parallelize(sparse_data), iterations=10)
    >>> svm.predict(SparseVector(2, {1: 1.0}))
    1
    >>> svm.predict(SparseVector(2, {0: -1.0}))
    0
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> svm.save(sc, path)
    >>> sameModel = SVMModel.load(sc, path)
    >>> sameModel.predict(SparseVector(2, {1: 1.0}))
    1
    >>> sameModel.predict(SparseVector(2, {0: -1.0}))
    0
    >>> from shutil import rmtree
    >>> try:
    ...    rmtree(path)
    ... except BaseException:
    ...    pass
    """
    def __init__(self, weights: Vector, intercept: float) -> None: ...
    @overload
    def predict(self, x: VectorLike) -> int | float: ...
    @overload
    def predict(self, x: RDD['VectorLike']) -> RDD[int | float]: ...
    def save(self, sc: SparkContext, path: str) -> None:
        """
        Save this model to the given path.
        """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> SVMModel:
        """
        Load a model from the given path.
        """

class SVMWithSGD:
    """
    Train a Support Vector Machine (SVM) using Stochastic Gradient Descent.

    .. versionadded:: 0.9.0
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], iterations: int = 100, step: float = 1.0, regParam: float = 0.01, miniBatchFraction: float = 1.0, initialWeights: VectorLike | None = None, regType: str = 'l2', intercept: bool = False, validateData: bool = True, convergenceTol: float = 0.001) -> SVMModel:
        '''
        Train a support vector machine on the given data.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of :py:class:`pyspark.mllib.regression.LabeledPoint`.
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
        regType : str, optional
            The type of regularizer used for training our model.
            Allowed values:

            - "l1" for using L1 regularization
            - "l2" for using L2 regularization (default)
            - None for no regularization

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
        '''

class NaiveBayesModel(Saveable, Loader['NaiveBayesModel']):
    """
    Model for Naive Bayes classifiers.

    .. versionadded:: 0.9.0

    Parameters
    ----------
    labels : :py:class:`numpy.ndarray`
        List of labels.
    pi : :py:class:`numpy.ndarray`
        Log of class priors, whose dimension is C, number of labels.
    theta : :py:class:`numpy.ndarray`
        Log of class conditional probabilities, whose dimension is C-by-D,
        where D is number of features.

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector
    >>> data = [
    ...     LabeledPoint(0.0, [0.0, 0.0]),
    ...     LabeledPoint(0.0, [0.0, 1.0]),
    ...     LabeledPoint(1.0, [1.0, 0.0]),
    ... ]
    >>> model = NaiveBayes.train(sc.parallelize(data))
    >>> model.predict(numpy.array([0.0, 1.0]))
    0.0
    >>> model.predict(numpy.array([1.0, 0.0]))
    1.0
    >>> model.predict(sc.parallelize([[1.0, 0.0]])).collect()
    [1.0]
    >>> sparse_data = [
    ...     LabeledPoint(0.0, SparseVector(2, {1: 0.0})),
    ...     LabeledPoint(0.0, SparseVector(2, {1: 1.0})),
    ...     LabeledPoint(1.0, SparseVector(2, {0: 1.0}))
    ... ]
    >>> model = NaiveBayes.train(sc.parallelize(sparse_data))
    >>> model.predict(SparseVector(2, {1: 1.0}))
    0.0
    >>> model.predict(SparseVector(2, {0: 1.0}))
    1.0
    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> model.save(sc, path)
    >>> sameModel = NaiveBayesModel.load(sc, path)
    >>> sameModel.predict(SparseVector(2, {0: 1.0})) == model.predict(SparseVector(2, {0: 1.0}))
    True
    >>> from shutil import rmtree
    >>> try:
    ...     rmtree(path)
    ... except OSError:
    ...     pass
    """
    labels: Incomplete
    pi: Incomplete
    theta: Incomplete
    def __init__(self, labels: numpy.ndarray, pi: numpy.ndarray, theta: numpy.ndarray) -> None: ...
    @overload
    def predict(self, x: VectorLike) -> numpy.float64: ...
    @overload
    def predict(self, x: RDD['VectorLike']) -> RDD[numpy.float64]: ...
    def save(self, sc: SparkContext, path: str) -> None:
        """
        Save this model to the given path.
        """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> NaiveBayesModel:
        """
        Load a model from the given path.
        """

class NaiveBayes:
    """
    Train a Multinomial Naive Bayes model.

    .. versionadded:: 0.9.0
    """
    @classmethod
    def train(cls, data: RDD[LabeledPoint], lambda_: float = 1.0) -> NaiveBayesModel:
        """
        Train a Naive Bayes model given an RDD of (label, features)
        vectors.

        This is the `Multinomial NB <http://tinyurl.com/lsdw6p>`_ which
        can handle all kinds of discrete data.  For example, by
        converting documents into TF-IDF vectors, it can be used for
        document classification. By making every vector a 0-1 vector,
        it can also be used as `Bernoulli NB <http://tinyurl.com/p7c96j6>`_.
        The input feature values must be nonnegative.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            The training data, an RDD of :py:class:`pyspark.mllib.regression.LabeledPoint`.
        lambda\\_ : float, optional
            The smoothing parameter.
            (default: 1.0)
        """

class StreamingLogisticRegressionWithSGD(StreamingLinearAlgorithm):
    """
    Train or predict a logistic regression model on streaming data.
    Training uses Stochastic Gradient Descent to update the model based on
    each new batch of incoming data from a DStream.

    Each batch of data is assumed to be an RDD of LabeledPoints.
    The number of data points per batch can vary, but the number
    of features must be constant. An initial weight
    vector must be provided.

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
    regParam : float, optional
        L2 Regularization parameter.
        (default: 0.0)
    convergenceTol : float, optional
        Value used to determine when to terminate iterations.
        (default: 0.001)
    """
    stepSize: Incomplete
    numIterations: Incomplete
    regParam: Incomplete
    miniBatchFraction: Incomplete
    convergenceTol: Incomplete
    def __init__(self, stepSize: float = 0.1, numIterations: int = 50, miniBatchFraction: float = 1.0, regParam: float = 0.0, convergenceTol: float = 0.001) -> None: ...
    def setInitialWeights(self, initialWeights: VectorLike) -> StreamingLogisticRegressionWithSGD:
        """
        Set the initial value of weights.

        This must be set before running trainOn and predictOn.
        """
    def trainOn(self, dstream: DStream[LabeledPoint]) -> None:
        """Train the model on the incoming dstream."""
