from _typeshed import Incomplete
from os import error as error
from pyspark.ml import Transformer
from pyspark.ml.param.shared import HasInputCol, HasOutputCol
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsReader, DefaultParamsWritable, DefaultParamsWriter
from typing import TypeVar

OPENAI_API_VERSION: str
RL = TypeVar('RL', bound='MLReadable')

class LangchainTransformerParamsWriter(DefaultParamsWriter):
    def saveImpl(self, path: str) -> None: ...

class LangchainTransformerParamsReader(DefaultParamsReader):
    def load(self, path: str) -> RL: ...

class LangchainTransformer(Transformer, HasInputCol, HasOutputCol, DefaultParamsReadable, DefaultParamsWritable):
    chain: Incomplete
    subscriptionKey: Incomplete
    url: Incomplete
    apiVersion: Incomplete
    running_on_synapse_internal: Incomplete
    errorCol: Incomplete
    def __init__(self, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, chain: Incomplete | None = None, subscriptionKey: Incomplete | None = None, url: Incomplete | None = None, apiVersion=..., errorCol: str = 'errorCol') -> None: ...
    def setParams(self, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, chain: Incomplete | None = None, subscriptionKey: Incomplete | None = None, url: Incomplete | None = None, apiVersion=..., errorCol: str = 'errorCol'): ...
    def setChain(self, value): ...
    def getChain(self): ...
    def setSubscriptionKey(self, value: str):
        """
        set the openAI api key
        """
    def getSubscriptionKey(self): ...
    def setUrl(self, value: str): ...
    def getUrl(self): ...
    def setApiVersion(self, value: str): ...
    def getApiVersion(self): ...
    def setInputCol(self, value: str):
        """
        Sets the value of :py:attr:`inputCol`.
        """
    def setOutputCol(self, value: str):
        """
        Sets the value of :py:attr:`outputCol`.
        """
    def setErrorCol(self, value: str):
        """
        Sets the value of :py:attr:`outputCol`.
        """
    def getErrorCol(self):
        """
        Returns:
            str: The name of the error column
        """
    def write(self) -> LangchainTransformerParamsWriter: ...
    @classmethod
    def read(cls) -> LangchainTransformerParamsReader[RL]:
        """Returns a LangchainTransformerParamsReader instance for this class."""
