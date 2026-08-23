from mlflow.entities._mlflow_object import _MLflowObject

class FileInfo(_MLflowObject):
    """
    Metadata about a file or directory.
    """
    def __init__(self, path, is_dir, file_size) -> None: ...
    def __eq__(self, other): ...
    @property
    def path(self):
        """String path of the file or directory."""
    @property
    def is_dir(self):
        """Whether the FileInfo corresponds to a directory."""
    @property
    def file_size(self):
        """Size of the file or directory. If the FileInfo is a directory, returns None."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
