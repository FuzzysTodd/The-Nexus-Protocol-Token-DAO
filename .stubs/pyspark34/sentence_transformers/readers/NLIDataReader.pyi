from . import InputExample as InputExample
from _typeshed import Incomplete

class NLIDataReader:
    """
    Reads in the Stanford NLI dataset and the MultiGenre NLI dataset
    """
    dataset_folder: Incomplete
    def __init__(self, dataset_folder) -> None: ...
    def get_examples(self, filename, max_examples: int = 0):
        """
        data_splits specified which data split to use (train, dev, test).
        Expects that self.dataset_folder contains the files s1.$data_split.gz,  s2.$data_split.gz,
        labels.$data_split.gz, e.g., for the train split, s1.train.gz, s2.train.gz, labels.train.gz
        """
    @staticmethod
    def get_labels(): ...
    def get_num_labels(self): ...
    def map_label(self, label): ...
