import mlflow
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.data.dataset import Dataset as Dataset
from mlflow.entities import RunTag as RunTag
from mlflow.entities.dataset_input import DatasetInput as DatasetInput
from mlflow.entities.input_tag import InputTag as InputTag
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.validation import MetricThreshold as MetricThreshold, ModelValidationFailedException as ModelValidationFailedException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils.annotations import developer_stable as developer_stable
from mlflow.utils.file_utils import TempDir as TempDir
from mlflow.utils.mlflow_tags import MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT
from mlflow.utils.proto_json_utils import NumpyEncoder as NumpyEncoder
from mlflow.utils.string_utils import generate_feature_name_if_not_string as generate_feature_name_if_not_string
from typing import Any, Dict

class _ModelType:
    REGRESSOR: str
    CLASSIFIER: str
    QUESTION_ANSWERING: str
    TEXT_SUMMARIZATION: str
    TEXT: str
    def __init__(self) -> None: ...
    @classmethod
    def values(cls): ...

class EvaluationMetric:
    '''
    A model evaluation metric.

    :param eval_fn:
        A function that computes the metric with the following signature:

        .. code-block:: python

            def eval_fn(
                eval_df: Union[pandas.Dataframe, pyspark.sql.DataFrame],
                builtin_metrics: Dict[str, float],
            ) -> float:
                """
                :param eval_df:
                    A Pandas or Spark DataFrame containing ``prediction`` and ``target`` column.
                    The ``prediction`` column contains the predictions made by the model.
                    The ``target`` column contains the corresponding labels to the predictions made
                    on that row.
                :param builtin_metrics:
                    A dictionary containing the metrics calculated by the default evaluator.
                    The keys are the names of the metrics and the values are the scalar values of
                    the metrics. Refer to the DefaultEvaluator behavior section for what metrics
                    will be returned based on the type of model (i.e. classifier or regressor).
                :return:
                    The metric value.
                """
                ...

    :param name: The name of the metric.
    :param greater_is_better: Whether a higher value of the metric is better.
    :param long_name: (Optional) The long name of the metric. For example,
        ``"root_mean_squared_error"`` for ``"mse"``.
    '''
    eval_fn: Incomplete
    name: Incomplete
    greater_is_better: Incomplete
    long_name: Incomplete
    def __init__(self, eval_fn, name, greater_is_better, long_name: Incomplete | None = None) -> None: ...

def make_metric(*, eval_fn, greater_is_better, name: Incomplete | None = None, long_name: Incomplete | None = None):
    '''
    A factory function to create an :py:class:`EvaluationMetric` object.

    :param eval_fn:
        A function that computes the metric with the following signature:

        .. code-block:: python

            def eval_fn(
                eval_df: Union[pandas.Dataframe, pyspark.sql.DataFrame],
                builtin_metrics: Dict[str, float],
            ) -> float:
                """
                :param eval_df:
                    A Pandas or Spark DataFrame containing ``prediction`` and ``target`` column.
                    The ``prediction`` column contains the predictions made by the model.
                    The ``target`` column contains the corresponding labels to the predictions made
                    on that row.
                :param builtin_metrics:
                    A dictionary containing the metrics calculated by the default evaluator.
                    The keys are the names of the metrics and the values are the scalar values of
                    the metrics. Refer to the DefaultEvaluator behavior section for what metrics
                    will be returned based on the type of model (i.e. classifier or regressor).
                :return:
                    The metric value.
                """
                ...

    :param greater_is_better: Whether a higher value of the metric is better.
    :param name: The name of the metric. This argument must be specified if ``eval_fn`` is a lambda
                 function or the ``eval_fn.__name__`` attribute is not available.
    :param long_name: (Optional) The long name of the metric. For example, ``"mean_squared_error"``
        for ``"mse"``.

    .. seealso::

        - :py:class:`mlflow.models.EvaluationMetric`
        - :py:func:`mlflow.evaluate`
    '''

