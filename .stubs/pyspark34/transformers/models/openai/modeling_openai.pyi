import torch
from ...activations import gelu_new as gelu_new, silu as silu
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel, SequenceSummary as SequenceSummary
from ...pytorch_utils import Conv1D as Conv1D, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_conv1d_layer as prune_conv1d_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_openai import OpenAIGPTConfig as OpenAIGPTConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
OPENAI_GPT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_openai_gpt(model, config, openai_checkpoint_folder_path):
    """Load tf pre-trained weights in a pytorch model (from NumPy arrays here)"""

ACT_FNS: Incomplete

class Attention(nn.Module):
    n_head: Incomplete
    split_size: Incomplete
    scale: Incomplete
    c_attn: Incomplete
    c_proj: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, nx, n_positions, config, scale: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def merge_heads(self, x): ...
    def split_heads(self, x, k: bool = False): ...
    def forward(self, x, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class MLP(nn.Module):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, n_state, config) -> None: ...
    def forward(self, x): ...

class Block(nn.Module):
    attn: Incomplete
    ln_1: Incomplete
    mlp: Incomplete
    ln_2: Incomplete
    def __init__(self, n_positions, config, scale: bool = False) -> None: ...
    def forward(self, x, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class OpenAIGPTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = OpenAIGPTConfig
    load_tf_weights = load_tf_weights_in_openai_gpt
    base_model_prefix: str

@dataclass
class OpenAIGPTDoubleHeadsModelOutput(ModelOutput):
    """
    Base class for outputs of models predicting if two sentences are consecutive or not.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        mc_loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `mc_labels` is provided):
            Multiple choice classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, num_choices, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        mc_logits (`torch.FloatTensor` of shape `(batch_size, num_choices)`):
            Prediction scores of the multiple choice classification head (scores for each choice before SoftMax).
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
    mc_loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    mc_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, mc_loss, logits, mc_logits, hidden_states, attentions) -> None: ...

OPENAI_GPT_START_DOCSTRING: str
OPENAI_GPT_INPUTS_DOCSTRING: str

class OpenAIGPTModel(OpenAIGPTPreTrainedModel):
    tokens_embed: Incomplete
    positions_embed: Incomplete
    drop: Incomplete
    h: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutput]: ...

class OpenAIGPTLMHeadModel(OpenAIGPTPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], CausalLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
    def prepare_inputs_for_generation(self, input_ids: torch.LongTensor, **kwargs) -> Dict[str, Any]: ...

class OpenAIGPTDoubleHeadsModel(OpenAIGPTPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    multiple_choice_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, mc_token_ids: Optional[torch.LongTensor] = None, labels: Optional[torch.LongTensor] = None, mc_labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], OpenAIGPTDoubleHeadsModelOutput]:
        '''
        mc_token_ids (`torch.LongTensor` of shape `(batch_size, num_choices)`, *optional*, default to index of the last token of the input):
            Index of the classification token in each input sequence. Selected in the range `[0, input_ids.size(-1) -
            1]`.
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-1, 0, ..., config.vocab_size]` All labels set to `-100` are
            ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        mc_labels (`torch.LongTensor` of shape `(batch_size)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where *num_choices* is the size of the second dimension of the input tensors. (see *input_ids* above)

        Return:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, OpenAIGPTDoubleHeadsModel
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("openai-gpt")
        >>> model = OpenAIGPTDoubleHeadsModel.from_pretrained("openai-gpt")
        >>> tokenizer.add_special_tokens(
        ...     {"cls_token": "[CLS]"}
        ... )  # Add a [CLS] to the vocabulary (we should train it also!)
        >>> model.resize_token_embeddings(len(tokenizer))

        >>> choices = ["Hello, my dog is cute [CLS]", "Hello, my cat is cute [CLS]"]
        >>> input_ids = torch.tensor([tokenizer.encode(s) for s in choices]).unsqueeze(0)  # Batch size 1, 2 choices
        >>> mc_token_ids = torch.tensor([input_ids.size(-1) - 1, input_ids.size(-1) - 1]).unsqueeze(0)  # Batch size 1

        >>> outputs = model(input_ids, mc_token_ids=mc_token_ids)
        >>> lm_logits = outputs.logits
        >>> mc_logits = outputs.mc_logits
        ```'''

class OpenAIGPTForSequenceClassification(OpenAIGPTPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
