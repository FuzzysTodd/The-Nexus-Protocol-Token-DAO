import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_scipy_available as is_scipy_available, is_vision_available as is_vision_available, logging as logging, replace_return_docstrings as replace_return_docstrings, requires_backends as requires_backends
from .configuration_yolos import YolosConfig as YolosConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import Tensor as Tensor, nn
from transformers.image_transforms import center_to_corners_format as center_to_corners_format
from typing import Dict, List, Optional, Set, Tuple, Union

logger: Incomplete
YOLOS_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class YolosObjectDetectionOutput(ModelOutput):
    """
    Output type of [`YolosForObjectDetection`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` are provided)):
            Total loss as a linear combination of a negative log-likehood (cross-entropy) for class prediction and a
            bounding box loss. The latter is defined as a linear combination of the L1 loss and the generalized
            scale-invariant IoU loss.
        loss_dict (`Dict`, *optional*):
            A dictionary containing the individual losses. Useful for logging.
        logits (`torch.FloatTensor` of shape `(batch_size, num_queries, num_classes + 1)`):
            Classification logits (including no-object) for all queries.
        pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_queries, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual image in the batch (disregarding
            possible padding). You can use [`~YolosImageProcessor.post_process`] to retrieve the unnormalized bounding
            boxes.
        auxiliary_outputs (`list[Dict]`, *optional*):
            Optional, only returned when auxilary losses are activated (i.e. `config.auxiliary_loss` is set to `True`)
            and labels are provided. It is a list of dictionaries containing the two above keys (`logits` and
            `pred_boxes`) for each decoder layer.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the decoder of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of
            the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    loss_dict: Optional[Dict] = ...
    logits: torch.FloatTensor = ...
    pred_boxes: torch.FloatTensor = ...
    auxiliary_outputs: Optional[List[Dict]] = ...
    last_hidden_state: Optional[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, loss_dict, logits, pred_boxes, auxiliary_outputs, last_hidden_state, hidden_states, attentions) -> None: ...

class YolosEmbeddings(nn.Module):
    """
    Construct the CLS token, detection tokens, position and patch embeddings.

    """
    cls_token: Incomplete
    detection_tokens: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    interpolation: Incomplete
    config: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class InterpolateInitialPositionEmbeddings(nn.Module):
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pos_embed, img_size=(800, 1344)) -> torch.Tensor: ...

class InterpolateMidPositionEmbeddings(nn.Module):
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pos_embed, img_size=(800, 1344)) -> torch.Tensor: ...

class YolosPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class YolosSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class YolosSelfOutput(nn.Module):
    """
    The residual connection is defined in YolosLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class YolosAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def prune_heads(self, heads: Set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class YolosIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class YolosOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class YolosLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class YolosEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    mid_position_embeddings: Incomplete
    interpolation: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, height, width, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class YolosPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = YolosConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

YOLOS_START_DOCSTRING: str
YOLOS_INPUTS_DOCSTRING: str

class YolosModel(YolosPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: YolosConfig, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self) -> YolosPatchEmbeddings: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]: ...

class YolosPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, hidden_states): ...

class YolosForObjectDetection(YolosPreTrainedModel):
    vit: Incomplete
    class_labels_classifier: Incomplete
    bbox_predictor: Incomplete
    def __init__(self, config: YolosConfig) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, labels: Optional[List[Dict]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, YolosObjectDetectionOutput]:
        '''
        labels (`List[Dict]` of len `(batch_size,)`, *optional*):
            Labels for computing the bipartite matching loss. List of dicts, each dictionary containing at least the
            following 2 keys: `\'class_labels\'` and `\'boxes\'` (the class labels and bounding boxes of an image in the
            batch respectively). The class labels themselves should be a `torch.LongTensor` of len `(number of bounding
            boxes in the image,)` and the boxes a `torch.FloatTensor` of shape `(number of bounding boxes in the image,
            4)`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, AutoModelForObjectDetection
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("hustvl/yolos-tiny")
        >>> model = AutoModelForObjectDetection.from_pretrained("hustvl/yolos-tiny")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> # convert outputs (bounding boxes and class logits) to COCO API
        >>> target_sizes = torch.tensor([image.size[::-1]])
        >>> results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[
        ...     0
        ... ]

        >>> for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        ...     box = [round(i, 2) for i in box.tolist()]
        ...     print(
        ...         f"Detected {model.config.id2label[label.item()]} with confidence "
        ...         f"{round(score.item(), 3)} at location {box}"
        ...     )
        Detected remote with confidence 0.994 at location [46.96, 72.61, 181.02, 119.73]
        Detected remote with confidence 0.975 at location [340.66, 79.19, 372.59, 192.65]
        Detected cat with confidence 0.984 at location [12.27, 54.25, 319.42, 470.99]
        Detected remote with confidence 0.922 at location [41.66, 71.96, 178.7, 120.33]
        Detected cat with confidence 0.914 at location [342.34, 21.48, 638.64, 372.46]
        ```'''

