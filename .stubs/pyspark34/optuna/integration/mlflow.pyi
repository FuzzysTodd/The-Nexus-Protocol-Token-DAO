import optuna
from optuna._experimental import experimental as experimental
from optuna._imports import try_import as try_import
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.trial import TrialState as TrialState

class MLflowCallback:
    '''Callback to track Optuna trials with MLflow.

    This callback adds relevant information that is
    tracked by Optuna to MLflow. The MLflow experiment
    will be named after the Optuna study name.

    Example:

        Add MLflow callback to Optuna optimization.

        .. testsetup::

            import pathlib
            import tempfile

            tempdir = tempfile.mkdtemp()
            YOUR_TRACKING_URI = pathlib.Path(tempdir).as_uri()

        .. testcode::

            import optuna
            from optuna.integration.mlflow import MLflowCallback


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                return (x - 2) ** 2


            mlflc = MLflowCallback(
                tracking_uri=YOUR_TRACKING_URI,
                metric_name="my metric score",
            )

            study = optuna.create_study(study_name="my_study")
            study.optimize(objective, n_trials=10, callbacks=[mlflc])

        .. testcleanup::

            import shutil

            shutil.rmtree(tempdir)

        .. testoutput::
            :hide:
            :options: +NORMALIZE_WHITESPACE

            INFO: \'my_study\' does not exist. Creating a new experiment

    Args:
        tracking_uri:
            The URI of the MLflow tracking server.

            Please refer to `mlflow.set_tracking_uri
            <https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_tracking_uri>`_
            for more details.
        metric_name:
            Name of the metric. Since the metric itself is just a number,
            `metric_name` can be used to give it a name. So you know later
            if it was roc-auc or accuracy.
        nest_trials:
            Flag indicating whether or not trials should be logged as
            nested runs. This is often helpful for aggregating trials
            to a particular study, under a given experiment.
        tag_study_user_attrs:
            Flag indicating whether or not to add the study\'s user attrs
            to the mlflow trial as tags. Please note that when this flag is
            set, key value pairs in study.user_attrs will supersede existing tags.
    '''
    def __init__(self, tracking_uri: str | None = None, metric_name: str = 'value', nest_trials: bool = False, tag_study_user_attrs: bool = False) -> None: ...
    def __call__(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> None: ...
