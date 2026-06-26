import torch
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, logging as logging
from ..bert.modeling_bert import BertModel as BertModel
from .configuration_retribert import RetriBertConfig as RetriBertConfig
from _typeshed import Incomplete
from typing import Optional

logger: Incomplete
RETRIBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class RetriBertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RetriBertConfig
    load_tf_weights: Incomplete
    base_model_prefix: str

RETRIBERT_START_DOCSTRING: str

class RetriBertModel(RetriBertPreTrainedModel):
    projection_dim: Incomplete
    bert_query: Incomplete
    bert_doc: Incomplete
    dropout: Incomplete
    project_query: Incomplete
    project_doc: Incomplete
    ce_loss: Incomplete
    def __init__(self, config: RetriBertConfig) -> None: ...
    def embed_sentences_checkpointed(self, input_ids, attention_mask, sent_encoder, checkpoint_batch_size: int = -1): ...
    def embed_questions(self, input_ids, attention_mask: Incomplete | None = None, checkpoint_batch_size: int = -1): ...
    def embed_answers(self, input_ids, attention_mask: Incomplete | None = None, checkpoint_batch_size: int = -1): ...
    def forward(self, input_ids_query: torch.LongTensor, attention_mask_query: Optional[torch.FloatTensor], input_ids_doc: torch.LongTensor, attention_mask_doc: Optional[torch.FloatTensor], checkpoint_batch_size: int = -1) -> torch.FloatTensor:
        """
        Args:
            input_ids_query (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary for the queries in a batch.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask_query (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            input_ids_doc (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary for the documents in a batch.
            attention_mask_doc (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on documents padding token indices.
            checkpoint_batch_size (`int`, *optional*, defaults to `-1`):
                If greater than 0, uses gradient checkpointing to only compute sequence representation on
                `checkpoint_batch_size` examples at a time on the GPU. All query representations are still compared to
                all document representations in the batch.

        Return:
            `torch.FloatTensor``: The bidirectional cross-entropy loss obtained while trying to match each query to its
            corresponding document and each document to its corresponding query in the batch
        """
