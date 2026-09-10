import mxnet as mx
import optuna
from optuna._imports import try_import as try_import

class MXNetPruningCallback:
    """MXNet callback to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    mxnet/mxnet_integration.py>`__
    if you want to add a pruning callback which observes accuracy.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        eval_metric:
            An evaluation metric name for pruning, e.g., ``cross-entropy`` and
            ``accuracy``. If using default metrics like mxnet.metrics.Accuracy, use it's
            default metric name. For custom metrics, use the metric_name provided to
            constructor. Please refer to `mxnet.metrics reference
            <https://mxnet.apache.org/api/python/metric/metric.html>`_ for further details.
    """
    def __init__(self, trial: optuna.trial.Trial, eval_metric: str) -> None: ...
    def __call__(self, param: mx.model.BatchEndParam) -> None: ...
