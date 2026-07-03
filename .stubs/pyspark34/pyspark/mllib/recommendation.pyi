import array
from pyspark import SparkContext
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.util import JavaLoader, JavaSaveable
from pyspark.rdd import RDD
from typing import List, NamedTuple, Tuple, Type

__all__ = ['MatrixFactorizationModel', 'ALS', 'Rating']

class Rating(NamedTuple):
    """
    Represents a (user, product, rating) tuple.

    .. versionadded:: 1.2.0

    Examples
    --------
    >>> r = Rating(1, 2, 5.0)
    >>> (r.user, r.product, r.rating)
    (1, 2, 5.0)
    >>> (r[0], r[1], r[2])
    (1, 2, 5.0)
    """
    user: int
    product: int
    rating: float
    def __reduce__(self) -> Tuple[Type['Rating'], Tuple[int, int, float]]: ...

class MatrixFactorizationModel(JavaModelWrapper, JavaSaveable, JavaLoader['MatrixFactorizationModel']):
    """A matrix factorisation model trained by regularized alternating
    least-squares.

    .. versionadded:: 0.9.0

    Examples
    --------
    >>> r1 = (1, 1, 1.0)
    >>> r2 = (1, 2, 2.0)
    >>> r3 = (2, 1, 2.0)
    >>> ratings = sc.parallelize([r1, r2, r3])
    >>> model = ALS.trainImplicit(ratings, 1, seed=10)
    >>> model.predict(2, 2)
    0.4...

    >>> testset = sc.parallelize([(1, 2), (1, 1)])
    >>> model = ALS.train(ratings, 2, seed=0)
    >>> model.predictAll(testset).collect()
    [Rating(user=1, product=1, rating=1.0...), Rating(user=1, product=2, rating=1.9...)]

    >>> model = ALS.train(ratings, 4, seed=10)
    >>> model.userFeatures().collect()
    [(1, array('d', [...])), (2, array('d', [...]))]

    >>> model.recommendUsers(1, 2)
    [Rating(user=2, product=1, rating=1.9...), Rating(user=1, product=1, rating=1.0...)]
    >>> model.recommendProducts(1, 2)
    [Rating(user=1, product=2, rating=1.9...), Rating(user=1, product=1, rating=1.0...)]
    >>> model.rank
    4

    >>> first_user = model.userFeatures().take(1)[0]
    >>> latents = first_user[1]
    >>> len(latents)
    4

    >>> model.productFeatures().collect()
    [(1, array('d', [...])), (2, array('d', [...]))]

    >>> first_product = model.productFeatures().take(1)[0]
    >>> latents = first_product[1]
    >>> len(latents)
    4

    >>> products_for_users = model.recommendProductsForUsers(1).collect()
    >>> len(products_for_users)
    2
    >>> products_for_users[0]
    (1, (Rating(user=1, product=2, rating=...),))

    >>> users_for_products = model.recommendUsersForProducts(1).collect()
    >>> len(users_for_products)
    2
    >>> users_for_products[0]
    (1, (Rating(user=2, product=1, rating=...),))

    >>> model = ALS.train(ratings, 1, nonnegative=True, seed=123456789)
    >>> model.predict(2, 2)
    3.73...

    >>> df = sqlContext.createDataFrame([Rating(1, 1, 1.0), Rating(1, 2, 2.0), Rating(2, 1, 2.0)])
    >>> model = ALS.train(df, 1, nonnegative=True, seed=123456789)
    >>> model.predict(2, 2)
    3.73...

    >>> model = ALS.trainImplicit(ratings, 1, nonnegative=True, seed=123456789)
    >>> model.predict(2, 2)
    0.4...

    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> model.save(sc, path)
    >>> sameModel = MatrixFactorizationModel.load(sc, path)
    >>> sameModel.predict(2, 2)
    0.4...
    >>> sameModel.predictAll(testset).collect()
    [Rating(...
    >>> from shutil import rmtree
    >>> try:
    ...     rmtree(path)
    ... except OSError:
    ...     pass
    """
    def predict(self, user: int, product: int) -> float:
        """
        Predicts rating for the given user and product.
        """
    def predictAll(self, user_product: RDD[Tuple[int, int]]) -> RDD[Rating]:
        """
        Returns a list of predicted ratings for input user and product
        pairs.
        """
    def userFeatures(self) -> RDD[Tuple[int, array.array]]:
        """
        Returns a paired RDD, where the first element is the user and the
        second is an array of features corresponding to that user.
        """
    def productFeatures(self) -> RDD[Tuple[int, array.array]]:
        """
        Returns a paired RDD, where the first element is the product and the
        second is an array of features corresponding to that product.
        """
    def recommendUsers(self, product: int, num: int) -> List[Rating]:
        '''
        Recommends the top "num" number of users for a given product and
        returns a list of Rating objects sorted by the predicted rating in
        descending order.
        '''
    def recommendProducts(self, user: int, num: int) -> List[Rating]:
        '''
        Recommends the top "num" number of products for a given user and
        returns a list of Rating objects sorted by the predicted rating in
        descending order.
        '''
    def recommendProductsForUsers(self, num: int) -> RDD[Tuple[int, Tuple[Rating, ...]]]:
        '''
        Recommends the top "num" number of products for all users. The
        number of recommendations returned per user may be less than "num".
        '''
    def recommendUsersForProducts(self, num: int) -> RDD[Tuple[int, Tuple[Rating, ...]]]:
        '''
        Recommends the top "num" number of users for all products. The
        number of recommendations returned per product may be less than
        "num".
        '''
    @property
    def rank(self) -> int:
        """Rank for the features in this model"""
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> MatrixFactorizationModel:
        """Load a model from the given path"""

