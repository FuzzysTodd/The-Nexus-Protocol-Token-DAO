from _typeshed import Incomplete
from py4j.java_gateway import JavaObject
from pyspark.sql._typing import DateTimeLiteral, DecimalLiteral, LiteralType
from pyspark.sql.types import DataType
from pyspark.sql.window import WindowSpec
from typing import Any, overload

__all__ = ['Column']

class Column:
    '''
    A column in a DataFrame.

    .. versionadded:: 1.3.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.

    Examples
    --------
    Column instances can be created by

    >>> df = spark.createDataFrame(
    ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])

    Select a column out of a DataFrame
    >>> df.name
    Column<\'name\'>
    >>> df["name"]
    Column<\'name\'>

    Create from an expression

    >>> df.age + 1
    Column<...>
    >>> 1 / df.age
    Column<...>
    '''
    def __init__(self, jc: JavaObject) -> None: ...
    __neg__: Incomplete
    __add__: Incomplete
    __sub__: Incomplete
    __mul__: Incomplete
    __div__: Incomplete
    __truediv__: Incomplete
    __mod__: Incomplete
    __radd__: Incomplete
    __rsub__: Incomplete
    __rmul__: Incomplete
    __rdiv__: Incomplete
    __rtruediv__: Incomplete
    __rmod__: Incomplete
    __pow__: Incomplete
    __rpow__: Incomplete
    def __eq__(self, other: Column | LiteralType | DecimalLiteral | DateTimeLiteral) -> Column:
        """binary function"""
    def __ne__(self, other: Any) -> Column:
        """binary function"""
    __lt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    __gt__: Incomplete
    eqNullSafe: Incomplete
    __and__: Incomplete
    __or__: Incomplete
    __invert__: Incomplete
    __rand__: Incomplete
    __ror__: Incomplete
    def __contains__(self, item: Any) -> None: ...
    bitwiseOR: Incomplete
    bitwiseAND: Incomplete
    bitwiseXOR: Incomplete
    def getItem(self, key: Any) -> Column:
        '''
        An expression that gets an item at position ``ordinal`` out of a list,
        or gets an item by key out of a dict.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        key
            a literal value, or a :class:`Column` expression.
            The result will only be true at a location if the item matches in the column.

             .. deprecated:: 3.0.0
                 :class:`Column` as a parameter is deprecated.

        Returns
        -------
        :class:`Column`
            Column representing the item(s) got at position out of a list or by key out of a dict.

        Examples
        --------
        >>> df = spark.createDataFrame([([1, 2], {"key": "value"})], ["l", "d"])
        >>> df.select(df.l.getItem(0), df.d.getItem("key")).show()
        +----+------+
        |l[0]|d[key]|
        +----+------+
        |   1| value|
        +----+------+
        '''
    def getField(self, name: Any) -> Column:
        '''
        An expression that gets a field by name in a :class:`StructType`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name
            a literal value, or a :class:`Column` expression.
            The result will only be true at a location if the field matches in the Column.

             .. deprecated:: 3.0.0
                 :class:`Column` as a parameter is deprecated.
        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column got by name.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df = spark.createDataFrame([Row(r=Row(a=1, b="b"))])
        >>> df.select(df.r.getField("b")).show()
        +---+
        |r.b|
        +---+
        |  b|
        +---+
        >>> df.select(df.r.a).show()
        +---+
        |r.a|
        +---+
        |  1|
        +---+
        '''
    def withField(self, fieldName: str, col: Column) -> Column:
        """
        An expression that adds/replaces a field in :class:`StructType` by name.

        .. versionadded:: 3.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        fieldName : str
            a literal value.
            The result will only be true at a location if any field matches in the Column.
        col : :class:`Column`
            A :class:`Column` expression for the column with `fieldName`.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column
            which field was added/replaced by fieldName.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> from pyspark.sql.functions import lit
        >>> df = spark.createDataFrame([Row(a=Row(b=1, c=2))])
        >>> df.withColumn('a', df['a'].withField('b', lit(3))).select('a.b').show()
        +---+
        |  b|
        +---+
        |  3|
        +---+
        >>> df.withColumn('a', df['a'].withField('d', lit(4))).select('a.d').show()
        +---+
        |  d|
        +---+
        |  4|
        +---+
        """
    def dropFields(self, *fieldNames: str) -> Column:
        '''
        An expression that drops fields in :class:`StructType` by name.
        This is a no-op if the schema doesn\'t contain field name(s).

        .. versionadded:: 3.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        fieldNames : str
            Desired field names (collects all positional arguments passed)
            The result will drop at a location if any field matches in the Column.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column with field dropped by fieldName.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> from pyspark.sql.functions import col, lit
        >>> df = spark.createDataFrame([
        ...     Row(a=Row(b=1, c=2, d=3, e=Row(f=4, g=5, h=6)))])
        >>> df.withColumn(\'a\', df[\'a\'].dropFields(\'b\')).show()
        +-----------------+
        |                a|
        +-----------------+
        |{2, 3, {4, 5, 6}}|
        +-----------------+

        >>> df.withColumn(\'a\', df[\'a\'].dropFields(\'b\', \'c\')).show()
        +--------------+
        |             a|
        +--------------+
        |{3, {4, 5, 6}}|
        +--------------+

        This method supports dropping multiple nested fields directly e.g.

        >>> df.withColumn("a", col("a").dropFields("e.g", "e.h")).show()
        +--------------+
        |             a|
        +--------------+
        |{1, 2, 3, {4}}|
        +--------------+

        However, if you are going to add/replace multiple nested fields,
        it is preferred to extract out the nested struct before
        adding/replacing multiple fields e.g.

        >>> df.select(col("a").withField(
        ...     "e", col("a.e").dropFields("g", "h")).alias("a")
        ... ).show()
        +--------------+
        |             a|
        +--------------+
        |{1, 2, 3, {4}}|
        +--------------+

        '''
    def __getattr__(self, item: Any) -> Column:
        '''
        An expression that gets an item at position ``ordinal`` out of a list,
        or gets an item by key out of a dict.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        item
            a literal value.

        Returns
        -------
        :class:`Column`
            Column representing the item got by key out of a dict.

        Examples
        --------
        >>> df = spark.createDataFrame([(\'abcedfg\', {"key": "value"})], ["l", "d"])
        >>> df.select(df.d.key).show()
        +------+
        |d[key]|
        +------+
        | value|
        +------+
        '''
    def __getitem__(self, k: Any) -> Column:
        '''
        An expression that gets an item at position ``ordinal`` out of a list,
        or gets an item by key out of a dict.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        k
            a literal value, or a slice object without step.

        Returns
        -------
        :class:`Column`
            Column representing the item got by key out of a dict, or substrings sliced by
            the given slice object.

        Examples
        --------
        >>> df = spark.createDataFrame([(\'abcedfg\', {"key": "value"})], ["l", "d"])
        >>> df.select(df.l[slice(1, 3)], df.d[\'key\']).show()
        +------------------+------+
        |substring(l, 1, 3)|d[key]|
        +------------------+------+
        |               abc| value|
        +------------------+------+
        '''
    def __iter__(self) -> None: ...
    contains: Incomplete
    startswith: Incomplete
    endswith: Incomplete
    def like(self, other: str) -> Column:
        '''
        SQL like expression. Returns a boolean :class:`Column` based on a SQL LIKE match.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : str
            a SQL LIKE pattern

        See Also
        --------
        pyspark.sql.Column.rlike

        Returns
        -------
        :class:`Column`
            Column of booleans showing whether each element
            in the Column is matched by SQL LIKE pattern.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.filter(df.name.like(\'Al%\')).collect()
        [Row(age=2, name=\'Alice\')]
        '''
    def rlike(self, other: str) -> Column:
        '''
        SQL RLIKE expression (LIKE with Regex). Returns a boolean :class:`Column` based on a regex
        match.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : str
            an extended regex expression

        Returns
        -------
        :class:`Column`
            Column of booleans showing whether each element
            in the Column is matched by extended regex expression.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.filter(df.name.rlike(\'ice$\')).collect()
        [Row(age=2, name=\'Alice\')]
        '''
    def ilike(self, other: str) -> Column:
        '''
        SQL ILIKE expression (case insensitive LIKE). Returns a boolean :class:`Column`
        based on a case insensitive match.

        .. versionadded:: 3.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : str
            a SQL LIKE pattern

        See Also
        --------
        pyspark.sql.Column.rlike

        Returns
        -------
        :class:`Column`
            Column of booleans showing whether each element
            in the Column is matched by SQL LIKE pattern.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.filter(df.name.ilike(\'%Ice\')).collect()
        [Row(age=2, name=\'Alice\')]
        '''
    @overload
    def substr(self, startPos: int, length: int) -> Column: ...
    @overload
    def substr(self, startPos: Column, length: Column) -> Column: ...
    def isin(self, *cols: Any) -> Column:
        '''
        A boolean expression that is evaluated to true if the value of this
        expression is contained by the evaluated values of the arguments.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols
            The result will only be true at a location if any value matches in the Column.

        Returns
        -------
        :class:`Column`
            Column of booleans showing whether each element in the Column is contained in cols.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df[df.name.isin("Bob", "Mike")].collect()
        [Row(age=5, name=\'Bob\')]
        >>> df[df.age.isin([1, 2, 3])].collect()
        [Row(age=2, name=\'Alice\')]
        '''
    asc: Incomplete
    asc_nulls_first: Incomplete
    asc_nulls_last: Incomplete
    desc: Incomplete
    desc_nulls_first: Incomplete
    desc_nulls_last: Incomplete
    isNull: Incomplete
    isNotNull: Incomplete
    def alias(self, *alias: str, **kwargs: Any) -> Column:
        '''
        Returns this column aliased with a new name or names (in the case of expressions that
        return more than one column, such as explode).

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        alias : str
            desired column names (collects all positional arguments passed)

        Other Parameters
        ----------------
        metadata: dict
            a dict of information to be stored in ``metadata`` attribute of the
            corresponding :class:`StructField <pyspark.sql.types.StructField>` (optional, keyword
            only argument)

            .. versionchanged:: 2.2.0
               Added optional ``metadata`` argument.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column is aliased with new name or names.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.select(df.age.alias("age2")).collect()
        [Row(age2=2), Row(age2=5)]
        >>> df.select(df.age.alias("age3", metadata={\'max\': 99})).schema[\'age3\'].metadata[\'max\']
        99
        '''
    name: Incomplete
    def cast(self, dataType: DataType | str) -> Column:
        '''
        Casts the column into type ``dataType``.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        dataType : :class:`DataType` or str
            a DataType or Python string literal with a DDL-formatted string
            to use when parsing the column to the same type.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column is cast into new type.

        Examples
        --------
        >>> from pyspark.sql.types import StringType
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.select(df.age.cast("string").alias(\'ages\')).collect()
        [Row(ages=\'2\'), Row(ages=\'5\')]
        >>> df.select(df.age.cast(StringType()).alias(\'ages\')).collect()
        [Row(ages=\'2\'), Row(ages=\'5\')]
        '''
    astype: Incomplete
    def between(self, lowerBound: Column | LiteralType | DateTimeLiteral | DecimalLiteral, upperBound: Column | LiteralType | DateTimeLiteral | DecimalLiteral) -> Column:
        '''
        True if the current column is between the lower bound and upper bound, inclusive.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        lowerBound : :class:`Column`, int, float, string, bool, datetime, date or Decimal
            a boolean expression that boundary start, inclusive.
        upperBound : :class:`Column`, int, float, string, bool, datetime, date or Decimal
            a boolean expression that boundary end, inclusive.

        Returns
        -------
        :class:`Column`
            Column of booleans showing whether each element of Column
            is between left and right (inclusive).

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.select(df.name, df.age.between(2, 4)).show()
        +-----+---------------------------+
        | name|((age >= 2) AND (age <= 4))|
        +-----+---------------------------+
        |Alice|                       true|
        |  Bob|                      false|
        +-----+---------------------------+
        '''
    def when(self, condition: Column, value: Any) -> Column:
        '''
        Evaluates a list of conditions and returns one of multiple possible result expressions.
        If :func:`Column.otherwise` is not invoked, None is returned for unmatched conditions.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        condition : :class:`Column`
            a boolean :class:`Column` expression.
        value
            a literal value, or a :class:`Column` expression.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column is in conditions.

        Examples
        --------
        >>> from pyspark.sql import functions as F
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.select(df.name, F.when(df.age > 4, 1).when(df.age < 3, -1).otherwise(0)).show()
        +-----+------------------------------------------------------------+
        | name|CASE WHEN (age > 4) THEN 1 WHEN (age < 3) THEN -1 ELSE 0 END|
        +-----+------------------------------------------------------------+
        |Alice|                                                          -1|
        |  Bob|                                                           1|
        +-----+------------------------------------------------------------+

        See Also
        --------
        pyspark.sql.functions.when
        '''
    def otherwise(self, value: Any) -> Column:
        '''
        Evaluates a list of conditions and returns one of multiple possible result expressions.
        If :func:`Column.otherwise` is not invoked, None is returned for unmatched conditions.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        value
            a literal value, or a :class:`Column` expression.

        Returns
        -------
        :class:`Column`
            Column representing whether each element of Column is unmatched conditions.

        Examples
        --------
        >>> from pyspark.sql import functions as F
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.select(df.name, F.when(df.age > 3, 1).otherwise(0)).show()
        +-----+-------------------------------------+
        | name|CASE WHEN (age > 3) THEN 1 ELSE 0 END|
        +-----+-------------------------------------+
        |Alice|                                    0|
        |  Bob|                                    1|
        +-----+-------------------------------------+

        See Also
        --------
        pyspark.sql.functions.when
        '''
    def over(self, window: WindowSpec) -> Column:
        '''
        Define a windowing column.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        window : :class:`WindowSpec`

        Returns
        -------
        :class:`Column`

        Examples
        --------
        >>> from pyspark.sql import Window
        >>> window = Window.partitionBy("name").orderBy("age")                 .rowsBetween(Window.unboundedPreceding, Window.currentRow)
        >>> from pyspark.sql.functions import rank, min, desc
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
        >>> df.withColumn("rank", rank().over(window))                 .withColumn("min", min(\'age\').over(window)).sort(desc("age")).show()
        +---+-----+----+---+
        |age| name|rank|min|
        +---+-----+----+---+
        |  5|  Bob|   1|  5|
        |  2|Alice|   1|  2|
        +---+-----+----+---+
        '''
    def __nonzero__(self) -> None: ...
    __bool__ = __nonzero__
