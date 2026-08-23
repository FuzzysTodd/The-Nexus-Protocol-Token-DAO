import numpy as np
import pandas as pd
from pyspark import SparkConf as SparkConf, SparkContext as SparkContext, __version__ as __version__
from pyspark.errors import PySparkAttributeError as PySparkAttributeError
from pyspark.sql.connect._typing import OptionalPrimitiveType as OptionalPrimitiveType
from pyspark.sql.connect.catalog import Catalog as Catalog
from pyspark.sql.connect.client import SparkConnectClient as SparkConnectClient
from pyspark.sql.connect.conf import RuntimeConf as RuntimeConf
from pyspark.sql.connect.dataframe import DataFrame as DataFrame
from pyspark.sql.connect.plan import CachedRelation as CachedRelation, LocalRelation as LocalRelation, Range as Range, SQL as SQL
from pyspark.sql.connect.readwriter import DataFrameReader as DataFrameReader
from pyspark.sql.connect.udf import UDFRegistration as UDFRegistration
from pyspark.sql.connect.utils import check_dependencies as check_dependencies
from pyspark.sql.pandas.serializers import ArrowStreamPandasSerializer as ArrowStreamPandasSerializer
from pyspark.sql.pandas.types import to_arrow_schema as to_arrow_schema, to_arrow_type as to_arrow_type
from pyspark.sql.session import classproperty as classproperty
from pyspark.sql.types import AtomicType as AtomicType, DataType as DataType, DayTimeIntervalType as DayTimeIntervalType, Row as Row, StructType as StructType, TimestampType as TimestampType
from pyspark.sql.utils import to_str as to_str
from typing import Any, Dict, Iterable, List, Tuple, overload

class SparkSession:
    class Builder:
        """Builder for :class:`SparkSession`."""
        def __init__(self) -> None: ...
        @overload
        def config(self, key: str, value: Any) -> SparkSession.Builder: ...
        @overload
        def config(self, *, map: Dict[str, 'OptionalPrimitiveType']) -> SparkSession.Builder: ...
        def master(self, master: str) -> SparkSession.Builder: ...
        def appName(self, name: str) -> SparkSession.Builder: ...
        def remote(self, location: str = 'sc://localhost') -> SparkSession.Builder: ...
        def enableHiveSupport(self) -> SparkSession.Builder: ...
        def getOrCreate(self) -> SparkSession: ...
    def builder(cls) -> Builder:
        """Creates a :class:`Builder` for constructing a :class:`SparkSession`."""
    def __init__(self, connectionString: str, userId: str | None = None) -> None:
        """
        Creates a new SparkSession for the Spark Connect interface.

        Parameters
        ----------
        connectionString: str, optional
            Connection string that is used to extract the connection parameters and configure
            the GRPC connection. Defaults to `sc://localhost`.
        userId : str, optional
            Optional unique user ID that is used to differentiate multiple users and
            isolate their Spark Sessions. If the `user_id` is not set, will default to
            the $USER environment. Defining the user ID as part of the connection string
            takes precedence.
        """
    def table(self, tableName: str) -> DataFrame: ...
    @property
    def read(self) -> DataFrameReader: ...
    def createDataFrame(self, data: pd.DataFrame | np.ndarray | Iterable[Any], schema: AtomicType | StructType | str | List[str] | Tuple[str, ...] | None = None) -> DataFrame: ...
    def sql(self, sqlQuery: str, args: Dict[str, Any] | None = None) -> DataFrame: ...
    def range(self, start: int, end: int | None = None, step: int = 1, numPartitions: int | None = None) -> DataFrame: ...
    @property
    def catalog(self) -> Catalog: ...
    def __del__(self) -> None: ...
    def stop(self) -> None: ...
    @classmethod
    def getActiveSession(cls) -> Any: ...
    def newSession(self) -> Any: ...
    @property
    def conf(self) -> RuntimeConf: ...
    @property
    def sparkContext(self) -> Any: ...
    @property
    def streams(self) -> Any: ...
    @property
    def readStream(self) -> Any: ...
    @property
    def udf(self) -> UDFRegistration: ...
    @property
    def version(self) -> str: ...
    @property
    def client(self) -> SparkConnectClient:
        """
        Gives access to the Spark Connect client. In normal cases this is not necessary to be used
        and only relevant for testing.
        Returns
        -------
        :class:`SparkConnectClient`
        """
