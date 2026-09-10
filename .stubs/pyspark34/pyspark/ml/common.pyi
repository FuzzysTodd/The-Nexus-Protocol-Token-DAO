import pyspark.context
from pyspark import RDD as RDD, SparkContext as SparkContext
from pyspark.ml._typing import C as C, JavaObjectOrPickleDump as JavaObjectOrPickleDump
from pyspark.serializers import AutoBatchedSerializer as AutoBatchedSerializer, CPickleSerializer as CPickleSerializer
from pyspark.sql import DataFrame as DataFrame, SparkSession as SparkSession
from typing import Any, Callable

def callJavaFunc(sc: pyspark.context.SparkContext, func: Callable[..., 'JavaObjectOrPickleDump'], *args: Any) -> JavaObjectOrPickleDump:
    """Call Java Function"""
def inherit_doc(cls) -> C:
    """
    A decorator that makes a class inherit documentation from its parents.
    """
