import abc
import lightgbm as lgb
import optuna
import tqdm
from _typeshed import Incomplete
from optuna._deprecated import deprecated as deprecated
from optuna._imports import try_import as try_import
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from sklearn.model_selection import BaseCrossValidator as BaseCrossValidator
from typing import Any, Callable, Dict, Generator, Iterator, List, Tuple

VALID_SET_TYPE: Incomplete

class _BaseTuner:
    lgbm_params: Incomplete
    lgbm_kwargs: Incomplete
    def __init__(self, lgbm_params: Dict[str, Any] | None = None, lgbm_kwargs: Dict[str, Any] | None = None) -> None: ...
    def higher_is_better(self) -> bool: ...
    def compare_validation_metrics(self, val_score: float, best_score: float) -> bool: ...

class _OptunaObjective(_BaseTuner):
    """Objective for hyperparameter-tuning with Optuna."""
    target_param_names: Incomplete
    pbar: Incomplete
    lgbm_params: Incomplete
    lgbm_kwargs: Incomplete
    train_set: Incomplete
    trial_count: int
    best_score: Incomplete
    best_booster_with_trial_number: Incomplete
    step_name: Incomplete
    model_dir: Incomplete
    pbar_fmt: str
    def __init__(self, target_param_names: List[str], lgbm_params: Dict[str, Any], train_set: lgb.Dataset, lgbm_kwargs: Dict[str, Any], best_score: float, step_name: str, model_dir: str | None, pbar: tqdm.tqdm | None = None) -> None: ...
    def __call__(self, trial: optuna.trial.Trial) -> float: ...

class _OptunaObjectiveCV(_OptunaObjective):
    def __init__(self, target_param_names: List[str], lgbm_params: Dict[str, Any], train_set: lgb.Dataset, lgbm_kwargs: Dict[str, Any], best_score: float, step_name: str, model_dir: str | None, pbar: tqdm.tqdm | None = None) -> None: ...
    best_score: Incomplete
    best_booster_with_trial_number: Incomplete
    def __call__(self, trial: optuna.trial.Trial) -> float: ...

class _LightGBMBaseTuner(_BaseTuner, metaclass=abc.ABCMeta):
    """Base class of LightGBM Tuners.

    This class has common attributes and methods of
    :class:`~optuna.integration.lightgbm.LightGBMTuner` and
    :class:`~optuna.integration.lightgbm.LightGBMTunerCV`.
    """
    study: Incomplete
    def __init__(self, params: Dict[str, Any], train_set: lgb.Dataset, num_boost_round: int = 1000, fobj: Callable[..., Any] | None = None, feval: Callable[..., Any] | None = None, feature_name: str = 'auto', categorical_feature: str = 'auto', early_stopping_rounds: int | None = None, verbose_eval: bool | int | None = True, callbacks: List[Callable[..., Any]] | None = None, time_budget: int | None = None, sample_size: int | None = None, study: optuna.study.Study | None = None, optuna_callbacks: List[Callable[[Study, FrozenTrial], None]] | None = None, verbosity: int | None = None, show_progress_bar: bool = True, model_dir: str | None = None, *, optuna_seed: int | None = None) -> None: ...
    @property
    def best_score(self) -> float:
        """Return the score of the best booster."""
    @property
    def best_params(self) -> Dict[str, Any]:
        """Return parameters of the best booster."""
    def get_best_booster(self) -> lgb.Booster:
        """Return the best booster.

        If the best booster cannot be found, :class:`ValueError` will be raised. To prevent the
        errors, please save boosters by specifying the ``model_dir`` argument of
        :meth:`~optuna.integration.lightgbm.LightGBMTuner.__init__`,
        when you resume tuning or you run tuning in parallel.
        """
    def run(self) -> None:
        """Perform the hyperparameter-tuning with given parameters."""
    train_subset: Incomplete
    def sample_train_set(self) -> None:
        """Make subset of `self.train_set` Dataset object."""
    def tune_feature_fraction(self, n_trials: int = 7) -> None: ...
    def tune_num_leaves(self, n_trials: int = 20) -> None: ...
    def tune_bagging(self, n_trials: int = 10) -> None: ...
    def tune_feature_fraction_stage2(self, n_trials: int = 6) -> None: ...
    def tune_regularization_factors(self, n_trials: int = 20) -> None: ...
    def tune_min_data_in_leaf(self) -> None: ...

