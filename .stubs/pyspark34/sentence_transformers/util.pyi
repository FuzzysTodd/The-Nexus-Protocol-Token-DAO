from _typeshed import Incomplete
from pathlib import Path
from torch import Tensor, device as device
from typing import Callable, Dict, List

logger: Incomplete

def pytorch_cos_sim(a: Tensor, b: Tensor):
    """
    Computes the cosine similarity cos_sim(a[i], b[j]) for all i and j.
    :return: Matrix with res[i][j]  = cos_sim(a[i], b[j])
    """
def cos_sim(a: Tensor, b: Tensor):
    """
    Computes the cosine similarity cos_sim(a[i], b[j]) for all i and j.
    :return: Matrix with res[i][j]  = cos_sim(a[i], b[j])
    """
def dot_score(a: Tensor, b: Tensor):
    """
    Computes the dot-product dot_prod(a[i], b[j]) for all i and j.
    :return: Matrix with res[i][j]  = dot_prod(a[i], b[j])
    """
def normalize_embeddings(embeddings: Tensor):
    """
    Normalizes the embeddings matrix, so that each sentence embedding has unit length
    """
def paraphrase_mining(model, sentences: List[str], show_progress_bar: bool = False, batch_size: int = 32, *args, **kwargs):
    """
    Given a list of sentences / texts, this function performs paraphrase mining. It compares all sentences against all
    other sentences and returns a list with the pairs that have the highest cosine similarity score.

    :param model: SentenceTransformer model for embedding computation
    :param sentences: A list of strings (texts or sentences)
    :param show_progress_bar: Plotting of a progress bar
    :param batch_size: Number of texts that are encoded simultaneously by the model
    :param query_chunk_size: Search for most similar pairs for #query_chunk_size at the same time. Decrease, to lower memory footprint (increases run-time).
    :param corpus_chunk_size: Compare a sentence simultaneously against #corpus_chunk_size other sentences. Decrease, to lower memory footprint (increases run-time).
    :param max_pairs: Maximal number of text pairs returned.
    :param top_k: For each sentence, we retrieve up to top_k other sentences
    :param score_function: Funtion for computing scores. By default, cosine similarity.
    :return: Returns a list of triplets with the format [score, id1, id2]
    """
def paraphrase_mining_embeddings(embeddings: Tensor, query_chunk_size: int = 5000, corpus_chunk_size: int = 100000, max_pairs: int = 500000, top_k: int = 100, score_function: Callable[[Tensor, Tensor], Tensor] = ...):
    """
    Given a list of sentences / texts, this function performs paraphrase mining. It compares all sentences against all
    other sentences and returns a list with the pairs that have the highest cosine similarity score.

    :param embeddings: A tensor with the embeddings
    :param query_chunk_size: Search for most similar pairs for #query_chunk_size at the same time. Decrease, to lower memory footprint (increases run-time).
    :param corpus_chunk_size: Compare a sentence simultaneously against #corpus_chunk_size other sentences. Decrease, to lower memory footprint (increases run-time).
    :param max_pairs: Maximal number of text pairs returned.
    :param top_k: For each sentence, we retrieve up to top_k other sentences
    :param score_function: Funtion for computing scores. By default, cosine similarity.
    :return: Returns a list of triplets with the format [score, id1, id2]
    """
def information_retrieval(*args, **kwargs):
    """This function is decprecated. Use semantic_search insted"""
def semantic_search(query_embeddings: Tensor, corpus_embeddings: Tensor, query_chunk_size: int = 100, corpus_chunk_size: int = 500000, top_k: int = 10, score_function: Callable[[Tensor, Tensor], Tensor] = ...):
    """
    This function performs a cosine similarity search between a list of query embeddings  and a list of corpus embeddings.
    It can be used for Information Retrieval / Semantic Search for corpora up to about 1 Million entries.

    :param query_embeddings: A 2 dimensional tensor with the query embeddings.
    :param corpus_embeddings: A 2 dimensional tensor with the corpus embeddings.
    :param query_chunk_size: Process 100 queries simultaneously. Increasing that value increases the speed, but requires more memory.
    :param corpus_chunk_size: Scans the corpus 100k entries at a time. Increasing that value increases the speed, but requires more memory.
    :param top_k: Retrieve top k matching entries.
    :param score_function: Funtion for computing scores. By default, cosine similarity.
    :return: Returns a sorted list with decreasing cosine similarity scores. Entries are dictionaries with the keys 'corpus_id' and 'score'
    """
def http_get(url, path) -> None:
    """
    Downloads a URL to a given path on disc
    """
def batch_to_device(batch, target_device: device):
    """
    send a pytorch batch to a device (CPU/GPU)
    """
def fullname(o):
    """
  Gives a full name (package_name.class_name) for a class / object in Python. Will
  be used to load the correct classes from JSON files
  """
def import_from_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
def community_detection(embeddings, threshold: float = 0.75, min_community_size: int = 10, init_max_size: int = 1000):
    """
    Function for Fast Community Detection

    Finds in the embeddings all communities, i.e. embeddings that are close (closer than threshold).

    Returns only communities that are larger than min_community_size. The communities are returned
    in decreasing order. The first element in each list is the central point in the community.
    """
def snapshot_download(repo_id: str, revision: str | None = None, cache_dir: str | Path | None = None, library_name: str | None = None, library_version: str | None = None, user_agent: Dict | str | None = None, ignore_files: List[str] | None = None) -> str:
    """
    Method derived from huggingface_hub.
    Adds a new parameters 'ignore_files', which allows to ignore certain files / file-patterns
    """
