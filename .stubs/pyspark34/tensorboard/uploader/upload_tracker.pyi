from _typeshed import Incomplete
from collections.abc import Generator

def readable_time_string():
    """Get a human-readable time string for the present."""
def readable_bytes_string(bytes):
    """Get a human-readable string for number of bytes."""

class UploadStats:
    """Statistics of uploading."""
    def __init__(self) -> None: ...
    def add_scalars(self, num_scalars) -> None:
        """Add a batch of scalars.

        Args:
          num_scalars: Number of scalars uploaded in this batch.
        """
    def add_tensors(self, num_tensors, num_tensors_skipped, tensor_bytes, tensor_bytes_skipped) -> None:
        """Add a batch of tensors.

        Args:
          num_tensors: Number of tensors encountered in this batch, including
            the ones skipped due to reasons such as large exceeding limit.
          num_tensors: Number of tensors skipped. This describes a subset of
            `num_tensors` and hence must be `<= num_tensors`.
          tensor_bytes: Total byte size of tensors encountered in this batch,
            including the skipped ones.
          tensor_bytes_skipped: Total byte size of the tensors skipped due to
            reasons such as size exceeding limit.
        """
    def add_blob(self, blob_bytes, is_skipped) -> None:
        """Add a blob.

        Args:
          blob_bytes: Byte size of the blob.
          is_skipped: Whether the uploading of the blob is skipped due to
            reasons such as size exceeding limit.
        """
    def add_plugin(self, plugin_name) -> None:
        """Add a plugin.

        Args:
          plugin_name: Name of the plugin.
        """
    @property
    def num_scalars(self): ...
    @property
    def num_tensors(self): ...
    @property
    def num_tensors_skipped(self): ...
    @property
    def tensor_bytes(self): ...
    @property
    def tensor_bytes_skipped(self): ...
    @property
    def num_blobs(self): ...
    @property
    def num_blobs_skipped(self): ...
    @property
    def blob_bytes(self): ...
    @property
    def blob_bytes_skipped(self): ...
    @property
    def plugin_names(self): ...
    def has_data(self):
        """Has any data been tracked by this instance.

        This counts the tensor and blob data that have been scanned
        but skipped.

        Returns:
          Whether this stats tracking object has tracked any data.
        """
    def summarize(self):
        '''Get a summary string for actually-uploaded and skipped data.

        Calling this property also marks the "last_summarized" timestamp, so that
        the has_new_data_since_last_summarize() will be able to report the correct value
        later.

        Returns:
          A tuple with two items:
          - A string summarizing all data uploaded so far.
          - If any data was skipped, a string for all skipped data. Else, `None`.
        '''
    def has_new_data_since_last_summarize(self): ...

class UploadTracker:
    """Tracker for uploader progress and status."""
    def __init__(self, verbosity, one_shot: bool = False) -> None: ...
    def has_data(self):
        """Determine if any data has been uploaded under the tracker's watch."""
    def add_plugin_name(self, plugin_name) -> None: ...
    def send_tracker(self) -> Generator[None, None, None]:
        """Create a context manager for a round of data sending."""
    def scalars_tracker(self, num_scalars) -> Generator[None, None, None]:
        """Create a context manager for tracking a scalar batch upload.

        Args:
          num_scalars: Number of scalars in the batch.
        """
    def tensors_tracker(self, num_tensors, num_tensors_skipped, tensor_bytes, tensor_bytes_skipped) -> Generator[None, None, None]:
        """Create a context manager for tracking a tensor batch upload.

        Args:
          num_tensors: Total number of tensors in the batch.
          num_tensors_skipped: Number of tensors skipped (a subset of
            `num_tensors`). Hence this must be `<= num_tensors`.
          tensor_bytes: Total byte size of the tensors in the batch.
          tensor_bytes_skipped: Byte size of skipped tensors in the batch (a
            subset of `tensor_bytes`). Must be `<= tensor_bytes`.
        """
    def blob_tracker(self, blob_bytes) -> Generator[Incomplete, None, None]:
        """Creates context manager tracker for uploading a blob.

        Args:
          blob_bytes: Total byte size of the blob being uploaded.
        """

class _BlobTracker:
    def __init__(self, upload_stats, blob_bytes) -> None: ...
    def mark_uploaded(self, is_uploaded) -> None: ...
