from . import InputExample as InputExample
from _typeshed import Incomplete

class TripletReader:
    """
    Reads in the a Triplet Dataset: Each line contains (at least) 3 columns, one anchor column (s1),
    one positive example (s2) and one negative example (s3)
    """
    dataset_folder: Incomplete
    s1_col_idx: Incomplete
    s2_col_idx: Incomplete
    s3_col_idx: Incomplete
    has_header: Incomplete
    delimiter: Incomplete
    quoting: Incomplete
    def __init__(self, dataset_folder, s1_col_idx: int = 0, s2_col_idx: int = 1, s3_col_idx: int = 2, has_header: bool = False, delimiter: str = '\t', quoting=...) -> None: ...
    def get_examples(self, filename, max_examples: int = 0):
        """

        """
