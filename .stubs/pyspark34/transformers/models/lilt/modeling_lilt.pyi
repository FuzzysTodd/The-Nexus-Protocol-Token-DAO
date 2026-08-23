import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_lilt import LiltConfig as LiltConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
LILT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class LiltTextEmbeddings(nn.Module):
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    padding_idx: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...
    def create_position_ids_from_input_ids(self, input_ids, padding_idx):
        """
        Args:
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding
        symbols are ignored. This is modified from fairseq's `utils.make_positions`.
            x: torch.Tensor x:
        Returns: torch.Tensor
        """
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        Args:
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.:
            inputs_embeds: torch.Tensor
        Returns: torch.Tensor
        """

class LiltLayoutEmbeddings(nn.Module):
    x_position_embeddings: Incomplete
    y_position_embeddings: Incomplete
    h_position_embeddings: Incomplete
    w_position_embeddings: Incomplete
    padding_idx: Incomplete
    box_position_embeddings: Incomplete
    box_linear_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, bbox: Incomplete | None = None, position_ids: Incomplete | None = None): ...

class LiltSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    layout_query: Incomplete
    layout_key: Incomplete
    layout_value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    channel_shrink_ratio: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x, r: int = 1): ...
    def forward(self, hidden_states, layout_inputs, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class LiltSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LiltAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    layout_output: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, layout_inputs: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class LiltIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class LiltOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LiltLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layout_intermediate: Incomplete
    layout_output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, layout_inputs: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...
    def feed_forward_chunk(self, attention_output): ...
    def layout_feed_forward_chunk(self, attention_output): ...

class LiltEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, layout_inputs: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple[torch.Tensor], BaseModelOutput]: ...

class LiltPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class LiltPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LiltConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    def update_keys_to_ignore(self, config, del_keys_to_ignore) -> None:
        """Remove some keys from ignore list"""

LILT_START_DOCSTRING: str
LILT_INPUTS_DOCSTRING: str

class LiltModel(LiltPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    layout_embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, bbox: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPooling]:
        '''

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, AutoModel
        >>> from datasets import load_dataset

        >>> tokenizer = AutoTokenizer.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")
        >>> model = AutoModel.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = tokenizer(words, boxes=boxes, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class LiltForSequenceClassification(LiltPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    lilt: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.Tensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, AutoModelForSequenceClassification
        >>> from datasets import load_dataset

        >>> tokenizer = AutoTokenizer.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")
        >>> model = AutoModelForSequenceClassification.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = tokenizer(words, boxes=boxes, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> predicted_class_idx = outputs.logits.argmax(-1).item()
        >>> predicted_class = model.config.id2label[predicted_class_idx]
        ```'''

class LiltForTokenClassification(LiltPreTrainedModel):
    num_labels: Incomplete
    lilt: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], TokenClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, AutoModelForTokenClassification
        >>> from datasets import load_dataset

        >>> tokenizer = AutoTokenizer.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")
        >>> model = AutoModelForTokenClassification.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = tokenizer(words, boxes=boxes, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> predicted_class_indices = outputs.logits.argmax(-1)
        ```'''

class LiltClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class LiltForQuestionAnswering(LiltPreTrainedModel):
    num_labels: Incomplete
    lilt: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], QuestionAnsweringModelOutput]:
        '''
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, AutoModelForQuestionAnswering
        >>> from datasets import load_dataset

        >>> tokenizer = AutoTokenizer.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")
        >>> model = AutoModelForQuestionAnswering.from_pretrained("SCUT-DLVCLab/lilt-roberta-en-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = tokenizer(words, boxes=boxes, return_tensors="pt")

        >>> outputs = model(**encoding)

        >>> answer_start_index = outputs.start_logits.argmax()
        >>> answer_end_index = outputs.end_logits.argmax()

        >>> predict_answer_tokens = encoding.input_ids[0, answer_start_index : answer_end_index + 1]
        >>> predicted_answer = tokenizer.decode(predict_answer_tokens)
        ```'''
