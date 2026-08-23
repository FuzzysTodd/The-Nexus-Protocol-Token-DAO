class DatasetsError(Exception):
    """Base class for exceptions in this library."""
class DefunctDatasetError(DatasetsError):
    """The dataset has been defunct."""
