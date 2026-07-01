from pyspark.pandas.utils import verify_temp_column_name as verify_temp_column_name
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.window import Window as Window
from typing import List

CORRELATION_VALUE_1_COLUMN: str
CORRELATION_VALUE_2_COLUMN: str
CORRELATION_CORR_OUTPUT_COLUMN: str
CORRELATION_COUNT_OUTPUT_COLUMN: str

def compute(sdf: SparkDataFrame, groupKeys: List[str], method: str) -> SparkDataFrame:
    """
    Compute correlation per group, excluding NA/null values.

    Input PySpark Dataframe should contain column `CORRELATION_VALUE_1_COLUMN` and
    column `CORRELATION_VALUE_2_COLUMN`, as well as the group columns.

    The returned PySpark Dataframe will contain the correlation column
    `CORRELATION_CORR_OUTPUT_COLUMN` and the non-null count column
    `CORRELATION_COUNT_OUTPUT_COLUMN`, as well as the group columns.
    """
