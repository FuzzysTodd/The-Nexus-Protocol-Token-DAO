import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithCrossAttentions as BaseModelOutputWithCrossAttentions, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_yoso import YosoConfig as YosoConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
YOSO_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_cuda_kernels(): ...
def to_contiguous(input_tensors): ...
def normalize(input_tensors): ...
def hashing(query, key, num_hash, hash_len): ...

class YosoCumulation(torch.autograd.Function):
    @staticmethod
    def forward(ctx, query_mask, key_mask, query, key, value, config): ...
    @staticmethod
    def backward(ctx, grad): ...

class YosoLSHCumulation(torch.autograd.Function):
    @staticmethod
    def forward(ctx, query_mask, key_mask, query, key, value, config): ...
    @staticmethod
    def backward(ctx, grad): ...

class YosoEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...

class YosoSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    use_expectation: Incomplete
    hash_code_len: Incomplete
    use_conv: Incomplete
    use_fast_hash: Incomplete
    num_hash: Incomplete
    lsh_backward: Incomplete
    lsh_config: Incomplete
    conv: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, layer): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False): ...

class YosoSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class YosoAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False): ...

class YosoIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class YosoOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class YosoLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    add_cross_attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output): ...

class YosoEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class YosoPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class YosoLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class YosoOnlyMLMHead(nn.Module):
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output: torch.Tensor) -> torch.Tensor: ...

class YosoPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = YosoConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

YOSO_START_DOCSTRING: str
YOSO_INPUTS_DOCSTRING: str

class YosoModel(YosoPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithCrossAttentions]: ...

class YosoForMaskedLM(YosoPreTrainedModel):
    yoso: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
        """

class YosoClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class YosoForSequenceClassification(YosoPreTrainedModel):
    num_labels: Incomplete
    yoso: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class YosoForMultipleChoice(YosoPreTrainedModel):
    yoso: Incomplete
    pre_classifier: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MultipleChoiceModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class YosoForTokenClassification(YosoPreTrainedModel):
    num_labels: Incomplete
    yoso: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class YosoForQuestionAnswering(YosoPreTrainedModel):
    num_labels: Incomplete
    yoso: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
        """
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
