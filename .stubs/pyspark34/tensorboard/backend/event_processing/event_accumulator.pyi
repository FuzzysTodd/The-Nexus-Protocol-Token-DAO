import dataclasses
from _typeshed import Incomplete
from tensorboard.backend.event_processing import directory_watcher as directory_watcher, event_file_loader as event_file_loader, event_util as event_util, io_wrapper as io_wrapper, plugin_asset_util as plugin_asset_util, reservoir as reservoir, tag_types as tag_types
from tensorboard.compat.proto import config_pb2 as config_pb2, event_pb2 as event_pb2, graph_pb2 as graph_pb2, meta_graph_pb2 as meta_graph_pb2, tensor_pb2 as tensor_pb2
from tensorboard.plugins.distribution import compressor as compressor
from tensorboard.util import tb_logging as tb_logging
from typing import Sequence, Tuple

logger: Incomplete

@dataclasses.dataclass(frozen=True)
class ScalarEvent:
    """Contains information of a scalar event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      value: A float or int value of the scalar.
    """
    wall_time: float
    step: int
    value: float
    def __init__(self, wall_time, step, value) -> None: ...

@dataclasses.dataclass(frozen=True)
class CompressedHistogramEvent:
    """Contains information of a compressed histogram event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      compressed_histogram_values: A sequence of tuples of basis points and
        associated values in a compressed histogram.
    """
    wall_time: float
    step: int
    compressed_histogram_values: Sequence[Tuple[float, float]]
    def __init__(self, wall_time, step, compressed_histogram_values) -> None: ...

@dataclasses.dataclass(frozen=True)
class HistogramValue:
    """Holds the information of the histogram values.

    Attributes:
      min: A float or int min value.
      max: A float or int max value.
      num: Total number of values.
      sum: Sum of all values.
      sum_squares: Sum of squares for all values.
      bucket_limit: Upper values per bucket.
      bucket: Numbers of values per bucket.
    """
    min: float
    max: float
    num: int
    sum: float
    sum_squares: float
    bucket_limit: Sequence[float]
    bucket: Sequence[int]
    def __init__(self, min, max, num, sum, sum_squares, bucket_limit, bucket) -> None: ...

@dataclasses.dataclass(frozen=True)
class HistogramEvent:
    """Contains information of a histogram event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      histogram_value: Information of the histogram values.
    """
    wall_time: float
    step: int
    histogram_value: HistogramValue
    def __init__(self, wall_time, step, histogram_value) -> None: ...

@dataclasses.dataclass(frozen=True)
class ImageEvent:
    """Contains information of an image event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      encoded_image_string: Image content encoded in bytes.
      width: Width of the image.
      height: Height of the image.
    """
    wall_time: float
    step: int
    encoded_image_string: bytes
    width: int
    height: int
    def __init__(self, wall_time, step, encoded_image_string, width, height) -> None: ...

@dataclasses.dataclass(frozen=True)
class AudioEvent:
    """Contains information of an audio event.

    Attributes:
      wall_time: Timestamp of the event in seconds.
      step: Global step of the event.
      encoded_audio_string: Audio content encoded in bytes.
      content_type: A string describes the type of the audio content.
      sample_rate: Sample rate of the audio in Hz. Must be positive.
      length_frames: Length of the audio in frames (samples per channel).
    """
    wall_time: float
    step: int
    encoded_audio_string: bytes
    content_type: str
    sample_rate: float
    length_frames: int
    def __init__(self, wall_time, step, encoded_audio_string, content_type, sample_rate, length_frames) -> None: ...

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

SUMMARY_TYPES: Incomplete
COMPRESSED_HISTOGRAMS: Incomplete
HISTOGRAMS: Incomplete
IMAGES: Incomplete
AUDIO: Incomplete
SCALARS: Incomplete
TENSORS: Incomplete
GRAPH: Incomplete
META_GRAPH: Incomplete
RUN_METADATA: Incomplete
NORMAL_HISTOGRAM_BPS: Incomplete
DEFAULT_SIZE_GUIDANCE: Incomplete
STORE_EVERYTHING_SIZE_GUIDANCE: Incomplete

