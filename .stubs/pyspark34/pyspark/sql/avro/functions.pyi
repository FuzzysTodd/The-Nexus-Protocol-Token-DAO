from pyspark.sql._typing import ColumnOrName as ColumnOrName
from pyspark.sql.column import Column as Column
from pyspark.sql.utils import get_active_spark_context as get_active_spark_context
from typing import Dict

def from_avro(data: ColumnOrName, jsonFormatSchema: str, options: Dict[str, str] | None = None) -> Column:
    '''
    Converts a binary column of Avro format into its corresponding catalyst value.
    The specified schema must match the read data, otherwise the behavior is undefined:
    it may fail or return arbitrary result.
    To deserialize the data with a compatible and evolved schema, the expected Avro schema can be
    set via the option avroSchema.

    .. versionadded:: 3.0.0

    Parameters
    ----------
    data : :class:`~pyspark.sql.Column` or str
        the binary column.
    jsonFormatSchema : str
        the avro schema in JSON string format.
    options : dict, optional
        options to control how the Avro record is parsed.

    Notes
    -----
    Avro is built-in but external data source module since Spark 2.4. Please deploy the
    application as per the deployment section of "Apache Avro Data Source Guide".

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.sql.avro.functions import from_avro, to_avro
    >>> data = [(1, Row(age=2, name=\'Alice\'))]
    >>> df = spark.createDataFrame(data, ("key", "value"))
    >>> avroDf = df.select(to_avro(df.value).alias("avro"))
    >>> avroDf.collect()
    [Row(avro=bytearray(b\'\\x00\\x00\\x04\\x00\\nAlice\'))]

    >>> jsonFormatSchema = \'\'\'{"type":"record","name":"topLevelRecord","fields":
    ...     [{"name":"avro","type":[{"type":"record","name":"value","namespace":"topLevelRecord",
    ...     "fields":[{"name":"age","type":["long","null"]},
    ...     {"name":"name","type":["string","null"]}]},"null"]}]}\'\'\'
    >>> avroDf.select(from_avro(avroDf.avro, jsonFormatSchema).alias("value")).collect()
    [Row(value=Row(avro=Row(age=2, name=\'Alice\')))]
    '''
def to_avro(data: ColumnOrName, jsonFormatSchema: str = '') -> Column:
    '''
    Converts a column into binary of avro format.

    .. versionadded:: 3.0.0

    Parameters
    ----------
    data : :class:`~pyspark.sql.Column` or str
        the data column.
    jsonFormatSchema : str, optional
        user-specified output avro schema in JSON string format.

    Notes
    -----
    Avro is built-in but external data source module since Spark 2.4. Please deploy the
    application as per the deployment section of "Apache Avro Data Source Guide".

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.sql.avro.functions import to_avro
    >>> data = [\'SPADES\']
    >>> df = spark.createDataFrame(data, "string")
    >>> df.select(to_avro(df.value).alias("suite")).collect()
    [Row(suite=bytearray(b\'\\x00\\x0cSPADES\'))]

    >>> jsonFormatSchema = \'\'\'["null", {"type": "enum", "name": "value",
    ...     "symbols": ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]}]\'\'\'
    >>> df.select(to_avro(df.value, jsonFormatSchema).alias("suite")).collect()
    [Row(suite=bytearray(b\'\\x02\\x00\'))]
    '''
