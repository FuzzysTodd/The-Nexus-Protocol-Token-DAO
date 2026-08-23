from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch
from ..utils._param_validation import StrOptions as StrOptions, validate_params as validate_params
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from ._svmlight_format_io import load_svmlight_files as load_svmlight_files
from _typeshed import Incomplete

XY_METADATA: Incomplete
TOPICS_METADATA: Incomplete
logger: Incomplete

def fetch_rcv1(*, data_home: Incomplete | None = None, subset: str = 'all', download_if_missing: bool = True, random_state: Incomplete | None = None, shuffle: bool = False, return_X_y: bool = False):
    """Load the RCV1 multilabel dataset (classification).

    Download it if necessary.

    Version: RCV1-v2, vectors, full sets, topics multilabels.

    =================   =====================
    Classes                               103
    Samples total                      804414
    Dimensionality                      47236
    Features            real, between 0 and 1
    =================   =====================

    Read more in the :ref:`User Guide <rcv1_dataset>`.

    .. versionadded:: 0.17

    Parameters
    ----------
    data_home : str, default=None
        Specify another download and cache folder for the datasets. By default
        all scikit-learn data is stored in '~/scikit_learn_data' subfolders.

    subset : {'train', 'test', 'all'}, default='all'
        Select the dataset to load: 'train' for the training set
        (23149 samples), 'test' for the test set (781265 samples),
        'all' for both, with the training samples first if shuffle is False.
        This follows the official LYRL2004 chronological split.

    download_if_missing : bool, default=True
        If False, raise an OSError if the data is not locally available
        instead of trying to download the data from the source site.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for dataset shuffling. Pass an int
        for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    shuffle : bool, default=False
        Whether to shuffle dataset.

    return_X_y : bool, default=False
        If True, returns ``(dataset.data, dataset.target)`` instead of a Bunch
        object. See below for more information about the `dataset.data` and
        `dataset.target` object.

        .. versionadded:: 0.20

    Returns
    -------
    dataset : :class:`~sklearn.utils.Bunch`
        Dictionary-like object. Returned only if `return_X_y` is False.
        `dataset` has the following attributes:

        - data : sparse matrix of shape (804414, 47236), dtype=np.float64
            The array has 0.16% of non zero values. Will be of CSR format.
        - target : sparse matrix of shape (804414, 103), dtype=np.uint8
            Each sample has a value of 1 in its categories, and 0 in others.
            The array has 3.15% of non zero values. Will be of CSR format.
        - sample_id : ndarray of shape (804414,), dtype=np.uint32,
            Identification number of each sample, as ordered in dataset.data.
        - target_names : ndarray of shape (103,), dtype=object
            Names of each target (RCV1 topics), as ordered in dataset.target.
        - DESCR : str
            Description of the RCV1 dataset.

    (data, target) : tuple
        A tuple consisting of `dataset.data` and `dataset.target`, as
        described above. Returned only if `return_X_y` is True.

        .. versionadded:: 0.20
    """
