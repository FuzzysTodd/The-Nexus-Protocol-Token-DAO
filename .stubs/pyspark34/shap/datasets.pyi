from _typeshed import Incomplete

github_data_url: str

def imagenet50(display: bool = False, resolution: int = 224, n_points: Incomplete | None = None):
    """ This is a set of 50 images representative of ImageNet images.

    This dataset was collected by randomly finding a working ImageNet link and then pasting the
    original ImageNet image into Google image search restricted to images licensed for reuse. A
    similar image (now with rights to reuse) was downloaded as a rough replacment for the original
    ImageNet image. The point is to have a random sample of ImageNet for use as a background
    distribution for explaining models trained on ImageNet data.

    Note that because the images are only rough replacements the labels might no longer be correct.
    """
def boston(display: bool = False, n_points: Incomplete | None = None):
    """Return the boston housing data in a nice package (DEPRECATED).

    This dataset is deprecated and will be removed in the next version (0.43.0).
    Please use :func:`shap.datasets.california` instead.
    """
def california(display: bool = False, n_points: Incomplete | None = None):
    """ Return the california housing data in a nice package. """
def linnerud(display: bool = False, n_points: Incomplete | None = None):
    """ Return the linnerud data in a nice package (multi-target regression). """
def imdb(display: bool = False, n_points: Incomplete | None = None):
    """ Return the classic IMDB sentiment analysis training data in a nice package.

    Full data is at: http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
    Paper to cite when using the data is: http://www.aclweb.org/anthology/P11-1015
    """
def communitiesandcrime(display: bool = False, n_points: Incomplete | None = None):
    """ Predict total number of non-violent crimes per 100K popuation.

    This dataset is from the classic UCI Machine Learning repository:
    https://archive.ics.uci.edu/ml/datasets/Communities+and+Crime+Unnormalized
    """
def diabetes(display: bool = False, n_points: Incomplete | None = None):
    """ Return the diabetes data in a nice package. """
def iris(display: bool = False, n_points: Incomplete | None = None):
    """ Return the classic iris data in a nice package. """
def adult(display: bool = False, n_points: Incomplete | None = None):
    """ Return the Adult census data in a nice package. """
def nhanesi(display: bool = False, n_points: Incomplete | None = None):
    """ A nicely packaged version of NHANES I data with surivival times as labels.
    """
def corrgroups60(display: bool = False, n_points: int = 1000):
    """ Correlated Groups 60

    A simulated dataset with tight correlations among distinct groups of features.
    """
def independentlinear60(display: bool = False, n_points: int = 1000):
    """ A simulated dataset with tight correlations among distinct groups of features.
    """
def a1a(n_points: Incomplete | None = None):
    """ A sparse dataset in scipy csr matrix format.
    """
def rank():
    """ Ranking datasets from lightgbm repository.
    """
def cache(url, file_name: Incomplete | None = None):
    """ Loads a file from the URL and caches it locally.
    """
