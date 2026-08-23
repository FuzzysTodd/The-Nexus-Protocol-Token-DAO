from _typeshed import Incomplete

class ResultDict(dict):
    """Dictionary holding analysis results.

    Conversion methods (e.g. to Pandas DataFrames) to be attached as necessary
    by each implementing method
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def to_df(self):
        """Convert dict structure into Pandas DataFrame."""
    def plot(self, ax: Incomplete | None = None):
        """Create bar chart of results"""
