from .core import PATH_TYPES as PATH_TYPES, fspath as fspath
from _typeshed import Incomplete

logger: Incomplete

def set_cache_path(path) -> None: ...
def titanic(): ...
def amazon(): ...
def msrank(): ...
def msrank_10k(): ...
def rotten_tomatoes():
    '''
    Contains information from kaggle [1], which is made available here under the Open Database License (ODbL) [2].

    Download "rotten_tomatoes" [1] data set.

    Will return two pandas.DataFrame-s, first with train part (rotten_tomatoes.data) and second with test part
    (rotten_tomatoes.test) of the dataset.

    NOTE: This is a preprocessed version of the dataset.

    [1]: https://www.kaggle.com/rpnuser8182/rotten-tomatoes
    [2]: https://opendatacommons.org/licenses/odbl/1-0/index.html
    '''
def imdb(): ...
def epsilon():
    '''
    Download "epsilon" [1] data set.

    Will return two pandas.DataFrame-s, first with train part (epsilon_normalized) and second with
    test part (epsilon_normalized.t) of the dataset. Object class will be located in the first
    column of dataset.

    NOTE: This is a preprocessed version of the dataset. It was converted from libsvm format into
    tsv (CatBoost doesn\'t support libsvm format out of the box).

    [1]: https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#epsilon
    '''
def monotonic1():
    """
    Dataset with monotonic constraints.
    Can be used for poisson regression.
    Has several numerical and several categorical features.
    The first column contains target values. Columns with names Cat* contain categorical features.
    Columns with names Num* contain numerical features.

    Dataset also contains several numerical features, for which monotonic constraints must hold.
    For features in columns named MonotonicNeg*, if feature value decreases, then prediction value must not decrease.
    Thus, if there are two samples x1, x2 with all features being equal except
    for a monotonic negative feature M, such that x1[M] > x2[M], then the following inequality must
    hold for predictions: f(x1) <= f(x2)
    """
def monotonic2():
    """
    Dataset with monotonic constraints.
    Can be used for regression.
    The first column contains target values.
    Other columns contain contain numerical features, for which monotonic constraints must hold.

    For features in columns named MonotonicNeg*, if feature value decreases, then prediction
    value must not decrease. Thus, if there are two samples x1, x2 with all features being
    equal except for a monotonic negative feature MNeg, such that x1[MNeg] > x2[MNeg], then
    the following inequality must hold for predictions: f(x1) <= f(x2)
    For features in columns named MonotonicPos*, if feature value decreases, then prediction
    value must not increase. Thus, if there are two samples x1, x2 with all features being
    equal except for a monotonic positive feature MPos, such that x1[MPos] > x2[MPos],
    then the following inequality must hold for predictions: f(x1) >= f(x2)
    """
def adult():
    '''
    Download "Adult Data Set" [1] from UCI Machine Learning Repository.

    Will return two pandas.DataFrame-s, first with train part (adult.data) and second with test part
    (adult.test) of the dataset.

    [1]: https://archive.ics.uci.edu/ml/datasets/Adult
    '''
def higgs():
    '''
    Download "higgs" [1] data set.

    Will return two pandas.DataFrame-s, first with train part and second with
    test part of the dataset. Object class will be located in the first
    column of dataset.

    [1]: https://archive.ics.uci.edu/ml/datasets/HIGGS
    '''
