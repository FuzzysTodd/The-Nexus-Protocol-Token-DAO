from ...modeling_outputs import BaseModelOutputWithPooling as BaseModelOutputWithPooling, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import ModuleUtilsMixin as ModuleUtilsMixin
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from _typeshed import Incomplete
from torch import nn

logger: Incomplete

class ModalEmbeddings(nn.Module):
    """Generic Modal Embeddings which takes in an encoder, and a transformer embedding."""
    config: Incomplete
    encoder: Incomplete
    proj_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    word_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, encoder, embeddings) -> None: ...
    def forward(self, input_modal, start_token: Incomplete | None = None, end_token: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None): ...

MMBT_START_DOCSTRING: str
MMBT_INPUTS_DOCSTRING: str

class MMBTModel(nn.Module, ModuleUtilsMixin):
    config: Incomplete
    transformer: Incomplete
    modal_encoder: Incomplete
    def __init__(self, config, transformer, encoder) -> None: ...
    def forward(self, input_modal, input_ids: Incomplete | None = None, modal_start_tokens: Incomplete | None = None, modal_end_tokens: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, modal_token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, modal_position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None):
        '''
        Returns:

        Examples:

        ```python
        # For example purposes. Not runnable.
        transformer = BertModel.from_pretrained("bert-base-uncased")
        encoder = ImageEncoder(args)
        mmbt = MMBTModel(config, transformer, encoder)
        ```'''
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...

class MMBTForClassification(nn.Module):
    '''
    **labels**: (*optional*) `torch.LongTensor` of shape `(batch_size,)`:
        Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
        config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
        `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

    Returns: *Tuple* comprising various elements depending on the configuration (config) and inputs: **loss**:
    (*optional*, returned when `labels` is provided) `torch.FloatTensor` of shape `(1,)`: Classification (or
    regression if config.num_labels==1) loss. **logits**:
        `torch.FloatTensor` of shape `(batch_size, config.num_labels)` Classification (or regression if
        config.num_labels==1) scores (before SoftMax).
    **hidden_states**: (*optional*, returned when `output_hidden_states=True`) list of `torch.FloatTensor` (one for
    the output of each layer + the output of the embeddings) of shape `(batch_size, sequence_length, hidden_size)`:
    Hidden-states of the model at the output of each layer plus the initial embedding outputs. **attentions**:
    (*optional*, returned when `output_attentions=True`) list of `torch.FloatTensor` (one for each layer) of shape
    `(batch_size, num_heads, sequence_length, sequence_length)`: Attentions weights after the attention softmax, used
    to compute the weighted average in the self-attention heads.

    Examples:

    ```python
    # For example purposes. Not runnable.
    transformer = BertModel.from_pretrained("bert-base-uncased")
    encoder = ImageEncoder(args)
    model = MMBTForClassification(config, transformer, encoder)
    outputs = model(input_modal, input_ids, labels=labels)
    loss, logits = outputs[:2]
    ```'''
    num_labels: Incomplete
    mmbt: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, transformer, encoder) -> None: ...
    def forward(self, input_modal, input_ids: Incomplete | None = None, modal_start_tokens: Incomplete | None = None, modal_end_tokens: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, modal_token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, modal_position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, labels: Incomplete | None = None, return_dict: Incomplete | None = None): ...
