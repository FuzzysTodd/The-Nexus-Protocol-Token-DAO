from _typeshed import Incomplete

class DataFrame: ...
class Series: ...

class BuiltinMetric:
    @staticmethod
    def params_with_defaults() -> None:
        """
        For each valid metric parameter, returns its default value and if this parameter is mandatory.
        Implemented in child classes.

        Returns
        ----------
        valid_params: dict: param_name -> {'default_value': default value or None, 'is_mandatory': bool}
        """
    def set_hints(self, **hints) -> None:
        """
        Sets hints for the metric. Hints are not validated.
        Implemented in child classes.

        Returns
        ----------
        self: for chained calls.
        """
    def eval(self, label, approx, weight: Incomplete | None = None, group_id: Incomplete | None = None, group_weight: Incomplete | None = None, subgroup_id: Incomplete | None = None, pairs: Incomplete | None = None, thread_count: int = -1):
        """
        Evaluate the metric with raw approxes and labels.

        Parameters
        ----------
        label : list or numpy.ndarrays or pandas.DataFrame or pandas.Series
            Object labels.

        approx : list or numpy.ndarrays or pandas.DataFrame or pandas.Series
            Object approxes.

        weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Object weights.

        group_id : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Object group ids.

        group_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Group weights.

        subgroup_id : list or numpy.ndarray, optional (default=None)
            subgroup id for each instance.
            If not None, giving 1 dimensional array like data.

        pairs : list or numpy.ndarray or pandas.DataFrame or string or pathlib.Path
            The pairs description.
            If list or numpy.ndarrays or pandas.DataFrame, giving 2 dimensional.
            The shape should be Nx2, where N is the pairs' count. The first element of the pair is
            the index of winner object in the training set. The second element of the pair is
            the index of loser object in the training set.
            If string or pathlib.Path, giving the path to the file with pairs description.

        thread_count : int, optional (default=-1)
            Number of threads to work with.
            If -1, then the number of threads is set to the number of CPU cores.

        Returns
        -------
        metric results : list with metric values.
        """
    def is_max_optimal(self):
        """
        Returns
        ----------
        bool : True if metric is maximizable, False otherwise
        """
    def is_min_optimal(self):
        """
        Returns
        ----------
        bool :  True if metric is minimizable, False otherwise
        """

class _MetricGenerator(type):
    def __new__(mcs, name, parents, attrs): ...
    def __call__(cls, **kwargs): ...
    def __setattr__(cls, name, value) -> None: ...
    def __delattr__(cls, name) -> None: ...
