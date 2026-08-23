import grpc
import pandas as pd
import pyarrow as pa
import pyspark.sql.connect.proto as pb2
from _typeshed import Incomplete
from pyspark.sql.connect._typing import DataTypeOrString
from pyspark.sql.types import DataType, StructType
from pyspark.storagelevel import StorageLevel
from types import TracebackType
from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, Tuple, Type

__all__ = ['ChannelBuilder', 'SparkConnectClient']

class ChannelBuilder:
    '''
    This is a helper class that is used to create a GRPC channel based on the given
    connection string per the documentation of Spark Connect.

    .. versionadded:: 3.4.0

    Examples
    --------
    >>> cb =  ChannelBuilder("sc://localhost")
    ... cb.endpoint
    "localhost:15002"

    >>> cb = ChannelBuilder("sc://localhost/;use_ssl=true;token=aaa")
    ... cb.secure
    True
    '''
    PARAM_USE_SSL: str
    PARAM_TOKEN: str
    PARAM_USER_ID: str
    PARAM_USER_AGENT: str
    MAX_MESSAGE_LENGTH: Incomplete
    @staticmethod
    def default_port() -> int: ...
    url: Incomplete
    params: Incomplete
    def __init__(self, url: str, channelOptions: List[Tuple[str, Any]] | None = None) -> None:
        """
        Constructs a new channel builder. This is used to create the proper GRPC channel from
        the connection string.

        Parameters
        ----------
        url : str
            Spark Connect connection string
        channelOptions: list of tuple, optional
            Additional options that can be passed to the GRPC channel construction.
        """
    def metadata(self) -> Iterable[Tuple[str, str]]:
        """
        Builds the GRPC specific metadata list to be injected into the request. All
        parameters will be converted to metadata except ones that are explicitly used
        by the channel.

        Returns
        -------
        A list of tuples (key, value)
        """
    @property
    def secure(self) -> bool: ...
    @property
    def endpoint(self) -> str: ...
    @property
    def userId(self) -> str | None:
        """
        Returns
        -------
        The user_id extracted from the parameters of the connection string or `None` if not
        specified.
        """
    @property
    def userAgent(self) -> str:
        '''
        Returns
        -------
        user_agent : str
            The user_agent parameter specified in the connection string,
            or "_SPARK_CONNECT_PYTHON" when not specified.
        '''
    def get(self, key: str) -> Any:
        """
        Parameters
        ----------
        key : str
            Parameter key name.

        Returns
        -------
        The parameter value if present, raises exception otherwise.
        """
    def toChannel(self) -> grpc.Channel:
        """
        Applies the parameters of the connection string and creates a new
        GRPC channel according to the configuration. Passes optional channel options to
        construct the channel.

        Returns
        -------
        GRPC Channel instance.
        """

