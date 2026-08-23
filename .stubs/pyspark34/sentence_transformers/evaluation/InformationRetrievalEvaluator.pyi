from . import SentenceEvaluator as SentenceEvaluator
from ..util import cos_sim as cos_sim, dot_score as dot_score
from _typeshed import Incomplete
from torch import Tensor as Tensor
from tqdm import tqdm as tqdm
from typing import Callable, Dict, List, Set

logger: Incomplete

class InformationRetrievalEvaluator(SentenceEvaluator):
    """
    This class evaluates an Information Retrieval (IR) setting.

    Given a set of queries and a large corpus set. It will retrieve for each query the top-k most similar document. It measures
    Mean Reciprocal Rank (MRR), Recall@k, and Normalized Discounted Cumulative Gain (NDCG)
    """
    queries_ids: Incomplete
    queries: Incomplete
    corpus_ids: Incomplete
    corpus: Incomplete
    relevant_docs: Incomplete
    corpus_chunk_size: Incomplete
    mrr_at_k: Incomplete
    ndcg_at_k: Incomplete
    accuracy_at_k: Incomplete
    precision_recall_at_k: Incomplete
    map_at_k: Incomplete
    show_progress_bar: Incomplete
    batch_size: Incomplete
    name: Incomplete
    write_csv: Incomplete
    score_functions: Incomplete
    score_function_names: Incomplete
    main_score_function: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    def __init__(self, queries: Dict[str, str], corpus: Dict[str, str], relevant_docs: Dict[str, Set[str]], corpus_chunk_size: int = 50000, mrr_at_k: List[int] = [10], ndcg_at_k: List[int] = [10], accuracy_at_k: List[int] = [1, 3, 5, 10], precision_recall_at_k: List[int] = [1, 3, 5, 10], map_at_k: List[int] = [100], show_progress_bar: bool = False, batch_size: int = 32, name: str = '', write_csv: bool = True, score_functions: List[Callable[[Tensor, Tensor], Tensor]] = ..., main_score_function: str = None) -> None: ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1, *args, **kwargs) -> float: ...
    def compute_metrices(self, model, corpus_model: Incomplete | None = None, corpus_embeddings: Tensor = None) -> Dict[str, float]: ...
    def compute_metrics(self, queries_result_list: List[object]): ...
    def output_scores(self, scores) -> None: ...
    @staticmethod
    def compute_dcg_at_k(relevances, k): ...
