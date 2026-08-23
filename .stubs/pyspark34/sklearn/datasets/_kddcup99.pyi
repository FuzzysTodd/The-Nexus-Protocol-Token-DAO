from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch, check_random_state as check_random_state
from ..utils._param_validation import StrOptions as StrOptions, validate_params as validate_params
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from _typeshed import Incomplete

ARCHIVE: Incomplete
ARCHIVE_10_PERCENT: Incomplete
logger: Incomplete

def fetch_kddcup99(*, subset: Incomplete | None = None, data_home: Incomplete | None = None, shuffle: bool = False, random_state: Incomplete | None = None, percent10: bool = True, download_if_missing: bool = True, return_X_y: bool = False, as_frame: bool = False):
    """Load the kddcup99 dataset (classification).

    Download it if necessary.

    =================   ====================================
    Classes                                               23
    Samples total                                    4898431
    Dimensionality                                        41
    Features            discrete (int) or continuous (float)
    =================   ====================================

    Read more in the :ref:`User Guide <kddcup99_dataset>`.

    .. versionadded:: 0.18

    Parameters
    ----------
    subset : {'SA', 'SF', 'http', 'smtp'}, default=None
        To return the corresponding classical subsets of kddcup 99.
        If None, return the entire kddcup 99 dataset.

    data_home : str, default=None
        Specify another download and cache folder for the datasets. By default
        all scikit-learn data is stored in '~/scikit_learn_data' subfolders.

        .. versionadded:: 0.19

    shuffle : bool, default=False
        Whether to shuffle dataset.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for dataset shuffling and for
        selection of abnormal samples if `subset='SA'`. Pass an int for
        reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    percent10 : bool, default=True
        Whether to load only 10 percent of the data.

    download_if_missing : bool, default=True
        If False, raise an OSError if the data is not locally available
        instead of trying to download the data from the source site.

    return_X_y : bool, default=False
        If True, returns ``(data, target)`` instead of a Bunch object. See
        below for more information about the `data` and `target` object.

        .. versionadded:: 0.20

    as_frame : bool, default=False
        If `True`, returns a pandas Dataframe for the ``data`` and ``target``
        objects in the `Bunch` returned object; `Bunch` return object will also
        have a ``frame`` member.

        .. versionadded:: 0.24

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : {ndarray, dataframe} of shape (494021, 41)
            The data matrix to learn. If `as_frame=True`, `data` will be a
            pandas DataFrame.
        target : {ndarray, series} of shape (494021,)
            The regression target for each sample. If `as_frame=True`, `target`
            will be a pandas Series.
        frame : dataframe of shape (494021, 42)
            Only present when `as_frame=True`. Contains `data` and `target`.
        DESCR : str
            The full description of the dataset.
        feature_names : list
            The names of the dataset columns
        target_names: list
            The names of the target columns

    (data, target) : tuple if ``return_X_y`` is True
        A tuple of two ndarray. The first containing a 2D array of
        shape (n_samples, n_features) with each row representing one
        sample and each column representing the features. The second
        ndarray of shape (n_samples,) containing the target samples.

        .. versionadded:: 0.20
    """
