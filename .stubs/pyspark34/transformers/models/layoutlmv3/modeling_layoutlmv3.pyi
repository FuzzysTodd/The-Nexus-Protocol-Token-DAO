import torch
import torch.nn as nn
from ...activations import ACT2FN as ACT2FN
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from .configuration_layoutlmv3 import LayoutLMv3Config as LayoutLMv3Config
from _typeshed import Incomplete
from transformers import apply_chunking_to_forward as apply_chunking_to_forward
from transformers.modeling_outputs import BaseModelOutput as BaseModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from transformers.modeling_utils import PreTrainedModel as PreTrainedModel
from transformers.utils import logging as logging
from typing import Optional, Tuple, Union

logger: Incomplete
LAYOUTLMV3_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LAYOUTLMV3_START_DOCSTRING: str
LAYOUTLMV3_MODEL_INPUTS_DOCSTRING: str
LAYOUTLMV3_DOWNSTREAM_INPUTS_DOCSTRING: str

class LayoutLMv3PatchEmbeddings(nn.Module):
    """LayoutLMv3 image (patch) embeddings. This class also automatically interpolates the position embeddings for varying
    image sizes."""
    patch_shape: Incomplete
    proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values, position_embedding: Incomplete | None = None): ...

class LayoutLMv3TextEmbeddings(nn.Module):
    """
    LayoutLMv3 text embeddings. Same as `RobertaEmbeddings` but with added spatial (layout) embeddings.
    """
    word_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    padding_idx: Incomplete
    position_embeddings: Incomplete
    x_position_embeddings: Incomplete
    y_position_embeddings: Incomplete
    h_position_embeddings: Incomplete
    w_position_embeddings: Incomplete
    def __init__(self, config) -> None: ...
    def calculate_spatial_position_embeddings(self, bbox): ...
    def create_position_ids_from_input_ids(self, input_ids, padding_idx):
        """
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding
        symbols are ignored. This is modified from fairseq's `utils.make_positions`.
        """
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.
        """
    def forward(self, input_ids: Incomplete | None = None, bbox: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...

class LayoutLMv3PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMv3Config
    base_model_prefix: str

class LayoutLMv3SelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    has_relative_attention_bias: Incomplete
    has_spatial_attention_bias: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def cogview_attention(self, attention_scores, alpha: int = 32):
        """
        https://arxiv.org/abs/2105.13290 Section 2.4 Stabilization of training: Precision Bottleneck Relaxation
        (PB-Relax). A replacement of the original nn.Softmax(dim=-1)(attention_scores). Seems the new attention_probs
        will result in a slower speed and a little bias. Can use torch.allclose(standard_attention_probs,
        cogview_attention_probs, atol=1e-08) for comparison. The smaller atol (e.g., 1e-08), the better.
        """
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...

class LayoutLMv3SelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LayoutLMv3Attention(nn.Module):
    self: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...

class LayoutLMv3Layer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...
    def feed_forward_chunk(self, attention_output): ...

class LayoutLMv3Encoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    has_relative_attention_bias: Incomplete
    has_spatial_attention_bias: Incomplete
    rel_pos_bins: Incomplete
    max_rel_pos: Incomplete
    rel_pos_onehot_size: Incomplete
    rel_pos_bias: Incomplete
    max_rel_2d_pos: Incomplete
    rel_2d_pos_bins: Incomplete
    rel_2d_pos_onehot_size: Incomplete
    rel_pos_x_bias: Incomplete
    rel_pos_y_bias: Incomplete
    def __init__(self, config) -> None: ...
    def relative_position_bucket(self, relative_position, bidirectional: bool = True, num_buckets: int = 32, max_distance: int = 128): ...
    def forward(self, hidden_states, bbox: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, position_ids: Incomplete | None = None, patch_height: Incomplete | None = None, patch_width: Incomplete | None = None): ...

class LayoutLMv3Intermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class LayoutLMv3Output(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LayoutLMv3Model(LayoutLMv3PreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    patch_embed: Incomplete
    cls_token: Incomplete
    pos_embed: Incomplete
    pos_drop: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    norm: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    visual_bbox: Incomplete
    def init_visual_bbox(self, image_size=(14, 14), max_len: int = 1000) -> None:
        """
        Create the bounding boxes for the visual (patch) tokens.
        """
    def calculate_visual_bbox(self, device, dtype, batch_size): ...
    def forward_image(self, pixel_values): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, AutoModel
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = AutoModel.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class LayoutLMv3ClassificationHead(nn.Module):
    """
    Head for sentence-level classification tasks. Reference: RobertaClassificationHead
    """
    pool_feature: Incomplete
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config, pool_feature: bool = False) -> None: ...
    def forward(self, x): ...

class LayoutLMv3ForTokenClassification(LayoutLMv3PreTrainedModel):
    num_labels: Incomplete
    layoutlmv3: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, pixel_values: Optional[torch.LongTensor] = None) -> Union[Tuple, TokenClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, AutoModelForTokenClassification
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = AutoModelForTokenClassification.from_pretrained("microsoft/layoutlmv3-base", num_labels=7)

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]
        >>> word_labels = example["ner_tags"]

        >>> encoding = processor(image, words, boxes=boxes, word_labels=word_labels, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''

class LayoutLMv3ForQuestionAnswering(LayoutLMv3PreTrainedModel):
    num_labels: Incomplete
    layoutlmv3: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, bbox: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.LongTensor] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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
        >>> from transformers import AutoProcessor, AutoModelForQuestionAnswering
        >>> from datasets import load_dataset
        >>> import torch

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = AutoModelForQuestionAnswering.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> question = "what\'s his name?"
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, question, words, boxes=boxes, return_tensors="pt")
        >>> start_positions = torch.tensor([1])
        >>> end_positions = torch.tensor([3])

        >>> outputs = model(**encoding, start_positions=start_positions, end_positions=end_positions)
        >>> loss = outputs.loss
        >>> start_scores = outputs.start_logits
        >>> end_scores = outputs.end_logits
        ```'''

class LayoutLMv3ForSequenceClassification(LayoutLMv3PreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    layoutlmv3: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, bbox: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.LongTensor] = None) -> Union[Tuple, SequenceClassifierOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, AutoModelForSequenceClassification
        >>> from datasets import load_dataset
        >>> import torch

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = AutoModelForSequenceClassification.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="pt")
        >>> sequence_label = torch.tensor([1])

        >>> outputs = model(**encoding, labels=sequence_label)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
