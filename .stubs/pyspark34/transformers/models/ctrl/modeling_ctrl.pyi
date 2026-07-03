import torch
from ...modeling_outputs import BaseModelOutputWithPast as BaseModelOutputWithPast, CausalLMOutputWithPast as CausalLMOutputWithPast, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import Conv1D as Conv1D, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_ctrl import CTRLConfig as CTRLConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
CTRL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def angle_defn(pos, i, d_model_size): ...
def positional_encoding(position, d_model_size, dtype): ...
def scaled_dot_product_attention(q, k, v, mask, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None): ...

class MultiHeadAttention(nn.Module):
    num_heads: Incomplete
    d_model_size: Incomplete
    depth: Incomplete
    Wq: Incomplete
    Wk: Incomplete
    Wv: Incomplete
    dense: Incomplete
    pruned_heads: Incomplete
    def __init__(self, d_model_size, num_heads) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def split_into_heads(self, x, batch_size): ...
    def forward(self, v, k, q, mask, layer_past: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

def point_wise_feed_forward_network(d_model_size, dff): ...

class EncoderLayer(nn.Module):
    multi_head_attention: Incomplete
    ffn: Incomplete
    layernorm1: Incomplete
    layernorm2: Incomplete
    dropout1: Incomplete
    dropout2: Incomplete
    def __init__(self, d_model_size, num_heads, dff, rate: float = 0.1) -> None: ...
    def forward(self, x, mask, layer_past: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class CTRLPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CTRLConfig
    base_model_prefix: str

CTRL_START_DOCSTRING: str
CTRL_INPUTS_DOCSTRING: str

class CTRLModel(CTRLPreTrainedModel):
    d_model_size: Incomplete
    num_layers: Incomplete
    pos_encoding: Incomplete
    w: Incomplete
    dropout: Incomplete
    h: Incomplete
    layernorm: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPast]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, CTRLModel
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("ctrl")
        >>> model = CTRLModel.from_pretrained("ctrl")

        >>> # CTRL was trained with control codes as the first token
        >>> inputs = tokenizer("Opinion My dog is cute", return_tensors="pt")
        >>> assert inputs["input_ids"][0, 0].item() in tokenizer.control_codes.values()

        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        >>> list(last_hidden_states.shape)
        [1, 5, 1280]
        ```'''

class CTRLLMHeadModel(CTRLPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], CausalLMOutputWithPast]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, CTRLLMHeadModel

        >>> tokenizer = AutoTokenizer.from_pretrained("ctrl")
        >>> model = CTRLLMHeadModel.from_pretrained("ctrl")

        >>> # CTRL was trained with control codes as the first token
        >>> inputs = tokenizer("Wikipedia The llama is", return_tensors="pt")
        >>> assert inputs["input_ids"][0, 0].item() in tokenizer.control_codes.values()

        >>> sequence_ids = model.generate(inputs["input_ids"])
        >>> sequences = tokenizer.batch_decode(sequence_ids)
        >>> sequences
        [\'Wikipedia The llama is a member of the family Bovidae. It is native to the Andes of Peru,\']

        >>> outputs = model(**inputs, labels=inputs["input_ids"])
        >>> round(outputs.loss.item(), 2)
        9.21

        >>> list(outputs.logits.shape)
        [1, 5, 246534]
        ```'''

class CTRLForSequenceClassification(CTRLPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Example of single-label classification:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, CTRLForSequenceClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("ctrl")
        >>> model = CTRLForSequenceClassification.from_pretrained("ctrl")

        >>> # CTRL was trained with control codes as the first token
        >>> inputs = tokenizer("Opinion My dog is cute", return_tensors="pt")
        >>> assert inputs["input_ids"][0, 0].item() in tokenizer.control_codes.values()

        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> predicted_class_id = logits.argmax().item()
        >>> model.config.id2label[predicted_class_id]
        \'LABEL_0\'
        ```

        ```python
        >>> import torch

        >>> torch.manual_seed(42)  # doctest: +IGNORE_RESULT
        >>> # To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
        >>> num_labels = len(model.config.id2label)
        >>> model = CTRLForSequenceClassification.from_pretrained("ctrl", num_labels=num_labels)

        >>> labels = torch.tensor(1)
        >>> loss = model(**inputs, labels=labels).loss
        >>> round(loss.item(), 2)
        0.35
        ```

        Example of multi-label classification:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, CTRLForSequenceClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("ctrl")
        >>> model = CTRLForSequenceClassification.from_pretrained("ctrl", problem_type="multi_label_classification")

        >>> # CTRL was trained with control codes as the first token
        >>> inputs = tokenizer("Opinion My dog is cute", return_tensors="pt")
        >>> assert inputs["input_ids"][0, 0].item() in tokenizer.control_codes.values()

        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> predicted_class_id = logits.argmax().item()
        >>> model.config.id2label[predicted_class_id]
        \'LABEL_0\'
        ```

        ```python
        >>> # To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
        >>> num_labels = len(model.config.id2label)
        >>> model = CTRLForSequenceClassification.from_pretrained("ctrl", num_labels=num_labels)

        >>> num_labels = len(model.config.id2label)
        >>> labels = torch.nn.functional.one_hot(torch.tensor([predicted_class_id]), num_classes=num_labels).to(
        ...     torch.float
        ... )
        >>> loss = model(**inputs, labels=labels).loss
        >>> loss.backward()  # doctest: +IGNORE_RESULT
        ```'''
