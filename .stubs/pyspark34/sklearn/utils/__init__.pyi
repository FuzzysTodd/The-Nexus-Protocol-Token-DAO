from . import metadata_routing as metadata_routing
from ..exceptions import DataConversionWarning as DataConversionWarning
from ._bunch import Bunch as Bunch
from ._estimator_html_repr import estimator_html_repr as estimator_html_repr
from .class_weight import compute_class_weight as compute_class_weight, compute_sample_weight as compute_sample_weight
from .deprecation import deprecated as deprecated
from .discovery import all_estimators as all_estimators
from .murmurhash import murmurhash3_32 as murmurhash3_32
from .validation import as_float_array as as_float_array, assert_all_finite as assert_all_finite, check_X_y as check_X_y, check_array as check_array, check_consistent_length as check_consistent_length, check_random_state as check_random_state, check_scalar as check_scalar, check_symmetric as check_symmetric, column_or_1d as column_or_1d, indexable as indexable
from _typeshed import Incomplete

__all__ = ['murmurhash3_32', 'as_float_array', 'assert_all_finite', 'check_array', 'check_random_state', 'compute_class_weight', 'compute_sample_weight', 'column_or_1d', 'check_consistent_length', 'check_X_y', 'check_scalar', 'indexable', 'check_symmetric', 'indices_to_mask', 'deprecated', 'parallel_backend', 'register_parallel_backend', 'resample', 'shuffle', 'check_matplotlib_support', 'all_estimators', 'DataConversionWarning', 'estimator_html_repr', 'Bunch', 'metadata_routing']

parallel_backend: Incomplete
register_parallel_backend: Incomplete

def resample(*arrays, replace: bool = True, n_samples: Incomplete | None = None, random_state: Incomplete | None = None, stratify: Incomplete | None = None):
    """Resample arrays or sparse matrices in a consistent way.

    The default strategy implements one step of the bootstrapping
    procedure.

    Parameters
    ----------
    *arrays : sequence of array-like of shape (n_samples,) or             (n_samples, n_outputs)
        Indexable data-structures can be arrays, lists, dataframes or scipy
        sparse matrices with consistent first dimension.

    replace : bool, default=True
        Implements resampling with replacement. If False, this will implement
        (sliced) random permutations.

    n_samples : int, default=None
        Number of samples to generate. If left to None this is
        automatically set to the first dimension of the arrays.
        If replace is False it should not be larger than the length of
        arrays.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for shuffling
        the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    stratify : array-like of shape (n_samples,) or (n_samples, n_outputs),             default=None
        If not None, data is split in a stratified fashion, using this as
        the class labels.

    Returns
    -------
    resampled_arrays : sequence of array-like of shape (n_samples,) or             (n_samples, n_outputs)
        Sequence of resampled copies of the collections. The original arrays
        are not impacted.

    See Also
    --------
    shuffle : Shuffle arrays or sparse matrices in a consistent way.

    Examples
    --------
    It is possible to mix sparse and dense arrays in the same run::

      >>> import numpy as np
      >>> X = np.array([[1., 0.], [2., 1.], [0., 0.]])
      >>> y = np.array([0, 1, 2])

      >>> from scipy.sparse import coo_matrix
      >>> X_sparse = coo_matrix(X)

      >>> from sklearn.utils import resample
      >>> X, X_sparse, y = resample(X, X_sparse, y, random_state=0)
      >>> X
      array([[1., 0.],
             [2., 1.],
             [1., 0.]])

      >>> X_sparse
      <3x2 sparse matrix of type '<... 'numpy.float64'>'
          with 4 stored elements in Compressed Sparse Row format>

      >>> X_sparse.toarray()
      array([[1., 0.],
             [2., 1.],
             [1., 0.]])

      >>> y
      array([0, 1, 0])

      >>> resample(y, n_samples=2, random_state=0)
      array([0, 1])

    Example using stratification::

      >>> y = [0, 0, 1, 1, 1, 1, 1, 1, 1]
      >>> resample(y, n_samples=5, replace=False, stratify=y,
      ...          random_state=0)
      [1, 1, 1, 0, 1]
    """
def shuffle(*arrays, random_state: Incomplete | None = None, n_samples: Incomplete | None = None):
    """Shuffle arrays or sparse matrices in a consistent way.

    This is a convenience alias to ``resample(*arrays, replace=False)`` to do
    random permutations of the collections.

    Parameters
    ----------
    *arrays : sequence of indexable data-structures
        Indexable data-structures can be arrays, lists, dataframes or scipy
        sparse matrices with consistent first dimension.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for shuffling
        the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    n_samples : int, default=None
        Number of samples to generate. If left to None this is
        automatically set to the first dimension of the arrays.  It should
        not be larger than the length of arrays.

    Returns
    -------
    shuffled_arrays : sequence of indexable data-structures
        Sequence of shuffled copies of the collections. The original arrays
        are not impacted.

    See Also
    --------
    resample : Resample arrays or sparse matrices in a consistent way.

    Examples
    --------
    It is possible to mix sparse and dense arrays in the same run::

      >>> import numpy as np
      >>> X = np.array([[1., 0.], [2., 1.], [0., 0.]])
      >>> y = np.array([0, 1, 2])

      >>> from scipy.sparse import coo_matrix
      >>> X_sparse = coo_matrix(X)

      >>> from sklearn.utils import shuffle
      >>> X, X_sparse, y = shuffle(X, X_sparse, y, random_state=0)
      >>> X
      array([[0., 0.],
             [2., 1.],
             [1., 0.]])

      >>> X_sparse
      <3x2 sparse matrix of type '<... 'numpy.float64'>'
          with 3 stored elements in Compressed Sparse Row format>

      >>> X_sparse.toarray()
      array([[0., 0.],
             [2., 1.],
             [1., 0.]])

      >>> y
      array([2, 1, 0])

      >>> shuffle(y, n_samples=2, random_state=0)
      array([0, 1])
    """
def indices_to_mask(indices, mask_length):
    """Convert list of indices to boolean mask.

    Parameters
    ----------
    indices : list-like
        List of integers treated as indices.
    mask_length : int
        Length of boolean mask to be generated.
        This parameter must be greater than max(indices).

    Returns
    -------
    mask : 1d boolean nd-array
        Boolean array that is True where indices are present, else False.

    Examples
    --------
    >>> from sklearn.utils import indices_to_mask
    >>> indices = [1, 2 , 3, 4]
    >>> indices_to_mask(indices, 5)
    array([False,  True,  True,  True,  True])
    """
def check_matplotlib_support(caller_name) -> None:
    """Raise ImportError with detailed error message if mpl is not installed.

    Plot utilities like any of the Display's plotting functions should lazily import
    matplotlib and call this helper before any computation.

    Parameters
    ----------
    caller_name : str
        The name of the caller that requires matplotlib.
    """
