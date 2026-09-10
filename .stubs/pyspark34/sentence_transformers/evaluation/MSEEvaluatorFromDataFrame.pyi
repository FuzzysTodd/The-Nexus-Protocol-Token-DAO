from _typeshed import Incomplete
from sentence_transformers import SentenceTransformer as SentenceTransformer
from sentence_transformers.evaluation import SentenceEvaluator as SentenceEvaluator
from sentence_transformers.util import batch_to_device as batch_to_device
from typing import Dict, List, Tuple

logger: Incomplete

class MSEEvaluatorFromDataFrame(SentenceEvaluator):
    """
    Computes the mean squared error (x100) between the computed sentence embedding
    and some target sentence embedding.
    :param dataframe:
        It must have the following format. Rows contains different, parallel sentences. Columns are the respective language codes
        [{'en': 'My sentence', 'es': 'Sentence in Spanisch', 'fr': 'Sentence in French'...},
         {'en': 'My second sentence', ....]
    :param combinations:
        Must be of the format [('en', 'es'), ('en', 'fr'), ...]
        First entry in a tuple is the source language. The sentence in the respective language will be fetched from the dataframe and passed to the teacher model.
        Second entry in a tuple the the target language. Sentence will be fetched from the dataframe and passed to the student model
    """
    combinations: Incomplete
    name: Incomplete
    batch_size: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    data: Incomplete
    teacher_embeddings: Incomplete
    def __init__(self, dataframe: List[Dict[str, str]], teacher_model: SentenceTransformer, combinations: List[Tuple[str, str]], batch_size: int = 8, name: str = '', write_csv: bool = True) -> None: ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1): ...
