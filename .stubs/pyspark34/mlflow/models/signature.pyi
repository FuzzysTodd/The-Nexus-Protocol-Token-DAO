import numpy as np
import pandas as pd
from _typeshed import Incomplete
from mlflow import environment_variables as environment_variables
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.models.utils import ModelInputExample as ModelInputExample
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository as ModelsArtifactRepository
from mlflow.store.artifact.runs_artifact_repo import RunsArtifactRepository as RunsArtifactRepository
from mlflow.types.schema import ParamSchema as ParamSchema, Schema as Schema
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path
from typing import Any, Dict

MlflowInferableDataset: Incomplete
MlflowInferableDataset = pd.DataFrame | np.ndarray | Dict[str, np.ndarray]

class ModelSignature:
    """
    ModelSignature specifies schema of model's inputs, outputs and params.

    ModelSignature can be :py:func:`inferred <mlflow.models.infer_signature>` from training
    dataset, model predictions using and params for inference, or constructed by hand by
    passing an input and output :py:class:`Schema <mlflow.types.Schema>`, and params
    :py:class:`ParamSchema <mlflow.types.ParamSchema>`.
    """
    inputs: Incomplete
    outputs: Incomplete
    params: Incomplete
    def __init__(self, inputs: Schema, outputs: Schema = None, params: ParamSchema = None) -> None: ...
    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize into a 'jsonable' dictionary.

        Input and output schema are represented as json strings. This is so that the
        representation is compact when embedded in an MLmodel yaml file.

        :return: dictionary representation with input and output schema represented as json strings.
        """
    @classmethod
    def from_dict(cls, signature_dict: Dict[str, Any]):
        '''
        Deserialize from dictionary representation.

        :param signature_dict: Dictionary representation of model signature.
                               Expected dictionary format:
                               `{\'inputs\': <json string>,
                               \'outputs\': <json string>,
                               \'params\': <json string>" }`

        :return: ModelSignature populated with the data form the dictionary.
        '''
    def __eq__(self, other) -> bool: ...

def infer_signature(model_input: Any, model_output: MlflowInferableDataset = None, params: Dict[str, Any] | None = None) -> ModelSignature:
    '''
    Infer an MLflow model signature from the training data (input), model predictions (output)
    and parameters (for inference).

    The signature represents model input and output as data frames with (optionally) named columns
    and data type specified as one of types defined in :py:class:`mlflow.types.DataType`. It also
    includes parameters schema for inference, .
    This method will raise an exception if the user data contains incompatible types or is not
    passed in one of the supported formats listed below.

    The input should be one of these:
      - pandas.DataFrame
      - pandas.Series
      - dictionary of { name -> numpy.ndarray}
      - numpy.ndarray
      - pyspark.sql.DataFrame
      - scipy.sparse.csr_matrix
      - scipy.sparse.csc_matrix

    The element types should be mappable to one of :py:class:`mlflow.types.DataType`.

    For pyspark.sql.DataFrame inputs, columns of type DateType and TimestampType are both inferred
    as type :py:data:`datetime <mlflow.types.DataType.datetime>`, which is coerced to
    TimestampType at inference.

    :param model_input: Valid input to the model. E.g. (a subset of) the training dataset.
    :param model_output: Valid model output. E.g. Model predictions for the (subset of) training
                         dataset.
    :param params: Valid parameters for inference. It should be a dictionary of parameters
                   that can be set on the model during inference by passing `params` to pyfunc
                   `predict` method.

                   An example of valid parameters:

                   .. code-block:: python

                        from mlflow.models import infer_signature
                        from mlflow.transformers import generate_signature_output

                        # Define parameters for inference
                        params = {
                            "num_beams": 5,
                            "max_length": 30,
                            "do_sample": True,
                            "remove_invalid_values": True,
                        }

                        # Infer the signature including parameters
                        signature = infer_signature(
                            data,
                            generate_signature_output(model, data),
                            params=params,
                        )

                        # Saving model with model signature
                        mlflow.transformers.save_model(
                            model,
                            path=model_path,
                            signature=signature,
                        )

                        pyfunc_loaded = mlflow.pyfunc.load_model(model_path)

                        # Passing params to `predict` function directly
                        result = pyfunc_loaded.predict(data, params=params)

                   .. Note:: Experimental: This parameter may change or be removed in a future
                                           release without warning.

    :return: ModelSignature
    '''

class _TypeHints:
    input: Incomplete
    output: Incomplete
    def __init__(self, input_: Incomplete | None = None, output: Incomplete | None = None) -> None: ...

def set_signature(model_uri: str, signature: ModelSignature):
    '''
    Sets the model signature for specified model artifacts.

    The process involves downloading the MLmodel file in the model artifacts (if it\'s non-local),
    updating its model signature, and then overwriting the existing MLmodel file. Should the
    artifact repository associated with the model artifacts disallow overwriting, this function will
    fail.

    Furthermore, as model registry artifacts are read-only, model artifacts located in the
    model registry and represented by ``models:/`` URI schemes are not compatible with this API.
    To set a signature on a model version, first set the signature on the source model artifacts.
    Following this, generate a new model version using the updated model artifacts. For more
    information about setting signatures on model versions, see
    `this doc section <https://www.mlflow.org/docs/latest/models.html#set-signature-on-mv>`_.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

                      Please note that model URIs with the ``models:/`` scheme are not supported.

    :param signature: ModelSignature to set on the model.

    .. code-block:: python
        :caption: Example

        import mlflow
        from mlflow.models import set_signature, infer_signature

        # load model from run artifacts
        run_id = "96771d893a5e46159d9f3b49bf9013e2"
        artifact_path = "models"
        model_uri = "runs:/{}/{}".format(run_id, artifact_path)
        model = mlflow.pyfunc.load_model(model_uri)

        # determine model signature
        test_df = ...
        predictions = model.predict(test_df)
        signature = infer_signature(test_df, predictions)

        # set the signature for the logged model
        set_signature(model_uri, signature)
    '''
