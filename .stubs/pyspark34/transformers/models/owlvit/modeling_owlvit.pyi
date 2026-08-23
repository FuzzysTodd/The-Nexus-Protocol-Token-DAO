import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_vision_available as is_vision_available, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_owlvit import OwlViTConfig as OwlViTConfig, OwlViTTextConfig as OwlViTTextConfig, OwlViTVisionConfig as OwlViTVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from transformers.image_transforms import center_to_corners_format as center_to_corners_format
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
OWLVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def contrastive_loss(logits: torch.Tensor) -> torch.Tensor: ...
def owlvit_loss(similarity: torch.Tensor) -> torch.Tensor: ...

@dataclass
class OwlViTOutput(ModelOutput):
    """
    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds (`torch.FloatTensor` of shape `(batch_size * num_max_text_queries, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`OwlViTTextModel`].
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`OwlViTVisionModel`].
        text_model_output (Tuple[`BaseModelOutputWithPooling`]):
            The output of the [`OwlViTTextModel`].
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`OwlViTVisionModel`].
    """
    loss: Optional[torch.FloatTensor] = ...
    logits_per_image: torch.FloatTensor = ...
    logits_per_text: torch.FloatTensor = ...
    text_embeds: torch.FloatTensor = ...
    image_embeds: torch.FloatTensor = ...
    text_model_output: BaseModelOutputWithPooling = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits_per_image, logits_per_text, text_embeds, image_embeds, text_model_output, vision_model_output) -> None: ...

def box_area(boxes: torch.Tensor) -> torch.Tensor:
    """
    Computes the area of a set of bounding boxes, which are specified by its (x1, y1, x2, y2) coordinates.

    Args:
        boxes (`torch.FloatTensor` of shape `(number_of_boxes, 4)`):
            Boxes for which the area will be computed. They are expected to be in (x1, y1, x2, y2) format with `0 <= x1
            < x2` and `0 <= y1 < y2`.

    Returns:
        `torch.FloatTensor`: a tensor containing the area for each box.
    """
def box_iou(boxes1: torch.Tensor, boxes2: torch.Tensor) -> torch.Tensor: ...
def generalized_box_iou(boxes1, boxes2):
    """
    Generalized IoU from https://giou.stanford.edu/. The boxes should be in [x0, y0, x1, y1] (corner) format.

    Returns:
        `torch.FloatTensor`: a [N, M] pairwise matrix, where N = len(boxes1) and M = len(boxes2)
    """

@dataclass
class OwlViTObjectDetectionOutput(ModelOutput):
    """
    Output type of [`OwlViTForObjectDetection`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` are provided)):
            Total loss as a linear combination of a negative log-likehood (cross-entropy) for class prediction and a
            bounding box loss. The latter is defined as a linear combination of the L1 loss and the generalized
            scale-invariant IoU loss.
        loss_dict (`Dict`, *optional*):
            A dictionary containing the individual losses. Useful for logging.
        logits (`torch.FloatTensor` of shape `(batch_size, num_patches, num_queries)`):
            Classification logits (including no-object) for all queries.
        pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual image in the batch (disregarding
            possible padding). You can use [`~OwlViTImageProcessor.post_process_object_detection`] to retrieve the
            unnormalized bounding boxes.
        text_embeds (`torch.FloatTensor` of shape `(batch_size, num_max_text_queries, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`OwlViTTextModel`].
        image_embeds (`torch.FloatTensor` of shape `(batch_size, patch_size, patch_size, output_dim`):
            Pooled output of [`OwlViTVisionModel`]. OWL-ViT represents images as a set of image patches and computes
            image embeddings for each patch.
        class_embeds (`torch.FloatTensor` of shape `(batch_size, num_patches, hidden_size)`):
            Class embeddings of all image patches. OWL-ViT represents images as a set of image patches where the total
            number of patches is (image_size / patch_size)**2.
        text_model_output (Tuple[`BaseModelOutputWithPooling`]):
            The output of the [`OwlViTTextModel`].
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`OwlViTVisionModel`].
    """
    loss: Optional[torch.FloatTensor] = ...
    loss_dict: Optional[Dict] = ...
    logits: torch.FloatTensor = ...
    pred_boxes: torch.FloatTensor = ...
    text_embeds: torch.FloatTensor = ...
    image_embeds: torch.FloatTensor = ...
    class_embeds: torch.FloatTensor = ...
    text_model_output: BaseModelOutputWithPooling = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, loss_dict, logits, pred_boxes, text_embeds, image_embeds, class_embeds, text_model_output, vision_model_output) -> None: ...

