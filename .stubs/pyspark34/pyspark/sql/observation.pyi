from typing import Any, Dict

__all__ = ['Observation']

class Observation:
    '''Class to observe (named) metrics on a :class:`DataFrame`.

    Metrics are aggregation expressions, which are applied to the DataFrame while it is being
    processed by an action.

    The metrics have the following guarantees:

    - It will compute the defined aggregates (metrics) on all the data that is flowing through
      the Dataset during the action.
    - It will report the value of the defined aggregate columns as soon as we reach the end of
      the action.

    The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or
    more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that
    contain references to the input Dataset\'s columns must always be wrapped in an aggregate
    function.

    An Observation instance collects the metrics while the first action is executed. Subsequent
    actions do not modify the metrics returned by `Observation.get`. Retrieval of the metric via
    `Observation.get` blocks until the first action has finished and metrics become available.

    .. versionadded:: 3.3.0

    Notes
    -----
    This class does not support streaming datasets.

    Examples
    --------
    >>> from pyspark.sql.functions import col, count, lit, max
    >>> from pyspark.sql import Observation
    >>> df = spark.createDataFrame([["Alice", 2], ["Bob", 5]], ["name", "age"])
    >>> observation = Observation("my metrics")
    >>> observed_df = df.observe(observation, count(lit(1)).alias("count"), max(col("age")))
    >>> observed_df.count()
    2
    >>> observation.get
    {\'count\': 2, \'max(age)\': 5}
    '''
    def __init__(self, name: str | None = None) -> None:
        """Constructs a named or unnamed Observation instance.

        Parameters
        ----------
        name : str, optional
            default is a random UUID string. This is the name of the Observation and the metric.
        """
    @property
    def get(self) -> Dict[str, Any]:
        """Get the observed metrics.

        Waits until the observed dataset finishes its first action. Only the result of the
        first action is available. Subsequent actions do not modify the result.

        Returns
        -------
        dict
            the observed metrics
        """
