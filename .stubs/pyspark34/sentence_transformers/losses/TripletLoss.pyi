from ..SentenceTransformer import SentenceTransformer as SentenceTransformer
from _typeshed import Incomplete
from enum import Enum
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class TripletDistanceMetric(Enum):
    """
    The metric for the triplet loss
    """
    COSINE: Incomplete
    EUCLIDEAN: Incomplete
    MANHATTAN: Incomplete

class TripletLoss(nn.Module):
    """
    This class implements triplet loss. Given a triplet of (anchor, positive, negative),
    the loss minimizes the distance between anchor and positive while it maximizes the distance
    between anchor and negative. It compute the following loss function:

    loss = max(||anchor - positive|| - ||anchor - negative|| + margin, 0).

    Margin is an important hyperparameter and needs to be tuned respectively.

    For further details, see: https://en.wikipedia.org/wiki/Triplet_loss

    :param model: SentenceTransformerModel
    :param distance_metric: Function to compute distance between two embeddings. The class TripletDistanceMetric contains common distance metrices that can be used.
    :param triplet_margin: The negative should be at least this much further away from the anchor than the positive.

    Example::

        from sentence_transformers import SentenceTransformer,  SentencesDataset, LoggingHandler, losses
        from sentence_transformers.readers import InputExample

        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        train_examples = [InputExample(texts=['Anchor 1', 'Positive 1', 'Negative 1']),
            InputExample(texts=['Anchor 2', 'Positive 2', 'Negative 2'])]
        train_dataset = SentencesDataset(train_examples, model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=train_batch_size)
        train_loss = losses.TripletLoss(model=model)
    """
    model: Incomplete
    distance_metric: Incomplete
    triplet_margin: Incomplete
    def __init__(self, model: SentenceTransformer, distance_metric=..., triplet_margin: float = 5) -> None: ...
    def get_config_dict(self): ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
