from .. import InputExample as InputExample
from _typeshed import Incomplete
from sentence_transformers import SentenceTransformer as SentenceTransformer, util as util
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class ContrastiveTensionLoss(nn.Module):
    """
        This loss expects as input a batch consisting of multiple mini-batches of sentence pairs (a_1, p_1), (a_2, p_2)..., (a_{K+1}, p_{K+1})
        where p_1 = a_1 = a_2 = ... a_{K+1} and p_2, p_3, ..., p_{K+1} are expected to be different from p_1 (this is done via random sampling).
        The corresponding labels y_1, y_2, ..., y_{K+1} for each mini-batch are assigned as: y_i = 1 if i == 1 and y_i = 0 otherwise.
        In other words, K represent the number of negative pairs and the positive pair is actually made of two identical sentences. The data generation
        process has already been implemented in readers/ContrastiveTensionReader.py
        For tractable optimization, two independent encoders ('model1' and 'model2') are created for encoding a_i and p_i, respectively. For inference,
        only model2 are used, which gives better performance. The training objective is binary cross entropy.
        For more information, see: https://openreview.net/pdf?id=Ov_sMNau-PF

    """
    model2: Incomplete
    model1: Incomplete
    criterion: Incomplete
    def __init__(self, model: SentenceTransformer) -> None:
        """
        :param model: SentenceTransformer model
        """
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...

class ContrastiveTensionLossInBatchNegatives(nn.Module):
    model2: Incomplete
    model1: Incomplete
    similarity_fct: Incomplete
    cross_entropy_loss: Incomplete
    logit_scale: Incomplete
    def __init__(self, model: SentenceTransformer, scale: float = 20.0, similarity_fct=...) -> None:
        """
        :param model: SentenceTransformer model
        """
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...

class ContrastiveTensionDataLoader:
    sentences: Incomplete
    batch_size: Incomplete
    pos_neg_ratio: Incomplete
    collate_fn: Incomplete
    def __init__(self, sentences, batch_size, pos_neg_ratio: int = 8) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
