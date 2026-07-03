from .trial import Trial as Trial
from _typeshed import Incomplete
from typing import Dict

logger: Incomplete

def is_nan_or_inf(value): ...

class ExperimentAnalysis:
    """Analyze results from a Tune experiment."""
    @property
    def best_trial(self) -> Trial:
        """Get the best trial of the experiment
        The best trial is determined by comparing the last trial results
        using the `metric` and `mode` parameters passed to `tune.run()`.
        If you didn't pass these parameters, use
        `get_best_trial(metric, mode, scope)` instead.
        """
    @property
    def best_config(self) -> Dict:
        """Get the config of the best trial of the experiment
        The best trial is determined by comparing the last trial results
        using the `metric` and `mode` parameters passed to `tune.run()`.
        If you didn't pass these parameters, use
        `get_best_config(metric, mode, scope)` instead.
        """
    @property
    def results(self) -> Dict[str, Dict]:
        """Get the last result of all the trials of the experiment"""
    def get_best_trial(self, metric: str | None = None, mode: str | None = None, scope: str = 'last', filter_nan_and_inf: bool = True) -> Trial | None:
        """Retrieve the best trial object.
        Compares all trials' scores on ``metric``.
        If ``metric`` is not specified, ``self.default_metric`` will be used.
        If `mode` is not specified, ``self.default_mode`` will be used.
        These values are usually initialized by passing the ``metric`` and
        ``mode`` parameters to ``tune.run()``.
        Args:
            metric (str): Key for trial info to order on. Defaults to
                ``self.default_metric``.
            mode (str): One of [min, max]. Defaults to ``self.default_mode``.
            scope (str): One of [all, last, avg, last-5-avg, last-10-avg].
                If `scope=last`, only look at each trial's final step for
                `metric`, and compare across trials based on `mode=[min,max]`.
                If `scope=avg`, consider the simple average over all steps
                for `metric` and compare across trials based on
                `mode=[min,max]`. If `scope=last-5-avg` or `scope=last-10-avg`,
                consider the simple average over the last 5 or 10 steps for
                `metric` and compare across trials based on `mode=[min,max]`.
                If `scope=all`, find each trial's min/max score for `metric`
                based on `mode`, and compare trials based on `mode=[min,max]`.
            filter_nan_and_inf (bool): If True (default), NaN or infinite
                values are disregarded and these trials are never selected as
                the best trial.
        """
    def get_best_config(self, metric: str | None = None, mode: str | None = None, scope: str = 'last') -> Dict | None:
        """Retrieve the best config corresponding to the trial.
        Compares all trials' scores on `metric`.
        If ``metric`` is not specified, ``self.default_metric`` will be used.
        If `mode` is not specified, ``self.default_mode`` will be used.
        These values are usually initialized by passing the ``metric`` and
        ``mode`` parameters to ``tune.run()``.
        Args:
            metric (str): Key for trial info to order on. Defaults to
                ``self.default_metric``.
            mode (str): One of [min, max]. Defaults to ``self.default_mode``.
            scope (str): One of [all, last, avg, last-5-avg, last-10-avg].
                If `scope=last`, only look at each trial's final step for
                `metric`, and compare across trials based on `mode=[min,max]`.
                If `scope=avg`, consider the simple average over all steps
                for `metric` and compare across trials based on
                `mode=[min,max]`. If `scope=last-5-avg` or `scope=last-10-avg`,
                consider the simple average over the last 5 or 10 steps for
                `metric` and compare across trials based on `mode=[min,max]`.
                If `scope=all`, find each trial's min/max score for `metric`
                based on `mode`, and compare trials based on `mode=[min,max]`.
        """
    @property
    def best_result(self) -> Dict:
        """Get the last result of the best trial of the experiment
        The best trial is determined by comparing the last trial results
        using the `metric` and `mode` parameters passed to `tune.run()`.
        If you didn't pass these parameters, use
        `get_best_trial(metric, mode, scope).last_result` instead.
        """
