from _typeshed import Incomplete

class StandardizeTransform:
    """class to reparameterize a model for standardized exog

    Parameters
    ----------
    data : array_like
        data that is standardized along axis=0
    ddof : None or int
        degrees of freedom for calculation of standard deviation.
        default is 1, in contrast to numpy.std
    const_idx : None or int
        If None, then the presence of a constant is detected if the standard
        deviation of a column is **equal** to zero. A constant column is
        not transformed. If this is an integer, then the corresponding column
        will not be transformed.
    demean : bool, default is True
        If demean is true, then the data will be demeaned, otherwise it will
        only be rescaled.

    Notes
    -----
    Warning: Not all options are tested and it is written for one use case.
    API changes are expected.

    This can be used to transform only the design matrix, exog, in a model,
    which is required in some discrete models when the endog cannot be rescaled
    or demeaned.
    The transformation is full rank and does not drop the constant.
    """
    mean: Incomplete
    scale: Incomplete
    const_idx: Incomplete
    def __init__(self, data, ddof: int = 1, const_idx: Incomplete | None = None, demean: bool = True) -> None: ...
    def transform(self, data):
        """standardize the data using the stored transformation
        """
    def transform_params(self, params):
        """Transform parameters of the standardized model to the original model

        Parameters
        ----------
        params : ndarray
            parameters estimated with the standardized model

        Returns
        -------
        params_new : ndarray
            parameters transformed to the parameterization of the original
            model
        """
    __call__ = transform
