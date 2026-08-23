from numpy import ndarray
from pyspark.mllib._typing import CorrMethodType, KolmogorovSmirnovTestDistNameType
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Matrix, Vector
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.stat.test import ChiSqTestResult, KolmogorovSmirnovTestResult
from pyspark.rdd import RDD
from typing import List, overload

__all__ = ['MultivariateStatisticalSummary', 'Statistics']

class MultivariateStatisticalSummary(JavaModelWrapper):
    """
    Trait for multivariate statistical summary of a data matrix.
    """
    def mean(self) -> ndarray: ...
    def variance(self) -> ndarray: ...
    def count(self) -> int: ...
    def numNonzeros(self) -> ndarray: ...
    def max(self) -> ndarray: ...
    def min(self) -> ndarray: ...
    def normL1(self) -> ndarray: ...
    def normL2(self) -> ndarray: ...

class Statistics:
    @staticmethod
    def colStats(rdd: RDD[Vector]) -> MultivariateStatisticalSummary:
        """
        Computes column-wise summary statistics for the input RDD[Vector].

        Parameters
        ----------
        rdd : :py:class:`pyspark.RDD`
            an RDD[Vector] for which column-wise summary statistics
            are to be computed.

        Returns
        -------
        :class:`MultivariateStatisticalSummary`
            object containing column-wise summary statistics.

        Examples
        --------
        >>> from pyspark.mllib.linalg import Vectors
        >>> rdd = sc.parallelize([Vectors.dense([2, 0, 0, -2]),
        ...                       Vectors.dense([4, 5, 0,  3]),
        ...                       Vectors.dense([6, 7, 0,  8])])
        >>> cStats = Statistics.colStats(rdd)
        >>> cStats.mean()
        array([ 4.,  4.,  0.,  3.])
        >>> cStats.variance()
        array([  4.,  13.,   0.,  25.])
        >>> cStats.count()
        3
        >>> cStats.numNonzeros()
        array([ 3.,  2.,  0.,  3.])
        >>> cStats.max()
        array([ 6.,  7.,  0.,  8.])
        >>> cStats.min()
        array([ 2.,  0.,  0., -2.])
        """
    @overload
    @staticmethod
    def corr(x: RDD[Vector], *, method: CorrMethodType | None = ...) -> Matrix: ...
    @overload
    @staticmethod
    def corr(x: RDD[float], y: RDD[float], method: CorrMethodType | None = ...) -> float: ...
    @overload
    @staticmethod
    def chiSqTest(observed: Matrix) -> ChiSqTestResult: ...
    @overload
    @staticmethod
    def chiSqTest(observed: Vector, expected: Vector | None = ...) -> ChiSqTestResult: ...
    @overload
    @staticmethod
    def chiSqTest(observed: RDD[LabeledPoint]) -> List[ChiSqTestResult]: ...
    @staticmethod
    def kolmogorovSmirnovTest(data: RDD[float], distName: KolmogorovSmirnovTestDistNameType = 'norm', *params: float) -> KolmogorovSmirnovTestResult:
        '''
        Performs the Kolmogorov-Smirnov (KS) test for data sampled from
        a continuous distribution. It tests the null hypothesis that
        the data is generated from a particular distribution.

        The given data is sorted and the Empirical Cumulative
        Distribution Function (ECDF) is calculated
        which for a given point is the number of points having a CDF
        value lesser than it divided by the total number of points.

        Since the data is sorted, this is a step function
        that rises by (1 / length of data) for every ordered point.

        The KS statistic gives us the maximum distance between the
        ECDF and the CDF. Intuitively if this statistic is large, the
        probability that the null hypothesis is true becomes small.
        For specific details of the implementation, please have a look
        at the Scala documentation.


        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            RDD, samples from the data
        distName : str, optional
            string, currently only "norm" is supported.
            (Normal distribution) to calculate the
            theoretical distribution of the data.
        params
            additional values which need to be provided for
            a certain distribution.
            If not provided, the default values are used.

        Returns
        -------
        :py:class:`pyspark.mllib.stat.KolmogorovSmirnovTestResult`
            object containing the test statistic, degrees of freedom, p-value,
            the method used, and the null hypothesis.

        Examples
        --------
        >>> kstest = Statistics.kolmogorovSmirnovTest
        >>> data = sc.parallelize([-1.0, 0.0, 1.0])
        >>> ksmodel = kstest(data, "norm")
        >>> print(round(ksmodel.pValue, 3))
        1.0
        >>> print(round(ksmodel.statistic, 3))
        0.175
        >>> ksmodel.nullHypothesis
        \'Sample follows theoretical distribution\'

        >>> data = sc.parallelize([2.0, 3.0, 4.0])
        >>> ksmodel = kstest(data, "norm", 3.0, 1.0)
        >>> print(round(ksmodel.pValue, 3))
        1.0
        >>> print(round(ksmodel.statistic, 3))
        0.175
        '''
