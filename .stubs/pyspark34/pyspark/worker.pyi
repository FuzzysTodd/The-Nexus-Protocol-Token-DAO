from _typeshed import Incomplete
from pyspark import shuffle as shuffle
from pyspark.broadcast import Broadcast as Broadcast
from pyspark.files import SparkFiles as SparkFiles
from pyspark.java_gateway import local_connect_and_auth as local_connect_and_auth
from pyspark.rdd import PythonEvalType as PythonEvalType
from pyspark.resource import ResourceInformation as ResourceInformation
from pyspark.serializers import BatchedSerializer as BatchedSerializer, CPickleSerializer as CPickleSerializer, SpecialLengths as SpecialLengths, UTF8Deserializer as UTF8Deserializer, read_bool as read_bool, read_int as read_int, read_long as read_long, write_int as write_int, write_long as write_long, write_with_length as write_with_length
from pyspark.sql.pandas.serializers import ApplyInPandasWithStateSerializer as ApplyInPandasWithStateSerializer, ArrowStreamPandasUDFSerializer as ArrowStreamPandasUDFSerializer, ArrowStreamUDFSerializer as ArrowStreamUDFSerializer, CogroupUDFSerializer as CogroupUDFSerializer
from pyspark.sql.pandas.types import to_arrow_type as to_arrow_type
from pyspark.sql.types import StructType as StructType
from pyspark.taskcontext import BarrierTaskContext as BarrierTaskContext, TaskContext as TaskContext
from pyspark.util import fail_on_stopiteration as fail_on_stopiteration, try_simplify_traceback as try_simplify_traceback

has_resource_module: bool
pickleSer: Incomplete
utf8_deserializer: Incomplete

def report_times(outfile, boot, init, finish) -> None: ...
def add_path(path) -> None: ...
def read_command(serializer, file): ...
def chain(f, g):
    """chain two functions together"""
def wrap_udf(f, return_type): ...
def wrap_scalar_pandas_udf(f, return_type): ...
def wrap_batch_iter_udf(f, return_type): ...
def wrap_cogrouped_map_pandas_udf(f, return_type, argspec): ...
def wrap_grouped_map_pandas_udf(f, return_type, argspec): ...
def wrap_grouped_map_pandas_udf_with_state(f, return_type):
    """
    Provides a new lambda instance wrapping user function of applyInPandasWithState.

    The lambda instance receives (key series, iterator of value series, state) and performs
    some conversion to be adapted with the signature of user function.

    See the function doc of inner function `wrapped` for more details on what adapter does.
    See the function doc of `mapper` function for
    `eval_type == PythonEvalType.SQL_GROUPED_MAP_PANDAS_UDF_WITH_STATE` for more details on
    the input parameters of lambda function.

    Along with the returned iterator, the lambda instance will also produce the return_type as
    converted to the arrow schema.
    """
def wrap_grouped_agg_pandas_udf(f, return_type): ...
def wrap_window_agg_pandas_udf(f, return_type, runner_conf, udf_index): ...
def wrap_unbounded_window_agg_pandas_udf(f, return_type): ...
def wrap_bounded_window_agg_pandas_udf(f, return_type): ...
def read_single_udf(pickleSer, infile, eval_type, runner_conf, udf_index): ...
def read_udfs(pickleSer, infile, eval_type): ...
def main(infile, outfile) -> None: ...
