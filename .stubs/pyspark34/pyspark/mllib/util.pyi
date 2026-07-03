from py4j.java_gateway import JavaObject as JavaObject
from pyspark import since as since
from pyspark.context import SparkContext as SparkContext
from pyspark.mllib._typing import VectorLike as VectorLike
from pyspark.mllib.common import callMLlibFunc as callMLlibFunc, inherit_doc as inherit_doc
from pyspark.mllib.linalg import SparseVector as SparseVector, Vector as Vector, Vectors as Vectors
from pyspark.mllib.regression import LabeledPoint as LabeledPoint
from pyspark.rdd import RDD as RDD
from pyspark.sql.dataframe import DataFrame as DataFrame
from typing import Generic, List, TypeVar

T = TypeVar('T')
L = TypeVar('L', bound='Loader')
JL = TypeVar('JL', bound='JavaLoader')

class MLUtils:
    """
    Helper methods to load, save and pre-process data used in MLlib.

    .. versionadded:: 1.0.0
    """
    @staticmethod
    def loadLibSVMFile(sc: SparkContext, path: str, numFeatures: int = -1, minPartitions: int | None = None) -> RDD['LabeledPoint']:
        '''
        Loads labeled data in the LIBSVM format into an RDD of
        LabeledPoint. The LIBSVM format is a text-based format used by
        LIBSVM and LIBLINEAR. Each line represents a labeled sparse
        feature vector using the following format:

        label index1:value1 index2:value2 ...

        where the indices are one-based and in ascending order. This
        method parses each line into a LabeledPoint, where the feature
        indices are converted to zero-based.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        sc : :py:class:`pyspark.SparkContext`
            Spark context
        path : str
            file or directory path in any Hadoop-supported file system URI
        numFeatures : int, optional
            number of features, which will be determined
            from the input data if a nonpositive value
            is given. This is useful when the dataset is
            already split into multiple files and you
            want to load them separately, because some
            features may not present in certain files,
            which leads to inconsistent feature
            dimensions.
        minPartitions : int, optional
            min number of partitions

        Returns
        -------
        :py:class:`pyspark.RDD`
            labeled data stored as an RDD of LabeledPoint

        Examples
        --------
        >>> from tempfile import NamedTemporaryFile
        >>> from pyspark.mllib.util import MLUtils
        >>> from pyspark.mllib.regression import LabeledPoint
        >>> tempFile = NamedTemporaryFile(delete=True)
        >>> _ = tempFile.write(b"+1 1:1.0 3:2.0 5:3.0\\n-1\\n-1 2:4.0 4:5.0 6:6.0")
        >>> tempFile.flush()
        >>> examples = MLUtils.loadLibSVMFile(sc, tempFile.name).collect()
        >>> tempFile.close()
        >>> examples[0]
        LabeledPoint(1.0, (6,[0,2,4],[1.0,2.0,3.0]))
        >>> examples[1]
        LabeledPoint(-1.0, (6,[],[]))
        >>> examples[2]
        LabeledPoint(-1.0, (6,[1,3,5],[4.0,5.0,6.0]))
        '''
    @staticmethod
    def saveAsLibSVMFile(data: RDD['LabeledPoint'], dir: str) -> None:
        '''
        Save labeled data in LIBSVM format.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            an RDD of LabeledPoint to be saved
        dir : str
            directory to save the data

        Examples
        --------
        >>> from tempfile import NamedTemporaryFile
        >>> from fileinput import input
        >>> from pyspark.mllib.regression import LabeledPoint
        >>> from glob import glob
        >>> from pyspark.mllib.util import MLUtils
        >>> examples = [LabeledPoint(1.1, Vectors.sparse(3, [(0, 1.23), (2, 4.56)])),
        ...             LabeledPoint(0.0, Vectors.dense([1.01, 2.02, 3.03]))]
        >>> tempFile = NamedTemporaryFile(delete=True)
        >>> tempFile.close()
        >>> MLUtils.saveAsLibSVMFile(sc.parallelize(examples), tempFile.name)
        >>> \'\'.join(sorted(input(glob(tempFile.name + "/part-0000*"))))
        \'0.0 1:1.01 2:2.02 3:3.03\\n1.1 1:1.23 3:4.56\\n\'
        '''
    @staticmethod
    def loadLabeledPoints(sc: SparkContext, path: str, minPartitions: int | None = None) -> RDD['LabeledPoint']:
        """
        Load labeled points saved using RDD.saveAsTextFile.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        sc : :py:class:`pyspark.SparkContext`
            Spark context
        path : str
            file or directory path in any Hadoop-supported file system URI
        minPartitions : int, optional
            min number of partitions

        Returns
        -------
        :py:class:`pyspark.RDD`
            labeled data stored as an RDD of LabeledPoint

        Examples
        --------
        >>> from tempfile import NamedTemporaryFile
        >>> from pyspark.mllib.util import MLUtils
        >>> from pyspark.mllib.regression import LabeledPoint
        >>> examples = [LabeledPoint(1.1, Vectors.sparse(3, [(0, -1.23), (2, 4.56e-7)])),
        ...             LabeledPoint(0.0, Vectors.dense([1.01, 2.02, 3.03]))]
        >>> tempFile = NamedTemporaryFile(delete=True)
        >>> tempFile.close()
        >>> sc.parallelize(examples, 1).saveAsTextFile(tempFile.name)
        >>> MLUtils.loadLabeledPoints(sc, tempFile.name).collect()
        [LabeledPoint(1.1, (3,[0,2],[-1.23,4.56e-07])), LabeledPoint(0.0, [1.01,2.02,3.03])]
        """
    @staticmethod
    def appendBias(data: Vector) -> Vector:
        """
        Returns a new vector with `1.0` (bias) appended to
        the end of the input vector.
        """
    @staticmethod
    def loadVectors(sc: SparkContext, path: str) -> RDD[Vector]:
        """
        Loads vectors saved using `RDD[Vector].saveAsTextFile`
        with the default number of partitions.
        """
    @staticmethod
    def convertVectorColumnsToML(dataset: DataFrame, *cols: str) -> DataFrame:
        '''
        Converts vector columns in an input DataFrame from the
        :py:class:`pyspark.mllib.linalg.Vector` type to the new
        :py:class:`pyspark.ml.linalg.Vector` type under the `spark.ml`
        package.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset
        \\*cols : str
            Vector columns to be converted.

            New vector columns will be ignored. If unspecified, all old
            vector columns will be converted excepted nested ones.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            the input dataset with old vector columns converted to the
            new vector type

        Examples
        --------
        >>> import pyspark
        >>> from pyspark.mllib.linalg import Vectors
        >>> from pyspark.mllib.util import MLUtils
        >>> df = spark.createDataFrame(
        ...     [(0, Vectors.sparse(2, [1], [1.0]), Vectors.dense(2.0, 3.0))],
        ...     ["id", "x", "y"])
        >>> r1 = MLUtils.convertVectorColumnsToML(df).first()
        >>> isinstance(r1.x, pyspark.ml.linalg.SparseVector)
        True
        >>> isinstance(r1.y, pyspark.ml.linalg.DenseVector)
        True
        >>> r2 = MLUtils.convertVectorColumnsToML(df, "x").first()
        >>> isinstance(r2.x, pyspark.ml.linalg.SparseVector)
        True
        >>> isinstance(r2.y, pyspark.mllib.linalg.DenseVector)
        True
        '''
    @staticmethod
    def convertVectorColumnsFromML(dataset: DataFrame, *cols: str) -> DataFrame:
        '''
        Converts vector columns in an input DataFrame to the
        :py:class:`pyspark.mllib.linalg.Vector` type from the new
        :py:class:`pyspark.ml.linalg.Vector` type under the `spark.ml`
        package.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset
        \\*cols : str
            Vector columns to be converted.

            Old vector columns will be ignored. If unspecified, all new
            vector columns will be converted except nested ones.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            the input dataset with new vector columns converted to the
            old vector type

        Examples
        --------
        >>> import pyspark
        >>> from pyspark.ml.linalg import Vectors
        >>> from pyspark.mllib.util import MLUtils
        >>> df = spark.createDataFrame(
        ...     [(0, Vectors.sparse(2, [1], [1.0]), Vectors.dense(2.0, 3.0))],
        ...     ["id", "x", "y"])
        >>> r1 = MLUtils.convertVectorColumnsFromML(df).first()
        >>> isinstance(r1.x, pyspark.mllib.linalg.SparseVector)
        True
        >>> isinstance(r1.y, pyspark.mllib.linalg.DenseVector)
        True
        >>> r2 = MLUtils.convertVectorColumnsFromML(df, "x").first()
        >>> isinstance(r2.x, pyspark.mllib.linalg.SparseVector)
        True
        >>> isinstance(r2.y, pyspark.ml.linalg.DenseVector)
        True
        '''
    @staticmethod
    def convertMatrixColumnsToML(dataset: DataFrame, *cols: str) -> DataFrame:
        '''
        Converts matrix columns in an input DataFrame from the
        :py:class:`pyspark.mllib.linalg.Matrix` type to the new
        :py:class:`pyspark.ml.linalg.Matrix` type under the `spark.ml`
        package.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset
        \\*cols : str
            Matrix columns to be converted.

            New matrix columns will be ignored. If unspecified, all old
            matrix columns will be converted excepted nested ones.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            the input dataset with old matrix columns converted to the
            new matrix type

        Examples
        --------
        >>> import pyspark
        >>> from pyspark.mllib.linalg import Matrices
        >>> from pyspark.mllib.util import MLUtils
        >>> df = spark.createDataFrame(
        ...     [(0, Matrices.sparse(2, 2, [0, 2, 3], [0, 1, 1], [2, 3, 4]),
        ...     Matrices.dense(2, 2, range(4)))], ["id", "x", "y"])
        >>> r1 = MLUtils.convertMatrixColumnsToML(df).first()
        >>> isinstance(r1.x, pyspark.ml.linalg.SparseMatrix)
        True
        >>> isinstance(r1.y, pyspark.ml.linalg.DenseMatrix)
        True
        >>> r2 = MLUtils.convertMatrixColumnsToML(df, "x").first()
        >>> isinstance(r2.x, pyspark.ml.linalg.SparseMatrix)
        True
        >>> isinstance(r2.y, pyspark.mllib.linalg.DenseMatrix)
        True
        '''
    @staticmethod
    def convertMatrixColumnsFromML(dataset: DataFrame, *cols: str) -> DataFrame:
        '''
        Converts matrix columns in an input DataFrame to the
        :py:class:`pyspark.mllib.linalg.Matrix` type from the new
        :py:class:`pyspark.ml.linalg.Matrix` type under the `spark.ml`
        package.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset
        \\*cols : str
            Matrix columns to be converted.

            Old matrix columns will be ignored. If unspecified, all new
            matrix columns will be converted except nested ones.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            the input dataset with new matrix columns converted to the
            old matrix type

        Examples
        --------
        >>> import pyspark
        >>> from pyspark.ml.linalg import Matrices
        >>> from pyspark.mllib.util import MLUtils
        >>> df = spark.createDataFrame(
        ...     [(0, Matrices.sparse(2, 2, [0, 2, 3], [0, 1, 1], [2, 3, 4]),
        ...     Matrices.dense(2, 2, range(4)))], ["id", "x", "y"])
        >>> r1 = MLUtils.convertMatrixColumnsFromML(df).first()
        >>> isinstance(r1.x, pyspark.mllib.linalg.SparseMatrix)
        True
        >>> isinstance(r1.y, pyspark.mllib.linalg.DenseMatrix)
        True
        >>> r2 = MLUtils.convertMatrixColumnsFromML(df, "x").first()
        >>> isinstance(r2.x, pyspark.mllib.linalg.SparseMatrix)
        True
        >>> isinstance(r2.y, pyspark.ml.linalg.DenseMatrix)
        True
        '''

