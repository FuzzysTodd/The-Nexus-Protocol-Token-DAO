from openai.datalib.numpy_helper import numpy as np
from typing import List

def get_embedding(text: str, engine: str = 'text-similarity-davinci-001', **kwargs) -> List[float]: ...
async def aget_embedding(text: str, engine: str = 'text-similarity-davinci-001', **kwargs) -> List[float]: ...
def get_embeddings(list_of_text: List[str], engine: str = 'text-similarity-babbage-001', **kwargs) -> List[List[float]]: ...
async def aget_embeddings(list_of_text: List[str], engine: str = 'text-similarity-babbage-001', **kwargs) -> List[List[float]]: ...
def cosine_similarity(a, b): ...
def plot_multiclass_precision_recall(y_score, y_true_untransformed, class_list, classifier_name) -> None:
    """
    Precision-Recall plotting for a multiclass problem. It plots average precision-recall, per class precision recall and reference f1 contours.

    Code slightly modified, but heavily based on https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
    """
def distances_from_embeddings(query_embedding: List[float], embeddings: List[List[float]], distance_metric: str = 'cosine') -> List[List]:
    """Return the distances between a query embedding and a list of embeddings."""
def indices_of_nearest_neighbors_from_distances(distances) -> np.ndarray:
    """Return a list of indices of nearest neighbors from a list of distances."""
def pca_components_from_embeddings(embeddings: List[List[float]], n_components: int = 2) -> np.ndarray:
    """Return the PCA components of a list of embeddings."""
def tsne_components_from_embeddings(embeddings: List[List[float]], n_components: int = 2, **kwargs) -> np.ndarray:
    """Returns t-SNE components of a list of embeddings."""
def chart_from_components(components: np.ndarray, labels: List[str] | None = None, strings: List[str] | None = None, x_title: str = 'Component 0', y_title: str = 'Component 1', mark_size: int = 5, **kwargs):
    """Return an interactive 2D chart of embedding components."""
def chart_from_components_3D(components: np.ndarray, labels: List[str] | None = None, strings: List[str] | None = None, x_title: str = 'Component 0', y_title: str = 'Component 1', z_title: str = 'Compontent 2', mark_size: int = 5, **kwargs):
    """Return an interactive 3D chart of embedding components."""
