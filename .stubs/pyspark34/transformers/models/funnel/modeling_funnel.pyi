import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_funnel import FunnelConfig as FunnelConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
FUNNEL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
INF: float

def load_tf_weights_in_funnel(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

class FunnelEmbeddings(nn.Module):
    word_embeddings: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None) -> torch.Tensor: ...

class FunnelAttentionStructure(nn.Module):
    """
    Contains helpers for `FunnelRelMultiheadAttention `.
    """
    cls_token_type_id: int
    config: Incomplete
    sin_dropout: Incomplete
    cos_dropout: Incomplete
    pooling_mult: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    seq_len: Incomplete
    def init_attention_inputs(self, inputs_embeds: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor]:
        """Returns the attention inputs associated to the inputs of the model."""
    def token_type_ids_to_mat(self, token_type_ids: torch.Tensor) -> torch.Tensor:
        """Convert `token_type_ids` to `token_type_mat`."""
    def get_position_embeds(self, seq_len: int, dtype: torch.dtype, device: torch.device) -> Union[Tuple[torch.Tensor], List[List[torch.Tensor]]]:
        """
        Create and cache inputs related to relative position encoding. Those are very different depending on whether we
        are using the factorized or the relative shift attention:

        For the factorized attention, it returns the matrices (phi, pi, psi, omega) used in the paper, appendix A.2.2,
        final formula.

        For the relative shift attention, it returns all possible vectors R used in the paper, appendix A.2.1, final
        formula.

        Paper link: https://arxiv.org/abs/2006.03236
        """
    def stride_pool_pos(self, pos_id: torch.Tensor, block_index: int):
        """
        Pool `pos_id` while keeping the cls token separate (if `config.separate_cls=True`).
        """
    def relative_pos(self, pos: torch.Tensor, stride: int, pooled_pos: Incomplete | None = None, shift: int = 1) -> torch.Tensor:
        """
        Build the relative positional vector between `pos` and `pooled_pos`.
        """
    def stride_pool(self, tensor: Union[torch.Tensor, Tuple[torch.Tensor], List[torch.Tensor]], axis: Union[int, Tuple[int], List[int]]) -> torch.Tensor:
        """
        Perform pooling by stride slicing the tensor along the given axis.
        """
    def pool_tensor(self, tensor: Union[torch.Tensor, Tuple[torch.Tensor], List[torch.Tensor]], mode: str = 'mean', stride: int = 2) -> torch.Tensor:
        """Apply 1D pooling to a tensor of size [B x T (x H)]."""
    def pre_attention_pooling(self, output, attention_inputs: Tuple[torch.Tensor]) -> Tuple[torch.Tensor, Tuple[torch.Tensor]]:
        """Pool `output` and the proper parts of `attention_inputs` before the attention layer."""
    def post_attention_pooling(self, attention_inputs: Tuple[torch.Tensor]) -> Tuple[torch.Tensor]:
        """Pool the proper parts of `attention_inputs` after the attention layer."""

class FunnelRelMultiheadAttention(nn.Module):
    config: Incomplete
    block_index: Incomplete
    hidden_dropout: Incomplete
    attention_dropout: Incomplete
    q_head: Incomplete
    k_head: Incomplete
    v_head: Incomplete
    r_w_bias: Incomplete
    r_r_bias: Incomplete
    r_kernel: Incomplete
    r_s_bias: Incomplete
    seg_embed: Incomplete
    post_proj: Incomplete
    layer_norm: Incomplete
    scale: Incomplete
    def __init__(self, config: FunnelConfig, block_index: int) -> None: ...
    def relative_positional_attention(self, position_embeds, q_head, context_len, cls_mask: Incomplete | None = None):
        """Relative attention score for the positional encodings"""
    def relative_token_type_attention(self, token_type_mat, q_head, cls_mask: Incomplete | None = None):
        """Relative attention score for the token_type_ids"""
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attention_inputs: Tuple[torch.Tensor], output_attentions: bool = False) -> Tuple[torch.Tensor, ...]: ...

