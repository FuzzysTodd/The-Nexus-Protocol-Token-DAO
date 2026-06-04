import pyspark.context
from py4j.java_gateway import JavaObject
from pyspark import RDD as RDD, SparkContext as SparkContext
from pyspark.mllib._typing import C as C, JavaObjectOrPickleDump as JavaObjectOrPickleDump
from pyspark.serializers import AutoBatchedSerializer as AutoBatchedSerializer, CPickleSerializer as CPickleSerializer
from pyspark.sql import DataFrame as DataFrame, SparkSession as SparkSession
from typing import Any, Callable

def callJavaFunc(sc: pyspark.context.SparkContext, func: Callable[..., 'JavaObjectOrPickleDump'], *args: Any) -> Any:
    """Call Java Function"""
def callMLlibFunc(name: str, *args: Any) -> Any:
    """Call API in PythonMLLibAPI"""

class JavaModelWrapper:
    """
    Wrapper for the model in JVM
    """
    def __init__(self, java_model: JavaObject) -> None: ...
    def __del__(self) -> None: ...
    def call(self, name: str, *a: Any) -> Any:
        """Call method of java_model"""

def inherit_doc(cls) -> C:
    """
    A decorator that makes a class inherit documentation from its parents.
    """