class Saveable:
    """
    Mixin for models and transformers which may be saved as files.

    .. versionadded:: 1.3.0
    """
    def save(self, sc: SparkContext, path: str) -> None:
        """
        Save this model to the given path.

        This saves:
         * human-readable (JSON) model metadata to path/metadata/
         * Parquet formatted data to path/data/

        The model may be loaded using :py:meth:`Loader.load`.

        Parameters
        ----------
        sc : :py:class:`pyspark.SparkContext`
            Spark context used to save model data.
        path : str
            Path specifying the directory in which to save
            this model. If the directory already exists,
            this method throws an exception.
        """

class JavaSaveable(Saveable):
    """
    Mixin for models that provide save() through their Scala
    implementation.

    .. versionadded:: 1.3.0
    """
    def save(self, sc: SparkContext, path: str) -> None:
        """Save this model to the given path."""

class Loader(Generic[T]):
    """
    Mixin for classes which can load saved models from files.

    .. versionadded:: 1.3.0
    """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> L:
        """
        Load a model from the given path. The model should have been
        saved using :py:meth:`Saveable.save`.

        Parameters
        ----------
        sc : :py:class:`pyspark.SparkContext`
            Spark context used for loading model files.
        path : str
            Path specifying the directory to which the model was saved.

        Returns
        -------
        object
            model instance
        """

