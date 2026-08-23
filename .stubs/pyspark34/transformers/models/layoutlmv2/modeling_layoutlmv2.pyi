import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, torch_int_div as torch_int_div
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_detectron2_available as is_detectron2_available, logging as logging, replace_return_docstrings as replace_return_docstrings, requires_backends as requires_backends
from .configuration_layoutlmv2 import LayoutLMv2Config as LayoutLMv2Config
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
LAYOUTLMV2_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class LayoutLMv2Embeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    x_position_embeddings: Incomplete
    y_position_embeddings: Incomplete
    h_position_embeddings: Incomplete
    w_position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...

class LayoutLMv2SelfAttention(nn.Module):
    fast_qkv: Incomplete
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    has_relative_attention_bias: Incomplete
    has_spatial_attention_bias: Incomplete
    qkv_linear: Incomplete
    q_bias: Incomplete
    v_bias: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def compute_qkv(self, hidden_states): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...

class LayoutLMv2Attention(nn.Module):
    self: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...

class LayoutLMv2SelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class LayoutLMv2Intermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class LayoutLMv2Output(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LayoutLMv2Layer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, rel_pos: Incomplete | None = None, rel_2d_pos: Incomplete | None = None): ...
    def feed_forward_chunk(self, attention_output): ...

def relative_position_bucket(relative_position, bidirectional: bool = True, num_buckets: int = 32, max_distance: int = 128):
    """
    Adapted from Mesh Tensorflow:
    https://github.com/tensorflow/mesh/blob/0cb87fe07da627bf0b7e60475d59f95ed6b5be3d/mesh_tensorflow/transformer/transformer_layers.py#L593
    Translate relative position to a bucket number for relative attention. The relative position is defined as
    memory_position - query_position, i.e. the distance in tokens from the attending position to the attended-to
    position. If bidirectional=False, then positive relative positions are invalid. We use smaller buckets for small
    absolute relative_position and larger buckets for larger absolute relative_positions. All relative positions
    >=max_distance map to the same bucket. All relative positions <=-max_distance map to the same bucket. This should
    allow for more graceful generalization to longer sequences than the model has been trained on.

    Args:
        relative_position: an int32 Tensor
        bidirectional: a boolean - whether the attention is bidirectional
        num_buckets: an integer
        max_distance: an integer

    Returns:
        a Tensor with the same shape as relative_position, containing int32 values in the range [0, num_buckets)
    """

class LayoutLMv2Encoder(nn.Module):
    config: Incomplete
    layer: Incomplete
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
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, bbox: Incomplete | None = None, position_ids: Incomplete | None = None): ...

class LayoutLMv2PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMv2Config
    pretrained_model_archive_map = LAYOUTLMV2_PRETRAINED_MODEL_ARCHIVE_LIST
    base_model_prefix: str

def my_convert_sync_batchnorm(module, process_group: Incomplete | None = None): ...

class LayoutLMv2VisualBackbone(nn.Module):
    cfg: Incomplete
    backbone: Incomplete
    out_feature_key: str
    pool: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, images): ...
    def synchronize_batch_norm(self) -> None: ...

LAYOUTLMV2_START_DOCSTRING: str
LAYOUTLMV2_INPUTS_DOCSTRING: str

