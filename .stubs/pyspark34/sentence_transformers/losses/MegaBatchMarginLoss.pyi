from .. import util as util
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class MegaBatchMarginLoss(nn.Module):
    """
    Loss function inspired from ParaNMT paper:
    https://www.aclweb.org/anthology/P18-1042/

    Given a large batch (like 500 or more examples) of (anchor_i, positive_i) pairs,
    find for each pair in the batch the hardest negative, i.e. find j != i such that cos_sim(anchor_i, positive_j)
    is maximal. Then create from this a triplet (anchor_i, positive_i, positive_j) where positive_j
    serves as the negative for this triplet.

    Train than as with the triplet loss
    """
    model: Incomplete
    positive_margin: Incomplete
    negative_margin: Incomplete
    mini_batch_size: Incomplete
    forward: Incomplete
    def __init__(self, model, positive_margin: float = 0.8, negative_margin: float = 0.3, use_mini_batched_version: bool = True, mini_batch_size: bool = 50) -> None:
        """
        :param model: SentenceTransformerModel
        :param positive_margin: Positive margin, cos(anchor, positive) should be > positive_margin
        :param negative_margin: Negative margin, cos(anchor, negative) should be < negative_margin
        :param use_mini_batched_version: As large batch sizes require a lot of memory, we can use a mini-batched version. We break down the large batch with 500 examples to smaller batches with fewer examples.
        :param mini_batch_size: Size for the mini-batches. Should be a devisor for the batch size in your data loader.
        """
    def forward_mini_batched(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
    def forward_non_mini_batched(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
