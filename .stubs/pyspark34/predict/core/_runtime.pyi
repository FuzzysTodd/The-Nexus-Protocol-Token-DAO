from ..core._cache import SynapsePredictModelCache as SynapsePredictModelCache
from ..utils._functions import BaseFunction as BaseFunction
from ..utils._model_runtime import ModelRuntime as ModelRuntime
from _typeshed import Incomplete
from typing import Any, Mapping

class RuntimeGenerator:
    """ A class for generating various model runtimes. """
    runtime: Incomplete
    model_alias: Incomplete
    model_uri: Incomplete
    meta_data: Incomplete
    functions: Incomplete
    process_function: Incomplete
    load_function: Incomplete
    predict_function: Incomplete
    num_threads: Incomplete
    supported_runtimes: Incomplete
    supported_runtime_msg: Incomplete
    def __init__(self, runtime: str, model_alias: str = '', model_uri: str = '', meta_data: Mapping[str, Any] = {}, functions: Mapping[str, BaseFunction] = {}, **kwargs) -> None:
        """ Initialize the class.

        Parameters
        ----------
        runtime : str
            Runtime types, should be casted into the enumeration ModelRuntime.
        model_alias : str
        model_uri : str
            File path of the model artifact.
        meta_data: Mapping[str, Any]
        functions: Mapping[str, BaseFunction]
        """
