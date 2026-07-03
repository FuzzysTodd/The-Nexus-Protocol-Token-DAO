from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.validation import check_array as check_array, check_consistent_length as check_consistent_length

def l1_min_c(X, y, *, loss: str = 'squared_hinge', fit_intercept: bool = True, intercept_scaling: float = 1.0):
    '''Return the lowest bound for C.

    The lower bound for C is computed such that for C in (l1_min_C, infinity)
    the model is guaranteed not to be empty. This applies to l1 penalized
    classifiers, such as LinearSVC with penalty=\'l1\' and
    linear_model.LogisticRegression with penalty=\'l1\'.

    This value is valid if class_weight parameter in fit() is not set.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training vector, where `n_samples` is the number of samples and
        `n_features` is the number of features.

    y : array-like of shape (n_samples,)
        Target vector relative to X.

    loss : {\'squared_hinge\', \'log\'}, default=\'squared_hinge\'
        Specifies the loss function.
        With \'squared_hinge\' it is the squared hinge loss (a.k.a. L2 loss).
        With \'log\' it is the loss of logistic regression models.

    fit_intercept : bool, default=True
        Specifies if the intercept should be fitted by the model.
        It must match the fit() method parameter.

    intercept_scaling : float, default=1.0
        When fit_intercept is True, instance vector x becomes
        [x, intercept_scaling],
        i.e. a "synthetic" feature with constant value equals to
        intercept_scaling is appended to the instance vector.
        It must match the fit() method parameter.

    Returns
    -------
    l1_min_c : float
        Minimum value for C.
    '''
