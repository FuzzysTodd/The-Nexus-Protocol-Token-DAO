from ..readers.InputExample import InputExample as InputExample
from _typeshed import Incomplete
from torch.utils.data import Dataset
from typing import List

class DenoisingAutoEncoderDataset(Dataset):
    """
    The DenoisingAutoEncoderDataset returns InputExamples in the format: texts=[noise_fn(sentence), sentence]
    It is used in combination with the DenoisingAutoEncoderLoss: Here, a decoder tries to re-construct the
    sentence without noise.

    :param sentences: A list of sentences
    :param noise_fn: A noise function: Given a string, it returns a string with noise, e.g. deleted words
    """
    sentences: Incomplete
    noise_fn: Incomplete
    def __init__(self, sentences: List[str], noise_fn=...) -> None: ...
    def __getitem__(self, item): ...
    def __len__(self) -> int: ...
    @staticmethod
    def delete(text, del_ratio: float = 0.6): ...
