from _typeshed import Incomplete
from tensorboard import errors as errors

DEFAULT_DEBUGGER_RUN_NAME: str
DEFAULT_PER_TYPE_ALERT_LIMIT: int
DEFAULT_RELOAD_INTERVAL_SEC: int

def run_repeatedly_in_background(target, interval_sec):
    """Run a target task repeatedly in the background.

    In the context of this module, `target` is the `update()` method of the
    underlying reader for tfdbg2-format data.
    This method is mocked by unit tests for deterministic behaviors during
    testing.

    Args:
      target: The target task to run in the background, a callable with no args.
      interval_sec: Time interval between repeats, in seconds.

    Returns:
      - A `threading.Event` object that can be used to interrupt an ongoing
          waiting interval between successive runs of `target`. To interrupt the
          interval, call the `set()` method of the object.
      - The `threading.Thread` object on which `target` is run repeatedly.
    """
def parse_tensor_name(tensor_name):
    """Helper function that extracts op name and slot from tensor name."""

class DebuggerV2EventMultiplexer:
    """A class used for accessing tfdbg v2 DebugEvent data on local filesystem.

    This class is a short-term hack, mirroring the EventMultiplexer for the main
    TensorBoard plugins (e.g., scalar, histogram and graphs.) As such, it only
    implements the methods relevant to the Debugger V2 pluggin.

    TODO(cais): Integrate it with EventMultiplexer and use the integrated class
    from MultiplexerDataProvider for a single path of accessing debugger and
    non-debugger data.
    """
    def __init__(self, logdir) -> None:
        """Constructor for the `DebugEventMultiplexer`.

        Args:
          logdir: Path to the directory to load the tfdbg v2 data from.
        """
    def FirstEventTimestamp(self, run):
        """Return the timestamp of the first DebugEvent of the given run.

        This may perform I/O if no events have been loaded yet for the run.

        Args:
          run: A string name of the run for which the timestamp is retrieved.
            This currently must be hardcoded as `DEFAULT_DEBUGGER_RUN_NAME`,
            as each logdir contains at most one DebugEvent file set (i.e., a
            run of a tfdbg2-instrumented TensorFlow program.)

        Returns:
            The wall_time of the first event of the run, which will be in seconds
            since the epoch as a `float`.
        """
    def PluginRunToTagToContent(self, plugin_name) -> None: ...
    def Runs(self):
        '''Return all the tfdbg2 run names in the logdir watched by this instance.

        The `Run()` method of this class is specialized for the tfdbg2-format
        DebugEvent files.

        As a side effect, this method unblocks the underlying reader\'s period
        reloading if a reader exists. This lets the reader update at a higher
        frequency than the default one with 30-second sleeping period between
        reloading when data is being queried actively from this instance.
        Note that this `Runs()` method is used by all other public data-access
        methods of this class (e.g., `ExecutionData()`, `GraphExecutionData()`).
        Hence calls to those methods will lead to accelerated data reloading of
        the reader.

        Returns:
          If tfdbg2-format data exists in the `logdir` of this object, returns:
              ```
              {runName: { "debugger-v2": [tag1, tag2, tag3] } }
              ```
              where `runName` is the hard-coded string `DEFAULT_DEBUGGER_RUN_NAME`
              string. This is related to the fact that tfdbg2 currently contains
              at most one DebugEvent file set per directory.
          If no tfdbg2-format data exists in the `logdir`, an empty `dict`.
        '''
    def Alerts(self, run, begin, end, alert_type_filter: Incomplete | None = None):
        """Get alerts from the debugged TensorFlow program.

        Args:
          run: The tfdbg2 run to get Alerts from.
          begin: Beginning alert index.
          end: Ending alert index.
          alert_type_filter: Optional filter string for alert type, used to
            restrict retrieved alerts data to a single type. If used,
            `begin` and `end` refer to the beginning and ending indices within
            the filtered alert type.
        """
    def ExecutionDigests(self, run, begin, end):
        """Get ExecutionDigests.

        Args:
          run: The tfdbg2 run to get `ExecutionDigest`s from.
          begin: Beginning execution index.
          end: Ending execution index.

        Returns:
          A JSON-serializable object containing the `ExecutionDigest`s and
          related meta-information
        """
    def ExecutionData(self, run, begin, end):
        """Get Execution data objects (Detailed, non-digest form).

        Args:
          run: The tfdbg2 run to get `ExecutionDigest`s from.
          begin: Beginning execution index.
          end: Ending execution index.

        Returns:
          A JSON-serializable object containing the `ExecutionDigest`s and
          related meta-information
        """
    def GraphExecutionDigests(self, run, begin, end, trace_id: Incomplete | None = None):
        """Get `GraphExecutionTraceDigest`s.

        Args:
          run: The tfdbg2 run to get `GraphExecutionTraceDigest`s from.
          begin: Beginning graph-execution index.
          end: Ending graph-execution index.

        Returns:
          A JSON-serializable object containing the `ExecutionDigest`s and
          related meta-information
        """
    def GraphExecutionData(self, run, begin, end, trace_id: Incomplete | None = None):
        """Get `GraphExecutionTrace`s.

        Args:
          run: The tfdbg2 run to get `GraphExecutionTrace`s from.
          begin: Beginning graph-execution index.
          end: Ending graph-execution index.

        Returns:
          A JSON-serializable object containing the `ExecutionDigest`s and
          related meta-information
        """
    def GraphInfo(self, run, graph_id):
        """Get the information regarding a TensorFlow graph.

        Args:
          run: Name of the run.
          graph_id: Debugger-generated ID of the graph in question.
            This information is available in the return values
            of `GraphOpInfo`, `GraphExecution`, etc.

        Returns:
          A JSON-serializable object containing the information regarding
            the TensorFlow graph.

        Raises:
          NotFoundError if the graph_id is not known to the debugger.
        """
    def GraphOpInfo(self, run, graph_id, op_name):
        """Get the information regarding a graph op's creation.

        Args:
          run: Name of the run.
          graph_id: Debugger-generated ID of the graph that contains
            the op in question. This ID is available from other methods
            of this class, e.g., the return value of `GraphExecutionDigests()`.
          op_name: Name of the op.

        Returns:
          A JSON-serializable object containing the information regarding
            the op's creation and its immediate inputs and consumers.

        Raises:
          NotFoundError if the graph_id or op_name does not exist.
        """
    def SourceFileList(self, run): ...
    def SourceLines(self, run, index): ...
    def StackFrames(self, run, stack_frame_ids): ...
