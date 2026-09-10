import optuna
from lightgbm import Dataset as Dataset
from lightgbm.callback import CallbackEnv as CallbackEnv
from optuna._imports import try_import as try_import
from optuna.integration._lightgbm_tuner import LightGBMTuner as LightGBMTuner, LightGBMTunerCV as LightGBMTunerCV

class LightGBMPruningCallback:
    """Callback for LightGBM to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    lightgbm/lightgbm_integration.py>`__
    if you want to add a pruning callback which observes AUC
    of a LightGBM model.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of
            the objective function.
        metric:
            An evaluation metric for pruning, e.g., ``binary_error`` and ``multi_error``.
            Please refer to
            `LightGBM reference
            <https://lightgbm.readthedocs.io/en/latest/Parameters.html#metric>`_
            for further details.
        valid_name:
            The name of the target validation.
            Validation names are specified by ``valid_names`` option of
            `train method
            <https://lightgbm.readthedocs.io/en/latest/Python-API.html#lightgbm.train>`_.
            If omitted, ``valid_0`` is used which is the default name of the first validation.
            Note that this argument will be ignored if you are calling
            `cv method <https://lightgbm.readthedocs.io/en/latest/Python-API.html#lightgbm.cv>`_
            instead of train method.
    """
    def __init__(self, trial: optuna.trial.Trial, metric: str, valid_name: str = 'valid_0') -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...