class EventAccumulator:
    """An `EventAccumulator` takes an event generator, and accumulates the
    values.

    The `EventAccumulator` is intended to provide a convenient Python interface
    for loading Event data written during a TensorFlow run. TensorFlow writes out
    `Event` protobuf objects, which have a timestamp and step number, and often
    contain a `Summary`. Summaries can have different kinds of data like an image,
    a scalar value, or a histogram. The Summaries also have a tag, which we use to
    organize logically related data. The `EventAccumulator` supports retrieving
    the `Event` and `Summary` data by its tag.

    Calling `Tags()` gets a map from `tagType` (e.g. `'images'`,
    `'compressedHistograms'`, `'scalars'`, etc) to the associated tags for those
    data types. Then, various functional endpoints (eg
    `Accumulator.Scalars(tag)`) allow for the retrieval of all data
    associated with that tag.

    The `Reload()` method synchronously loads all of the data written so far.

    Histograms, audio, and images are very large, so storing all of them is not
    recommended.

    Fields:
      audios: A reservoir.Reservoir of audio summaries.
      compressed_histograms: A reservoir.Reservoir of compressed
          histogram summaries.
      histograms: A reservoir.Reservoir of histogram summaries.
      images: A reservoir.Reservoir of image summaries.
      most_recent_step: Step of last Event proto added. This should only
          be accessed from the thread that calls Reload. This is -1 if
          nothing has been loaded yet.
      most_recent_wall_time: Timestamp of last Event proto added. This is
          a float containing seconds from the UNIX epoch, or -1 if
          nothing has been loaded yet. This should only be accessed from
          the thread that calls Reload.
      path: A file path to a directory containing tf events files, or a single
          tf events file. The accumulator will load events from this path.
      scalars: A reservoir.Reservoir of scalar summaries.
      tensors: A reservoir.Reservoir of tensor summaries.

    @@Tensors
    """
    scalars: Incomplete
    summary_metadata: Incomplete
    histograms: Incomplete
    compressed_histograms: Incomplete
    images: Incomplete
    audios: Incomplete
    tensors: Incomplete
    path: Incomplete
    purge_orphaned_data: Incomplete
    most_recent_step: int
    most_recent_wall_time: int
    file_version: Incomplete
    accumulated_attrs: Incomplete
    def __init__(self, path, size_guidance: Incomplete | None = None, compression_bps=..., purge_orphaned_data: bool = True) -> None:
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
          compression_bps: Information on how the `EventAccumulator` should compress
            histogram data for the `CompressedHistograms` tag (for details see
            `ProcessCompressedHistogram`).
          purge_orphaned_data: Whether to discard any events that were "orphaned" by
            a TensorFlow restart.
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
    def SummaryMetadata(self, tag):
        """Given a summary tag name, return the associated metadata object.

        Args:
          tag: The name of a tag, as a string.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          A `SummaryMetadata` protobuf.
        """
    def Tags(self):
        """Return all tags found in the value stream.

        Returns:
          A `{tagType: ['list', 'of', 'tags']}` dictionary.
        """
    def Scalars(self, tag):
        """Given a summary tag, return all associated `ScalarEvent`s.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `ScalarEvent`s.
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
    def Histograms(self, tag):
        """Given a summary tag, return all associated histograms.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `HistogramEvent`s.
        """
    def CompressedHistograms(self, tag):
        """Given a summary tag, return all associated compressed histograms.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `CompressedHistogramEvent`s.
        """
    def Images(self, tag):
        """Given a summary tag, return all associated images.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `ImageEvent`s.
        """
    def Audio(self, tag):
        """Given a summary tag, return all associated audio.

        Args:
          tag: A string tag associated with the events.

        Raises:
          KeyError: If the tag is not found.

        Returns:
          An array of `AudioEvent`s.
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