def dice_loss(inputs, targets, num_boxes):
    """
    Compute the DICE loss, similar to generalized IOU for masks

    Args:
        inputs: A float tensor of arbitrary shape.
                The predictions for each example.
        targets: A float tensor with the same shape as inputs. Stores the binary
                 classification label for each element in inputs (0 for the negative class and 1 for the positive
                 class).
    """
def sigmoid_focal_loss(inputs, targets, num_boxes, alpha: float = 0.25, gamma: float = 2):
    """
    Loss used in RetinaNet for dense detection: https://arxiv.org/abs/1708.02002.

    Args:
        inputs (`torch.FloatTensor` of arbitrary shape):
            The predictions for each example.
        targets (`torch.FloatTensor` with the same shape as `inputs`)
            A tensor storing the binary classification label for each element in the `inputs` (0 for the negative class
            and 1 for the positive class).
        alpha (`float`, *optional*, defaults to `0.25`):
            Optional weighting factor in the range (0,1) to balance positive vs. negative examples.
        gamma (`int`, *optional*, defaults to `2`):
            Exponent of the modulating factor (1 - p_t) to balance easy vs hard examples.

    Returns:
        Loss tensor
    """

class YolosLoss(nn.Module):
    '''
    This class computes the losses for YolosForObjectDetection/YolosForSegmentation. The process happens in two steps:
    1) we compute hungarian assignment between ground truth boxes and the outputs of the model 2) we supervise each
    pair of matched ground-truth / prediction (supervise class and box).

    A note on the `num_classes` argument (copied from original repo in detr.py): "the naming of the `num_classes`
    parameter of the criterion is somewhat misleading. It indeed corresponds to `max_obj_id` + 1, where `max_obj_id` is
    the maximum id for a class in your dataset. For example, COCO has a `max_obj_id` of 90, so we pass `num_classes` to
    be 91. As another example, for a dataset that has a single class with `id` 1, you should pass `num_classes` to be 2
    (`max_obj_id` + 1). For more details on this, check the following discussion
    https://github.com/facebookresearch/detr/issues/108#issuecomment-650269223"


    Args:
        matcher (`YolosHungarianMatcher`):
            Module able to compute a matching between targets and proposals.
        num_classes (`int`):
            Number of object categories, omitting the special no-object category.
        eos_coef (`float`):
            Relative classification weight applied to the no-object category.
        losses (`List[str]`):
            List of all the losses to be applied. See `get_loss` for a list of all available losses.
    '''
    matcher: Incomplete
    num_classes: Incomplete
    eos_coef: Incomplete
    losses: Incomplete
    def __init__(self, matcher, num_classes, eos_coef, losses) -> None: ...
    def loss_labels(self, outputs, targets, indices, num_boxes):
        '''
        Classification loss (NLL) targets dicts must contain the key "class_labels" containing a tensor of dim
        [nb_target_boxes]
        '''
    def loss_cardinality(self, outputs, targets, indices, num_boxes):
        """
        Compute the cardinality error, i.e. the absolute error in the number of predicted non-empty boxes.

        This is not really a loss, it is intended for logging purposes only. It doesn't propagate gradients.
        """
    def loss_boxes(self, outputs, targets, indices, num_boxes):
        '''
        Compute the losses related to the bounding boxes, the L1 regression loss and the GIoU loss.

        Targets dicts must contain the key "boxes" containing a tensor of dim [nb_target_boxes, 4]. The target boxes
        are expected in format (center_x, center_y, w, h), normalized by the image size.
        '''
    def loss_masks(self, outputs, targets, indices, num_boxes):
        '''
        Compute the losses related to the masks: the focal loss and the dice loss.

        Targets dicts must contain the key "masks" containing a tensor of dim [nb_target_boxes, h, w].
        '''
    def get_loss(self, loss, outputs, targets, indices, num_boxes): ...
    def forward(self, outputs, targets):
        """
        This performs the loss computation.

        Args:
             outputs (`dict`, *optional*):
                Dictionary of tensors, see the output specification of the model for the format.
             targets (`List[dict]`, *optional*):
                List of dicts, such that `len(targets) == batch_size`. The expected keys in each dict depends on the
                losses applied, see each loss' doc.
        """

