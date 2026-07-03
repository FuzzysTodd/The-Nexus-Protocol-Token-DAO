from pyspark.ml.param.shared import *
from pyspark import sql as sql
from pyspark.sql import DataFrame as DataFrame

basestring = str

def streamToPowerBI(df, url, options=...): ...
def writeToPowerBI(df, url, options=...) -> None: ...
