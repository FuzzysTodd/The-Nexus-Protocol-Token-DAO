from pyspark.sql import SparkSession
from typing import List, Optional

def configure_spark_with_delta_pip(spark_session_builder: SparkSession.Builder, extra_packages: Optional[List[str]] = ...) -> SparkSession.Builder:
    '''
    Utility function to configure a SparkSession builder such that the generated SparkSession
    will automatically download the required Delta Lake JARs from Maven. This function is
    required when you want to

    1. Install Delta Lake locally using pip, and

    2. Execute your Python code using Delta Lake + Pyspark directly, that is, not using
       `spark-submit --packages io.delta:...` or `pyspark --packages io.delta:...`.

        builder = SparkSession.builder             .master("local[*]")             .appName("test")

        spark = configure_spark_with_delta_pip(builder).getOrCreate()

    3. If you would like to add more packages, use the `extra_packages` parameter.

        builder = SparkSession.builder             .master("local[*]")             .appName("test")
        my_packages = ["org.apache.spark:spark-sql-kafka-0-10_2.12:x.y.z"]
        spark = configure_spark_with_delta_pip(builder, extra_packages=my_packages).getOrCreate()

    :param spark_session_builder: SparkSession.Builder object being used to configure and
                                  create a SparkSession.
    :param extra_packages: Set other packages to add to Spark session besides Delta Lake.
    :return: Updated SparkSession.Builder object

    .. versionadded:: 1.0

    .. note:: Evolving
    '''
