import numpy as np
import os
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers import AutoTokenizer as AutoTokenizer
from typing import Optional, Union

logger: Incomplete

def convert_tfrecord_to_np(block_records_path: str, num_block_records: int) -> np.ndarray: ...

class ScaNNSearcher:
    """Note that ScaNNSearcher cannot currently be used within the model. In future versions, it might however be included."""
    searcher: Incomplete
    def __init__(self, db, num_neighbors, dimensions_per_block: int = 2, num_leaves: int = 1000, num_leaves_to_search: int = 100, training_sample_size: int = 100000) -> None:
        """Build scann searcher."""
    def search_batched(self, question_projection): ...

class RealmRetriever:
    '''The retriever of REALM outputting the retrieved evidence block and whether the block has answers as well as answer
    positions."

        Parameters:
            block_records (`np.ndarray`):
                A numpy array which cantains evidence texts.
            tokenizer ([`RealmTokenizer`]):
                The tokenizer to encode retrieved texts.
    '''
    block_records: Incomplete
    tokenizer: Incomplete
    def __init__(self, block_records, tokenizer) -> None: ...
    def __call__(self, retrieved_block_ids, question_input_ids, answer_ids, max_length: Incomplete | None = None, return_tensors: str = 'pt'): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Optional[Union[str, os.PathLike]], *init_inputs, **kwargs): ...
    def save_pretrained(self, save_directory) -> None: ...
    def block_has_answer(self, concat_inputs, answer_ids):
        """check if retrieved_blocks has answers."""
