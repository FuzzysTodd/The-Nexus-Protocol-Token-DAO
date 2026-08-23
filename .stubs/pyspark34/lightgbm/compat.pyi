from _typeshed import Incomplete
from dask.distributed import Client as Client, Future as Future
from sklearn.utils.validation import NotFittedError

PANDAS_INSTALLED: bool

class pd_Series:
    """Dummy class for pandas.Series."""
    def __init__(self, *args, **kwargs) -> None: ...

class pd_DataFrame:
    """Dummy class for pandas.DataFrame."""
    def __init__(self, *args, **kwargs) -> None: ...

class pd_CategoricalDtype:
    """Dummy class for pandas.CategoricalDtype."""
    def __init__(self, *args, **kwargs) -> None: ...

MATPLOTLIB_INSTALLED: bool
GRAPHVIZ_INSTALLED: bool
dt_DataTable: Incomplete
DATATABLE_INSTALLED: bool

class dt_DataTable:
    """Dummy class for datatable.DataTable."""
    def __init__(self, *args, **kwargs) -> None: ...

SKLEARN_INSTALLED: bool
LGBMNotFittedError = NotFittedError

class _LGBMModelBase:
    """Dummy class for sklearn.base.BaseEstimator."""
class _LGBMClassifierBase:
    """Dummy class for sklearn.base.ClassifierMixin."""
class _LGBMRegressorBase:
    """Dummy class for sklearn.base.RegressorMixin."""
LGBMNotFittedError = ValueError
DASK_INSTALLED: bool

class Client:
    """Dummy class for dask.distributed.Client."""
    def __init__(self, *args, **kwargs) -> None: ...

class Future:
    """Dummy class for dask.distributed.Future."""
    def __init__(self, *args, **kwargs) -> None: ...

class dask_Array:
    """Dummy class for dask.array.Array."""
    def __init__(self, *args, **kwargs) -> None: ...

class dask_DataFrame:
    """Dummy class for dask.dataframe.DataFrame."""
    def __init__(self, *args, **kwargs) -> None: ...

class dask_Series:
    """Dummy class for dask.dataframe.Series."""
    def __init__(self, *args, **kwargs) -> None: ...
