from pyspark.ml.param.shared import *
from pyspark import sql as sql

basestring = str

def readFromPaths(df, pathCol, imageCol: str = 'image'):
    """
    Reads images from a column of filenames

    Args:
        df (DataFrame): The DataFrame to be processed
        pathCol  (str): The name of the column containing filenames
        imageCol (str): The name of the added column of images

    Returns:
        df: The dataframe with loaded images
    """
def readFromStrings(df, bytesCol, imageCol: str = 'image', dropPrefix: bool = False):
    """
    Reads images from a column of filenames

    Args:
        df (DataFrame): The DataFrame to be processed
        pathCol  (str): The name of the column containing filenames
        imageCol (str): The name of the added column of images

    Returns:
        df: The dataframe with loaded images
    """
