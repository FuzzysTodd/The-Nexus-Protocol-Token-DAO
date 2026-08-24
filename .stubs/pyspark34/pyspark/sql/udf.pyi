from _typeshed import Incomplete
from pyspark.sql._typing import ColumnOrName, DataTypeOrString, UserDefinedFunctionLike
from pyspark.sql.column import Column
from pyspark.sql.session import SparkSession
from pyspark.sql.types import DataType
from typing import Any, Callable

__all__ = ['UDFRegistration']

class UserDefinedFunction:
    """
    User defined function in Python

    .. versionadded:: 1.3

    Notes
    -----
    The constructor of this class is not supposed to be directly called.
    Use :meth:`pyspark.sql.functions.udf` or :meth:`pyspark.sql.functions.pandas_udf`
    to create this instance.
    """
    func: Incomplete
    evalType: Incomplete
    deterministic: Incomplete
    def __init__(self, func: Callable[..., Any], returnType: DataTypeOrString = ..., name: str | None = None, evalType: int = ..., deterministic: bool = True) -> None: ...
    @property
    def returnType(self) -> DataType: ...
    def __call__(self, *cols: ColumnOrName) -> Column: ...
    def asNondeterministic(self) -> UserDefinedFunction:
        """
        Updates UserDefinedFunction to nondeterministic.

        .. versionadded:: 2.3
        """