class MetricValue:
    def __init__(self, name: str, value: int | float, type: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int | float: ...
    @property
    def metric_type(self) -> str: ...

class PlanMetrics:
    def __init__(self, name: str, id: int, parent: int, metrics: List[MetricValue]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def plan_id(self) -> int: ...
    @property
    def parent_plan_id(self) -> int: ...
    @property
    def metrics(self) -> List[MetricValue]: ...

class PlanObservedMetrics:
    def __init__(self, name: str, metrics: List[pb2.Expression.Literal]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def metrics(self) -> List[pb2.Expression.Literal]: ...

class AnalyzeResult:
    schema: Incomplete
    explain_string: Incomplete
    tree_string: Incomplete
    is_local: Incomplete
    is_streaming: Incomplete
    input_files: Incomplete
    spark_version: Incomplete
    parsed: Incomplete
    is_same_semantics: Incomplete
    semantic_hash: Incomplete
    storage_level: Incomplete
    def __init__(self, schema: DataType | None, explain_string: str | None, tree_string: str | None, is_local: bool | None, is_streaming: bool | None, input_files: List[str] | None, spark_version: str | None, parsed: DataType | None, is_same_semantics: bool | None, semantic_hash: int | None, storage_level: StorageLevel | None) -> None: ...
    @classmethod
    def fromProto(cls, pb: Any) -> AnalyzeResult: ...

class ConfigResult:
    pairs: Incomplete
    warnings: Incomplete
    def __init__(self, pairs: List[Tuple[str, str | None]], warnings: List[str]) -> None: ...
    @classmethod
    def fromProto(cls, pb: pb2.ConfigResponse) -> ConfigResult: ...

class SparkConnectClient:
    """
    Conceptually the remote spark session that communicates with the server

    .. versionadded:: 3.4.0
    """
    @classmethod
    def retry_exception(cls, e: Exception) -> bool: ...
    def __init__(self, connectionString: str, userId: str | None = None, channelOptions: List[Tuple[str, Any]] | None = None, retryPolicy: Dict[str, Any] | None = None) -> None:
        """
        Creates a new SparkSession for the Spark Connect interface.

        Parameters
        ----------
        connectionString: Optional[str]
            Connection string that is used to extract the connection parameters and configure
            the GRPC connection. Defaults to `sc://localhost`.
        userId : Optional[str]
            Optional unique user ID that is used to differentiate multiple users and
            isolate their Spark Sessions. If the `user_id` is not set, will default to
            the $USER environment. Defining the user ID as part of the connection string
            takes precedence.
        """
    def register_udf(self, function: Any, return_type: DataTypeOrString, name: str | None = None, eval_type: int = ..., deterministic: bool = True) -> str:
        """
        Create a temporary UDF in the session catalog on the other side. We generate a
        temporary name for it.
        """
    def register_java(self, name: str, javaClassName: str, return_type: DataTypeOrString | None = None, aggregate: bool = False) -> None: ...
    def to_table_as_iterator(self, plan: pb2.Plan) -> Iterator[StructType | pa.Table]:
        """
        Return given plan as a PyArrow Table iterator.
        """
    def to_table(self, plan: pb2.Plan) -> Tuple['pa.Table', StructType | None]:
        """
        Return given plan as a PyArrow Table.
        """
    def to_pandas(self, plan: pb2.Plan) -> pd.DataFrame:
        """
        Return given plan as a pandas DataFrame.
        """
    def schema(self, plan: pb2.Plan) -> StructType:
        """
        Return schema for given plan.
        """
    def explain_string(self, plan: pb2.Plan, explain_mode: str = 'extended') -> str:
        """
        Return explain string for given plan.
        """
    def execute_command(self, command: pb2.Command) -> Tuple[pd.DataFrame | None, Dict[str, Any]]:
        """
        Execute given command.
        """
    def same_semantics(self, plan: pb2.Plan, other: pb2.Plan) -> bool:
        """
        return if two plans have the same semantics.
        """
    def semantic_hash(self, plan: pb2.Plan) -> int:
        """
        returns a `hashCode` of the logical query plan.
        """
    def close(self) -> None:
        """
        Close the channel.
        """
    def config(self, operation: pb2.ConfigRequest.Operation) -> ConfigResult:
        """
        Call the config RPC of Spark Connect.

        Parameters
        ----------
        operation : str
           Operation kind

        Returns
        -------
        The result of the config call.
        """

class RetryState:
    """
    Simple state helper that captures the state between retries of the exceptions. It
    keeps track of the last exception thrown and how many in total. When the task
    finishes successfully done() returns True.
    """
    def __init__(self) -> None: ...
    def set_exception(self, exc: BaseException | None) -> None: ...
    def exception(self) -> BaseException | None: ...
    def set_done(self) -> None: ...
    def count(self) -> int: ...
    def done(self) -> bool: ...

class AttemptManager:
    """
    Simple ContextManager that is used to capture the exception thrown inside the context.
    """
    def __init__(self, check: Callable[..., bool], retry_state: RetryState) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...

class Retrying:
    """
    This helper class is used as a generator together with a context manager to
    allow retrying exceptions in particular code blocks. The Retrying can be configured
    with a lambda function that is can be filtered what kind of exceptions should be
    retried.

    In addition, there are several parameters that are used to configure the exponential
    backoff behavior.

    An example to use this class looks like this:

    .. code-block:: python

        for attempt in Retrying(can_retry=lambda x: isinstance(x, TransientError)):
            with attempt:
                # do the work.

    """
    def __init__(self, max_retries: int, initial_backoff: int, max_backoff: int, backoff_multiplier: float, can_retry: Callable[..., bool] = ...) -> None: ...
    def __iter__(self) -> Generator[AttemptManager, None, None]:
        """
        Generator function to wrap the exception producing code block.

        Returns
        -------
        A generator that yields the current attempt.
        """
