from . import SentenceEvaluator as SentenceEvaluator
from _typeshed import Incomplete
from sentence_transformers.util import paraphrase_mining as paraphrase_mining
from typing import Dict, List, Tuple

logger: Incomplete

class ParaphraseMiningEvaluator(SentenceEvaluator):
    """
    Given a large set of sentences, this evaluator performs paraphrase (duplicate) mining and
    identifies the pairs with the highest similarity. It compare the extracted paraphrase pairs
     with a set of gold labels and computes the F1 score.
    """
    sentences: Incomplete
    ids: Incomplete
    name: Incomplete
    show_progress_bar: Incomplete
    batch_size: Incomplete
    query_chunk_size: Incomplete
    corpus_chunk_size: Incomplete
    max_pairs: Incomplete
    top_k: Incomplete
    duplicates: Incomplete
    total_num_duplicates: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, sentences_map: Dict[str, str], duplicates_list: List[Tuple[str, str]] = None, duplicates_dict: Dict[str, Dict[str, bool]] = None, add_transitive_closure: bool = False, query_chunk_size: int = 5000, corpus_chunk_size: int = 100000, max_pairs: int = 500000, top_k: int = 100, show_progress_bar: bool = False, batch_size: int = 16, name: str = '', write_csv: bool = True) -> None:
        """

        :param sentences_map: A dictionary that maps sentence-ids to sentences, i.e. sentences_map[id] => sentence.
        :param duplicates_list: Duplicates_list is a list with id pairs [(id1, id2), (id1, id5)] that identifies the duplicates / paraphrases in the sentences_map
        :param duplicates_dict: A default dictionary mapping [id1][id2] to true if id1 and id2 are duplicates. Must be symmetric, i.e., if [id1][id2] => True, then [id2][id1] => True.
        :param add_transitive_closure: If true, it adds a transitive closure, i.e. if dup[a][b] and dup[b][c], then dup[a][c]
        :param query_chunk_size: To identify the paraphrases, the cosine-similarity between all sentence-pairs will be computed. As this might require a lot of memory, we perform a batched computation.  #query_batch_size sentences will be compared against up to #corpus_batch_size sentences. In the default setting, 5000 sentences will be grouped together and compared up-to against 100k other sentences.
        :param corpus_chunk_size: The corpus will be batched, to reduce the memory requirement
        :param max_pairs: We will only extract up to #max_pairs potential paraphrase candidates.
        :param top_k: For each query, we extract the top_k most similar pairs and add it to a sorted list. I.e., for one sentence we cannot find more than top_k paraphrases
        :param show_progress_bar: Output a progress bar
        :param batch_size: Batch size for computing sentence embeddings
        :param name: Name of the experiment
        :param write_csv: Write results to CSV file
        """
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
    @staticmethod
    def add_transitive_closure(graph): ...
