from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_DEFAULT_PREDICTION_DEVICE as MLFLOW_DEFAULT_PREDICTION_DEVICE, MLFLOW_HUGGINGFACE_DEVICE_MAP_STRATEGY as MLFLOW_HUGGINGFACE_DEVICE_MAP_STRATEGY, MLFLOW_HUGGINGFACE_DISABLE_ACCELERATE_FEATURES as MLFLOW_HUGGINGFACE_DISABLE_ACCELERATE_FEATURES, MLFLOW_HUGGINGFACE_MODEL_MAX_SHARD_SIZE as MLFLOW_HUGGINGFACE_MODEL_MAX_SHARD_SIZE, MLFLOW_HUGGINGFACE_USE_DEVICE_MAP as MLFLOW_HUGGINGFACE_USE_DEVICE_MAP, MLFLOW_HUGGINGFACE_USE_LOW_CPU_MEM_USAGE as MLFLOW_HUGGINGFACE_USE_LOW_CPU_MEM_USAGE
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature, infer_pip_requirements as infer_pip_requirements, infer_signature as infer_signature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.types.schema import ColSpec as ColSpec, Schema as Schema, TensorSpec as TensorSpec
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, docstring_version_compatibility_warning as docstring_version_compatibility_warning, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict, List, NamedTuple

FLAVOR_NAME: str

def get_default_pip_requirements(model) -> List[str]:
    """
    :param model: The model instance to be saved in order to provide the required underlying
                  deep learning execution framework dependency requirements. Note that this must
                  be the actual model instance and not a Pipeline.
    :return: A list of default pip requirements for MLflow Models that have been produced with the
             ``transformers`` flavor. Calls to :py:func:`save_model()` and :py:func:`log_model()`
             produce a pip environment that contain these requirements at a minimum.
    """
def get_default_conda_env(model):
    """
    :return: The default Conda environment for MLflow Models produced with the ``transformers``
             flavor, based on the model instance framework type of the model to be logged.
    """