class EvaluationArtifact(metaclass=ABCMeta):
    """
    A model evaluation artifact containing an artifact uri and content.
    """
    def __init__(self, uri, content: Incomplete | None = None) -> None: ...
    @property
    def content(self):
        """
        The content of the artifact (representation varies)
        """
    @property
    def uri(self) -> str:
        """
        The URI of the artifact
        """

class EvaluationResult:
    """
    Represents the model evaluation outputs of a `mlflow.evaluate()` API call, containing
    both scalar metrics and output artifacts such as performance plots.
    """
    def __init__(self, metrics, artifacts, baseline_model_metrics: Incomplete | None = None) -> None: ...
    @classmethod
    def load(cls, path):
        """Load the evaluation results from the specified local filesystem path"""
    def save(self, path) -> None:
        """Write the evaluation results to the specified local filesystem path"""
    @property
    def metrics(self) -> Dict[str, Any]:
        """
        A dictionary mapping scalar metric names to scalar metric values
        """
    @property
    def artifacts(self) -> Dict[str, 'mlflow.models.EvaluationArtifact']:
        '''
        A dictionary mapping standardized artifact names (e.g. "roc_data") to
        artifact content and location information
        '''
    @property
    def baseline_model_metrics(self) -> Dict[str, Any]:
        """
        A dictionary mapping scalar metric names to scalar metric values for the baseline model
        """

