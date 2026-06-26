from . import SentenceEvaluator as SentenceEvaluator
from ..util import cos_sim as cos_sim, dot_score as dot_score
from _typeshed import Incomplete

logger: Incomplete

class RerankingEvaluator(SentenceEvaluator):
    """
    This class evaluates a SentenceTransformer model for the task of re-ranking.

    Given a query and a list of documents, it computes the score [query, doc_i] for all possible
    documents and sorts them in decreasing order. Then, MRR@10 and MAP is compute to measure the quality of the ranking.

    :param samples: Must be a list and each element is of the form: {'query': '', 'positive': [], 'negative': []}. Query is the search query,
     positive is a list of positive (relevant) documents, negative is a list of negative (irrelevant) documents.
    """
    samples: Incomplete
    name: Incomplete
    mrr_at_k: Incomplete
    similarity_fct: Incomplete
    batch_size: Incomplete
    show_progress_bar: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, samples, mrr_at_k: int = 10, name: str = '', write_csv: bool = True, similarity_fct=..., batch_size: int = 64, show_progress_bar: bool = False) -> None: ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
    def compute_metrices(self, model): ...
