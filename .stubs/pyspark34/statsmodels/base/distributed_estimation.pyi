from _typeshed import Incomplete
from statsmodels.base.elastic_net import RegularizedResults as RegularizedResults
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults
from statsmodels.regression.linear_model import OLS as OLS

class DistributedModel:
    __doc__: str
    partitions: Incomplete
    model_class: Incomplete
    init_kwds: Incomplete
    estimation_method: Incomplete
    estimation_kwds: Incomplete
    join_method: Incomplete
    join_kwds: Incomplete
    results_class: Incomplete
    results_kwds: Incomplete
    def __init__(self, partitions, model_class: Incomplete | None = None, init_kwds: Incomplete | None = None, estimation_method: Incomplete | None = None, estimation_kwds: Incomplete | None = None, join_method: Incomplete | None = None, join_kwds: Incomplete | None = None, results_class: Incomplete | None = None, results_kwds: Incomplete | None = None) -> None: ...
    def fit(self, data_generator, fit_kwds: Incomplete | None = None, parallel_method: str = 'sequential', parallel_backend: Incomplete | None = None, init_kwds_generator: Incomplete | None = None):
        '''Performs the distributed estimation using the corresponding
        DistributedModel

        Parameters
        ----------
        data_generator : generator
            A generator that produces a sequence of tuples where the first
            element in the tuple corresponds to an endog array and the
            element corresponds to an exog array.
        fit_kwds : dict-like or None
            Keywords needed for the model fitting.
        parallel_method : str
            type of distributed estimation to be used, currently
            "sequential", "joblib" and "dask" are supported.
        parallel_backend : None or joblib parallel_backend object
            used to allow support for more complicated backends,
            ex: dask.distributed
        init_kwds_generator : generator or None
            Additional keyword generator that produces model init_kwds
            that may vary based on data partition.  The current usecase
            is for WLS and GLS

        Returns
        -------
        join_method result.  For the default, _join_debiased, it returns a
        p length array.
        '''
    def fit_sequential(self, data_generator, fit_kwds, init_kwds_generator: Incomplete | None = None):
        """Sequentially performs the distributed estimation using
        the corresponding DistributedModel

        Parameters
        ----------
        data_generator : generator
            A generator that produces a sequence of tuples where the first
            element in the tuple corresponds to an endog array and the
            element corresponds to an exog array.
        fit_kwds : dict-like
            Keywords needed for the model fitting.
        init_kwds_generator : generator or None
            Additional keyword generator that produces model init_kwds
            that may vary based on data partition.  The current usecase
            is for WLS and GLS

        Returns
        -------
        join_method result.  For the default, _join_debiased, it returns a
        p length array.
        """
    def fit_joblib(self, data_generator, fit_kwds, parallel_backend, init_kwds_generator: Incomplete | None = None):
        """Performs the distributed estimation in parallel using joblib

        Parameters
        ----------
        data_generator : generator
            A generator that produces a sequence of tuples where the first
            element in the tuple corresponds to an endog array and the
            element corresponds to an exog array.
        fit_kwds : dict-like
            Keywords needed for the model fitting.
        parallel_backend : None or joblib parallel_backend object
            used to allow support for more complicated backends,
            ex: dask.distributed
        init_kwds_generator : generator or None
            Additional keyword generator that produces model init_kwds
            that may vary based on data partition.  The current usecase
            is for WLS and GLS

        Returns
        -------
        join_method result.  For the default, _join_debiased, it returns a
        p length array.
        """

class DistributedResults(LikelihoodModelResults):
    """
    Class to contain model results

    Parameters
    ----------
    model : class instance
        Class instance for model used for distributed data,
        this particular instance uses fake data and is really
        only to allow use of methods like predict.
    params : ndarray
        Parameter estimates from the fit model.
    """
    def __init__(self, model, params) -> None: ...
    def predict(self, exog, *args, **kwargs):
        """Calls self.model.predict for the provided exog.  See
        Results.predict.

        Parameters
        ----------
        exog : array_like NOT optional
            The values for which we want to predict, unlike standard
            predict this is NOT optional since the data in self.model
            is fake.
        *args :
            Some models can take additional arguments. See the
            predict method of the model for the details.
        **kwargs :
            Some models can take additional keywords arguments. See the
            predict method of the model for the details.

        Returns
        -------
            prediction : ndarray, pandas.Series or pandas.DataFrame
            See self.model.predict
        """