class UDFRegistration:
    """
    Wrapper for user-defined function registration. This instance can be accessed by
    :attr:`spark.udf` or :attr:`sqlContext.udf`.

    .. versionadded:: 1.3.1
    """
    sparkSession: Incomplete
    def __init__(self, sparkSession: SparkSession) -> None: ...
    def register(self, name: str, f: Callable[..., Any] | UserDefinedFunctionLike, returnType: DataTypeOrString | None = None) -> UserDefinedFunctionLike:
        '''Register a Python function (including lambda function) or a user-defined function
        as a SQL function.

        .. versionadded:: 1.3.1

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str,
            name of the user-defined function in SQL statements.
        f : function, :meth:`pyspark.sql.functions.udf` or :meth:`pyspark.sql.functions.pandas_udf`
            a Python function, or a user-defined function. The user-defined function can
            be either row-at-a-time or vectorized. See :meth:`pyspark.sql.functions.udf` and
            :meth:`pyspark.sql.functions.pandas_udf`.
        returnType : :class:`pyspark.sql.types.DataType` or str, optional
            the return type of the registered user-defined function. The value can
            be either a :class:`pyspark.sql.types.DataType` object or a DDL-formatted type string.
            `returnType` can be optionally specified when `f` is a Python function but not
            when `f` is a user-defined function. Please see the examples below.

        Returns
        -------
        function
            a user-defined function

        Notes
        -----
        To register a nondeterministic Python function, users need to first build
        a nondeterministic user-defined function for the Python function and then register it
        as a SQL function.

        Examples
        --------
        1. When `f` is a Python function:

            `returnType` defaults to string type and can be optionally specified. The produced
            object must match the specified type. In this case, this API works as if
            `register(name, f, returnType=StringType())`.

            >>> strlen = spark.udf.register("stringLengthString", lambda x: len(x))
            >>> spark.sql("SELECT stringLengthString(\'test\')").collect()
            [Row(stringLengthString(test)=\'4\')]

            >>> spark.sql("SELECT \'foo\' AS text").select(strlen("text")).collect()
            [Row(stringLengthString(text)=\'3\')]

            >>> from pyspark.sql.types import IntegerType
            >>> _ = spark.udf.register("stringLengthInt", lambda x: len(x), IntegerType())
            >>> spark.sql("SELECT stringLengthInt(\'test\')").collect()
            [Row(stringLengthInt(test)=4)]

            >>> from pyspark.sql.types import IntegerType
            >>> _ = spark.udf.register("stringLengthInt", lambda x: len(x), IntegerType())
            >>> spark.sql("SELECT stringLengthInt(\'test\')").collect()
            [Row(stringLengthInt(test)=4)]

        2. When `f` is a user-defined function (from Spark 2.3.0):

            Spark uses the return type of the given user-defined function as the return type of
            the registered user-defined function. `returnType` should not be specified.
            In this case, this API works as if `register(name, f)`.

            >>> from pyspark.sql.types import IntegerType
            >>> from pyspark.sql.functions import udf
            >>> slen = udf(lambda s: len(s), IntegerType())
            >>> _ = spark.udf.register("slen", slen)
            >>> spark.sql("SELECT slen(\'test\')").collect()
            [Row(slen(test)=4)]

            >>> import random
            >>> from pyspark.sql.functions import udf
            >>> from pyspark.sql.types import IntegerType
            >>> random_udf = udf(lambda: random.randint(0, 100), IntegerType()).asNondeterministic()
            >>> new_random_udf = spark.udf.register("random_udf", random_udf)
            >>> spark.sql("SELECT random_udf()").collect()  # doctest: +SKIP
            [Row(random_udf()=82)]

            >>> import pandas as pd  # doctest: +SKIP
            >>> from pyspark.sql.functions import pandas_udf
            >>> @pandas_udf("integer")  # doctest: +SKIP
            ... def add_one(s: pd.Series) -> pd.Series:
            ...     return s + 1
            ...
            >>> _ = spark.udf.register("add_one", add_one)  # doctest: +SKIP
            >>> spark.sql("SELECT add_one(id) FROM range(3)").collect()  # doctest: +SKIP
            [Row(add_one(id)=1), Row(add_one(id)=2), Row(add_one(id)=3)]

            >>> @pandas_udf("integer")  # doctest: +SKIP
            ... def sum_udf(v: pd.Series) -> int:
            ...     return v.sum()
            ...
            >>> _ = spark.udf.register("sum_udf", sum_udf)  # doctest: +SKIP
            >>> q = "SELECT sum_udf(v1) FROM VALUES (3, 0), (2, 0), (1, 1) tbl(v1, v2) GROUP BY v2"
            >>> spark.sql(q).collect()  # doctest: +SKIP
            [Row(sum_udf(v1)=1), Row(sum_udf(v1)=5)]

        '''
    def registerJavaFunction(self, name: str, javaClassName: str, returnType: DataTypeOrString | None = None) -> None:
        '''Register a Java user-defined function as a SQL function.

        In addition to a name and the function itself, the return type can be optionally specified.
        When the return type is not specified we would infer it via reflection.

        .. versionadded:: 2.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            name of the user-defined function
        javaClassName : str
            fully qualified name of java class
        returnType : :class:`pyspark.sql.types.DataType` or str, optional
            the return type of the registered Java function. The value can be either
            a :class:`pyspark.sql.types.DataType` object or a DDL-formatted type string.

        Examples
        --------
        >>> from pyspark.sql.types import IntegerType
        >>> spark.udf.registerJavaFunction(
        ...     "javaStringLength", "test.org.apache.spark.sql.JavaStringLength", IntegerType())
        ... # doctest: +SKIP
        >>> spark.sql("SELECT javaStringLength(\'test\')").collect()  # doctest: +SKIP
        [Row(javaStringLength(test)=4)]

        >>> spark.udf.registerJavaFunction(
        ...     "javaStringLength2", "test.org.apache.spark.sql.JavaStringLength")
        ... # doctest: +SKIP
        >>> spark.sql("SELECT javaStringLength2(\'test\')").collect()  # doctest: +SKIP
        [Row(javaStringLength2(test)=4)]

        >>> spark.udf.registerJavaFunction(
        ...     "javaStringLength3", "test.org.apache.spark.sql.JavaStringLength", "integer")
        ... # doctest: +SKIP
        >>> spark.sql("SELECT javaStringLength3(\'test\')").collect()  # doctest: +SKIP
        [Row(javaStringLength3(test)=4)]
        '''
    def registerJavaUDAF(self, name: str, javaClassName: str) -> None:
        '''Register a Java user-defined aggregate function as a SQL function.

        .. versionadded:: 2.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        name : str
            name of the user-defined aggregate function
        javaClassName : str
            fully qualified name of java class

        Examples
        --------
        >>> spark.udf.registerJavaUDAF("javaUDAF", "test.org.apache.spark.sql.MyDoubleAvg")
        ... # doctest: +SKIP
        >>> df = spark.createDataFrame([(1, "a"),(2, "b"), (3, "a")],["id", "name"])
        >>> df.createOrReplaceTempView("df")
        >>> q = "SELECT name, javaUDAF(id) as avg from df group by name order by name desc"
        >>> spark.sql(q).collect()  # doctest: +SKIP
        [Row(name=\'b\', avg=102.0), Row(name=\'a\', avg=102.0)]
        '''
