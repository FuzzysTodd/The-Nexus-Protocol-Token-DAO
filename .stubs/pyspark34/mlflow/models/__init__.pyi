from ..utils.environment import infer_pip_requirements as infer_pip_requirements
from .evaluation import EvaluationArtifact as EvaluationArtifact, EvaluationMetric as EvaluationMetric, EvaluationResult as EvaluationResult, MetricThreshold as MetricThreshold, evaluate as evaluate, list_evaluators as list_evaluators, make_metric as make_metric
from .flavor_backend import FlavorBackend as FlavorBackend
from .model import Model as Model, get_model_info as get_model_info
from .signature import ModelSignature as ModelSignature, infer_signature as infer_signature, set_signature as set_signature
from .utils import ModelInputExample as ModelInputExample, add_libraries_to_model as add_libraries_to_model, validate_schema as validate_schema
from _typeshed import Incomplete

__all__ = ['Model', 'FlavorBackend', 'infer_pip_requirements', 'evaluate', 'make_metric', 'EvaluationMetric', 'EvaluationArtifact', 'EvaluationResult', 'get_model_info', 'list_evaluators', 'MetricThreshold', 'build_docker', 'ModelSignature', 'ModelInputExample', 'infer_signature', 'validate_schema', 'add_libraries_to_model', 'set_signature']

def build_docker(model_uri: Incomplete | None = None, name: str = 'mlflow-pyfunc', env_manager=..., mlflow_home: Incomplete | None = None, install_mlflow: bool = False, enable_mlserver: bool = False) -> None:
    '''
    Builds a Docker image whose default entrypoint serves an MLflow model at port 8080, using the
    python_function flavor. The container serves the model referenced by ``model_uri``, if
    specified. If ``model_uri`` is not specified, an MLflow Model directory must be mounted as a
    volume into the /opt/ml/model directory in the container.

    .. warning::

        If ``model_uri`` is unspecified, the resulting image doesn\'t support serving models with
        the RFunc or Java MLeap model servers.

    NB: by default, the container will start nginx and gunicorn processes. If you don\'t need the
    nginx process to be started (for instance if you deploy your container to Google Cloud Run),
    you can disable it via the DISABLE_NGINX environment variable:

    .. code:: bash

        docker run -p 5001:8080 -e DISABLE_NGINX=true "my-image-name"

    See https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html for more information on the
    \'python_function\' flavor.
    '''
