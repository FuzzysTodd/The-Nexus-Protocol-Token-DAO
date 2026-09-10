import dataclasses
from _typeshed import Incomplete
from tensorboard.backend.event_processing import directory_loader as directory_loader, directory_watcher as directory_watcher, event_file_loader as event_file_loader, event_util as event_util, io_wrapper as io_wrapper, plugin_asset_util as plugin_asset_util, reservoir as reservoir, tag_types as tag_types
from tensorboard.compat.proto import config_pb2 as config_pb2, event_pb2 as event_pb2, graph_pb2 as graph_pb2, meta_graph_pb2 as meta_graph_pb2, tensor_pb2 as tensor_pb2
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete
TENSORS: Incomplete
GRAPH: Incomplete
META_GRAPH: Incomplete
RUN_METADATA: Incomplete
DEFAULT_SIZE_GUIDANCE: Incomplete
STORE_EVERYTHING_SIZE_GUIDANCE: Incomplete

@dataclasses.dataclass(frozen=True)
class TensorEvent:
    """A tensor event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      tensor_proto: A `TensorProto`.
    """
    wall_time: float
    step: int
    tensor_proto: tensor_pb2.TensorProto
    def __init__(self, wall_time, step, tensor_proto) -> None: ...

class EventAccumulator:
    """An `EventAccumulator` takes an event generator, and accumulates the
    values.

    The `EventAccumulator` is intended to provide a convenient Python
    interface for loading Event data written during a TensorFlow run.
    TensorFlow writes out `Event` protobuf objects, which have a timestamp
    and step number, and often contain a `Summary`. Summaries can have
    different kinds of data stored as arbitrary tensors. The Summaries
    also have a tag, which we use to organize logically related data. The
    `EventAccumulator` supports retrieving the `Event` and `Summary` data
    by its tag.

    Calling `Tags()` gets a map from `tagType` (i.e., `tensors`) to the
    associated tags for those data types. Then, the functional endpoint
    (i.g., `Accumulator.Tensors(tag)`) allows for the retrieval of all
    data associated with that tag.

    The `Reload()` method synchronously loads all of the data written so far.

    Fields:
      most_recent_step: Step of last Event proto added. This should only
          be accessed from the thread that calls Reload. This is -1 if
          nothing has been loaded yet.
      most_recent_wall_time: Timestamp of last Event proto added. This is
          a float containing seconds from the UNIX epoch, or -1 if
          nothing has been loaded yet. This should only be accessed from
          the thread that calls Reload.
      path: A file path to a directory containing tf events files, or a single
          tf events file. The accumulator will load events from this path.
      tensors_by_tag: A dictionary mapping each tag name to a
        reservoir.Reservoir of tensor summaries. Each such reservoir will
        only use a single key, given by `_TENSOR_RESERVOIR_KEY`.

    @@Tensors
    """
    summary_metadata: Incomplete
    tensors_by_tag: Incomplete
    path: Incomplete
    purge_orphaned_data: Incomplete
    most_recent_step: int
    most_recent_wall_time: int
    file_version: Incomplete
    def __init__(self, path, size_guidance: Incomplete | None = None, tensor_size_guidance: Incomplete | None = None, purge_orphaned_data: bool = True, event_file_active_filter: Incomplete | None = None, detect_file_replacement: Incomplete | None = None) -> None:
        '''Construct the `EventAccumulator`.

        Args:
          path: A file path to a directory containing tf events files, or a single
            tf events file. The accumulator will load events from this path.
          size_guidance: Information on how much data the EventAccumulator should
            store in memory. The DEFAULT_SIZE_GUIDANCE tries not to store too much
            so as to avoid OOMing the client. The size_guidance should be a map
            from a `tagType` string to an integer representing the number of
            items to keep per tag for items of that `tagType`. If the size is 0,
            all events are stored.
          tensor_size_guidance: Like `size_guidance`, but allowing finer
            granularity for tensor summaries. Should be a map from the
            `plugin_name` field on the `PluginData` proto to an integer
            representing the number of items to keep per tag. Plugins for
            which there is no entry in this map will default to the value of
            `size_guidance[event_accumulator.TENSORS]`. Defaults to `{}`.
          purge_orphaned_data: Whether to discard any events that were "orphaned" by
            a TensorFlow restart.
          event_file_active_filter: Optional predicate for determining whether an
            event file latest load timestamp should be considered active. If passed,
            this will enable multifile directory loading.
          detect_file_replacement: Optional boolean; if True, event file loading
            will try to detect when a file has been replaced with a new version
            that contains additional data, by monitoring the file size.
        '''
    def Reload(self):
        """Loads all events added since the last call to `Reload`.

        If `Reload` was never called, loads all events in the file.

        Returns:
          The `EventAccumulator`.
        """
    def PluginAssets(self, plugin_name):
        """Return a list of all plugin assets for the given plugin.

        Args:
          plugin_name: The string name of a plugin to retrieve assets for.

        Returns:
          A list of string plugin asset names, or empty list if none are available.
          If the plugin was not registered, an empty list is returned.
        """
    def RetrievePluginAsset(self, plugin_name, asset_name):
        """Return the contents of a given plugin asset.

        Args:
          plugin_name: The string name of a plugin.
          asset_name: The string name of an asset.

        Returns:
          The string contents of the plugin asset.

        Raises:
          KeyError: If the asset is not available.
        """
    def FirstEventTimestamp(self):
        """Returns the timestamp in seconds of the first event.

        If the first event has been loaded (either by this method or by `Reload`,
        this returns immediately. Otherwise, it will load in the first event. Note
        that this means that calling `Reload` will cause this to block until
        `Reload` has finished.

        Returns:
          The timestamp in seconds of the first event that was loaded.

        Raises:
          ValueError: If no events have been loaded and there were no events found
          on disk.
        """
    def GetSourceWriter(self) -> str | None:
        """Returns the name of the event writer."""
    def PluginTagToContent(self, plugin_name):
        """Returns a dict mapping tags to content specific to that plugin.

        Args:
          plugin_name: The name of the plugin for which to fetch plugin-specific
            content.

        Raises:
          KeyError: if the plugin name is not found.

        Returns:
          A dict mapping tag names to bytestrings of plugin-specific content-- by
          convention, in the form of binary serialized protos.
        """
    def ActivePlugins(self):
        """Return a set of plugins with summary data.

        Returns:
          The distinct union of `plugin_data.plugin_name` fields from
          all the `SummaryMetadata` protos stored in this accumulator.
        """
    def SummaryMetadata(self, tag):
        """Given a summary tag name, return the associated metadata object.

        Args:
          tag: The name of a tag, as a string.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          A `SummaryMetadata` protobuf.
        """
    def AllSummaryMetadata(self):
        """Return summary metadata for all tags.

        Returns:
          A dict `d` such that `d[tag]` is a `SummaryMetadata` proto for
          the keyed tag.
        """
    def Tags(self):
        """Return all tags found in the value stream.

        Returns:
          A `{tagType: ['list', 'of', 'tags']}` dictionary.
        """
    def Graph(self):
        """Return the graph definition, if there is one.

        If the graph is stored directly, return that.  If no graph is stored
        directly but a metagraph is stored containing a graph, return that.

        Raises:
          ValueError: If there is no graph for this run.

        Returns:
          The `graph_def` proto.
        """
    def SerializedGraph(self):
        """Return the graph definition in serialized form, if there is one."""
    def MetaGraph(self):
        """Return the metagraph definition, if there is one.

        Raises:
          ValueError: If there is no metagraph for this run.

        Returns:
          The `meta_graph_def` proto.
        """
    def RunMetadata(self, tag):
        """Given a tag, return the associated session.run() metadata.

        Args:
          tag: A string tag associated with the event.

        Raises:
          ValueError: If the tag is not found.

        Returns:
          The metadata in form of `RunMetadata` proto.
        """
    def Tensors(self, tag):
        """Given a summary tag, return all associated tensors.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `TensorEvent`s.
        """
