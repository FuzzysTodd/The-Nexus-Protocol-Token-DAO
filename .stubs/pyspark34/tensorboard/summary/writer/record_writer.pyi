from tensorboard.compat.tensorflow_stub.pywrap_tensorflow import masked_crc32c as masked_crc32c

class RecordWriter:
    """Write encoded protobuf to a file with packing defined in tensorflow."""
    def __init__(self, writer) -> None:
        """Open a file to keep the tensorboard records.

        Args:
        writer: A file-like object that implements `write`, `flush` and `close`.
        """
    def write(self, data) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self): ...
