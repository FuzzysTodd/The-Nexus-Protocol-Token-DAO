from .BatchHardTripletLoss import BatchHardTripletLoss as BatchHardTripletLoss, BatchHardTripletLossDistanceFunction as BatchHardTripletLossDistanceFunction
from _typeshed import Incomplete
from sentence_transformers.SentenceTransformer import SentenceTransformer as SentenceTransformer
from torch import Tensor as Tensor, nn as nn
from typing import Dict, Iterable

class BatchHardSoftMarginTripletLoss(BatchHardTripletLoss):
    """
    BatchHardSoftMarginTripletLoss takes a batch with (label, sentence) pairs and computes the loss for all possible, valid
    triplets, i.e., anchor and positive must have the same label, anchor and negative a different label. The labels
    must be integers, with same label indicating sentences from the same class. You train dataset
    must contain at least 2 examples per label class. The margin is computed automatically.

    Source: https://github.com/NegatioN/OnlineMiningTripletLoss/blob/master/online_triplet_loss/losses.py
    Paper: In Defense of the Triplet Loss for Person Re-Identification, https://arxiv.org/abs/1703.07737
    Blog post: https://omoindrot.github.io/triplet-loss

    :param model: SentenceTransformer model
    :param distance_metric: Function that returns a distance between two emeddings. The class SiameseDistanceMetric contains pre-defined metrices that can be used


    Example::

       from sentence_transformers import SentenceTransformer,  SentencesDataset, LoggingHandler, losses
       from sentence_transformers.readers import InputExample

       model = SentenceTransformer('distilbert-base-nli-mean-tokens')
       train_examples = [InputExample(texts=['Sentence from class 0'], label=0), InputExample(texts=['Another sentence from class 0'], label=0),
           InputExample(texts=['Sentence from class 1'], label=1), InputExample(texts=['Sentence from class 2'], label=2)]
       train_dataset = SentencesDataset(train_examples, model)
       train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=train_batch_size)
       train_loss = losses.BatchHardSoftMarginTripletLoss(model=model)
    """
    sentence_embedder: Incomplete
    distance_metric: Incomplete
    def __init__(self, model: SentenceTransformer, distance_metric=...) -> None: ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
    def batch_hard_triplet_soft_margin_loss(self, labels: Tensor, embeddings: Tensor) -> Tensor:
        """Build the triplet loss over a batch of embeddings.
        For each anchor, we get the hardest positive and hardest negative to form a triplet.
        Args:
            labels: labels of the batch, of size (batch_size,)
            embeddings: tensor of shape (batch_size, embed_dim)
            squared: Boolean. If true, output is the pairwise squared euclidean distance matrix.
                     If false, output is the pairwise euclidean distance matrix.
        Returns:
            Label_Sentence_Triplet: scalar tensor containing the triplet loss
        """
