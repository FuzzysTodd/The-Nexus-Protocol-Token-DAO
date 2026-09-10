from pyspark.ml.param.shared import *
from pyspark import sql as sql
from pyspark.sql import DataFrame as DataFrame

basestring = str

def streamToAzureSearch(df, **options): ...
def writeToAzureSearch(df, **options) -> None: ...
