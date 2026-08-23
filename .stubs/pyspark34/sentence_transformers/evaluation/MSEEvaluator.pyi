from _typeshed import Incomplete
from sentence_transformers.evaluation import SentenceEvaluator as SentenceEvaluator
from typing import List

logger: Incomplete

class MSEEvaluator(SentenceEvaluator):
    """
    Computes the mean squared error (x100) between the computed sentence embedding
    and some target sentence embedding.

    The MSE is computed between ||teacher.encode(source_sentences) - student.encode(target_sentences)||.

    For multilingual knowledge distillation (https://arxiv.org/abs/2004.09813), source_sentences are in English
    and target_sentences are in a different language like German, Chinese, Spanish...

    :param source_sentences: Source sentences are embedded with the teacher model
    :param target_sentences: Target sentences are ambedding with the student model.
    :param show_progress_bar: Show progress bar when computing embeddings
    :param batch_size: Batch size to compute sentence embeddings
    :param name: Name of the evaluator
    :param write_csv: Write results to CSV file
    """
    source_embeddings: Incomplete
    target_sentences: Incomplete
    show_progress_bar: Incomplete
    batch_size: Incomplete
    name: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, source_sentences: List[str], target_sentences: List[str], teacher_model: Incomplete | None = None, show_progress_bar: bool = False, batch_size: int = 32, name: str = '', write_csv: bool = True) -> None: ...
    def __call__(self, model, output_path, epoch: int = -1, steps: int = -1): ...
