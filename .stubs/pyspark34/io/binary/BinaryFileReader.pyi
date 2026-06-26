from pyspark.ml.param.shared import *
from pyspark.sql.types import *
from _typeshed import Incomplete

basestring = str
BinaryFileFields: Incomplete
BinaryFileSchema: Incomplete

def readBinaryFiles(self, path, recursive: bool = False, sampleRatio: float = 1.0, inspectZip: bool = True, seed: int = 0):
    '''
    Reads the directory of binary files from the local or remote (WASB) source
    This function is attached to SparkSession class.

    :Example:

    >>> spark.readBinaryFiles(path, recursive, sampleRatio = 1.0, inspectZip = True)

    Args:
         path (str): Path to the file directory
         recursive (b (double): Fraction of the files loaded into the dataframe

    Returns:
        DataFrame: DataFrame with a single column "value"; see binaryFileSchema for details

    '''
def streamBinaryFiles(self, path, sampleRatio: float = 1.0, inspectZip: bool = True, seed: int = 0):
    '''
    Streams the directory of binary files from the local or remote (WASB) source
    This function is attached to SparkSession class.

    :Example:

    >>> spark.streamBinaryFiles(path, sampleRatio = 1.0, inspectZip = True)

    Args:
         path (str): Path to the file directory

    Returns:
        DataFrame: DataFrame with a single column "value"; see binaryFileSchema for details

    '''
def isBinaryFile(df, column):
    """
    Returns True if the column contains binary files

    Args:
        df (DataFrame): The DataFrame to be processed
        column (bool): The name of the column being inspected

    Returns:
        bool: True if the colum is a binary files column

    """