class YolosMLPPredictionHead(nn.Module):
    """
    Very simple multi-layer perceptron (MLP, also called FFN), used to predict the normalized center coordinates,
    height and width of a bounding box w.r.t. an image.

    Copied from https://github.com/facebookresearch/detr/blob/master/models/detr.py

    """
    num_layers: Incomplete
    layers: Incomplete
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers) -> None: ...
    def forward(self, x): ...

class YolosHungarianMatcher(nn.Module):
    """
    This class computes an assignment between the targets and the predictions of the network.

    For efficiency reasons, the targets don't include the no_object. Because of this, in general, there are more
    predictions than targets. In this case, we do a 1-to-1 matching of the best predictions, while the others are
    un-matched (and thus treated as non-objects).

    Args:
        class_cost:
            The relative weight of the classification error in the matching cost.
        bbox_cost:
            The relative weight of the L1 error of the bounding box coordinates in the matching cost.
        giou_cost:
            The relative weight of the giou loss of the bounding box in the matching cost.
    """
    class_cost: Incomplete
    bbox_cost: Incomplete
    giou_cost: Incomplete
    def __init__(self, class_cost: float = 1, bbox_cost: float = 1, giou_cost: float = 1) -> None: ...
    def forward(self, outputs, targets):
        '''
        Args:
            outputs (`dict`):
                A dictionary that contains at least these entries:
                * "logits": Tensor of dim [batch_size, num_queries, num_classes] with the classification logits
                * "pred_boxes": Tensor of dim [batch_size, num_queries, 4] with the predicted box coordinates.
            targets (`List[dict]`):
                A list of targets (len(targets) = batch_size), where each target is a dict containing:
                * "class_labels": Tensor of dim [num_target_boxes] (where num_target_boxes is the number of
                  ground-truth
                 objects in the target) containing the class labels
                * "boxes": Tensor of dim [num_target_boxes, 4] containing the target box coordinates.

        Returns:
            `List[Tuple]`: A list of size `batch_size`, containing tuples of (index_i, index_j) where:
            - index_i is the indices of the selected predictions (in order)
            - index_j is the indices of the corresponding selected targets (in order)
            For each batch element, it holds: len(index_i) = len(index_j) = min(num_queries, num_target_boxes)
        '''

def box_area(boxes: Tensor) -> Tensor:
    """
    Computes the area of a set of bounding boxes, which are specified by its (x1, y1, x2, y2) coordinates.

    Args:
        boxes (`torch.FloatTensor` of shape `(number_of_boxes, 4)`):
            Boxes for which the area will be computed. They are expected to be in (x1, y1, x2, y2) format with `0 <= x1
            < x2` and `0 <= y1 < y2`.

    Returns:
        `torch.FloatTensor`: a tensor containing the area for each box.
    """
def box_iou(boxes1, boxes2): ...
def generalized_box_iou(boxes1, boxes2):
    """
    Generalized IoU from https://giou.stanford.edu/. The boxes should be in [x0, y0, x1, y1] (corner) format.

    Returns:
        `torch.FloatTensor`: a [N, M] pairwise matrix, where N = len(boxes1) and M = len(boxes2)
    """

class NestedTensor:
    tensors: Incomplete
    mask: Incomplete
    def __init__(self, tensors, mask: Optional[Tensor]) -> None: ...
    def to(self, device): ...
    def decompose(self): ...

def nested_tensor_from_tensor_list(tensor_list: List[Tensor]): ...
