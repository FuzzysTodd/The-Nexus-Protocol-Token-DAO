from . import get_data_home as get_data_home, load_files as load_files
from .. import preprocessing as preprocessing
from ..feature_extraction.text import CountVectorizer as CountVectorizer
from ..utils import Bunch as Bunch, check_random_state as check_random_state
from ..utils._param_validation import StrOptions as StrOptions, validate_params as validate_params
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from _typeshed import Incomplete

logger: Incomplete
ARCHIVE: Incomplete
CACHE_NAME: str
TRAIN_FOLDER: str
TEST_FOLDER: str

def strip_newsgroup_header(text):
    '''
    Given text in "news" format, strip the headers, by removing everything
    before the first blank line.

    Parameters
    ----------
    text : str
        The text from which to remove the signature block.
    '''
def strip_newsgroup_quoting(text):
    '''
    Given text in "news" format, strip lines beginning with the quote
    characters > or |, plus lines that often introduce a quoted section
    (for example, because they contain the string \'writes:\'.)

    Parameters
    ----------
    text : str
        The text from which to remove the signature block.
    '''
def strip_newsgroup_footer(text):
    '''
    Given text in "news" format, attempt to remove a signature block.

    As a rough heuristic, we assume that signatures are set apart by either
    a blank line or a line made of hyphens, and that it is the last such line
    in the file (disregarding blank lines at the end).

    Parameters
    ----------
    text : str
        The text from which to remove the signature block.
    '''
def fetch_20newsgroups(*, data_home: Incomplete | None = None, subset: str = 'train', categories: Incomplete | None = None, shuffle: bool = True, random_state: int = 42, remove=(), download_if_missing: bool = True, return_X_y: bool = False):
    """Load the filenames and data from the 20 newsgroups dataset (classification).

    Download it if necessary.

    =================   ==========
    Classes                     20
    Samples total            18846
    Dimensionality               1
    Features                  text
    =================   ==========

    Read more in the :ref:`User Guide <20newsgroups_dataset>`.

    Parameters
    ----------
    data_home : str, default=None
        Specify a download and cache folder for the datasets. If None,
        all scikit-learn data is stored in '~/scikit_learn_data' subfolders.

    subset : {'train', 'test', 'all'}, default='train'
        Select the dataset to load: 'train' for the training set, 'test'
        for the test set, 'all' for both, with shuffled ordering.

    categories : array-like, dtype=str, default=None
        If None (default), load all the categories.
        If not None, list of category names to load (other categories
        ignored).

    shuffle : bool, default=True
        Whether or not to shuffle the data: might be important for models that
        make the assumption that the samples are independent and identically
        distributed (i.i.d.), such as stochastic gradient descent.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for dataset shuffling. Pass an int
        for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    remove : tuple, default=()
        May contain any subset of ('headers', 'footers', 'quotes'). Each of
        these are kinds of text that will be detected and removed from the
        newsgroup posts, preventing classifiers from overfitting on
        metadata.

        'headers' removes newsgroup headers, 'footers' removes blocks at the
        ends of posts that look like signatures, and 'quotes' removes lines
        that appear to be quoting another post.

        'headers' follows an exact standard; the other filters are not always
        correct.

    download_if_missing : bool, default=True
        If False, raise an OSError if the data is not locally available
        instead of trying to download the data from the source site.

    return_X_y : bool, default=False
        If True, returns `(data.data, data.target)` instead of a Bunch
        object.

        .. versionadded:: 0.22

    Returns
    -------
    bunch : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : list of shape (n_samples,)
            The data list to learn.
        target: ndarray of shape (n_samples,)
            The target labels.
        filenames: list of shape (n_samples,)
            The path to the location of the data.
        DESCR: str
            The full description of the dataset.
        target_names: list of shape (n_classes,)
            The names of target classes.

    (data, target) : tuple if `return_X_y=True`
        A tuple of two ndarrays. The first contains a 2D array of shape
        (n_samples, n_classes) with each row representing one sample and each
        column representing the features. The second array of shape
        (n_samples,) contains the target samples.

        .. versionadded:: 0.22
    """
def fetch_20newsgroups_vectorized(*, subset: str = 'train', remove=(), data_home: Incomplete | None = None, download_if_missing: bool = True, return_X_y: bool = False, normalize: bool = True, as_frame: bool = False):
    """Load and vectorize the 20 newsgroups dataset (classification).

    Download it if necessary.

    This is a convenience function; the transformation is done using the
    default settings for
    :class:`~sklearn.feature_extraction.text.CountVectorizer`. For more
    advanced usage (stopword filtering, n-gram extraction, etc.), combine
    fetch_20newsgroups with a custom
    :class:`~sklearn.feature_extraction.text.CountVectorizer`,
    :class:`~sklearn.feature_extraction.text.HashingVectorizer`,
    :class:`~sklearn.feature_extraction.text.TfidfTransformer` or
    :class:`~sklearn.feature_extraction.text.TfidfVectorizer`.

    The resulting counts are normalized using
    :func:`sklearn.preprocessing.normalize` unless normalize is set to False.

    =================   ==========
    Classes                     20
    Samples total            18846
    Dimensionality          130107
    Features                  real
    =================   ==========

    Read more in the :ref:`User Guide <20newsgroups_dataset>`.

    Parameters
    ----------
    subset : {'train', 'test', 'all'}, default='train'
        Select the dataset to load: 'train' for the training set, 'test'
        for the test set, 'all' for both, with shuffled ordering.

    remove : tuple, default=()
        May contain any subset of ('headers', 'footers', 'quotes'). Each of
        these are kinds of text that will be detected and removed from the
        newsgroup posts, preventing classifiers from overfitting on
        metadata.

        'headers' removes newsgroup headers, 'footers' removes blocks at the
        ends of posts that look like signatures, and 'quotes' removes lines
        that appear to be quoting another post.

    data_home : str, default=None
        Specify an download and cache folder for the datasets. If None,
        all scikit-learn data is stored in '~/scikit_learn_data' subfolders.

    download_if_missing : bool, default=True
        If False, raise an OSError if the data is not locally available
        instead of trying to download the data from the source site.

    return_X_y : bool, default=False
        If True, returns ``(data.data, data.target)`` instead of a Bunch
        object.

        .. versionadded:: 0.20

    normalize : bool, default=True
        If True, normalizes each document's feature vector to unit norm using
        :func:`sklearn.preprocessing.normalize`.

        .. versionadded:: 0.22

    as_frame : bool, default=False
        If True, the data is a pandas DataFrame including columns with
        appropriate dtypes (numeric, string, or categorical). The target is
        a pandas DataFrame or Series depending on the number of
        `target_columns`.

        .. versionadded:: 0.24

    Returns
    -------
    bunch : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data: {sparse matrix, dataframe} of shape (n_samples, n_features)
            The input data matrix. If ``as_frame`` is `True`, ``data`` is
            a pandas DataFrame with sparse columns.
        target: {ndarray, series} of shape (n_samples,)
            The target labels. If ``as_frame`` is `True`, ``target`` is a
            pandas Series.
        target_names: list of shape (n_classes,)
            The names of target classes.
        DESCR: str
            The full description of the dataset.
        frame: dataframe of shape (n_samples, n_features + 1)
            Only present when `as_frame=True`. Pandas DataFrame with ``data``
            and ``target``.

            .. versionadded:: 0.24

    (data, target) : tuple if ``return_X_y`` is True
        `data` and `target` would be of the format defined in the `Bunch`
        description above.

        .. versionadded:: 0.20
    """
