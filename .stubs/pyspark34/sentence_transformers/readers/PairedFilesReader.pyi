from . import InputExample as InputExample
from _typeshed import Incomplete

class PairedFilesReader:
    """
    Reads in the a Pair Dataset, split in two files
    """
    filepaths: Incomplete
    def __init__(self, filepaths) -> None: ...
    def get_examples(self, max_examples: int = 0):
        """
        """
