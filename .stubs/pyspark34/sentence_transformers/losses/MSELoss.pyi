from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

class MSELoss(nn.Module):
    """
    Computes the MSE loss between the computed sentence embedding and a target sentence embedding. This loss
    is used when extending sentence embeddings to new languages as described in our publication
    Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation: https://arxiv.org/abs/2004.09813

    For an example, see the documentation on extending language models to new languages.
    """
    model: Incomplete
    loss_fct: Incomplete
    def __init__(self, model) -> None: ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
