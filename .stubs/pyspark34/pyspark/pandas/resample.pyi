from abc import ABCMeta
from pyspark import SparkContext as SparkContext
from pyspark.pandas._typing import FrameLike as FrameLike
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.internal import InternalField as InternalField, InternalFrame as InternalFrame, SPARK_DEFAULT_INDEX_NAME as SPARK_DEFAULT_INDEX_NAME
from pyspark.pandas.missing.resample import MissingPandasLikeDataFrameResampler as MissingPandasLikeDataFrameResampler, MissingPandasLikeSeriesResampler as MissingPandasLikeSeriesResampler
from pyspark.pandas.series import Series as Series, first_series as first_series
from pyspark.pandas.utils import scol_for as scol_for, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column
from pyspark.sql.types import NumericType as NumericType, StructField as StructField, TimestampType as TimestampType
from typing import Any, Generic, List

class Resampler(Generic[FrameLike], metaclass=ABCMeta):
    """
    Class for resampling datetimelike data, a groupby-like operation.

    It's easiest to use obj.resample(...) to use Resampler.

    Parameters
    ----------
    psdf : DataFrame

    Returns
    -------
    a Resampler of the appropriate type

    Notes
    -----
    After resampling, see aggregate, apply, and transform functions.
    """
    def __init__(self, psdf: DataFrame, resamplekey: Series | None, rule: str, closed: str | None = None, label: str | None = None, agg_columns: List[Series] = []) -> None: ...
    def min(self) -> FrameLike:
        '''
        Compute min of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").min().sort_index()
                           A         B
        2022-05-01  0.171162  0.338864
        2022-05-04  0.010527  0.561204
        2022-05-07       NaN       NaN
        2022-05-10  0.813726  0.745100
        '''
    def max(self) -> FrameLike:
        '''
        Compute max of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").max().sort_index()
                           A         B
        2022-05-01  0.420538  0.859182
        2022-05-04  0.270533  0.691041
        2022-05-07       NaN       NaN
        2022-05-10  0.813726  0.745100
        '''
    def sum(self) -> FrameLike:
        '''
        Compute sum of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").sum().sort_index()
                           A         B
        2022-05-01  0.800160  1.679727
        2022-05-04  0.281060  1.252245
        2022-05-07  0.000000  0.000000
        2022-05-10  0.813726  0.745100
        '''
    def mean(self) -> FrameLike:
        '''
        Compute mean of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").mean().sort_index()
                           A         B
        2022-05-01  0.266720  0.559909
        2022-05-04  0.140530  0.626123
        2022-05-07       NaN       NaN
        2022-05-10  0.813726  0.745100
        '''
    def std(self) -> FrameLike:
        '''
        Compute std of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").std().sort_index()
                           A         B
        2022-05-01  0.134509  0.268835
        2022-05-04  0.183852  0.091809
        2022-05-07       NaN       NaN
        2022-05-10       NaN       NaN
        '''
    def var(self) -> FrameLike:
        '''
        Compute var of resampled values.

        .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> from datetime import datetime
        >>> np.random.seed(22)
        >>> dates = [
        ...    datetime(2022, 5, 1, 4, 5, 6),
        ...    datetime(2022, 5, 3),
        ...    datetime(2022, 5, 3, 23, 59, 59),
        ...    datetime(2022, 5, 4),
        ...    pd.NaT,
        ...    datetime(2022, 5, 4, 0, 0, 1),
        ...    datetime(2022, 5, 11),
        ... ]
        >>> df = ps.DataFrame(
        ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
        ... )
        >>> df
                                    A         B
        2022-05-01 04:05:06  0.208461  0.481681
        2022-05-03 00:00:00  0.420538  0.859182
        2022-05-03 23:59:59  0.171162  0.338864
        2022-05-04 00:00:00  0.270533  0.691041
        NaT                  0.220405  0.811951
        2022-05-04 00:00:01  0.010527  0.561204
        2022-05-11 00:00:00  0.813726  0.745100
        >>> df.resample("3D").var().sort_index()
                           A         B
        2022-05-01  0.018093  0.072272
        2022-05-04  0.033802  0.008429
        2022-05-07       NaN       NaN
        2022-05-10       NaN       NaN
        '''

class DataFrameResampler(Resampler[DataFrame]):
    def __init__(self, psdf: DataFrame, resamplekey: Series | None, rule: str, closed: str | None = None, label: str | None = None, agg_columns: List[Series] = []) -> None: ...
    def __getattr__(self, item: str) -> Any: ...

class SeriesResampler(Resampler[Series]):
    def __init__(self, psser: Series, resamplekey: Series | None, rule: str, closed: str | None = None, label: str | None = None, agg_columns: List[Series] = []) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
