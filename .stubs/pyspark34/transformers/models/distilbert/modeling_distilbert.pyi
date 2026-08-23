import torch
from ...activations import get_activation as get_activation
from ...deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_distilbert import DistilBertConfig as DistilBertConfig
from _typeshed import Incomplete
from torch import nn
from transformers.configuration_utils import PretrainedConfig as PretrainedConfig
from typing import List, Optional, Tuple, Union

logger: Incomplete
DISTILBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def create_sinusoidal_embeddings(n_pos: int, dim: int, out: torch.Tensor): ...

class Embeddings(nn.Module):
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """
        Parameters:
            input_ids: torch.tensor(bs, max_seq_length) The token ids to embed.

        Returns: torch.tensor(bs, max_seq_length, dim) The embedded tokens (plus position embeddings, no token_type
        embeddings)
        """

class MultiHeadSelfAttention(nn.Module):
    n_heads: Incomplete
    dim: Incomplete
    dropout: Incomplete
    q_lin: Incomplete
    k_lin: Incomplete
    v_lin: Incomplete
    out_lin: Incomplete
    pruned_heads: Incomplete
    attention_head_size: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def prune_heads(self, heads: List[int]): ...
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, ...]:
        """
        Parameters:
            query: torch.tensor(bs, seq_length, dim)
            key: torch.tensor(bs, seq_length, dim)
            value: torch.tensor(bs, seq_length, dim)
            mask: torch.tensor(bs, seq_length)

        Returns:
            weights: torch.tensor(bs, n_heads, seq_length, seq_length) Attention weights context: torch.tensor(bs,
            seq_length, dim) Contextualized layer. Optional: only if `output_attentions=True`
        """

class FFN(nn.Module):
    dropout: Incomplete
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    lin1: Incomplete
    lin2: Incomplete
    activation: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
    def ff_chunk(self, input: torch.Tensor) -> torch.Tensor: ...

class TransformerBlock(nn.Module):
    attention: Incomplete
    sa_layer_norm: Incomplete
    ffn: Incomplete
    output_layer_norm: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def forward(self, x: torch.Tensor, attn_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, ...]:
        """
        Parameters:
            x: torch.tensor(bs, seq_length, dim)
            attn_mask: torch.tensor(bs, seq_length)

        Returns:
            sa_weights: torch.tensor(bs, n_heads, seq_length, seq_length) The attention weights ffn_output:
            torch.tensor(bs, seq_length, dim) The output of the transformer block contextualization.
        """

class Transformer(nn.Module):
    n_layers: Incomplete
    layer: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def forward(self, x: torch.Tensor, attn_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: Optional[bool] = None) -> Union[BaseModelOutput, Tuple[torch.Tensor, ...]]:
        """
        Parameters:
            x: torch.tensor(bs, seq_length, dim) Input sequence embedded.
            attn_mask: torch.tensor(bs, seq_length) Attention mask on the sequence.

        Returns:
            hidden_state: torch.tensor(bs, seq_length, dim) Sequence of hidden states in the last (top)
            layer all_hidden_states: Tuple[torch.tensor(bs, seq_length, dim)]
                Tuple of length n_layers with the hidden states from each layer.
                Optional: only if output_hidden_states=True
            all_attentions: Tuple[torch.tensor(bs, n_heads, seq_length, seq_length)]
                Tuple of length n_layers with the attention weights from each layer
                Optional: only if output_attentions=True
        """

class DistilBertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DistilBertConfig
    load_tf_weights: Incomplete
    base_model_prefix: str

DISTILBERT_START_DOCSTRING: str
DISTILBERT_INPUTS_DOCSTRING: str