def save_model(transformers_model, path: str, processor: Incomplete | None = None, task: str | None = None, model_card: Incomplete | None = None, inference_config: Dict[str, Any] | None = None, code_paths: List[str] | None = None, mlflow_model: Model | None = None, signature: ModelSignature | None = None, input_example: ModelInputExample | None = None, pip_requirements: List[str] | str | None = None, extra_pip_requirements: List[str] | str | None = None, conda_env: Incomplete | None = None, metadata: Dict[str, Any] = None, **kwargs) -> None:
    '''
    Save a trained transformers model to a path on the local file system.

    :param transformers_model:
        A trained transformers `Pipeline` or a dictionary that maps required components of a
        pipeline to the named keys of ["model", "image_processor", "tokenizer",
        "feature_extractor"]. The `model` key in the dictionary must map to a value that inherits
        from `PreTrainedModel`, `TFPreTrainedModel`, or `FlaxPreTrainedModel`.
        All other component entries in the dictionary must support the defined task type that is
        associated with the base model type configuration.

        An example of supplying component-level parts of a transformers model is shown below:

        .. code-block:: python

          from transformers import MobileBertForQuestionAnswering, AutoTokenizer

          architecture = "csarron/mobilebert-uncased-squad-v2"
          tokenizer = AutoTokenizer.from_pretrained(architecture)
          model = MobileBertForQuestionAnswering.from_pretrained(architecture)

          with mlflow.start_run():
              components = {
                  "model": model,
                  "tokenizer": tokenizer,
              }
              mlflow.transformers.save_model(
                  transformers_model=components,
                  path="path/to/save/model",
              )

        An example of submitting a `Pipeline` from a default pipeline instantiation:

        .. code-block:: python

          from transformers import pipeline

          qa_pipe = pipeline("question-answering", "csarron/mobilebert-uncased-squad-v2")

          with mlflow.start_run():
              mlflow.transformers.save_model(
                  transformers_model=qa_pipe,
                  path="path/to/save/model",
              )

    :param path: Local path destination for the serialized model to be saved.
    :param processor: An optional ``Processor`` subclass object. Some model architectures,
                      particularly multi-modal types, utilize Processors to combine text
                      encoding and image or audio encoding in a single entrypoint.

                      .. Note:: If a processor is supplied when saving a model, the
                                model will be unavailable for loading as a ``Pipeline`` or for
                                usage with pyfunc inference.

    :param task: The transformers-specific task type of the model. These strings are utilized so
                 that a pipeline can be created with the appropriate internal call architecture
                 to meet the needs of a given model. If this argument is not specified, the
                 pipeline utilities within the transformers library will be used to infer the
                 correct task type. If the value specified is not a supported type within the
                 version of transformers that is currently installed, an Exception will be thrown.
    :param model_card: An Optional `ModelCard` instance from `huggingface-hub`. If provided, the
                       contents of the model card will be saved along with the provided
                       `transformers_model`. If not provided, an attempt will be made to fetch
                       the card from the base pretrained model that is provided (or the one that is
                       included within a provided `Pipeline`).

                       .. Note:: In order for a ModelCard to be fetched (if not provided),
                                 the huggingface_hub package must be installed and the version
                                 must be >=0.10.0

    :param inference_config:
        A dict of valid overrides that can be applied to a pipeline instance during inference.
        These arguments are used exclusively for the case of loading the model as a ``pyfunc``
        Model or for use in Spark.
        These values are not applied to a returned Pipeline from a call to
        ``mlflow.transformers.load_model()``

        .. Warning:: If the key provided is not compatible with either the
                  Pipeline instance for the task provided or is not a valid
                  override to any arguments available in the Model, an
                  Exception will be raised at runtime. It is very important
                  to validate the entries in this dictionary to ensure
                  that they are valid prior to saving or logging.

        An example of providing overrides for a question generation model:

        .. code-block:: python

            from transformers import pipeline, AutoTokenizer

            task = "text-generation"
            architecture = "gpt2"

            sentence_pipeline = pipeline(
                task=task, tokenizer=AutoTokenizer.from_pretrained(architecture), model=architecture
            )

            # Validate that the overrides function
            prompts = ["Generative models are", "I\'d like a coconut so that I can"]

            # validation of config prior to save or log
            inference_config = {
                "top_k": 2,
                "num_beams": 5,
                "max_length": 30,
                "temperature": 0.62,
                "top_p": 0.85,
                "repetition_penalty": 1.15,
            }

            # Verify that no exceptions are thrown
            sentence_pipeline(prompts, **inference_config)

            mlflow.transformers.save_model(
                transformers_model=sentence_pipeline,
                path="/path/for/model",
                task=task,
                inference_config=inference_config,
            )

    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: An MLflow model object that specifies the flavor that this model is being
                         added to.
    :param signature: A Model Signature object that describes the input and output Schema of the
                      model. The model signature can be inferred using `infer_signature` function
                      of `mlflow.models.signature`.
                      Example:

                      .. code-block:: python

                        from mlflow.models import infer_signature
                        from mlflow.transformers import generate_signature_output
                        from transformers import pipeline

                        en_to_de = pipeline("translation_en_to_de")

                        data = "MLflow is great!"
                        output = generate_signature_output(en_to_de, data)
                        signature = infer_signature(data, output)

                        mlflow.transformers.save_model(
                            transformers_model=en_to_de,
                            path="/path/to/save/model",
                            signature=signature,
                            input_example=data,
                        )

                        loaded = mlflow.pyfunc.load_model("/path/to/save/model")
                        print(loaded.predict(data))
                        # MLflow ist großartig!

                      If an input_example is provided and the signature is not, a signature will
                      be inferred automatically and applied to the MLmodel file iff the
                      pipeline type is a text-based model (NLP). If the pipeline type is not
                      a supported type, this inference functionality will not function correctly
                      and a warning will be issued. In order to ensure that a precise signature
                      is logged, it is recommended to explicitly provide one.
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param conda_env: {{ conda_env }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    :param kwargs: Optional additional configurations for transformers serialization.
    :return: None
    '''