@dataclass
class OwlViTImageGuidedObjectDetectionOutput(ModelOutput):
    """
    Output type of [`OwlViTForObjectDetection.image_guided_detection`].

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, num_patches, num_queries)`):
            Classification logits (including no-object) for all queries.
        target_pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual target image in the batch
            (disregarding possible padding). You can use [`~OwlViTImageProcessor.post_process_object_detection`] to
            retrieve the unnormalized bounding boxes.
        query_pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual query image in the batch
            (disregarding possible padding). You can use [`~OwlViTImageProcessor.post_process_object_detection`] to
            retrieve the unnormalized bounding boxes.
        image_embeds (`torch.FloatTensor` of shape `(batch_size, patch_size, patch_size, output_dim`):
            Pooled output of [`OwlViTVisionModel`]. OWL-ViT represents images as a set of image patches and computes
            image embeddings for each patch.
        query_image_embeds (`torch.FloatTensor` of shape `(batch_size, patch_size, patch_size, output_dim`):
            Pooled output of [`OwlViTVisionModel`]. OWL-ViT represents images as a set of image patches and computes
            image embeddings for each patch.
        class_embeds (`torch.FloatTensor` of shape `(batch_size, num_patches, hidden_size)`):
            Class embeddings of all image patches. OWL-ViT represents images as a set of image patches where the total
            number of patches is (image_size / patch_size)**2.
        text_model_output (Tuple[`BaseModelOutputWithPooling`]):
            The output of the [`OwlViTTextModel`].
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`OwlViTVisionModel`].
    """
    logits: torch.FloatTensor = ...
    image_embeds: torch.FloatTensor = ...
    query_image_embeds: torch.FloatTensor = ...
    target_pred_boxes: torch.FloatTensor = ...
    query_pred_boxes: torch.FloatTensor = ...
    class_embeds: torch.FloatTensor = ...
    text_model_output: BaseModelOutputWithPooling = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, logits, image_embeds, query_image_embeds, target_pred_boxes, query_pred_boxes, class_embeds, text_model_output, vision_model_output) -> None: ...

class OwlViTVisionEmbeddings(nn.Module):
    config: Incomplete
    embed_dim: Incomplete
    class_embedding: Incomplete
    patch_embedding: Incomplete
    num_patches: Incomplete
    num_positions: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: OwlViTVisionConfig) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class OwlViTTextEmbeddings(nn.Module):
    token_embedding: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: OwlViTTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None) -> torch.Tensor: ...

class OwlViTAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    config: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    dropout: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class OwlViTMLP(nn.Module):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class OwlViTEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: OwlViTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, causal_attention_mask: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
                `(config.encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class OwlViTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = OwlViTConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

OWLVIT_START_DOCSTRING: str
OWLVIT_TEXT_INPUTS_DOCSTRING: str
OWLVIT_VISION_INPUTS_DOCSTRING: str
OWLVIT_INPUTS_DOCSTRING: str
OWLVIT_OBJECT_DETECTION_INPUTS_DOCSTRING: str
OWLVIT_IMAGE_GUIDED_OBJECT_DETECTION_INPUTS_DOCSTRING: str

class OwlViTEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`OwlViTEncoderLayer`].

    Args:
        config: OwlViTConfig
    """
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: OwlViTConfig) -> None: ...
    def forward(self, inputs_embeds, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        """
        Args:
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`).
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:
                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.
                [What are attention masks?](../glossary#attention-mask)
            causal_attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Causal mask for the text model. Mask values selected in `[0, 1]`:
                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.
                [What are attention masks?](../glossary#attention-mask)
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class OwlViTTextTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: OwlViTTextConfig) -> None: ...
    def forward(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:
        """

class OwlViTTextModel(OwlViTPreTrainedModel):
    config_class = OwlViTTextConfig
    text_model: Incomplete
    def __init__(self, config: OwlViTTextConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:
        ```python
        >>> from transformers import AutoProcessor, OwlViTTextModel

        >>> model = OwlViTTextModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> inputs = processor(
        ...     text=[["a photo of a cat", "a photo of a dog"], ["photo of a astranaut"]], return_tensors="pt"
        ... )
        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```'''

class OwlViTVisionTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    pre_layernorm: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def __init__(self, config: OwlViTVisionConfig) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:
        """

class OwlViTVisionModel(OwlViTPreTrainedModel):
    config_class = OwlViTVisionConfig
    main_input_name: str
    vision_model: Incomplete
    def __init__(self, config: OwlViTVisionConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, OwlViTVisionModel

        >>> model = OwlViTVisionModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```'''

class OwlViTModel(OwlViTPreTrainedModel):
    config_class = OwlViTConfig
    projection_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def __init__(self, config: OwlViTConfig) -> None: ...
    def get_text_features(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            text_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The text embeddings obtained by
            applying the projection layer to the pooled output of [`OwlViTTextModel`].

        Examples:
        ```python
        >>> from transformers import AutoProcessor, OwlViTModel

        >>> model = OwlViTModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> inputs = processor(
        ...     text=[["a photo of a cat", "a photo of a dog"], ["photo of a astranaut"]], return_tensors="pt"
        ... )
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            image_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`OwlViTVisionModel`].

        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, OwlViTModel

        >>> model = OwlViTModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> inputs = processor(images=image, return_tensors="pt")
        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def forward(self, input_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_base_image_embeds: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, OwlViTOutput]:
        '''
        Returns:

        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, OwlViTModel

        >>> model = OwlViTModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> inputs = processor(text=[["a photo of a cat", "a photo of a dog"]], images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```'''

class OwlViTBoxPredictionHead(nn.Module):
    dense0: Incomplete
    dense1: Incomplete
    gelu: Incomplete
    dense2: Incomplete
    def __init__(self, config: OwlViTConfig) -> None: ...
    def forward(self, image_features: torch.Tensor) -> torch.FloatTensor: ...

class OwlViTClassPredictionHead(nn.Module):
    query_dim: Incomplete
    dense0: Incomplete
    logit_shift: Incomplete
    logit_scale: Incomplete
    elu: Incomplete
    def __init__(self, config: OwlViTConfig) -> None: ...
    def forward(self, image_embeds: torch.FloatTensor, query_embeds: Optional[torch.FloatTensor], query_mask: Optional[torch.Tensor]) -> Tuple[torch.FloatTensor]: ...

class OwlViTForObjectDetection(OwlViTPreTrainedModel):
    config_class = OwlViTConfig
    owlvit: Incomplete
    class_head: Incomplete
    box_head: Incomplete
    layer_norm: Incomplete
    sigmoid: Incomplete
    def __init__(self, config: OwlViTConfig) -> None: ...
    def normalize_grid_corner_coordinates(self, feature_map: torch.FloatTensor): ...
    def compute_box_bias(self, feature_map: torch.FloatTensor) -> torch.FloatTensor: ...
    def box_predictor(self, image_feats: torch.FloatTensor, feature_map: torch.FloatTensor) -> torch.FloatTensor:
        """
        Args:
            image_feats:
                Features extracted from the image, returned by the `image_text_embedder` method.
            feature_map:
                A spatial re-arrangement of image_features, also returned by the `image_text_embedder` method.
        Returns:
            pred_boxes:
                List of predicted boxes (cxcywh normalized to 0, 1) nested within a dictionary.
        """
    def class_predictor(self, image_feats: torch.FloatTensor, query_embeds: Optional[torch.FloatTensor] = None, query_mask: Optional[torch.Tensor] = None) -> Tuple[torch.FloatTensor]:
        """
        Args:
            image_feats:
                Features extracted from the `image_text_embedder`.
            query_embeds:
                Text query embeddings.
            query_mask:
                Must be provided with query_embeddings. A mask indicating which query embeddings are valid.
        """
    def image_text_embedder(self, input_ids: torch.Tensor, pixel_values: torch.FloatTensor, attention_mask: torch.Tensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None) -> Tuple[torch.FloatTensor]: ...
    def image_embedder(self, pixel_values: torch.FloatTensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None) -> Tuple[torch.FloatTensor]: ...
    def embed_image_query(self, query_image_features: torch.FloatTensor, query_feature_map: torch.FloatTensor) -> torch.FloatTensor: ...
    def image_guided_detection(self, pixel_values: torch.FloatTensor, query_pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> OwlViTImageGuidedObjectDetectionOutput:
        '''
        Returns:

        Examples:
        ```python
        >>> import requests
        >>> from PIL import Image
        >>> import torch
        >>> from transformers import AutoProcessor, OwlViTForObjectDetection

        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch16")
        >>> model = OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch16")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> query_url = "http://images.cocodataset.org/val2017/000000001675.jpg"
        >>> query_image = Image.open(requests.get(query_url, stream=True).raw)
        >>> inputs = processor(images=image, query_images=query_image, return_tensors="pt")
        >>> with torch.no_grad():
        ...     outputs = model.image_guided_detection(**inputs)
        >>> # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
        >>> target_sizes = torch.Tensor([image.size[::-1]])
        >>> # Convert outputs (bounding boxes and class logits) to COCO API
        >>> results = processor.post_process_image_guided_detection(
        ...     outputs=outputs, threshold=0.6, nms_threshold=0.3, target_sizes=target_sizes
        ... )
        >>> i = 0  # Retrieve predictions for the first image
        >>> boxes, scores = results[i]["boxes"], results[i]["scores"]
        >>> for box, score in zip(boxes, scores):
        ...     box = [round(i, 2) for i in box.tolist()]
        ...     print(f"Detected similar object with confidence {round(score.item(), 3)} at location {box}")
        Detected similar object with confidence 0.782 at location [-0.06, -1.52, 637.96, 271.16]
        Detected similar object with confidence 1.0 at location [39.64, 71.61, 176.21, 117.15]
        ```'''
    def forward(self, input_ids: torch.Tensor, pixel_values: torch.FloatTensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> OwlViTObjectDetectionOutput:
        '''
        Returns:

        Examples:
        ```python
        >>> import requests
        >>> from PIL import Image
        >>> import torch
        >>> from transformers import AutoProcessor, OwlViTForObjectDetection

        >>> processor = AutoProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> model = OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> texts = [["a photo of a cat", "a photo of a dog"]]
        >>> inputs = processor(text=texts, images=image, return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
        >>> target_sizes = torch.Tensor([image.size[::-1]])
        >>> # Convert outputs (bounding boxes and class logits) to final bounding boxes and scores
        >>> results = processor.post_process_object_detection(
        ...     outputs=outputs, threshold=0.1, target_sizes=target_sizes
        ... )

        >>> i = 0  # Retrieve predictions for the first image for the corresponding text queries
        >>> text = texts[i]
        >>> boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]

        >>> for box, score, label in zip(boxes, scores, labels):
        ...     box = [round(i, 2) for i in box.tolist()]
        ...     print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")
        Detected a photo of a cat with confidence 0.707 at location [324.97, 20.44, 640.58, 373.29]
        Detected a photo of a cat with confidence 0.717 at location [1.46, 55.26, 315.55, 472.17]
        ```'''
