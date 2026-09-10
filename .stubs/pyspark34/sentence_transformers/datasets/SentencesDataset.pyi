from .. import SentenceTransformer as SentenceTransformer
from ..readers.InputExample import InputExample as InputExample
from _typeshed import Incomplete
from torch.utils.data import Dataset
from typing import List

class SentencesDataset(Dataset):
    """
    DEPRECATED: This class is no longer used. Instead of wrapping your List of InputExamples in a SentencesDataset
    and then passing it to the DataLoader, you can pass the list of InputExamples directly to the dataset loader.
    """
    examples: Incomplete
    def __init__(self, examples: List[InputExample], model: SentenceTransformer) -> None: ...
    def __getitem__(self, item): ...
    def __len__(self) -> int: ...