def log_model(transformers_model, artifact_path: str, processor: Incomplete | None = None, task: str | None = None, model_card: Incomplete | None = None, inference_config: Dict[str, Any] | None = None, code_paths: List[str] | None = None, registered_model_name: str = None, signature: ModelSignature | None = None, input_example: ModelInputExample | None = None, await_registration_for=..., pip_requirements: List[str] | str | None = None, extra_pip_requirements: List[str] | str | None = None, conda_env: Incomplete | None = None, metadata: Dict[str, Any] = None, **kwargs):
    '''
    Log a ``transformers`` object as an MLflow artifact for the current run.

    :param transformers_model:
        A trained transformers `Pipeline` or a dictionary that maps required components of a
        pipeline to the named keys of ["model", "image_processor", "tokenizer",
        "feature_extractor"]. The `model` key in the dictionary must map to a value that inherits
        from `PreTrainedModel`, `TFPreTrainedModel`, or `FlaxPreTrainedModel`.
        All other component entries in the dictionary must support the defined task type that is
        associated with the base model type configuration.

        An example of supplying component-level parts of a transformers model is shown below:

        .. code-block:: python

          from transformers import MobileBertForQuestionAnswering, AutoTokenizer

          architecture = "csarron/mobilebert-uncased-squad-v2"
          tokenizer = AutoTokenizer.from_pretrained(architecture)
          model = MobileBertForQuestionAnswering.from_pretrained(architecture)

          with mlflow.start_run():
              components = {
                  "model": model,
                  "tokenizer": tokenizer,
              }
              mlflow.transformers.log_model(
                  transformers_model=components,
                  artifact_path="my_model",
              )

        An example of submitting a `Pipeline` from a default pipeline instantiation:

        .. code-block:: python

          from transformers import pipeline

          qa_pipe = pipeline("question-answering", "csarron/mobilebert-uncased-squad-v2")

          with mlflow.start_run():
              mlflow.transformers.log_model(
                  transformers_model=qa_pipe,
                  artifact_path="my_pipeline",
              )

    :param artifact_path: Local path destination for the serialized model to be saved.
    :param processor: An optional ``Processor`` subclass object. Some model architectures,
                  particularly multi-modal types, utilize Processors to combine text
                  encoding and image or audio encoding in a single entrypoint.

                  .. Note:: If a processor is supplied when logging a model, the
                            model will be unavailable for loading as a ``Pipeline`` or for usage
                            with pyfunc inference.

    :param task: The transformers-specific task type of the model. These strings are utilized so
                 that a pipeline can be created with the appropriate internal call architecture
                 to meet the needs of a given model. If this argument is not specified, the
                 pipeline utilities within the transformers library will be used to infer the
                 correct task type. If the value specified is not a supported type within the
                 version of transformers that is currently installed, an Exception will be thrown.
    :param model_card: An Optional `ModelCard` instance from `huggingface-hub`. If provided, the
                       contents of the model card will be saved along with the provided
                       `transformers_model`. If not provided, an attempt will be made to fetch
                       the card from the base pretrained model that is provided (or the one that is
                       included within a provided `Pipeline`).

                       .. Note:: In order for a ModelCard to be fetched (if not provided),
                                 the huggingface_hub package must be installed and the version
                                 must be >=0.10.0

    :param inference_config:
        A dict of valid overrides that can be applied to a pipeline instance during inference.
        These arguments are used exclusively for the case of loading the model as a ``pyfunc``
        Model or for use in Spark.
        These values are not applied to a returned Pipeline from a call to
        ``mlflow.transformers.load_model()``

        .. Warning:: If the key provided is not compatible with either the
                     Pipeline instance for the task provided or is not a valid
                     override to any arguments available in the Model, an
                     Exception will be raised at runtime. It is very important
                     to validate the entries in this dictionary to ensure
                     that they are valid prior to saving or logging.

        An example of providing overrides for a question generation model:

        .. code-block:: python

          from transformers import pipeline, AutoTokenizer

          task = "text-generation"
          architecture = "gpt2"

          sentence_pipeline = pipeline(
              task=task, tokenizer=AutoTokenizer.from_pretrained(architecture), model=architecture
          )

          # Validate that the overrides function
          prompts = ["Generative models are", "I\'d like a coconut so that I can"]

          # validation of config prior to save or log
          inference_config = {
              "top_k": 2,
              "num_beams": 5,
              "max_length": 30,
              "temperature": 0.62,
              "top_p": 0.85,
              "repetition_penalty": 1.15,
          }

          # Verify that no exceptions are thrown
          sentence_pipeline(prompts, **inference_config)

          with mlflow.start_run():
              mlflow.transformers.log_model(
                  transformers_model=sentence_pipeline,
                  artifact_path="my_sentence_generator",
                  task=task,
                  inference_config=inference_config,
              )

    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.
    :param signature: A Model Signature object that describes the input and output Schema of the
                      model. The model signature can be inferred using `infer_signature` function
                      of `mlflow.models.signature`.
                      Example:

                      .. code-block:: python

                        from mlflow.models import infer_signature
                        from mlflow.transformers import generate_signature_output
                        from transformers import pipeline

                        en_to_de = pipeline("translation_en_to_de")

                        data = "MLflow is great!"
                        output = generate_signature_output(en_to_de, data)
                        signature = infer_signature(data, output)

                        with mlflow.start_run() as run:
                            mlflow.transformers.log_model(
                                transformers_model=en_to_de,
                                artifact_path="english_to_german_translator",
                                signature=signature,
                                input_example=data,
                            )

                        model_uri = f"runs:/{run.info.run_id}/english_to_german_translator"
                        loaded = mlflow.pyfunc.load_model(model_uri)

                        print(loaded.predict(data))
                        # MLflow ist großartig!

                      If an input_example is provided and the signature is not, a signature will
                      be inferred automatically and applied to the MLmodel file iff the
                      pipeline type is a text-based model (NLP). If the pipeline type is not
                      a supported type, this inference functionality will not function correctly
                      and a warning will be issued. In order to ensure that a precise signature
                      is logged, it is recommended to explicitly provide one.
    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version
                                   to finish being created and is in ``READY`` status.
                                   By default, the function waits for five minutes.
                                   Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param conda_env: {{ conda_env }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: Additional arguments for :py:class:`mlflow.models.model.Model`
    '''
