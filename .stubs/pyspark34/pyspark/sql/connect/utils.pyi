from pyspark.sql.pandas.utils import require_minimum_pandas_version as require_minimum_pandas_version, require_minimum_pyarrow_version as require_minimum_pyarrow_version

def check_dependencies(mod_name: str) -> None: ...
def require_minimum_grpc_version() -> None:
    """Raise ImportError if minimum version of grpc is not installed"""
