from pyspark import SparkContext as SparkContext, sql as sql
from pyspark.sql import DataFrame as DataFrame

basestring = str

def confusionMatrix(df, y_col, y_hat_col, labels) -> None: ...
def roc(df, y_col, y_hat_col, thresh: float = 0.5): ...
