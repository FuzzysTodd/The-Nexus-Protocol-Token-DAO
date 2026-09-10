from .ContrastiveLoss import SiameseDistanceMetric as SiameseDistanceMetric
from _typeshed import Incomplete
from sentence_transformers.SentenceTransformer import SentenceTransformer as SentenceTransformer
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class OnlineContrastiveLoss(nn.Module):
    """
    Online Contrastive loss. Similar to ConstrativeLoss, but it selects hard positive (positives that are far apart)
     and hard negative pairs (negatives that are close) and computes the loss only for these pairs. Often yields
     better performances than  ConstrativeLoss.

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
        train_loss = losses.OnlineContrastiveLoss(model=model)
    """
    model: Incomplete
    margin: Incomplete
    distance_metric: Incomplete
    def __init__(self, model: SentenceTransformer, distance_metric=..., margin: float = 0.5) -> None: ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor, size_average: bool = False): ...
