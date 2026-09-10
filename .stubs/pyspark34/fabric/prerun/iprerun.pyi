import abc
from abc import ABC, abstractmethod
from pyspark.sql.session import SparkSession as SparkSession

class IPrerun(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def initialize(self, global_namespace: dict) -> None: ...
    @abstractmethod
    def init_personalized_session(self, spark: SparkSession) -> None: ...
    @abstractmethod
    def add_custom_magic(self, jvmMagicHelper) -> None: ...