class ALS:
    """Alternating Least Squares matrix factorization

    .. versionadded:: 0.9.0
    """
    @classmethod
    def train(cls, ratings: RDD[Rating] | RDD[Tuple[int, int, float]], rank: int, iterations: int = 5, lambda_: float = 0.01, blocks: int = -1, nonnegative: bool = False, seed: int | None = None) -> MatrixFactorizationModel:
        """
        Train a matrix factorization model given an RDD of ratings by users
        for a subset of products. The ratings matrix is approximated as the
        product of two lower-rank matrices of a given rank (number of
        features). To solve for these features, ALS is run iteratively with
        a configurable level of parallelism.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        ratings : :py:class:`pyspark.RDD`
            RDD of `Rating` or (userID, productID, rating) tuple.
        rank : int
            Number of features to use (also referred to as the number of latent factors).
        iterations : int, optional
            Number of iterations of ALS.
            (default: 5)
        lambda\\_ : float, optional
            Regularization parameter.
            (default: 0.01)
        blocks : int, optional
            Number of blocks used to parallelize the computation. A value
            of -1 will use an auto-configured number of blocks.
            (default: -1)
        nonnegative : bool, optional
            A value of True will solve least-squares with nonnegativity
            constraints.
            (default: False)
        seed : bool, optional
            Random seed for initial matrix factorization model. A value
            of None will use system time as the seed.
            (default: None)
        """
    @classmethod
    def trainImplicit(cls, ratings: RDD[Rating] | RDD[Tuple[int, int, float]], rank: int, iterations: int = 5, lambda_: float = 0.01, blocks: int = -1, alpha: float = 0.01, nonnegative: bool = False, seed: int | None = None) -> MatrixFactorizationModel:
        """
        Train a matrix factorization model given an RDD of 'implicit
        preferences' of users for a subset of products. The ratings matrix
        is approximated as the product of two lower-rank matrices of a
        given rank (number of features). To solve for these features, ALS
        is run iteratively with a configurable level of parallelism.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        ratings : :py:class:`pyspark.RDD`
            RDD of `Rating` or (userID, productID, rating) tuple.
        rank : int
            Number of features to use (also referred to as the number of latent factors).
        iterations : int, optional
            Number of iterations of ALS.
            (default: 5)
        lambda\\_ : float, optional
            Regularization parameter.
            (default: 0.01)
        blocks : int, optional
            Number of blocks used to parallelize the computation. A value
            of -1 will use an auto-configured number of blocks.
            (default: -1)
        alpha : float, optional
            A constant used in computing confidence.
            (default: 0.01)
        nonnegative : bool, optional
            A value of True will solve least-squares with nonnegativity
            constraints.
            (default: False)
        seed : int, optional
            Random seed for initial matrix factorization model. A value
            of None will use system time as the seed.
            (default: None)
        """
