from ..core._model import SparkMLModel as SparkMLModel, SparkMlflowModel as SparkMlflowModel, SynapsePredictModel as SynapsePredictModel
from ..utils._functions import BaseFunction as BaseFunction
from azureml.core import Workspace as Workspace
from typing import Any, Mapping

def bind_model(return_types: str, runtime: str, model_alias: str = '', model_uri: str = '', meta_data: Mapping[str, Any] = {}, functions: Mapping[str, BaseFunction] = {}, aml_workspace: Workspace | None = None, num_threads: int = 0, sparkml_model_type: str = '') -> SynapsePredictModel:
    """Wrapper of _create_udf."""
