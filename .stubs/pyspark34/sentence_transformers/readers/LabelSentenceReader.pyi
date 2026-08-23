from . import InputExample as InputExample
from _typeshed import Incomplete

class LabelSentenceReader:
    """Reads in a file that has at least two columns: a label and a sentence.
    This reader can for example be used with the BatchHardTripletLoss.
    Maps labels automatically to integers"""
    folder: Incomplete
    label_map: Incomplete
    label_col_idx: Incomplete
    sentence_col_idx: Incomplete
    separator: Incomplete
    def __init__(self, folder, label_col_idx: int = 0, sentence_col_idx: int = 1, separator: str = '\t') -> None: ...
    def get_examples(self, filename, max_examples: int = 0): ...
