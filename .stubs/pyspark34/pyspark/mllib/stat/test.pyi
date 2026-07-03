from pyspark.mllib.common import JavaModelWrapper
from typing import Generic, Tuple, TypeVar

__all__ = ['ChiSqTestResult', 'KolmogorovSmirnovTestResult']

DF = TypeVar('DF', int, float, Tuple[int, ...], Tuple[float, ...])

class TestResult(JavaModelWrapper, Generic[DF]):
    """
    Base class for all test results.
    """
    @property
    def pValue(self) -> float:
        """
        The probability of obtaining a test statistic result at least as
        extreme as the one that was actually observed, assuming that the
        null hypothesis is true.
        """
    @property
    def degreesOfFreedom(self) -> DF:
        """
        Returns the degree(s) of freedom of the hypothesis test.
        Return type should be Number(e.g. Int, Double) or tuples of Numbers.
        """
    @property
    def statistic(self) -> float:
        """
        Test statistic.
        """
    @property
    def nullHypothesis(self) -> str:
        """
        Null hypothesis of the test.
        """

class ChiSqTestResult(TestResult[int]):
    """
    Contains test results for the chi-squared hypothesis test.
    """
    @property
    def method(self) -> str:
        """
        Name of the test method
        """

class KolmogorovSmirnovTestResult(TestResult[int]):
    """
    Contains test results for the Kolmogorov-Smirnov test.
    """
