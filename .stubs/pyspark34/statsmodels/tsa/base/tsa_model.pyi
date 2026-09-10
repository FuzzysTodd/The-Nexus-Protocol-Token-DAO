import statsmodels.base.model as base
import statsmodels.base.wrapper as wrap
from _typeshed import Incomplete
from pandas import Index
from statsmodels.base.data import PandasData as PandasData
from statsmodels.compat.pandas import is_float_index as is_float_index, is_int_index as is_int_index, is_numeric_dtype as is_numeric_dtype
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning

def get_index_loc(key, index):
    """
    Get the location of a specific key in an index

    Parameters
    ----------
    key : label
        The key for which to find the location if the underlying index is
        a DateIndex or a location if the underlying index is a RangeIndex
        or an Index with an integer dtype.
    index : pd.Index
        The index to search.

    Returns
    -------
    loc : int
        The location of the key
    index : pd.Index
        The index including the key; this is a copy of the original index
        unless the index had to be expanded to accommodate `key`.
    index_was_expanded : bool
        Whether or not the index was expanded to accommodate `key`.

    Notes
    -----
    If `key` is past the end of of the given index, and the index is either
    an Index with an integral dtype or a date index, this function extends
    the index up to and including key, and then returns the location in the
    new index.
    """
def get_index_label_loc(key, index, row_labels):
    """
    Get the location of a specific key in an index or model row labels

    Parameters
    ----------
    key : label
        The key for which to find the location if the underlying index is
        a DateIndex or is only being used as row labels, or a location if
        the underlying index is a RangeIndex or a NumericIndex.
    index : pd.Index
        The index to search.
    row_labels : pd.Index
        Row labels to search if key not found in index

    Returns
    -------
    loc : int
        The location of the key
    index : pd.Index
        The index including the key; this is a copy of the original index
        unless the index had to be expanded to accommodate `key`.
    index_was_expanded : bool
        Whether or not the index was expanded to accommodate `key`.

    Notes
    -----
    This function expands on `get_index_loc` by first trying the given
    base index (or the model's index if the base index was not given) and
    then falling back to try again with the model row labels as the base
    index.
    """
def get_prediction_index(start, end, nobs, base_index, index: Incomplete | None = None, silent: bool = False, index_none: bool = False, index_generated: Incomplete | None = None, data: Incomplete | None = None) -> tuple[int, int, int, Index | None]:
    """
    Get the location of a specific key in an index or model row labels

    Parameters
    ----------
    start : label
        The key at which to start prediction. Depending on the underlying
        model's index, may be an integer, a date (string, datetime object,
        pd.Timestamp, or pd.Period object), or some other object in the
        model's row labels.
    end : label
        The key at which to end prediction (note that this key will be
        *included* in prediction). Depending on the underlying
        model's index, may be an integer, a date (string, datetime object,
        pd.Timestamp, or pd.Period object), or some other object in the
        model's row labels.
    nobs : int
    base_index : pd.Index

    index : pd.Index, optional
        Optionally an index to associate the predicted results to. If None,
        an attempt is made to create an index for the predicted results
        from the model's index or model's row labels.
    silent : bool, optional
        Argument to silence warnings.

    Returns
    -------
    start : int
        The index / observation location at which to begin prediction.
    end : int
        The index / observation location at which to end in-sample
        prediction. The maximum value for this is nobs-1.
    out_of_sample : int
        The number of observations to forecast after the end of the sample.
    prediction_index : pd.Index or None
        The index associated with the prediction results. This index covers
        the range [start, end + out_of_sample]. If the model has no given
        index and no given row labels (i.e. endog/exog is not Pandas), then
        this will be None.

    Notes
    -----
    The arguments `start` and `end` behave differently, depending on if
    they are integer or not. If either is an integer, then it is assumed
    to refer to a *location* in the index, not to an index value. On the
    other hand, if it is a date string or some other type of object, then
    it is assumed to refer to an index *value*. In all cases, the returned
    `start` and `end` values refer to index *locations* (so in the former
    case, the given location is validated and returned whereas in the
    latter case a location is found that corresponds to the given index
    value).

    This difference in behavior is necessary to support `RangeIndex`. This
    is because integers for a RangeIndex could refer either to index values
    or to index locations in an ambiguous way (while for `NumericIndex`,
    since we have required them to be full indexes, there is no ambiguity).
    """

class TimeSeriesModel(base.LikelihoodModel):
    __doc__: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, dates: Incomplete | None = None, freq: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    exog_names: Incomplete

class TimeSeriesModelResults(base.LikelihoodModelResults):
    data: Incomplete
    def __init__(self, model, params, normalized_cov_params, scale: float = 1.0) -> None: ...

class TimeSeriesResultsWrapper(wrap.ResultsWrapper): ...