class DistilBertModel(DistilBertPreTrainedModel):
    embeddings: Incomplete
    transformer: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`):
                The number of new position embedding matrix. If position embeddings are learned, increasing the size
                will add newly initialized vectors at the end, whereas reducing the size will remove vectors from the
                end. If position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the
                size will add correct vectors at the end following the position encoding algorithm, whereas reducing
                the size will remove vectors from the end.
        """
    def get_input_embeddings(self) -> nn.Embedding: ...
    def set_input_embeddings(self, new_embeddings: nn.Embedding): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[BaseModelOutput, Tuple[torch.Tensor, ...]]: ...

class DistilBertForMaskedLM(DistilBertPreTrainedModel):
    activation: Incomplete
    distilbert: Incomplete
    vocab_transform: Incomplete
    vocab_layer_norm: Incomplete
    vocab_projector: Incomplete
    mlm_loss_fct: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`):
                The number of new position embedding matrix. If position embeddings are learned, increasing the size
                will add newly initialized vectors at the end, whereas reducing the size will remove vectors from the
                end. If position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the
                size will add correct vectors at the end following the position encoding algorithm, whereas reducing
                the size will remove vectors from the end.
        """
    def get_output_embeddings(self) -> nn.Module: ...
    def set_output_embeddings(self, new_embeddings: nn.Module): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MaskedLMOutput, Tuple[torch.Tensor, ...]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
        """

class DistilBertForSequenceClassification(DistilBertPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    distilbert: Incomplete
    pre_classifier: Incomplete
    classifier: Incomplete
    dropout: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`):
                The number of new position embedding matrix. If position embeddings are learned, increasing the size
                will add newly initialized vectors at the end, whereas reducing the size will remove vectors from the
                end. If position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the
                size will add correct vectors at the end following the position encoding algorithm, whereas reducing
                the size will remove vectors from the end.
        """
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[SequenceClassifierOutput, Tuple[torch.Tensor, ...]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class DistilBertForQuestionAnswering(DistilBertPreTrainedModel):
    distilbert: Incomplete
    qa_outputs: Incomplete
    dropout: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`):
                The number of new position embedding matrix. If position embeddings are learned, increasing the size
                will add newly initialized vectors at the end, whereas reducing the size will remove vectors from the
                end. If position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the
                size will add correct vectors at the end following the position encoding algorithm, whereas reducing
                the size will remove vectors from the end.
        """
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[QuestionAnsweringModelOutput, Tuple[torch.Tensor, ...]]:
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

class DistilBertForTokenClassification(DistilBertPreTrainedModel):
    num_labels: Incomplete
    distilbert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`):
                The number of new position embedding matrix. If position embeddings are learned, increasing the size
                will add newly initialized vectors at the end, whereas reducing the size will remove vectors from the
                end. If position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the
                size will add correct vectors at the end following the position encoding algorithm, whereas reducing
                the size will remove vectors from the end.
        """
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[TokenClassifierOutput, Tuple[torch.Tensor, ...]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class DistilBertForMultipleChoice(DistilBertPreTrainedModel):
    distilbert: Incomplete
    pre_classifier: Incomplete
    classifier: Incomplete
    dropout: Incomplete
    def __init__(self, config: PretrainedConfig) -> None: ...
    def get_position_embeddings(self) -> nn.Embedding:
        """
        Returns the position embeddings
        """
    def resize_position_embeddings(self, new_num_position_embeddings: int):
        """
        Resizes position embeddings of the model if `new_num_position_embeddings != config.max_position_embeddings`.

        Arguments:
            new_num_position_embeddings (`int`)
                The number of new position embeddings. If position embeddings are learned, increasing the size will add
                newly initialized vectors at the end, whereas reducing the size will remove vectors from the end. If
                position embeddings are not learned (*e.g.* sinusoidal position embeddings), increasing the size will
                add correct vectors at the end following the position encoding algorithm, whereas reducing the size
                will remove vectors from the end.
        """
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MultipleChoiceModelOutput, Tuple[torch.Tensor, ...]]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, DistilBertForMultipleChoice
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
        >>> model = DistilBertForMultipleChoice.from_pretrained("distilbert-base-cased")

        >>> prompt = "In Italy, pizza served in formal settings, such as at a restaurant, is presented unsliced."
        >>> choice0 = "It is eaten with a fork and a knife."
        >>> choice1 = "It is eaten while held in the hand."
        >>> labels = torch.tensor(0).unsqueeze(0)  # choice0 is correct (according to Wikipedia ;)), batch size 1

        >>> encoding = tokenizer([[prompt, choice0], [prompt, choice1]], return_tensors="pt", padding=True)
        >>> outputs = model(**{k: v.unsqueeze(0) for k, v in encoding.items()}, labels=labels)  # batch size is 1

        >>> # the linear classifier still needs to be trained
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