class JavaLoader(Loader[T]):
    """
    Mixin for classes which can load saved models using its Scala
    implementation.

    .. versionadded:: 1.3.0
    """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> JL:
        """Load a model from the given path."""

class LinearDataGenerator:
    """Utils for generating linear data.

    .. versionadded:: 1.5.0
    """
    @staticmethod
    def generateLinearInput(intercept: float, weights: VectorLike, xMean: VectorLike, xVariance: VectorLike, nPoints: int, seed: int, eps: float) -> List['LabeledPoint']:
        """
        .. versionadded:: 1.5.0

        Parameters
        ----------
        intercept : float
            bias factor, the term c in X'w + c
        weights : :py:class:`pyspark.mllib.linalg.Vector` or convertible
            feature vector, the term w in X'w + c
        xMean : :py:class:`pyspark.mllib.linalg.Vector` or convertible
            Point around which the data X is centered.
        xVariance : :py:class:`pyspark.mllib.linalg.Vector` or convertible
            Variance of the given data
        nPoints : int
            Number of points to be generated
        seed : int
            Random Seed
        eps : float
            Used to scale the noise. If eps is set high,
            the amount of gaussian noise added is more.

        Returns
        -------
        list
            of :py:class:`pyspark.mllib.regression.LabeledPoints` of length nPoints
        """
    @staticmethod
    def generateLinearRDD(sc: SparkContext, nexamples: int, nfeatures: int, eps: float, nParts: int = 2, intercept: float = 0.0) -> RDD['LabeledPoint']:
        """
        Generate an RDD of LabeledPoints.
        """