class LightGBMTuner(_LightGBMBaseTuner):
    """Hyperparameter tuner for LightGBM.

    It optimizes the following hyperparameters in a stepwise manner:
    ``lambda_l1``, ``lambda_l2``, ``num_leaves``, ``feature_fraction``, ``bagging_fraction``,
    ``bagging_freq`` and ``min_child_samples``.

    You can find the details of the algorithm and benchmark results in `this blog article <https:/
    /medium.com/optuna/lightgbm-tuner-new-optuna-integration-for-hyperparameter-optimization-8b709
    5e99258>`_ by `Kohei Ozaki <https://www.kaggle.com/confirm>`_, a Kaggle Grandmaster.

    Arguments and keyword arguments for `lightgbm.train()
    <https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html>`_ can be passed.
    The arguments that only :class:`~optuna.integration.lightgbm.LightGBMTuner` has are
    listed below:

    Args:
        time_budget:
            A time budget for parameter tuning in seconds.

        study:
            A :class:`~optuna.study.Study` instance to store optimization results. The
            :class:`~optuna.trial.Trial` instances in it has the following user attributes:
            ``elapsed_secs`` is the elapsed time since the optimization starts.
            ``average_iteration_time`` is the average time of iteration to train the booster
            model in the trial. ``lgbm_params`` is a JSON-serialized dictionary of LightGBM
            parameters used in the trial.

        optuna_callbacks:
            List of Optuna callback functions that are invoked at the end of each trial.
            Each function must accept two parameters with the following types in this order:
            :class:`~optuna.study.Study` and :class:`~optuna.FrozenTrial`.
            Please note that this is not a ``callbacks`` argument of `lightgbm.train()`_ .

        model_dir:
            A directory to save boosters. By default, it is set to :obj:`None` and no boosters are
            saved. Please set shared directory (e.g., directories on NFS) if you want to access
            :meth:`~optuna.integration.LightGBMTuner.get_best_booster` in distributed environments.
            Otherwise, it may raise :obj:`ValueError`. If the directory does not exist, it will be
            created. The filenames of the boosters will be ``{model_dir}/{trial_number}.pkl``
            (e.g., ``./boosters/0.pkl``).

        verbosity:
            A verbosity level to change Optuna's logging level. The level is aligned to
            `LightGBM's verbosity`_ .

            .. warning::
                Deprecated in v2.0.0. ``verbosity`` argument will be removed in the future.
                The removal of this feature is currently scheduled for v4.0.0,
                but this schedule is subject to change.

                Please use :func:`~optuna.logging.set_verbosity` instead.

        show_progress_bar:
            Flag to show progress bars or not. To disable progress bar, set this :obj:`False`.

            .. note::
                Progress bars will be fragmented by logging messages of LightGBM and Optuna.
                Please suppress such messages to show the progress bars properly.

        optuna_seed:
            ``seed`` of :class:`~optuna.samplers.TPESampler` for random number generator
            that affects sampling for ``num_leaves``, ``bagging_fraction``, ``bagging_freq``,
            ``lambda_l1``, and ``lambda_l2``.

            .. note::
                The `deterministic`_ parameter of LightGBM makes training reproducible.
                Please enable it when you use this argument.

    .. _lightgbm.train(): https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html
    .. _LightGBM's verbosity: https://lightgbm.readthedocs.io/en/latest/Parameters.html#verbosity
    .. _deterministic: https://lightgbm.readthedocs.io/en/latest/Parameters.html#deterministic
    """
    def __init__(self, params: Dict[str, Any], train_set: lgb.Dataset, num_boost_round: int = 1000, valid_sets: VALID_SET_TYPE | None = None, valid_names: Any | None = None, fobj: Callable[..., Any] | None = None, feval: Callable[..., Any] | None = None, feature_name: str = 'auto', categorical_feature: str = 'auto', early_stopping_rounds: int | None = None, evals_result: Dict[Any, Any] | None = None, verbose_eval: bool | int | None = True, learning_rates: List[float] | None = None, keep_training_booster: bool = False, callbacks: List[Callable[..., Any]] | None = None, time_budget: int | None = None, sample_size: int | None = None, study: optuna.study.Study | None = None, optuna_callbacks: List[Callable[[Study, FrozenTrial], None]] | None = None, model_dir: str | None = None, verbosity: int | None = None, show_progress_bar: bool = True, *, optuna_seed: int | None = None) -> None: ...
    @property
    def best_booster(self) -> lgb.Booster:
        """Return the best booster."""

