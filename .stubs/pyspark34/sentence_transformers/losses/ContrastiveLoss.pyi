from _typeshed import Incomplete
from enum import Enum
from sentence_transformers.SentenceTransformer import SentenceTransformer as SentenceTransformer
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class SiameseDistanceMetric(Enum):
    """
    The metric for the contrastive loss
    """
    EUCLIDEAN: Incomplete
    MANHATTAN: Incomplete
    COSINE_DISTANCE: Incomplete

class ContrastiveLoss(nn.Module):
    """
    Contrastive loss. Expects as input two texts and a label of either 0 or 1. If the label == 1, then the distance between the
    two embeddings is reduced. If the label == 0, then the distance between the embeddings is increased.

    Further information: http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf

    :param model: SentenceTransformer model
    :param distance_metric: Function that returns a distance between two emeddings. The class SiameseDistanceMetric contains pre-defined metrices that can be used
    :param margin: Negative samples (label == 0) should have a distance of at least the margin value.
    :param size_average: Average by the size of the mini-batch.

    Example::

        from sentence_transformers import SentenceTransformer,  SentencesDataset, LoggingHandler, losses
        from sentence_transformers.readers import InputExample

        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        train_examples = [InputExample(texts=['This is a positive pair', 'Where the distance will be minimized'], label=1),
            InputExample(texts=['This is a negative pair', 'Their distance will be increased'], label=0)]
        train_dataset = SentencesDataset(train_examples, model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=train_batch_size)
        train_loss = losses.ContrastiveLoss(model=model)

    """
    distance_metric: Incomplete
    margin: Incomplete
    model: Incomplete
    size_average: Incomplete
    def __init__(self, model: SentenceTransformer, distance_metric=..., margin: float = 0.5, size_average: bool = True) -> None: ...
    def get_config_dict(self): ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
