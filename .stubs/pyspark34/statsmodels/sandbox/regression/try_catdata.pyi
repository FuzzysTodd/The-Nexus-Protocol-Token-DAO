from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange

def labelmeanfilter(y, x): ...
def labelmeanfilter_nd(y, x): ...
def labelmeanfilter_str(ys, x): ...
def groupstatsbin(factors, values):
    """uses np.bincount, assumes factors/labels are integers
    """
def convertlabels(ys, indices: Incomplete | None = None):
    """convert labels based on multiple variables or string labels to unique
    index labels 0,1,2,...,nk-1 where nk is the number of distinct labels
    """
def groupsstats_1d(y, x, labelsunique):
    """use ndimage to get fast mean and variance"""
def cat2dummy(y, nonseq: int = 0): ...
def groupsstats_dummy(y, x, nonseq: int = 0): ...