class LayoutLMv2Pooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class LayoutLMv2Model(LayoutLMv2PreTrainedModel):
    config: Incomplete
    has_visual_segment_embedding: Incomplete
    embeddings: Incomplete
    visual: Incomplete
    visual_proj: Incomplete
    visual_segment_embedding: Incomplete
    visual_LayerNorm: Incomplete
    visual_dropout: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, image: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2Model, set_seed
        >>> from PIL import Image
        >>> import torch
        >>> from datasets import load_dataset

        >>> set_seed(88)

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2Model.from_pretrained("microsoft/layoutlmv2-base-uncased")


        >>> dataset = load_dataset("hf-internal-testing/fixtures_docvqa")
        >>> image_path = dataset["test"][0]["file"]
        >>> image = Image.open(image_path).convert("RGB")

        >>> encoding = processor(image, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state

        >>> last_hidden_states.shape
        torch.Size([1, 342, 768])
        ```
        '''

class LayoutLMv2ForSequenceClassification(LayoutLMv2PreTrainedModel):
    num_labels: Incomplete
    layoutlmv2: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, image: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForSequenceClassification, set_seed
        >>> from PIL import Image
        >>> import torch
        >>> from datasets import load_dataset

        >>> set_seed(88)

        >>> dataset = load_dataset("rvl_cdip", split="train", streaming=True)
        >>> data = next(iter(dataset))
        >>> image = data["image"].convert("RGB")

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2ForSequenceClassification.from_pretrained(
        ...     "microsoft/layoutlmv2-base-uncased", num_labels=dataset.info.features["label"].num_classes
        ... )

        >>> encoding = processor(image, return_tensors="pt")
        >>> sequence_label = torch.tensor([data["label"]])

        >>> outputs = model(**encoding, labels=sequence_label)

        >>> loss, logits = outputs.loss, outputs.logits
        >>> predicted_idx = logits.argmax(dim=-1).item()
        >>> predicted_answer = dataset.info.features["label"].names[4]
        >>> predicted_idx, predicted_answer
        (4, \'advertisement\')
        ```
        '''

class LayoutLMv2ForTokenClassification(LayoutLMv2PreTrainedModel):
    num_labels: Incomplete
    layoutlmv2: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, image: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForTokenClassification, set_seed
        >>> from PIL import Image
        >>> from datasets import load_dataset

        >>> set_seed(88)

        >>> datasets = load_dataset("nielsr/funsd", split="test")
        >>> labels = datasets.features["ner_tags"].feature.names
        >>> id2label = {v: k for v, k in enumerate(labels)}

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased", revision="no_ocr")
        >>> model = LayoutLMv2ForTokenClassification.from_pretrained(
        ...     "microsoft/layoutlmv2-base-uncased", num_labels=len(labels)
        ... )

        >>> data = datasets[0]
        >>> image = Image.open(data["image_path"]).convert("RGB")
        >>> words = data["words"]
        >>> boxes = data["bboxes"]  # make sure to normalize your bounding boxes
        >>> word_labels = data["ner_tags"]
        >>> encoding = processor(
        ...     image,
        ...     words,
        ...     boxes=boxes,
        ...     word_labels=word_labels,
        ...     padding="max_length",
        ...     truncation=True,
        ...     return_tensors="pt",
        ... )

        >>> outputs = model(**encoding)
        >>> logits, loss = outputs.logits, outputs.loss

        >>> predicted_token_class_ids = logits.argmax(-1)
        >>> predicted_tokens_classes = [id2label[t.item()] for t in predicted_token_class_ids[0]]
        >>> predicted_tokens_classes[:5]
        [\'B-ANSWER\', \'B-HEADER\', \'B-HEADER\', \'B-HEADER\', \'B-HEADER\']
        ```
        '''

class LayoutLMv2ForQuestionAnswering(LayoutLMv2PreTrainedModel):
    num_labels: Incomplete
    layoutlmv2: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, has_visual_segment_embedding: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, bbox: Optional[torch.LongTensor] = None, image: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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

        Example:

        In this example below, we give the LayoutLMv2 model an image (of texts) and ask it a question. It will give us
        a prediction of what it thinks the answer is (the span of the answer within the texts parsed from the image).

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForQuestionAnswering, set_seed
        >>> import torch
        >>> from PIL import Image
        >>> from datasets import load_dataset

        >>> set_seed(88)
        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2ForQuestionAnswering.from_pretrained("microsoft/layoutlmv2-base-uncased")

        >>> dataset = load_dataset("hf-internal-testing/fixtures_docvqa")
        >>> image_path = dataset["test"][0]["file"]
        >>> image = Image.open(image_path).convert("RGB")
        >>> question = "When is coffee break?"
        >>> encoding = processor(image, question, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> predicted_start_idx = outputs.start_logits.argmax(-1).item()
        >>> predicted_end_idx = outputs.end_logits.argmax(-1).item()
        >>> predicted_start_idx, predicted_end_idx
        (154, 287)

        >>> predicted_answer_tokens = encoding.input_ids.squeeze()[predicted_start_idx : predicted_end_idx + 1]
        >>> predicted_answer = processor.tokenizer.decode(predicted_answer_tokens)
        >>> predicted_answer  # results are not very good without further fine-tuning
        \'council mem - bers conducted by trrf treasurer philip g. kuehn to get answers which the public ...
        ```

        ```python
        >>> target_start_index = torch.tensor([7])
        >>> target_end_index = torch.tensor([14])
        >>> outputs = model(**encoding, start_positions=target_start_index, end_positions=target_end_index)
        >>> predicted_answer_span_start = outputs.start_logits.argmax(-1).item()
        >>> predicted_answer_span_end = outputs.end_logits.argmax(-1).item()
        >>> predicted_answer_span_start, predicted_answer_span_end
        (154, 287)
        ```
        '''
