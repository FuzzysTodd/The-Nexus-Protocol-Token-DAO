from numpy import ndarray
from pyspark.mllib.common import callMLlibFunc as callMLlibFunc
from pyspark.rdd import RDD as RDD
from typing import Iterable

class KernelDensity:
    """
    Estimate probability density at required points given an RDD of samples
    from the population.

    Examples
    --------
    >>> kd = KernelDensity()
    >>> sample = sc.parallelize([0.0, 1.0])
    >>> kd.setSample(sample)
    >>> kd.estimate([0.0, 1.0])
    array([ 0.12938758,  0.12938758])
    """
    def __init__(self) -> None: ...
    def setBandwidth(self, bandwidth: float) -> None:
        """Set bandwidth of each sample. Defaults to 1.0"""
    def setSample(self, sample: RDD[float]) -> None:
        """Set sample points from the population. Should be a RDD"""
    def estimate(self, points: Iterable[float]) -> ndarray:
        """Estimate the probability density at points"""