class LightGBMTunerCV(_LightGBMBaseTuner):
    """Hyperparameter tuner for LightGBM with cross-validation.

    It employs the same stepwise approach as
    :class:`~optuna.integration.lightgbm.LightGBMTuner`.
    :class:`~optuna.integration.lightgbm.LightGBMTunerCV` invokes `lightgbm.cv()`_ to train
    and validate boosters while :class:`~optuna.integration.lightgbm.LightGBMTuner` invokes
    `lightgbm.train()`_. See
    `a simple example <https://github.com/optuna/optuna-examples/tree/main/lightgbm/
    lightgbm_tuner_cv.py>`_ which optimizes the validation log loss of cancer detection.

    Arguments and keyword arguments for `lightgbm.cv()`_ can be passed except
    ``metrics``, ``init_model`` and ``eval_train_metric``.
    The arguments that only :class:`~optuna.integration.lightgbm.LightGBMTunerCV` has are
    listed below:

    Args:
        time_budget:
            A time budget for parameter tuning in seconds.

        study:
            A :class:`~optuna.study.Study` instance to store optimization results. The
            :class:`~optuna.trial.Trial` instances in it has the following user attributes:
            ``elapsed_secs`` is the elapsed time since the optimization starts.
            ``average_iteration_time`` is the average time of iteration to train the booster
            model in the trial. ``lgbm_params`` is a JSON-serialized dictionary of LightGBM
            parameters used in the trial.

        optuna_callbacks:
            List of Optuna callback functions that are invoked at the end of each trial.
            Each function must accept two parameters with the following types in this order:
            :class:`~optuna.study.Study` and :class:`~optuna.FrozenTrial`.
            Please note that this is not a ``callbacks`` argument of `lightgbm.train()`_ .

        model_dir:
            A directory to save boosters. By default, it is set to :obj:`None` and no boosters are
            saved. Please set shared directory (e.g., directories on NFS) if you want to access
            :meth:`~optuna.integration.LightGBMTunerCV.get_best_booster`
            in distributed environments.
            Otherwise, it may raise :obj:`ValueError`. If the directory does not exist, it will be
            created. The filenames of the boosters will be ``{model_dir}/{trial_number}.pkl``
            (e.g., ``./boosters/0.pkl``).

        verbosity:
            A verbosity level to change Optuna's logging level. The level is aligned to
            `LightGBM's verbosity`_ .

            .. warning::
                Deprecated in v2.0.0. ``verbosity`` argument will be removed in the future.
                The removal of this feature is currently scheduled for v4.0.0,
                but this schedule is subject to change.

                Please use :func:`~optuna.logging.set_verbosity` instead.

        show_progress_bar:
            Flag to show progress bars or not. To disable progress bar, set this :obj:`False`.

            .. note::
                Progress bars will be fragmented by logging messages of LightGBM and Optuna.
                Please suppress such messages to show the progress bars properly.

        return_cvbooster:
            Flag to enable :meth:`~optuna.integration.LightGBMTunerCV.get_best_booster`.

        optuna_seed:
            ``seed`` of :class:`~optuna.samplers.TPESampler` for random number generator
            that affects sampling for ``num_leaves``, ``bagging_fraction``, ``bagging_freq``,
            ``lambda_l1``, and ``lambda_l2``.

            .. note::
                The `deterministic`_ parameter of LightGBM makes training reproducible.
                Please enable it when you use this argument.

    .. _lightgbm.train(): https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html
    .. _lightgbm.cv(): https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.cv.html
    .. _LightGBM's verbosity: https://lightgbm.readthedocs.io/en/latest/Parameters.html#verbosity
    .. _deterministic: https://lightgbm.readthedocs.io/en/latest/Parameters.html#deterministic
    """
    def __init__(self, params: Dict[str, Any], train_set: lgb.Dataset, num_boost_round: int = 1000, folds: Generator[Tuple[int, int], None, None] | Iterator[Tuple[int, int]] | BaseCrossValidator | None = None, nfold: int = 5, stratified: bool = True, shuffle: bool = True, fobj: Callable[..., Any] | None = None, feval: Callable[..., Any] | None = None, feature_name: str = 'auto', categorical_feature: str = 'auto', early_stopping_rounds: int | None = None, fpreproc: Callable[..., Any] | None = None, verbose_eval: bool | int | None = True, show_stdv: bool = True, seed: int = 0, callbacks: List[Callable[..., Any]] | None = None, time_budget: int | None = None, sample_size: int | None = None, study: optuna.study.Study | None = None, optuna_callbacks: List[Callable[[Study, FrozenTrial], None]] | None = None, verbosity: int | None = None, show_progress_bar: bool = True, model_dir: str | None = None, return_cvbooster: bool | None = None, *, optuna_seed: int | None = None) -> None: ...
    def get_best_booster(self) -> lgb.CVBooster:
        """Return the best cvbooster.

        If the best booster cannot be found, :class:`ValueError` will be raised.
        To prevent the errors, please save boosters by specifying
        both of the ``model_dir`` and the ``return_cvbooster`` arguments of
        :meth:`~optuna.integration.lightgbm.LightGBMTunerCV.__init__`,
        when you resume tuning or you run tuning in parallel.
        """