class FunnelPositionwiseFFN(nn.Module):
    linear_1: Incomplete
    activation_function: Incomplete
    activation_dropout: Incomplete
    linear_2: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, hidden: torch.Tensor) -> torch.Tensor: ...

class FunnelLayer(nn.Module):
    attention: Incomplete
    ffn: Incomplete
    def __init__(self, config: FunnelConfig, block_index: int) -> None: ...
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attention_inputs, output_attentions: bool = False) -> Tuple: ...

class FunnelEncoder(nn.Module):
    config: Incomplete
    attention_structure: Incomplete
    blocks: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, inputs_embeds: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[Tuple, BaseModelOutput]: ...

def upsample(x: torch.Tensor, stride: int, target_len: int, separate_cls: bool = True, truncate_seq: bool = False) -> torch.Tensor:
    """
    Upsample tensor `x` to match `target_len` by repeating the tokens `stride` time on the sequence length dimension.
    """

class FunnelDecoder(nn.Module):
    config: Incomplete
    attention_structure: Incomplete
    layers: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, final_hidden: torch.Tensor, first_block_hidden: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[Tuple, BaseModelOutput]: ...

class FunnelDiscriminatorPredictions(nn.Module):
    """Prediction module for the discriminator, made up of two dense layers."""
    config: Incomplete
    dense: Incomplete
    dense_prediction: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, discriminator_hidden_states: torch.Tensor) -> torch.Tensor: ...

class FunnelPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = FunnelConfig
    load_tf_weights = load_tf_weights_in_funnel
    base_model_prefix: str

class FunnelClassificationHead(nn.Module):
    linear_hidden: Incomplete
    dropout: Incomplete
    linear_out: Incomplete
    def __init__(self, config: FunnelConfig, n_labels: int) -> None: ...
    def forward(self, hidden: torch.Tensor) -> torch.Tensor: ...

@dataclass
class FunnelForPreTrainingOutput(ModelOutput):
    """
    Output type of [`FunnelForPreTraining`].

    Args:
        loss (*optional*, returned when `labels` is provided, `torch.FloatTensor` of shape `(1,)`):
            Total loss of the ELECTRA-style objective.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Prediction scores of the head (scores for each token before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions) -> None: ...

FUNNEL_START_DOCSTRING: str
FUNNEL_INPUTS_DOCSTRING: str

class FunnelBaseModel(FunnelPreTrainedModel):
    embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Embedding: ...
    def set_input_embeddings(self, new_embeddings: nn.Embedding) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class FunnelModel(FunnelPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Embedding: ...
    def set_input_embeddings(self, new_embeddings: nn.Embedding) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class FunnelForPreTraining(FunnelPreTrainedModel):
    funnel: Incomplete
    discriminator_predictions: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, FunnelForPreTrainingOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the ELECTRA-style loss. Input should be a sequence of tokens (see `input_ids`
            docstring) Indices should be in `[0, 1]`:

            - 0 indicates the token is an original token,
            - 1 indicates the token was replaced.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, FunnelForPreTraining
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("funnel-transformer/small")
        >>> model = FunnelForPreTraining.from_pretrained("funnel-transformer/small")

        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
        >>> logits = model(**inputs).logits
        ```'''

class FunnelForMaskedLM(FunnelPreTrainedModel):
    funnel: Incomplete
    lm_head: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def get_output_embeddings(self) -> nn.Linear: ...
    def set_output_embeddings(self, new_embeddings: nn.Embedding) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """

class FunnelForSequenceClassification(FunnelPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    funnel: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class FunnelForMultipleChoice(FunnelPreTrainedModel):
    funnel: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MultipleChoiceModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class FunnelForTokenClassification(FunnelPreTrainedModel):
    num_labels: Incomplete
    funnel: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class FunnelForQuestionAnswering(FunnelPreTrainedModel):
    num_labels: Incomplete
    funnel: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: FunnelConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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
