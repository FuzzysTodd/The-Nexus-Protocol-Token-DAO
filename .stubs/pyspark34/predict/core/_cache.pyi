from ..utils._functions import BaseFunction as BaseFunction
from ..utils._mlflow_convert import convert_to_mlflow as convert_to_mlflow, is_mlflow_model as is_mlflow_model
from ..utils._model_loader import load_model as load_model
from pyspark.sql import SparkSession as SparkSession

class SynapsePredictModelCache:
    """
    Caches models in memory on Spark Executors, to avoid continually reloading from disk.

    This class has to be part of a different module than the one that _uses_ it. This is
    because Spark will pickle classes that are defined in the local scope, but relies on
    Python's module loading behavior for classes in different modules. In this case, we
    are relying on the fact that Python will load a module at-most-once, and can therefore
    store per-process state in a static map.
    """
    TASKS_PER_CPU_CORE: int
