import numpy as np
from _typeshed import Incomplete
from pandas.api.extensions import ExtensionDtype
from pyspark.pandas.base import IndexOpsMixin as IndexOpsMixin
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.generic import Frame as Frame
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.series import Series as Series
from typing import Any, Tuple, TypeVar

T = TypeVar('T')
FrameLike = TypeVar('FrameLike', bound='Frame')
IndexOpsLike = TypeVar('IndexOpsLike', bound='IndexOpsMixin')
Scalar: Incomplete
Label = Tuple[Any, ...]
Name = Any | Label
Axis = int | str
Dtype = np.dtype | ExtensionDtype
DataFrameOrSeries: Incomplete
SeriesOrIndex: Incomplete
