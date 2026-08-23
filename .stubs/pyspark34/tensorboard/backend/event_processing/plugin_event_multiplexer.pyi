from _typeshed import Incomplete
from tensorboard.backend.event_processing import directory_watcher as directory_watcher, io_wrapper as io_wrapper
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class EventMultiplexer:
    """An `EventMultiplexer` manages access to multiple `EventAccumulator`s.

    Each `EventAccumulator` is associated with a `run`, which is a self-contained
    TensorFlow execution. The `EventMultiplexer` provides methods for extracting
    information about events from multiple `run`s.

    Example usage for loading specific runs from files:

    ```python
    x = EventMultiplexer({'run1': 'path/to/run1', 'run2': 'path/to/run2'})
    x.Reload()
    ```

    Example usage for loading a directory where each subdirectory is a run

    ```python
    (eg:) /parent/directory/path/
          /parent/directory/path/run1/
          /parent/directory/path/run1/events.out.tfevents.1001
          /parent/directory/path/run1/events.out.tfevents.1002

          /parent/directory/path/run2/
          /parent/directory/path/run2/events.out.tfevents.9232

          /parent/directory/path/run3/
          /parent/directory/path/run3/events.out.tfevents.9232
    x = EventMultiplexer().AddRunsFromDirectory('/parent/directory/path')
    (which is equivalent to:)
    x = EventMultiplexer({'run1': '/parent/directory/path/run1', 'run2':...}
    ```

    If you would like to watch `/parent/directory/path`, wait for it to be created
      (if necessary) and then periodically pick up new runs, use
      `AutoloadingMultiplexer`
    @@Tensors
    """
    purge_orphaned_data: Incomplete
    def __init__(self, run_path_map: Incomplete | None = None, size_guidance: Incomplete | None = None, tensor_size_guidance: Incomplete | None = None, purge_orphaned_data: bool = True, max_reload_threads: Incomplete | None = None, event_file_active_filter: Incomplete | None = None, detect_file_replacement: Incomplete | None = None) -> None:
        '''Constructor for the `EventMultiplexer`.

        Args:
          run_path_map: Dict `{run: path}` which specifies the
            name of a run, and the path to find the associated events. If it is
            None, then the EventMultiplexer initializes without any runs.
          size_guidance: A dictionary mapping from `tagType` to the number of items
            to store for each tag of that type. See
            `event_accumulator.EventAccumulator` for details.
          tensor_size_guidance: A dictionary mapping from `plugin_name` to
            the number of items to store for each tag of that type. See
            `event_accumulator.EventAccumulator` for details.
          purge_orphaned_data: Whether to discard any events that were "orphaned" by
            a TensorFlow restart.
          max_reload_threads: The max number of threads that TensorBoard can use
            to reload runs. Each thread reloads one run at a time. If not provided,
            reloads runs serially (one after another).
          event_file_active_filter: Optional predicate for determining whether an
            event file latest load timestamp should be considered active. If passed,
            this will enable multifile directory loading.
          detect_file_replacement: Optional boolean; if True, event file loading
            will try to detect when a file has been replaced with a new version
            that contains additional data, by monitoring the file size.
        '''
    def AddRun(self, path, name: Incomplete | None = None):
        """Add a run to the multiplexer.

        If the name is not specified, it is the same as the path.

        If a run by that name exists, and we are already watching the right path,
          do nothing. If we are watching a different path, replace the event
          accumulator.

        If `Reload` has been called, it will `Reload` the newly created
        accumulators.

        Args:
          path: Path to the event files (or event directory) for given run.
          name: Name of the run to add. If not provided, is set to path.

        Returns:
          The `EventMultiplexer`.
        """
    def AddRunsFromDirectory(self, path, name: Incomplete | None = None):
        '''Load runs from a directory; recursively walks subdirectories.

        If path doesn\'t exist, no-op. This ensures that it is safe to call
          `AddRunsFromDirectory` multiple times, even before the directory is made.

        If path is a directory, load event files in the directory (if any exist) and
          recursively call AddRunsFromDirectory on any subdirectories. This mean you
          can call AddRunsFromDirectory at the root of a tree of event logs and
          TensorBoard will load them all.

        If the `EventMultiplexer` is already loaded this will cause
        the newly created accumulators to `Reload()`.
        Args:
          path: A string path to a directory to load runs from.
          name: Optionally, what name to apply to the runs. If name is provided
            and the directory contains run subdirectories, the name of each subrun
            is the concatenation of the parent name and the subdirectory name. If
            name is provided and the directory contains event files, then a run
            is added called "name" and with the events from the path.

        Raises:
          ValueError: If the path exists and isn\'t a directory.

        Returns:
          The `EventMultiplexer`.
        '''
    def Reload(self):
        """Call `Reload` on every `EventAccumulator`."""
    def PluginAssets(self, plugin_name):
        """Get index of runs and assets for a given plugin.

        Args:
          plugin_name: Name of the plugin we are checking for.

        Returns:
          A dictionary that maps from run_name to a list of plugin
            assets for that run.
        """
    def RetrievePluginAsset(self, run, plugin_name, asset_name):
        """Return the contents for a specific plugin asset from a run.

        Args:
          run: The string name of the run.
          plugin_name: The string name of a plugin.
          asset_name: The string name of an asset.

        Returns:
          The string contents of the plugin asset.

        Raises:
          KeyError: If the asset is not available.
        """
    def FirstEventTimestamp(self, run):
        """Return the timestamp of the first event of the given run.

        This may perform I/O if no events have been loaded yet for the run.

        Args:
          run: A string name of the run for which the timestamp is retrieved.

        Returns:
          The wall_time of the first event of the run, which will typically be
          seconds since the epoch.

        Raises:
          KeyError: If the run is not found.
          ValueError: If the run has no events loaded and there are no events on
            disk to load.
        """
    def GetSourceWriter(self, run) -> str | None:
        """Returns the source writer name from the first event of the given run.

        Assuming each run has only one source writer.

        Args:
          run: A string name of the run from which the event source information
            is retrieved.

        Returns:
          Name of the writer that wrote the events in the run.
        """
    def Graph(self, run):
        """Retrieve the graph associated with the provided run.

        Args:
          run: A string name of a run to load the graph for.

        Raises:
          KeyError: If the run is not found.
          ValueError: If the run does not have an associated graph.

        Returns:
          The `GraphDef` protobuf data structure.
        """
    def SerializedGraph(self, run):
        """Retrieve the serialized graph associated with the provided run.

        Args:
          run: A string name of a run to load the graph for.

        Raises:
          KeyError: If the run is not found.
          ValueError: If the run does not have an associated graph.

        Returns:
          The serialized form of the `GraphDef` protobuf data structure.
        """
    def MetaGraph(self, run):
        """Retrieve the metagraph associated with the provided run.

        Args:
          run: A string name of a run to load the graph for.

        Raises:
          KeyError: If the run is not found.
          ValueError: If the run does not have an associated graph.

        Returns:
          The `MetaGraphDef` protobuf data structure.
        """
    def RunMetadata(self, run, tag):
        """Get the session.run() metadata associated with a TensorFlow run and
        tag.

        Args:
          run: A string name of a TensorFlow run.
          tag: A string name of the tag associated with a particular session.run().

        Raises:
          KeyError: If the run is not found, or the tag is not available for the
            given run.

        Returns:
          The metadata in the form of `RunMetadata` protobuf data structure.
        """
    def Tensors(self, run, tag):
        """Retrieve the tensor events associated with a run and tag.

        Args:
          run: A string name of the run for which values are retrieved.
          tag: A string name of the tag for which values are retrieved.

        Raises:
          KeyError: If the run is not found, or the tag is not available for
            the given run.

        Returns:
          An array of `event_accumulator.TensorEvent`s.
        """
    def PluginRunToTagToContent(self, plugin_name):
        """Returns a 2-layer dictionary of the form {run: {tag: content}}.

        The `content` referred above is the content field of the PluginData proto
        for the specified plugin within a Summary.Value proto.

        Args:
          plugin_name: The name of the plugin for which to fetch content.

        Returns:
          A dictionary of the form {run: {tag: content}}.
        """
    def ActivePlugins(self):
        """Return a set of plugins with summary data.

        Returns:
          The distinct union of `plugin_data.plugin_name` fields from
          all the `SummaryMetadata` protos stored in any run known to
          this multiplexer.
        """
    def SummaryMetadata(self, run, tag):
        """Return the summary metadata for the given tag on the given run.

        Args:
          run: A string name of the run for which summary metadata is to be
            retrieved.
          tag: A string name of the tag whose summary metadata is to be
            retrieved.

        Raises:
          KeyError: If the run is not found, or the tag is not available for
            the given run.

        Returns:
          A `SummaryMetadata` protobuf.
        """
    def AllSummaryMetadata(self):
        """Return summary metadata for all time series.

        Returns:
          A nested dict `d` such that `d[run][tag]` is a
          `SummaryMetadata` proto for the keyed time series.
        """
    def Runs(self):
        """Return all the run names in the `EventMultiplexer`.

        Returns:
        ```
          {runName: { scalarValues: [tagA, tagB, tagC],
                      graph: true, meta_graph: true}}
        ```
        """
    def RunPaths(self):
        """Returns a dict mapping run names to event file paths."""
    def GetAccumulator(self, run):
        """Returns EventAccumulator for a given run.

        Args:
          run: String name of run.

        Returns:
          An EventAccumulator object.

        Raises:
          KeyError: If run does not exist.
        """