def load_model(model_uri: str, dst_path: str = None, return_type: str = 'pipeline', device: Incomplete | None = None, **kwargs):
    '''
    Load a ``transformers`` object from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to utilize for downloading the model artifact.
                     This directory must already exist if provided. If unspecified, a local output
                     path will be created.
    :param return_type: A return type modifier for the stored ``transformers`` object.
                        If set as "components", the return type will be a dictionary of the saved
                        individual components of either the ``Pipeline`` or the pre-trained model.
                        The components for NLP-focused models will typically consist of a
                        return representation as shown below with a text-classification example:

                        .. code-block:: python

                          {"model": BertForSequenceClassification, "tokenizer": BertTokenizerFast}

                        Vision models will return an ``ImageProcessor`` instance of the appropriate
                        type, while multi-modal models will return both a ``FeatureExtractor`` and
                        a ``Tokenizer`` along with the model.
                        Returning "components" can be useful for certain model types that do not
                        have the desired pipeline return types for certain use cases.
                        If set as "pipeline", the model, along with any and all required
                        ``Tokenizer``, ``FeatureExtractor``, ``Processor``, or ``ImageProcessor``
                        objects will be returned within a ``Pipeline`` object of the appropriate
                        type defined by the ``task`` set by the model instance type. To override
                        this behavior, supply a valid ``task`` argument during model logging or
                        saving. Default is "pipeline".
    :param device: The device on which to load the model. Default is None. Use 0 to
                   load to the default GPU.
    :param kwargs: Optional configuration options for loading of a ``transformers`` object.
                   For information on parameters and their usage, see
                   `transformers documentation <https://huggingface.co/docs/transformers/index>`_.
    :return: A ``transformers`` model instance or a dictionary of components
    '''
def is_gpu_available(): ...

class _TransformersModel(NamedTuple):
    """
    Type validator class for models that are submitted as a dictionary for saving and logging.
    Usage of this class should always leverage the type-checking from the class method
    'from_dict()' instead of the instance-based configuration that is utilized with instantiating
    a NamedTuple instance (it uses '__new__()' instead of an '__init__()'  dunder method, making
    type validation on instantiation overly complex if we were to support that approach).
    """
    model: Any
    tokenizer: Any = ...
    feature_extractor: Any = ...
    image_processor: Any = ...
    processor: Any = ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, model, tokenizer: Incomplete | None = None, feature_extractor: Incomplete | None = None, image_processor: Incomplete | None = None, processor: Incomplete | None = None, **kwargs): ...

def generate_signature_output(pipeline, data, inference_config: Incomplete | None = None):
    """
    Utility for generating the response output for the purposes of extracting an output signature
    for model saving and logging. This function simulates loading of a saved model or pipeline
    as a ``pyfunc`` model without having to incur a write to disk.

    :param pipeline: A ``transformers`` pipeline object. Note that component-level or model-level
                     inputs are not permitted for extracting an output example.
    :param data: An example input that is compatible with the given pipeline
    :param inference_config: Any additional inference configuration, provided as kwargs, to inform
                             the format of the output type from a pipeline inference call.
    :return: The output from the ``pyfunc`` pipeline wrapper's ``predict`` method
    """

class _TransformersWrapper:
    pipeline: Incomplete
    flavor_config: Incomplete
    inference_config: Incomplete
    def __init__(self, pipeline, flavor_config: Incomplete | None = None, inference_config: Incomplete | None = None) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def autolog(log_input_examples: bool = False, log_model_signatures: bool = False, log_models: bool = False, log_datasets: bool = False, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, extra_tags: Incomplete | None = None):
    """
    This autologging integration is solely used for disabling spurious autologging of irrelevant
    sub-models that are created during the training and evaluation of transformers-based models.
    Autologging functionality is not implemented fully for the transformers flavor.
    """
