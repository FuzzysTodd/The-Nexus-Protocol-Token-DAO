from _typeshed import Incomplete

DEFAULT_HADOOP: str
DEFAULT_HIVE: str
SUPPORTED_HADOOP_VERSIONS: Incomplete
SUPPORTED_HIVE_VERSIONS: Incomplete
UNSUPPORTED_COMBINATIONS: Incomplete

def checked_package_name(spark_version, hadoop_version, hive_version):
    """
    Check the generated package name, here we need to use the final hadoop version.
    """
def checked_versions(spark_version, hadoop_version, hive_version):
    """
    Check the valid combinations of supported versions in Spark distributions.

    Parameters
    ----------
    spark_version : str
        Spark version. It should be X.X.X such as '3.0.0' or spark-3.0.0.
    hadoop_version : str
        Hadoop version. It should be X such as '2' or 'hadoop2'.
        'without' and 'without-hadoop' are supported as special keywords for Hadoop free
        distribution.
    hive_version : str
        Hive version. It should be X.X such as '2.3' or 'hive2.3'.

    Parameters
    ----------
    tuple
        fully-qualified versions of Spark, Hadoop and Hive in a tuple.
        For example, spark-3.2.0, hadoop3 and hive2.3.
    """
def convert_old_hadoop_version(spark_version, hadoop_version): ...
def install_spark(dest, spark_version, hadoop_version, hive_version) -> None:
    """
    Installs Spark that corresponds to the given Hadoop version in the current
    library directory.

    Parameters
    ----------
    dest : str
        The location to download and install the Spark.
    spark_version : str
        Spark version. It should be spark-X.X.X form.
    hadoop_version : str
        Hadoop version. It should be hadoopX.X
        such as 'hadoop2.7' or 'without-hadoop'.
    hive_version : str
        Hive version. It should be hiveX.X such as 'hive2.3'.
    """
def get_preferred_mirrors(): ...
def download_to_file(response, path, chunk_size=...) -> None: ...
