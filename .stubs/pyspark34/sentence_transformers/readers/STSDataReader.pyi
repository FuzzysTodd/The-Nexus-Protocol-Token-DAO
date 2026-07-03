from . import InputExample as InputExample
from _typeshed import Incomplete

class STSDataReader:
    """
    Reads in the STS dataset. Each line contains two sentences (s1_col_idx, s2_col_idx) and one label (score_col_idx)

    Default values expects a tab seperated file with the first & second column the sentence pair and third column the score (0...1). Default config normalizes scores from 0...5 to 0...1
    """
    dataset_folder: Incomplete
    score_col_idx: Incomplete
    s1_col_idx: Incomplete
    s2_col_idx: Incomplete
    delimiter: Incomplete
    quoting: Incomplete
    normalize_scores: Incomplete
    min_score: Incomplete
    max_score: Incomplete
    def __init__(self, dataset_folder, s1_col_idx: int = 0, s2_col_idx: int = 1, score_col_idx: int = 2, delimiter: str = '\t', quoting=..., normalize_scores: bool = True, min_score: int = 0, max_score: int = 5) -> None: ...
    def get_examples(self, filename, max_examples: int = 0):
        """
        filename specified which data split to use (train.csv, dev.csv, test.csv).
        """

class STSBenchmarkDataReader(STSDataReader):
    """
    Reader especially for the STS benchmark dataset. There, the sentences are in column 5 and 6, the score is in column 4.
    Scores are normalized from 0...5 to 0...1
    """
    def __init__(self, dataset_folder, s1_col_idx: int = 5, s2_col_idx: int = 6, score_col_idx: int = 4, delimiter: str = '\t', quoting=..., normalize_scores: bool = True, min_score: int = 0, max_score: int = 5) -> None: ...
