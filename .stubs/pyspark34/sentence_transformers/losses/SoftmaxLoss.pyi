from ..SentenceTransformer import SentenceTransformer as SentenceTransformer
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

logger: Incomplete

class SoftmaxLoss(nn.Module):
    """
    This loss was used in our SBERT publication (https://arxiv.org/abs/1908.10084) to train the SentenceTransformer
    model on NLI data. It adds a softmax classifier on top of the output of two transformer networks.

    :param model: SentenceTransformer model
    :param sentence_embedding_dimension: Dimension of your sentence embeddings
    :param num_labels: Number of different labels
    :param concatenation_sent_rep: Concatenate vectors u,v for the softmax classifier?
    :param concatenation_sent_difference: Add abs(u-v) for the softmax classifier?
    :param concatenation_sent_multiplication: Add u*v for the softmax classifier?

    Example::

        from sentence_transformers import SentenceTransformer, SentencesDataset, losses
        from sentence_transformers.readers import InputExample

        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        train_examples = [InputExample(texts=['First pair, sent A', 'First pair, sent B'], label=0),
            InputExample(texts=['Second Pair, sent A', 'Second Pair, sent B'], label=3)]
        train_dataset = SentencesDataset(train_examples, model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=train_batch_size)
        train_loss = losses.SoftmaxLoss(model=model, sentence_embedding_dimension=model.get_sentence_embedding_dimension(), num_labels=train_num_labels)
    """
    model: Incomplete
    num_labels: Incomplete
    concatenation_sent_rep: Incomplete
    concatenation_sent_difference: Incomplete
    concatenation_sent_multiplication: Incomplete
    classifier: Incomplete
    def __init__(self, model: SentenceTransformer, sentence_embedding_dimension: int, num_labels: int, concatenation_sent_rep: bool = True, concatenation_sent_difference: bool = True, concatenation_sent_multiplication: bool = False) -> None: ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
