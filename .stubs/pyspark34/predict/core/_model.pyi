from ..core._cache import SynapsePredictModelCache as SynapsePredictModelCache
from _typeshed import Incomplete
from pyspark.ml import Transformer
from pyspark.ml.param.shared import HasInputCols, HasOutputCol
from pyspark.sql import SparkSession as SparkSession
from typing import Callable

class SynapsePredictModel:
    """
    Wrapper of udf and transformer
    """
    udf: Incomplete
    model_alias: Incomplete
    def __init__(self, spark: SparkSession, model_alias: str, udf: Callable) -> None:
        """
        Parameters
        ----------
        spark : SparkSession
            The session to register the udf in.
        model_alias : str
            A unique alias, we will register the udf under the name of hash alias
        udf : Callable
            The udf will be registered.
        """
    def register(self):
        """
        hash the model alias and register the udf under the name of the hash
        spark does not like `/` in the udf name
        """
    def create_transformer(self, inputCols: Incomplete | None = None, outputCol: Incomplete | None = None) -> Transformer:
        """
        Parameters
        ----------
        inputCols : list
            A list of column names, indicate the input columns.
        outputCols : str
            A name of column, indicate the output column.

        Returns
        ----------
        Transformer
        """

class SynapsePredictTransformer(Transformer, HasInputCols, HasOutputCol):
    model: Incomplete
    def __init__(self, model: SynapsePredictModel, inputCols: Incomplete | None = None, outputCol: Incomplete | None = None) -> None: ...
    def setInputCols(self, value): ...
    def setOutputCol(self, value): ...

class SparkMLModel:
    sparkml_model_type: Incomplete
    model_uri: Incomplete
    def __init__(self, sparkml_model_type, model_uri) -> None: ...
    def register(self): ...

class SparkMlflowModel:
    model_uri: Incomplete
    def __init__(self, model_uri) -> None: ...
    def register(self): ...
