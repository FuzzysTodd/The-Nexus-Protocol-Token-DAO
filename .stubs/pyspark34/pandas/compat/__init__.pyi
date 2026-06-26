from pandas.compat._constants import IS64 as IS64, PY310 as PY310, PY311 as PY311, PY39 as PY39, PYPY as PYPY
from pandas.compat.numpy import is_numpy_dev as is_numpy_dev, np_version_under1p21 as np_version_under1p21
from pandas.compat.pyarrow import pa_version_under11p0 as pa_version_under11p0, pa_version_under7p0 as pa_version_under7p0, pa_version_under8p0 as pa_version_under8p0, pa_version_under9p0 as pa_version_under9p0

__all__ = ['is_numpy_dev', 'np_version_under1p21', 'pa_version_under7p0', 'pa_version_under8p0', 'pa_version_under9p0', 'pa_version_under11p0', 'IS64', 'PY39', 'PY310', 'PY311', 'PYPY']
