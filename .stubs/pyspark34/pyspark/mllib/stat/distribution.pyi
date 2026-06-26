from pyspark.mllib.linalg import Matrix, Vector
from typing import NamedTuple

__all__ = ['MultivariateGaussian']

class MultivariateGaussian(NamedTuple):
    """Represents a (mu, sigma) tuple

    Examples
    --------
    >>> m = MultivariateGaussian(Vectors.dense([11,12]),DenseMatrix(2, 2, (1.0, 3.0, 5.0, 2.0)))
    >>> (m.mu, m.sigma.toArray())
    (DenseVector([11.0, 12.0]), array([[ 1., 5.],[ 3., 2.]]))
    >>> (m[0], m[1])
    (DenseVector([11.0, 12.0]), array([[ 1., 5.],[ 3., 2.]]))
    """
    mu: Vector
    sigma: Matrix