class EvaluationDataset:
    """
    An input dataset for model evaluation. This is intended for use with the
    :py:func:`mlflow.models.evaluate()`
    API.
    """
    NUM_SAMPLE_ROWS_FOR_HASH: int
    SPARK_DATAFRAME_LIMIT: int
    def __init__(self, data, *, targets: Incomplete | None = None, name: Incomplete | None = None, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> None:
        """
        The values of the constructor arguments comes from the `evaluate` call.
        """
    @property
    def feature_names(self): ...
    @property
    def features_data(self):
        """
        return features data as a numpy array or a pandas DataFrame.
        """
    @property
    def labels_data(self):
        """
        return labels data as a numpy array
        """
    @property
    def has_targets(self):
        """
        Returns True if the dataset has targets, False otherwise.
        """
    @property
    def targets_name(self):
        """
        return targets name
        """
    @property
    def name(self):
        """
        Dataset name, which is specified dataset name or the dataset hash if user don't specify
        name.
        """
    @property
    def path(self):
        """
        Dataset path
        """
    @property
    def hash(self):
        """
        Dataset hash, includes hash on first 20 rows and last 20 rows.
        """
    def __hash__(self): ...
    def __eq__(self, other): ...

class ModelEvaluator(metaclass=ABCMeta):
    @abstractmethod
    def can_evaluate(self, *, model_type, evaluator_config, **kwargs) -> bool:
        '''
        :param model_type: A string describing the model type (e.g., "regressor", "classifier", …).
        :param evaluator_config: A dictionary of additional configurations for
                                 the evaluator.
        :param kwargs: For forwards compatibility, a placeholder for additional arguments
                       that may be added to the evaluation interface in the future.
        :return: True if the evaluator can evaluate the specified model on the
                 specified dataset. False otherwise.
        '''
    @abstractmethod
    def evaluate(self, *, model, model_type, dataset, run_id, evaluator_config, custom_metrics: Incomplete | None = None, custom_artifacts: Incomplete | None = None, baseline_model: Incomplete | None = None, **kwargs):
        '''
        The abstract API to log metrics and artifacts, and return evaluation results.

        :param model: A pyfunc model instance, used as the candidate_model
                      to be compared with baseline_model (specified by the `baseline_model` param)
                      for model validation.
        :param model_type: A string describing the model type
                           (e.g., ``"regressor"``, ``"classifier"``, …).
        :param dataset: An instance of `mlflow.models.evaluation.base._EvaluationDataset`
                        containing features and labels (optional) for model evaluation.
        :param run_id: The ID of the MLflow Run to which to log results.
        :param evaluator_config: A dictionary of additional configurations for
                                 the evaluator.
        :param custom_metrics: A list of :py:class:`EvaluationMetric` objects.
        :param custom_artifacts: A list of callable custom artifact functions.
        :param kwargs: For forwards compatibility, a placeholder for additional arguments that
                       may be added to the evaluation interface in the future.
        :param baseline_model: (Optional) A string URI referring to a MLflow model with the pyfunc
                                          flavor as a baseline model to be compared with the
                                          candidate model (specified by the `model` param) for model
                                          validation. (pyfunc model instance is not allowed)
        :return: A :py:class:`mlflow.models.EvaluationResult` instance containing
                 evaluation metrics for candidate model and baseline model and
                 artifacts for candidate model.
        '''

def list_evaluators():
    """
    Return a name list for all available Evaluators.
    """
def evaluate(model: str, data, *, model_type: str, targets: Incomplete | None = None, dataset_path: Incomplete | None = None, feature_names: list = None, evaluators: Incomplete | None = None, evaluator_config: Incomplete | None = None, custom_metrics: Incomplete | None = None, custom_artifacts: Incomplete | None = None, validation_thresholds: Incomplete | None = None, baseline_model: Incomplete | None = None, env_manager: str = 'local'):
    '''
    Evaluate a PyFunc model on the specified dataset using one or more specified ``evaluators``, and
    log resulting metrics & artifacts to MLflow Tracking. Set thresholds on the generated metrics to
    validate model quality. For additional overview information, see
    :ref:`the Model Evaluation documentation <model-evaluation>`.

    Default Evaluator behavior:
     - The default evaluator, which can be invoked with ``evaluators="default"`` or
       ``evaluators=None``, supports the ``"regressor"`` and ``"classifier"`` model types.
       It generates a variety of model performance metrics, model performance plots, and
       model explanations.

     - For both the ``"regressor"`` and ``"classifier"`` model types, the default evaluator
       generates model summary plots and feature importance plots using
       `SHAP <https://shap.readthedocs.io/en/latest/index.html>`_.

     - For regressor models, the default evaluator additionally logs:
        - **metrics**: example_count, mean_absolute_error, mean_squared_error,
          root_mean_squared_error, sum_on_target, mean_on_target, r2_score, max_error,
          mean_absolute_percentage_error.

     - For binary classifiers, the default evaluator additionally logs:
        - **metrics**: true_negatives, false_positives, false_negatives, true_positives, recall,
          precision, f1_score, accuracy_score, example_count, log_loss, roc_auc,
          precision_recall_auc.
        - **artifacts**: lift curve plot, precision-recall plot, ROC plot.

     - For multiclass classifiers, the default evaluator additionally logs:
        - **metrics**: accuracy_score, example_count, f1_score_micro, f1_score_macro, log_loss
        - **artifacts**: A CSV file for "per_class_metrics" (per-class metrics includes
          true_negatives/false_positives/false_negatives/true_positives/recall/precision/roc_auc,
          precision_recall_auc), precision-recall merged curves plot, ROC merged curves plot.

     - For question-answering models, the default evaluator logs:
        - **metrics**: ``exact_match``, `mean_perplexity`_ (requires `evaluate`_, `pytorch`_,
          `transformers`_), `toxicity_ratio`_ (requires `evaluate`_, `pytorch`_, `transformers`_),
          `mean_ari_grade_level`_ (requires `textstat`_), `mean_flesch_kincaid_grade_level`_
          (requires `textstat`_).
        - **artifacts**: A JSON file containing the inputs, outputs, targets (if the ``targets``
          argument is supplied), and per-row metrics of the model in tabular format.

        .. _mean_perplexity:
            https://huggingface.co/spaces/evaluate-metric/perplexity

        .. _toxicity_ratio:
            https://huggingface.co/spaces/evaluate-measurement/toxicity

        .. _pytorch:
            https://pytorch.org/get-started/locally/

        .. _transformers:
            https://huggingface.co/docs/transformers/installation

        .. _mean_ari_grade_level:
            https://en.wikipedia.org/wiki/Automated_readability_index

        .. _mean_flesch_kincaid_grade_level:
            https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level

        .. _evaluate:
            https://pypi.org/project/evaluate

        .. _textstat:
            https://pypi.org/project/textstat

     - For text-summarization models, the default evaluator logs:
        - **metrics**: `ROUGE`_ (requires `evaluate`_, `nltk`_, and `rouge_score`_ to be installed),
          `mean_perplexity`_ (requires `evaluate`_, `pytorch`_,
          `transformers`_), `toxicity_ratio`_ (requires `evaluate`_, `pytorch`_, `transformers`_),
          `mean_ari_grade_level`_ (requires `textstat`_), `mean_flesch_kincaid_grade_level`_
          (requires `textstat`_).
        - **artifacts**: A JSON file containing the inputs, outputs, targets (if the ``targets``
          argument is supplied), and per-row metrics of the model in the tabular format.

        .. _ROUGE:
            https://huggingface.co/spaces/evaluate-metric/rouge

        .. _mean_perplexity:
            https://huggingface.co/spaces/evaluate-metric/perplexity

        .. _toxicity_ratio:
            https://huggingface.co/spaces/evaluate-measurement/toxicity

        .. _pytorch:
            https://pytorch.org/get-started/locally/

        .. _transformers:
            https://huggingface.co/docs/transformers/installation

        .. _mean_ari_grade_level:
            https://en.wikipedia.org/wiki/Automated_readability_index

        .. _mean_flesch_kincaid_grade_level:
            https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level

        .. _evaluate:
            https://pypi.org/project/evaluate

        .. _nltk:
            https://pypi.org/project/nltk

        .. _rouge_score:
            https://pypi.org/project/rouge-score

        .. _textstat:
            https://pypi.org/project/textstat

     - For text models, the default evaluator logs:
        - **metrics**: `mean_perplexity`_ (requires `evaluate`_, `pytorch`_,
          `transformers`_), `toxicity_ratio`_ (requires `evaluate`_, `pytorch`_, `transformers`_),
          `mean_ari_grade_level`_ (requires `textstat`_), `mean_flesch_kincaid_grade_level`_
          (requires `textstat`_).
        - **artifacts**: A JSON file containing the inputs, outputs, targets (if the ``targets``
          argument is supplied), and per-row metrics of the model in tabular format.

        .. _evaluate:
            https://pypi.org/project/evaluate

        .. _mean_perplexity:
            https://huggingface.co/spaces/evaluate-metric/perplexity

        .. _toxicity_ratio:
            https://huggingface.co/spaces/evaluate-measurement/toxicity

        .. _pytorch:
            https://pytorch.org/get-started/locally/

        .. _transformers:
            https://huggingface.co/docs/transformers/installation

        .. _mean_ari_grade_level:
            https://en.wikipedia.org/wiki/Automated_readability_index

        .. _mean_flesch_kincaid_grade_level:
            https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level

        .. _textstat:
            https://pypi.org/project/textstat

     - For sklearn models, the default evaluator additionally logs the model\'s evaluation criterion
       (e.g. mean accuracy for a classifier) computed by `model.score` method.

     - The metrics/artifacts listed above are logged to the active MLflow run.
       If no active run exists, a new MLflow run is created for logging these metrics and
       artifacts. Note that no metrics/artifacts are logged for the ``baseline_model``.

     - Additionally, information about the specified dataset - hash, name (if specified), path
       (if specified), and the UUID of the model that evaluated it - is logged to the
       ``mlflow.datasets`` tag.

     - The available ``evaluator_config`` options for the default evaluator include:
        - **log_model_explainability**: A boolean value specifying whether or not to log model
          explainability insights, default value is True.
        - **explainability_algorithm**: A string to specify the SHAP Explainer algorithm for model
          explainability. Supported algorithm includes: \'exact\', \'permutation\', \'partition\',
          \'kernel\'.
          If not set, ``shap.Explainer`` is used with the "auto" algorithm, which chooses the best
          Explainer based on the model.
        - **explainability_nsamples**: The number of sample rows to use for computing model
          explainability insights. Default value is 2000.
        - **explainability_kernel_link**: The kernel link function used by shap kernal explainer.
          Available values are "identity" and "logit". Default value is "identity".
        - **max_classes_for_multiclass_roc_pr**:
          For multiclass classification tasks, the maximum number of classes for which to log
          the per-class ROC curve and Precision-Recall curve. If the number of classes is
          larger than the configured maximum, these curves are not logged.
        - **metric_prefix**: An optional prefix to prepend to the name of each metric and artifact
          produced during evaluation.
        - **log_metrics_with_dataset_info**: A boolean value specifying whether or not to include
          information about the evaluation dataset in the name of each metric logged to MLflow
          Tracking during evaluation, default value is True.
        - **pos_label**: If specified, the positive label to use when computing classification
          metrics such as precision, recall, f1, etc. for binary classification models. For
          multiclass classification and regression models, this parameter will be ignored.
        - **average**: The averaging method to use when computing classification metrics such as
          precision, recall, f1, etc. for multiclass classification models
          (default: ``\'weighted\'``). For binary classification and regression models, this
          parameter will be ignored.
        - **sample_weights**: Weights for each sample to apply when computing model performance
          metrics.

     - Limitations of evaluation dataset:
        - For classification tasks, dataset labels are used to infer the total number of classes.
        - For binary classification tasks, the negative label value must be 0 or -1 or False, and
          the positive label value must be 1 or True.

     - Limitations of metrics/artifacts computation:
        - For classification tasks, some metric and artifact computations require the model to
          output class probabilities. Currently, for scikit-learn models, the default evaluator
          calls the ``predict_proba`` method on the underlying model to obtain probabilities. For
          other model types, the default evaluator does not compute metrics/artifacts that require
          probability outputs.

     - Limitations of default evaluator logging model explainability insights:
        - The ``shap.Explainer`` ``auto`` algorithm uses the ``Linear`` explainer for linear models
          and the ``Tree`` explainer for tree models. Because SHAP\'s ``Linear`` and ``Tree``
          explainers do not support multi-class classification, the default evaluator falls back to
          using the ``Exact`` or ``Permutation`` explainers for multi-class classification tasks.
        - Logging model explainability insights is not currently supported for PySpark models.
        - The evaluation dataset label values must be numeric or boolean, all feature values
          must be numeric, and each feature column must only contain scalar values.

     - Limitations when environment restoration is enabled:
        - When environment restoration is enabled for the evaluated model (i.e. a non-local
          ``env_manager`` is specified), the model is loaded as a client that invokes a MLflow
          Model Scoring Server process in an independent Python environment with the model\'s
          training time dependencies installed. As such, methods like ``predict_proba`` (for
          probability outputs) or ``score`` (computes the evaluation criterian for sklearn models)
          of the model become inaccessible and the default evaluator does not compute metrics or
          artifacts that require those methods.
        - Because the model is an MLflow Model Server process, SHAP explanations are slower to
          compute. As such, model explainaibility is disabled when a non-local ``env_manager``
          specified, unless the ``evaluator_config`` option **log_model_explainability** is
          explicitly set to ``True``.

    :param model: A pyfunc model instance, or a URI referring to such a model.

    :param data: One of the following:

                 - A numpy array or list of evaluation features, excluding labels.

                 - A Pandas DataFrame or Spark DataFrame, containing evaluation features and
                   labels. If ``feature_names`` argument not specified, all columns are regarded
                   as feature columns. Otherwise, only column names present in ``feature_names``
                   are regarded as feature columns. If it is Spark DataFrame, only the first 10000
                   rows in the Spark DataFrame will be used as evaluation data.

                 - A :py:class`mlflow.data.dataset.Dataset` instance containing evaluation features
                   and labels.

    :param targets: If ``data`` is a numpy array or list, a numpy array or list of evaluation
                    labels. If ``data`` is a DataFrame, the string name of a column from ``data``
                    that contains evaluation labels. Required for classifier and regressor models,
                    but optional for question-answering, text-summarization, and text models. If
                    ``data`` is a :py:class`mlflow.data.dataset.Dataset` that defines targets,
                    then ``targets`` is optional.

    :param model_type: A string describing the model type. The default evaluator
                       supports the following model types:

                       - ``\'classifier\'``
                       - ``\'regressor\'``
                       - ``\'question-answering\'``
                       - ``\'text-summarization\'``
                       - ``\'text\'``

                       .. note::
                            ``\'question-answering\'``, ``\'text-summarization\'``, and ``\'text\'``
                            are experimental and may be changed or removed in a future release.

    :param dataset_path: (Optional) The path where the data is stored. Must not contain double
                         quotes (``“``). If specified, the path is logged to the ``mlflow.datasets``
                         tag for lineage tracking purposes.

    :param feature_names: (Optional) If the ``data`` argument is a feature data numpy array or list,
                          ``feature_names`` is a list of the feature names for each feature. If
                          ``None``, then the ``feature_names`` are generated using the format
                          ``feature_{feature_index}``. If the ``data`` argument is a Pandas
                          DataFrame or a Spark DataFrame, ``feature_names`` is a list of the names
                          of the feature columns in the DataFrame. If ``None``, then all columns
                          except the label column are regarded as feature columns.

    :param evaluators: The name of the evaluator to use for model evaluation, or a list of
                       evaluator names. If unspecified, all evaluators capable of evaluating the
                       specified model on the specified dataset are used. The default evaluator
                       can be referred to by the name ``"default"``. To see all available
                       evaluators, call :py:func:`mlflow.models.list_evaluators`.

    :param evaluator_config: A dictionary of additional configurations to supply to the evaluator.
                             If multiple evaluators are specified, each configuration should be
                             supplied as a nested dictionary whose key is the evaluator name.

    :param custom_metrics:
        (Optional) A list of :py:class:`EvaluationMetric <mlflow.models.EvaluationMetric>` objects.

        .. code-block:: python
            :caption: Example usage of custom metrics

            import mlflow
            import numpy as np


            def root_mean_squared_error(eval_df, _builtin_metrics):
                return np.sqrt((np.abs(eval_df["prediction"] - eval_df["target"]) ** 2).mean)


            rmse_metric = mlflow.models.make_metric(
                eval_fn=root_mean_squared_error,
                greater_is_better=False,
            )
            mlflow.evaluate(..., custom_metrics=[rmse_metric])

    :param custom_artifacts:
        (Optional) A list of custom artifact functions with the following signature:

        .. code-block:: python

            def custom_artifact(
                eval_df: Union[pandas.Dataframe, pyspark.sql.DataFrame],
                builtin_metrics: Dict[str, float],
                artifacts_dir: str,
            ) -> Dict[str, Any]:
                """
                :param eval_df:
                    A Pandas or Spark DataFrame containing ``prediction`` and ``target`` column.
                    The ``prediction`` column contains the predictions made by the model.
                    The ``target`` column contains the corresponding labels to the predictions made
                    on that row.
                :param builtin_metrics:
                    A dictionary containing the metrics calculated by the default evaluator.
                    The keys are the names of the metrics and the values are the scalar values of
                    the metrics. Refer to the DefaultEvaluator behavior section for what metrics
                    will be returned based on the type of model (i.e. classifier or regressor).
                :param artifacts_dir:
                    A temporary directory path that can be used by the custom artifacts function to
                    temporarily store produced artifacts. The directory will be deleted after the
                    artifacts are logged.
                :return:
                    A dictionary that maps artifact names to artifact objects
                    (e.g. a Matplotlib Figure) or to artifact paths within ``artifacts_dir``.
                """
                ...

        Object types that artifacts can be represented as:

            - A string uri representing the file path to the artifact. MLflow will infer the type of
              the artifact based on the file extension.
            - A string representation of a JSON object. This will be saved as a .json artifact.
            - Pandas DataFrame. This will be resolved as a CSV artifact.
            - Numpy array. This will be saved as a .npy artifact.
            - Matplotlib Figure. This will be saved as an image artifact. Note that
              ``matplotlib.pyplot.savefig`` is called behind the scene with default configurations.
              To customize, either save the figure with the desired configurations and return its
              file path or define customizations through environment variables in
              ``matplotlib.rcParams``.
            - Other objects will be attempted to be pickled with the default protocol.

        .. code-block:: python
            :caption: Example usage of custom artifacts

            import mlflow
            import matplotlib.pyplot as plt


            def scatter_plot(eval_df, builtin_metrics, artifacts_dir):
                plt.scatter(eval_df["prediction"], eval_df["target"])
                plt.xlabel("Targets")
                plt.ylabel("Predictions")
                plt.title("Targets vs. Predictions")
                plt.savefig(os.path.join(artifacts_dir, "example.png"))
                plt.close()
                return {"pred_target_scatter": os.path.join(artifacts_dir, "example.png")}


            def pred_sample(eval_df, _builtin_metrics, _artifacts_dir):
                return {"pred_sample": pred_sample.head(10)}


            mlflow.evaluate(..., custom_artifacts=[scatter_plot, pred_sample])

    :param validation_thresholds: (Optional) A dictionary of metric name to
        :py:class:`mlflow.models.MetricThreshold` used for model validation. Each metric name must
        either be the name of a builtin metric or the name of a custom metric defined in the
        ``custom_metrics`` parameter.

        .. code-block:: python
            :caption: Example of Model Validation

            from mlflow.models import MetricThreshold

            thresholds = {
                "accuracy_score": MetricThreshold(
                    # accuracy should be >=0.8
                    threshold=0.8,
                    # accuracy should be at least 5 percent greater than baseline model accuracy
                    min_absolute_change=0.05,
                    # accuracy should be at least 0.05 greater than baseline model accuracy
                    min_relative_change=0.05,
                    greater_is_better=True,
                ),
            }

            with mlflow.start_run():
                mlflow.evaluate(
                    model=your_candidate_model,
                    data,
                    targets,
                    model_type,
                    dataset_name,
                    evaluators,
                    validation_thresholds=thresholds,
                    baseline_model=your_baseline_model,
                )

        See :ref:`the Model Validation documentation <model-validation>`
        for more details.

    :param baseline_model: (Optional) A string URI referring to an MLflow model with the pyfunc
                           flavor. If specified, the candidate ``model`` is compared to this
                           baseline for model validation purposes.

    :param env_manager: Specify an environment manager to load the candidate ``model`` and
                        ``baseline_model`` in isolated Python evironments and restore their
                        dependencies. Default value is ``local``, and the following values are
                        supported:

                         - ``virtualenv``: (Recommended) Use virtualenv to restore the python
                           environment that was used to train the model.
                         - ``conda``:  Use Conda to restore the software environment that was used
                           to train the model.
                         - ``local``: Use the current Python environment for model inference, which
                           may differ from the environment used to train the model and may lead to
                           errors or invalid predictions.

    :return: An :py:class:`mlflow.models.EvaluationResult` instance containing
             metrics of candidate model and baseline model, and artifacts of candidate model.
    '''
