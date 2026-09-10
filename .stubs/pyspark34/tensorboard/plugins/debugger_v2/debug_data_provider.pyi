from _typeshed import Incomplete
from tensorboard.data import provider as provider
from tensorboard.plugins.debugger_v2 import debug_data_multiplexer as debug_data_multiplexer

PLUGIN_NAME: str
ALERTS_BLOB_TAG_PREFIX: str
EXECUTION_DIGESTS_BLOB_TAG_PREFIX: str
EXECUTION_DATA_BLOB_TAG_PREFIX: str
GRAPH_EXECUTION_DIGESTS_BLOB_TAG_PREFIX: str
GRAPH_EXECUTION_DATA_BLOB_TAG_PREFIX: str
GRAPH_INFO_BLOB_TAG_PREFIX: str
GRAPH_OP_INFO_BLOB_TAG_PREFIX: str
SOURCE_FILE_LIST_BLOB_TAG: str
SOURCE_FILE_BLOB_TAG_PREFIX: str
STACK_FRAMES_BLOB_TAG_PREFIX: str

def alerts_run_tag_filter(run, begin, end, alert_type: Incomplete | None = None):
    """Create a RunTagFilter for Alerts.

    Args:
      run: tfdbg2 run name.
      begin: Beginning index of alerts.
      end: Ending index of alerts.
      alert_type: Optional alert type, used to restrict retrieval of alerts
        data to a single type of alerts.

    Returns:
      `RunTagFilter` for the run and range of Alerts.
    """
def execution_digest_run_tag_filter(run, begin, end):
    """Create a RunTagFilter for ExecutionDigests.

    This differs from `execution_data_run_tag_filter()` in that it is for
    the small-size digest objects for execution debug events, instead of the
    full-size data objects.

    Args:
      run: tfdbg2 run name.
      begin: Beginning index of ExecutionDigests.
      end: Ending index of ExecutionDigests.

    Returns:
      `RunTagFilter` for the run and range of ExecutionDigests.
    """
def execution_data_run_tag_filter(run, begin, end):
    """Create a RunTagFilter for Execution data objects.

    This differs from `execution_digest_run_tag_filter()` in that it is
    for the detailed data objects for execution, instead of the digests.

    Args:
      run: tfdbg2 run name.
      begin: Beginning index of Execution.
      end: Ending index of Execution.

    Returns:
      `RunTagFilter` for the run and range of ExecutionDigests.
    """
def graph_execution_digest_run_tag_filter(run, begin, end, trace_id: Incomplete | None = None):
    """Create a RunTagFilter for GraphExecutionTraceDigests.

    This differs from `graph_execution_data_run_tag_filter()` in that it is for
    the small-size digest objects for intra-graph execution debug events, instead
    of the full-size data objects.

    Args:
      run: tfdbg2 run name.
      begin: Beginning index of GraphExecutionTraceDigests.
      end: Ending index of GraphExecutionTraceDigests.

    Returns:
      `RunTagFilter` for the run and range of GraphExecutionTraceDigests.
    """
def graph_execution_data_run_tag_filter(run, begin, end, trace_id: Incomplete | None = None):
    """Create a RunTagFilter for GraphExecutionTrace.

    This method differs from `graph_execution_digest_run_tag_filter()` in that
    it is for full-sized data objects for intra-graph execution events.

    Args:
      run: tfdbg2 run name.
      begin: Beginning index of GraphExecutionTrace.
      end: Ending index of GraphExecutionTrace.

    Returns:
      `RunTagFilter` for the run and range of GraphExecutionTrace.
    """
def graph_op_info_run_tag_filter(run, graph_id, op_name):
    '''Create a RunTagFilter for graph op info.

    Args:
      run: tfdbg2 run name.
      graph_id: Debugger-generated ID of the graph. This is assumed to
        be the ID of the graph that immediately encloses the op in question.
      op_name: Name of the op in question. (e.g., "Dense_1/MatMul")

    Returns:
      `RunTagFilter` for the run and range of graph op info.
    '''
def graph_info_run_tag_filter(run, graph_id):
    """Create a RunTagFilter for graph info.

    Args:
      run: tfdbg2 run name.
      graph_id: Debugger-generated ID of the graph in question.

    Returns:
      `RunTagFilter` for the run and range of graph info.
    """
def source_file_list_run_tag_filter(run):
    """Create a RunTagFilter for listing source files.

    Args:
      run: tfdbg2 run name.

    Returns:
      `RunTagFilter` for listing the source files in the tfdbg2 run.
    """
def source_file_run_tag_filter(run, index):
    """Create a RunTagFilter for listing source files.

    Args:
      run: tfdbg2 run name.
      index: The index for the source file of which the content is to be
        accessed.

    Returns:
      `RunTagFilter` for accessing the content of the source file.
    """
def stack_frames_run_tag_filter(run, stack_frame_ids):
    """Create a RunTagFilter for querying stack frames.

    Args:
      run: tfdbg2 run name.
      stack_frame_ids: The stack_frame_ids being requested.

    Returns:
      `RunTagFilter` for accessing the content of the source file.
    """

class LocalDebuggerV2DataProvider(provider.DataProvider):
    """A DataProvider implementation for tfdbg v2 data on local filesystem.

    In this implementation, `experiment_id` is assumed to be the path to the
    logdir that contains the DebugEvent file set.
    """
    def __init__(self, logdir) -> None:
        """Constructor of LocalDebuggerV2DataProvider.

        Args:
          logdir: Path to the directory from which the tfdbg v2 data will be
            loaded.
        """
    def list_runs(self, ctx: Incomplete | None = None, *, experiment_id):
        """List runs available.

        Args:
          experiment_id: currently unused, because the backing
            DebuggerV2EventMultiplexer does not accommodate multiple experiments.

        Returns:
          Run names as a list of str.
        """
    def list_scalars(self, ctx: Incomplete | None = None, *, experiment_id, plugin_name, run_tag_filter: Incomplete | None = None) -> None: ...
    def read_scalars(self, ctx: Incomplete | None = None, *, experiment_id, plugin_name, downsample: Incomplete | None = None, run_tag_filter: Incomplete | None = None) -> None: ...
    def list_blob_sequences(self, ctx: Incomplete | None = None, *, experiment_id, plugin_name, run_tag_filter: Incomplete | None = None) -> None: ...
    def read_blob_sequences(self, ctx: Incomplete | None = None, *, experiment_id, plugin_name, downsample: Incomplete | None = None, run_tag_filter: Incomplete | None = None): ...
    def read_blob(self, ctx: Incomplete | None = None, *, blob_key): ...
