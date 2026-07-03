import numpy as np
import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_scipy_available as is_scipy_available, replace_return_docstrings as replace_return_docstrings, requires_backends as requires_backends
from .configuration_oneformer import OneFormerConfig as OneFormerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import Tensor as Tensor, nn
from transformers import AutoBackbone as AutoBackbone
from transformers.utils import logging as logging
from typing import Dict, List, Optional, Tuple

logger: Incomplete
ONEFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def multiscale_deform_attn_core_pytorch(value: Tensor, value_spatial_shapes: Tensor, sampling_locations: Tensor, attention_weights: Tensor) -> Tensor: ...
def dice_loss(inputs: Tensor, labels: Tensor, num_masks: int) -> Tensor:
    """
    Compute the DICE loss, similar to generalized IOU for masks as follows:

    $$ \\mathcal{L}_{\\text{dice}(x, y) = 1 - \\frac{2 * x \\cap y }{x \\cup y + 1}} $$

    In practice, since `labels` is a binary mask, (only 0s and 1s), dice can be computed as follow

    $$ \\mathcal{L}_{\\text{dice}(x, y) = 1 - \\frac{2 * x * y }{x + y + 1}} $$

    Args:
        inputs (`torch.Tensor`):
            A tensor representing a mask.
        labels (`torch.Tensor`):
            A tensor with the same shape as inputs. Stores the binary classification labels for each element in inputs
            (0 for the negative class and 1 for the positive class).
        num_masks (`int`):
            The number of masks present in the current batch, used for normalization.

    Returns:
        `torch.Tensor`: The computed loss.
    """
def sigmoid_cross_entropy_loss(inputs: torch.Tensor, labels: torch.Tensor, num_masks: int) -> torch.Tensor:
    """
    Args:
        inputs (`torch.Tensor`):
            A float tensor of arbitrary shape.
        labels (`torch.Tensor`):
            A tensor with the same shape as inputs. Stores the binary classification labels for each element in inputs
            (0 for the negative class and 1 for the positive class).

    Returns:
        loss (`torch.Tensor`): The computed loss.
    """
def pair_wise_dice_loss(inputs: Tensor, labels: Tensor) -> Tensor:
    """
    A pair wise version of the dice loss, see `dice_loss` for usage.

    Args:
        inputs (`torch.Tensor`):
            A tensor representing a mask
        labels (`torch.Tensor`):
            A tensor with the same shape as inputs. Stores the binary classification labels for each element in inputs
            (0 for the negative class and 1 for the positive class).

    Returns:
        `torch.Tensor`: The computed loss between each pairs.
    """
def pair_wise_sigmoid_cross_entropy_loss(inputs: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    """
    A pair wise version of the cross entropy loss, see `sigmoid_cross_entropy_loss` for usage.

    Args:
        inputs (`torch.Tensor`):
            A tensor representing a mask.
        labels (`torch.Tensor`):
            A tensor with the same shape as inputs. Stores the binary classification labels for each element in inputs
            (0 for the negative class and 1 for the positive class).

    Returns:
        loss (`torch.Tensor`): The computed loss between each pairs.
    """
def sample_point(input_features: torch.Tensor, point_coordinates: torch.Tensor, add_dim: bool = False, **kwargs) -> torch.Tensor:
    """
    A wrapper around `torch.nn.functional.grid_sample` to support 3D point_coordinates tensors.

    Args:
        input_features (`torch.Tensor` of shape (batch_size, channels, height, width)):
            A tensor that contains features map on a height * width grid
        point_coordinates (`torch.Tensor` of shape (batch_size, num_points, 2) or (batch_size, grid_height, grid_width,:
        2)):
            A tensor that contains [0, 1] * [0, 1] normalized point coordinates
        add_dim (`bool`):
            boolean value to keep track of added dimension

    Returns:
        point_features (`torch.Tensor` of shape (batch_size, channels, num_points) or (batch_size, channels,
        height_grid, width_grid):
            A tensor that contains features for points in `point_coordinates`.
    """

class OneFormerHungarianMatcher(nn.Module):
    cost_class: Incomplete
    cost_mask: Incomplete
    cost_dice: Incomplete
    num_points: Incomplete
    def __init__(self, cost_class: float = 1.0, cost_mask: float = 1.0, cost_dice: float = 1.0, num_points: int = 12544) -> None:
        """This class computes an assignment between the labels and the predictions of the network.

        For efficiency reasons, the labels don't include the no_object. Because of this, in general, there are more
        predictions than labels. In this case, we do a 1-to-1 matching of the best predictions, while the others are
        un-matched (and thus treated as non-objects).

        Params:
            cost_class (float, *optional*, defaults to 1.0):
                This is the relative weight of the classification error in the matching cost.
            cost_mask (float, *optional*,  defaults to 1.0):
                This is the relative weight of the sigmoid ce loss of the binary mask in the matching cost.
            cost_dice (float, *optional*, defaults to 1.0):
                This is the relative weight of the dice loss of the binary mask in the matching cost
            num_points (int, *optional*, defaults to 12544):
                Number of points to be sampled for dice and mask loss matching cost.
        """
    def forward(self, masks_queries_logits, class_queries_logits, mask_labels, class_labels) -> List[Tuple[Tensor]]:
        """Performs the matching

        Params:
            masks_queries_logits (`torch.Tensor`):
                A tensor` of dim `batch_size, num_queries, num_labels` with the
                  classification logits.
            class_queries_logits (`torch.Tensor`):
                A tensor` of dim `batch_size, num_queries, height, width` with the
                  predicted masks.

            class_labels (`torch.Tensor`):
                A tensor` of dim `num_target_boxes` (where num_target_boxes is the number
                  of ground-truth objects in the target) containing the class labels.
            mask_labels (`torch.Tensor`):
                A tensor` of dim `num_target_boxes, height, width` containing the target
                  masks.

        Returns:
            `List[Tuple[Tensor]]`: A list of size batch_size, containing tuples of (index_i, index_j) where:
                - index_i is the indices of the selected predictions (in order)
                - index_j is the indices of the corresponding selected labels (in order)
            For each batch element, it holds:
                len(index_i) = len(index_j) = min(num_queries, num_targets).
        """

class OneFormerLoss(nn.Module):
    num_classes: Incomplete
    matcher: Incomplete
    weight_dict: Incomplete
    eos_coef: Incomplete
    num_points: Incomplete
    oversample_ratio: Incomplete
    importance_sample_ratio: Incomplete
    contrastive_temperature: Incomplete
    logit_scale: Incomplete
    def __init__(self, num_classes: int, matcher: OneFormerHungarianMatcher, weight_dict: Dict[str, float], eos_coef: float, num_points: int, oversample_ratio: float, importance_sample_ratio: float, contrastive_temperature: float = None) -> None:
        """
        This class computes the losses using the class predictions, mask predictions and the contrastive queries.

        Oneformer calculates the classification CE loss on the class predictions. Mask predictions are used for
        calculating the binary CE loss and dice loss. The contrastive queries are used for calculating the contrastive
        loss.

        Args:
            num_labels (`int`):
                The number of classes.
            matcher (`OneFormerHungarianMatcher`):
                A torch module that computes the assigments between the predictions and labels.
            weight_dict (`Dict[str, float]`):
                A dictionary of weights to be applied to the different losses.
            eos_coef (`float`):
                Weight to apply to the null class.
            num_points (`int`):
                Number of points to be sampled for dice and mask loss calculations.
            oversample_ratio (`float`):
                Required for pointwise loss calculation.
            importance_sample_ratio (`float`):
                Required for pointwise loss calculation.
            contrastive_temperature (`float`):
                Temperature for scaling the contrastive logits.
        """
    def loss_contrastive(self, contrastive_queries_logits: Tensor, text_queries: Tensor):
        """Compute the query-text contrastive loss.

        Args:
            contrastive_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, hidden_dim`
            text_queries (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, hidden_dim`
        Returns:
            `Dict[str, Tensor]`: A dict of `torch.Tensor` containing the following key:
            - **loss_contrastive** -- The query-text contrastive loss computed using task-guided queries
                                    and text queries derived from input text list.
        """
    def loss_labels(self, class_queries_logits: Tensor, class_labels: List[Tensor], indices: Tuple[np.array]) -> Dict[str, Tensor]:
        """Compute the losses related to the labels using cross entropy.

        Args:
            class_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, num_labels`
            class_labels (`List[torch.Tensor]`):
                List of class labels of shape `(labels)`.
            indices (`Tuple[np.array])`:
                The indices computed by the Hungarian matcher.

        Returns:
            `Dict[str, Tensor]`: A dict of `torch.Tensor` containing the following key:
            - **loss_cross_entropy** -- The loss computed using cross entropy on the predicted and ground truth labels.
        """
    def loss_masks(self, masks_queries_logits: Tensor, mask_labels: List[Tensor], indices: Tuple[np.array], num_masks: int) -> Dict[str, Tensor]:
        """Compute the losses related to the masks using focal and dice loss.

        Args:
            masks_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, height, width`
            mask_labels (`torch.Tensor`):
                List of mask labels of shape `(labels, height, width)`.
            indices (`Tuple[np.array])`:
                The indices computed by the Hungarian matcher.
            num_masks (`int)`:
                The number of masks, used for normalization.

        Returns:
            `Dict[str, Tensor]`: A dict of `torch.Tensor` containing two keys:
            - **loss_mask** -- The loss computed using sigmoid ce loss on the predicted and ground truth masks.
            - **loss_dice** -- The loss computed using dice loss on the predicted on the predicted and ground truth
              masks.
        """
    def calculate_uncertainty(self, logits: torch.Tensor) -> torch.Tensor:
        """
        In Mask2Former paper, uncertainty is estimated as L1 distance between 0.0 and the logit prediction in 'logits'
        for the foreground class in `classes`.

        Args:
            logits (`torch.Tensor`):
            A tensor of shape (R, 1, ...) for class-specific or class-agnostic, where R is the total number of predicted masks in all images and C is:
            the number of foreground classes. The values are logits.

        Returns:
            scores (`torch.Tensor`): A tensor of shape (R, 1, ...) that contains uncertainty scores with the most
            uncertain locations having the highest uncertainty score.
        """
    def sample_points_using_uncertainty(self, logits: torch.Tensor, uncertainty_function, num_points: int, oversample_ratio: int, importance_sample_ratio: float) -> torch.Tensor:
        """
        This function is meant for sampling points in [0, 1] * [0, 1] coordinate space based on their uncertainty. The
        uncertainty is calculated for each point using the passed `uncertainty function` that takes points logit
        prediction as input.

        Args:
            logits (`float`):
                Logit predictions for P points.
            uncertainty_function:
                A function that takes logit predictions for P points and returns their uncertainties.
            num_points (`int`):
                The number of points P to sample.
            oversample_ratio (`int`):
                Oversampling parameter.
            importance_sample_ratio (`float`):
                Ratio of points that are sampled via importance sampling.

        Returns:
            point_coordinates (`torch.Tensor`):
                Coordinates for P sampled points.
        """
    def forward(self, masks_queries_logits: Tensor, class_queries_logits: Tensor, contrastive_queries_logits: Tensor, mask_labels: List[Tensor], class_labels: List[Tensor], text_queries: Tensor, auxiliary_predictions: Optional[Dict[str, Tensor]] = None, calculate_contrastive_loss: bool = True) -> Dict[str, Tensor]:
        """
        This performs the loss computation.

        Args:
            masks_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, height, width`
            class_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, num_labels`
            contrastive_queries_logits (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, hidden_dim`
            mask_labels (`torch.Tensor`):
                List of mask labels of shape `(labels, height, width)`.
            class_labels (`List[torch.Tensor]`):
                List of class labels of shape `(labels)`.
            text_queries (`torch.Tensor`):
                A tensor of shape `batch_size, num_queries, hidden_dim`
            auxiliary_predictions (`Dict[str, torch.Tensor]`, *optional*):
                if `use_auxiliary_loss` was set to `true` in [`OneFormerConfig`], then it contains the logits from the
                inner layers of the Detr's Decoder.
            calculate_contrastive_loss (`bool`, *optional*, defaults to `True`):
                Whether or not to calculate the contrastive loss.

        Returns:
            `Dict[str, Tensor]`: A dict of `torch.Tensor` containing two keys:
            - **loss_cross_entropy** -- The loss computed using cross entropy on the predicted and ground truth labels.
            - **loss_mask** -- The loss computed using sigmoid ce loss on the predicted and ground truth masks.
            - **loss_dice** -- The loss computed using dice loss on the predicted on the predicted and ground truth
              masks.
            - **loss_contrastive** -- The query-text contrstive loss computed using object and text queries.
            if `use_auxiliary_loss` was set to `true` in [`OneFormerConfig`], the dictionary contains addional losses
            for each auxiliary predictions.
        """
    def get_num_masks(self, class_labels: torch.Tensor, device: torch.device) -> torch.Tensor:
        """
        Computes the average number of target masks across the batch, for normalization purposes.
        """

@dataclass
class OneFormerTransformerDecoderOutput(BaseModelOutput):
    """
    Base class for outputs of the Transformer decoder. This class adds attributes for class predictions, mask
    predictions and contrastive logits to BaseModelOutputWithCrossAttentions.

    Args:
        object_logits (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`):
            Queries representation for the region proposals.
        contrastive_logits (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`):
            Queries representation for the contrastive loss.
        prediction_masks (`torch.FloatTensor` of shape `(batch_size, num_queries, height, width)`):
            Mask predictions from last layer of the transformer decoder.
        prediction_class (`torch.FloatTensor` of shape `(batch_size, num_queries, num_classes+1)`):
            Class predictions from last layer of the transformer decoder.
        auxiliary_predictions (Tuple of Dict of `str, torch.FloatTensor`, *optional*):
            Tuple of class and mask predictions from each layer of the transformer decoder.
    """
    object_queries: torch.FloatTensor = ...
    contrastive_logits: Optional[torch.FloatTensor] = ...
    prediction_masks: torch.FloatTensor = ...
    prediction_class: torch.FloatTensor = ...
    auxiliary_predictions: Optional[Tuple[Dict[str, torch.FloatTensor]]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, object_queries, contrastive_logits, prediction_masks, prediction_class, auxiliary_predictions) -> None: ...

@dataclass
class OneFormerPixelDecoderOutput(ModelOutput):
    """
    OneFormer's pixel decoder module output, practically a Multi-Scale Deformable Attention based decoder. It returns
    the mask features and the multiscale features.

    Args:
        multi_scale_features (`tuple(torch.FloatTensor)`):
            Tuple of multi-scale features of scales [1/8, 1/16, 1/32] and shape `(batch_size, num_channels, height,
            width)`from the Multi-Scale Deformable Attenntion based Pixel Decoder.
        mask_features (`torch.FloatTensor`):
            Tensor of shape `(batch_size, num_channels, height, width)`, 1/4 scale features from the last Pixel Decoder
            Layer.
        attentions (`tuple(torch.FloatTensor)`, *optional*):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights from pixel decoder. Returned when `output_attentions=True` is passed
            or when `config.output_attentions=True`
    """
    multi_scale_features: Tuple[torch.FloatTensor] = ...
    mask_features: torch.FloatTensor = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, multi_scale_features, mask_features, attentions) -> None: ...

@dataclass
class OneFormerPixelLevelModuleOutput(ModelOutput):
    """
    OneFormer's pixel level module output. It returns both the last and (optionally) the hidden states from the
    `encoder` and `decoder`. By default, the `encoder` is a Swin/Dinat Backbone and the `decoder` is a Multi-Scale
    Deformable Attention based decoder.

    Args:
        encoder_features (List of `(torch.FloatTensor)`):
            List of `torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`. Hidden-states (also
            called feature maps) of the model at the output of each stage.
        decoder_features (List of `(torch.FloatTensor)`):
            List of `torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`. Hidden-states (also
            called feature maps) of the model at the output of each stage.
        decoder_last_feature (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)):
            1/4 scale features from the last Pixel Decoder Layer.
    """
    encoder_features: List[torch.FloatTensor] = ...
    decoder_features: List[torch.FloatTensor] = ...
    decoder_last_feature: torch.FloatTensor = ...
    def __init__(self, encoder_features, decoder_features, decoder_last_feature) -> None: ...

@dataclass
class OneFormerModelOutput(ModelOutput):
    """
    Class for outputs of [`OneFormerModel`]. This class returns all the needed hidden states to compute the logits.

    Args:
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, num_channels, height, width)`. Hidden-states (also called feature maps) of the encoder
            model at the output of each stage.
        pixel_decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, num_channels, height, width)`. Hidden-states (also called feature maps) of the pixel
            decoder model at the output of each stage.
        transformer_decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states (also called feature maps) of the
            transformer decoder at the output of each stage.
        transformer_decoder_object_queries (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`)
            Output object queries from the last layer in the transformer decoder.
        transformer_decoder_contrastive_queries (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`)
            Contrastive queries from the transformer decoder.
        transformer_decoder_mask_predictions (`torch.FloatTensor` of shape `(batch_size, num_queries, height, width)`)
            Mask Predictions from the last layer in the transformer decoder.
        transformer_decoder_class_predictions (`torch.FloatTensor` of shape `(batch_size, num_queries, num_classes+1)`):
            Class Predictions from the last layer in the transformer decoder.
        transformer_decoder_auxiliary_predictions (Tuple of Dict of `str, torch.FloatTensor`, *optional*):
            Tuple of class and mask predictions from each layer of the transformer decoder.
        text_queries (`torch.FloatTensor`, *optional* of shape `(batch_size, num_queries, hidden_dim)`)
            Text queries derived from the input text list used for calculating contrastive loss during training.
        task_token (`torch.FloatTensor` of shape `(batch_size, hidden_dim)`)
            1D task token to condition the queries.
        attentions (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tuple(torch.FloatTensor)` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Self and Cross Attentions weights from transformer decoder.
    """
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    pixel_decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    transformer_decoder_hidden_states: Optional[torch.FloatTensor] = ...
    transformer_decoder_object_queries: torch.FloatTensor = ...
    transformer_decoder_contrastive_queries: Optional[torch.FloatTensor] = ...
    transformer_decoder_mask_predictions: torch.FloatTensor = ...
    transformer_decoder_class_predictions: torch.FloatTensor = ...
    transformer_decoder_auxiliary_predictions: Optional[Tuple[Dict[str, torch.FloatTensor]]] = ...
    text_queries: Optional[torch.FloatTensor] = ...
    task_token: torch.FloatTensor = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, encoder_hidden_states, pixel_decoder_hidden_states, transformer_decoder_hidden_states, transformer_decoder_object_queries, transformer_decoder_contrastive_queries, transformer_decoder_mask_predictions, transformer_decoder_class_predictions, transformer_decoder_auxiliary_predictions, text_queries, task_token, attentions) -> None: ...

@dataclass
class OneFormerForUniversalSegmentationOutput(ModelOutput):
    """
    Class for outputs of [`OneFormerForUniversalSegmentationOutput`].

    This output can be directly passed to [`~OneFormerImageProcessor.post_process_semantic_segmentation`] or
    [`~OneFormerImageProcessor.post_process_instance_segmentation`] or
    [`~OneFormerImageProcessor.post_process_panoptic_segmentation`] depending on the task. Please, see
    [`~OneFormerImageProcessor] for details regarding usage.

    Args:
        loss (`torch.Tensor`, *optional*):
            The computed loss, returned when labels are present.
        class_queries_logits (`torch.FloatTensor`):
            A tensor of shape `(batch_size, num_queries, num_labels + 1)` representing the proposed classes for each
            query. Note the `+ 1` is needed because we incorporate the null class.
        masks_queries_logits (`torch.FloatTensor`):
            A tensor of shape `(batch_size, num_queries, height, width)` representing the proposed masks for each
            query.
        auxiliary_predictions (List of Dict of `str, torch.FloatTensor`, *optional*):
            List of class and mask predictions from each layer of the transformer decoder.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, num_channels, height, width)`. Hidden-states (also called feature maps) of the encoder
            model at the output of each stage.
        pixel_decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, num_channels, height, width)`. Hidden-states (also called feature maps) of the pixel
            decoder model at the output of each stage.
        transformer_decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states (also called feature maps) of the
            transformer decoder at the output of each stage.
        transformer_decoder_object_queries (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`)
            Output object queries from the last layer in the transformer decoder.
        transformer_decoder_contrastive_queries (`torch.FloatTensor` of shape `(batch_size, num_queries, hidden_dim)`)
            Contrastive queries from the transformer decoder.
        transformer_decoder_mask_predictions (`torch.FloatTensor` of shape `(batch_size, num_queries, height, width)`)
            Mask Predictions from the last layer in the transformer decoder.
        transformer_decoder_class_predictions (`torch.FloatTensor` of shape `(batch_size, num_queries, num_classes+1)`):
            Class Predictions from the last layer in the transformer decoder.
        transformer_decoder_auxiliary_predictions (List of Dict of `str, torch.FloatTensor`, *optional*):
            List of class and mask predictions from each layer of the transformer decoder.
        text_queries (`torch.FloatTensor`, *optional* of shape `(batch_size, num_queries, hidden_dim)`)
            Text queries derived from the input text list used for calculating contrastive loss during training.
        task_token (`torch.FloatTensor` of shape `(batch_size, hidden_dim)`)
            1D task token to condition the queries.
        attentions (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tuple(torch.FloatTensor)` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Self and Cross Attentions weights from transformer decoder.
    """
    loss: Optional[torch.FloatTensor] = ...
    class_queries_logits: torch.FloatTensor = ...
    masks_queries_logits: torch.FloatTensor = ...
    auxiliary_predictions: List[Dict[str, torch.FloatTensor]] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    pixel_decoder_hidden_states: Optional[List[torch.FloatTensor]] = ...
    transformer_decoder_hidden_states: Optional[torch.FloatTensor] = ...
    transformer_decoder_object_queries: torch.FloatTensor = ...
    transformer_decoder_contrastive_queries: Optional[torch.FloatTensor] = ...
    transformer_decoder_mask_predictions: torch.FloatTensor = ...
    transformer_decoder_class_predictions: torch.FloatTensor = ...
    transformer_decoder_auxiliary_predictions: Optional[List[Dict[str, torch.FloatTensor]]] = ...
    text_queries: Optional[torch.FloatTensor] = ...
    task_token: torch.FloatTensor = ...
    attentions: Optional[Tuple[Tuple[torch.FloatTensor]]] = ...
    def __init__(self, loss, class_queries_logits, masks_queries_logits, auxiliary_predictions, encoder_hidden_states, pixel_decoder_hidden_states, transformer_decoder_hidden_states, transformer_decoder_object_queries, transformer_decoder_contrastive_queries, transformer_decoder_mask_predictions, transformer_decoder_class_predictions, transformer_decoder_auxiliary_predictions, text_queries, task_token, attentions) -> None: ...

class OneFormerPixelDecoderFrozenBatchNorm2d(nn.Module):
    """
    BatchNorm2d where the batch statistics and the affine parameters are fixed.

    Copy-paste from torchvision.misc.ops with added eps before rqsrt, without which any other models than
    torchvision.models.resnet[18,34,50,101] produce nans.
    """
    def __init__(self, n) -> None: ...
    def forward(self, x): ...

class OneFormerPixelDecoderEncoderMultiscaleDeformableAttention(nn.Module):
    """
    Multiscale deformable attention as proposed in Deformable DETR.
    """
    im2col_step: int
    d_model: Incomplete
    n_levels: Incomplete
    n_heads: Incomplete
    n_points: Incomplete
    sampling_offsets: Incomplete
    attention_weights: Incomplete
    value_proj: Incomplete
    output_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, n_levels: int, n_points: int) -> None: ...
    def with_pos_embed(self, tensor: torch.Tensor, position_embeddings: Optional[Tensor]): ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, position_embeddings: Optional[torch.Tensor] = None, reference_points: Incomplete | None = None, spatial_shapes: Incomplete | None = None, level_start_index: Incomplete | None = None, output_attentions: bool = False): ...

class OneFormerPixelDecoderEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    is_training: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, position_embeddings: torch.Tensor = None, reference_points: Incomplete | None = None, spatial_shapes: Incomplete | None = None, level_start_index: Incomplete | None = None, output_attentions: bool = False):
        """
        Args:
            hidden_states (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Input to the layer.
            attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
                Attention mask.
            position_embeddings (`torch.FloatTensor`, *optional*):
                Position embeddings, to be added to `hidden_states`.
            reference_points (`torch.FloatTensor`, *optional*):
                Reference points.
            spatial_shapes (`torch.LongTensor`, *optional*):
                Spatial shapes of the backbone feature maps.
            level_start_index (`torch.LongTensor`, *optional*):
                Level start index.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class OneFormerPixelDecoderEncoderOnly(nn.Module):
    """
    Transformer encoder consisting of *config.encoder_layers* deformable attention layers. Each layer is a
    [`OneFormerPixelDecoderEncoderLayer`].

    The encoder updates the flattened multi-scale feature maps through multiple deformable attention layers.

    Args:
        config: OneFormerConfig
    """
    config: Incomplete
    dropout: Incomplete
    layers: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    @staticmethod
    def get_reference_points(spatial_shapes, valid_ratios, device):
        """
        Get reference points for each feature map. Used in decoder.

        Args:
            spatial_shapes (`torch.LongTensor` of shape `(num_feature_levels, 2)`):
                Spatial shapes of each feature map.
            valid_ratios (`torch.FloatTensor` of shape `(batch_size, num_feature_levels, 2)`):
                Valid ratios of each feature map.
            device (`torch.device`):
                Device on which to create the tensors.
        Returns:
            `torch.FloatTensor` of shape `(batch_size, num_queries, num_feature_levels, 2)`
        """
    def forward(self, inputs_embeds: Incomplete | None = None, attention_mask: Incomplete | None = None, position_embeddings: Incomplete | None = None, spatial_shapes: Incomplete | None = None, level_start_index: Incomplete | None = None, valid_ratios: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None):
        """
        Args:
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Flattened feature map (output of the backbone + projection layer) that is passed to the encoder.
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding pixel features. Mask values selected in `[0, 1]`:
                - 1 for pixel features that are real (i.e. **not masked**),
                - 0 for pixel features that are padding (i.e. **masked**).
                [What are attention masks?](../glossary#attention-mask)
            position_embeddings (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Position embeddings that are added to the queries and keys in each self-attention layer.
            spatial_shapes (`torch.LongTensor` of shape `(num_feature_levels, 2)`):
                Spatial shapes of each feature map.
            level_start_index (`torch.LongTensor` of shape `(num_feature_levels)`):
                Starting index of each feature map.
            valid_ratios (`torch.FloatTensor` of shape `(batch_size, num_feature_levels, 2)`):
                Ratio of valid area in each feature level.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~file_utils.ModelOutput`] instead of a plain tuple.
        """

class OneFormerPixelDecoder(nn.Module):
    config: Incomplete
    position_embedding: Incomplete
    num_feature_levels: int
    transformer_feature_strides: Incomplete
    feature_channels: Incomplete
    level_embed: Incomplete
    input_projections: Incomplete
    encoder: Incomplete
    mask_projection: Incomplete
    common_stride: Incomplete
    num_fpn_levels: Incomplete
    lateral_convs: Incomplete
    output_convs: Incomplete
    def __init__(self, config: OneFormerConfig, feature_channels) -> None: ...
    def get_valid_ratio(self, mask):
        """Get the valid ratio of all feature maps."""
    def forward(self, features, encoder_outputs: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class OneFormerPixelLevelModule(nn.Module):
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: OneFormerConfig) -> None:
        """
        Pixel Level Module proposed in [Masked-attention Mask Transformer for Universal Image
        Segmentation](https://arxiv.org/abs/2112.01527). It runs the input image through a backbone and a pixel
        decoder, generating multi-scale feature maps and pixel embeddings.

        Args:
            config ([`OneFormerConfig`]):
                The configuration used to instantiate this model.
        """
    def forward(self, pixel_values: Tensor, output_hidden_states: bool = False) -> OneFormerPixelLevelModuleOutput: ...

class OneFormerAttention(nn.Module):
    """
    Multi-headed attention from 'Attention Is All You Need' paper. Here, we add position embeddings to the queries and
    keys (as explained in the DETR paper).
    """
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, is_decoder: bool = False, bias: bool = True) -> None: ...
    def with_pos_embed(self, tensor: torch.Tensor, position_embeddings: Optional[Tensor]): ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, position_embeddings: Optional[torch.Tensor] = None, key_value_states: Optional[torch.Tensor] = None, key_value_position_embeddings: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class OneFormerTransformerDecoderSelfAttentionLayer(nn.Module):
    self_attn: Incomplete
    norm: Incomplete
    dropout: Incomplete
    activation: Incomplete
    normalize_before: Incomplete
    def __init__(self, embed_dim, num_heads, dropout: float = 0.0, activation: str = 'relu', normalize_before: bool = False) -> None: ...
    def with_pos_embed(self, tensor, pos: Optional[Tensor]): ...
    def forward_post(self, output, output_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward_pre(self, output, output_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward(self, output, output_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...

class OneFormerTransformerDecoderCrossAttentionLayer(nn.Module):
    multihead_attn: Incomplete
    norm: Incomplete
    dropout: Incomplete
    activation: Incomplete
    normalize_before: Incomplete
    def __init__(self, embed_dim, num_heads, dropout: float = 0.0, activation: str = 'relu', normalize_before: bool = False) -> None: ...
    def with_pos_embed(self, tensor, pos: Optional[Tensor]): ...
    def forward_post(self, output, memory, memory_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward_pre(self, output, memory, memory_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward(self, output, memory, memory_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...

class OneFormerTransformerDecoderFFNLayer(nn.Module):
    linear1: Incomplete
    dropout: Incomplete
    linear2: Incomplete
    norm: Incomplete
    activation: Incomplete
    normalize_before: Incomplete
    def __init__(self, d_model, dim_feedforward: int = 2048, dropout: float = 0.0, activation: str = 'relu', normalize_before: bool = False) -> None: ...
    def with_pos_embed(self, tensor, pos: Optional[Tensor]): ...
    def forward_post(self, output): ...
    def forward_pre(self, output): ...
    def forward(self, output): ...

class OneFormerMLPPredictionHead(nn.Module):
    layers: Incomplete
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_layers: int = 3) -> None:
        """
        A classic Multi Layer Perceptron (MLP).

        Args:
            input_dim (`int`):
                The input dimensions.
            hidden_dim (`int`):
                The hidden dimensions.
            output_dim (`int`):
                The output dimensions.
            num_layers (int, *optional*, defaults to 3):
                The number of layers.
        """
    def forward(self, input: Tensor) -> Tensor: ...

class OneFormerTransformerDecoderLayer(nn.Module):
    embed_dim: Incomplete
    num_feature_levels: int
    cross_attn: Incomplete
    self_attn: Incomplete
    ffn: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def forward(self, index: int, output: torch.Tensor, multi_stage_features: List[torch.Tensor], multi_stage_positional_embeddings: List[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, query_embeddings: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False):
        """
        Args:
            index (`int`): index of the layer in the Transformer decoder.
            output (`torch.FloatTensor`): the object queries of shape `(N, batch, hidden_dim)`
            multi_stage_features (`List[torch.Tensor]`): the multi-scale features from the pixel decoder.
            multi_stage_positional_embeddings (`List[torch.Tensor]`):
                positional embeddings for the multi_stage_features
            attention_mask (`torch.FloatTensor`): attention mask for the masked cross attention layer
            query_embeddings (`torch.FloatTensor`, *optional*):
                position embeddings that are added to the queries and keys in the self-attention layer.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class OneFormerTransformerDecoderQueryTransformerDecoder(nn.Module):
    layers: Incomplete
    num_layers: Incomplete
    norm: Incomplete
    return_intermediate: Incomplete
    def __init__(self, decoder_layer, num_layers, norm: Incomplete | None = None, return_intermediate: bool = False) -> None: ...
    def forward(self, output, memory, output_mask: Optional[Tensor] = None, memory_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...

class OneFormerTransformerDecoderQueryTransformerDecoderLayer(nn.Module):
    self_attn: Incomplete
    multihead_attn: Incomplete
    linear1: Incomplete
    dropout: Incomplete
    linear2: Incomplete
    norm1: Incomplete
    norm2: Incomplete
    norm3: Incomplete
    dropout1: Incomplete
    dropout2: Incomplete
    dropout3: Incomplete
    activation: Incomplete
    normalize_before: Incomplete
    def __init__(self, d_model, nhead, dim_feedforward: int = 2048, dropout: float = 0.1, activation: str = 'relu', normalize_before: bool = False) -> None: ...
    def with_pos_embed(self, tensor, pos: Optional[Tensor]): ...
    def forward_post(self, output, memory, output_mask: Optional[Tensor] = None, memory_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward_pre(self, output, memory, output_mask: Optional[Tensor] = None, memory_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...
    def forward(self, output, memory, output_mask: Optional[Tensor] = None, memory_mask: Optional[Tensor] = None, output_key_padding_mask: Optional[Tensor] = None, memory_key_padding_mask: Optional[Tensor] = None, pos: Optional[Tensor] = None, query_pos: Optional[Tensor] = None): ...

class OneFormerTransformerDecoderQueryTransformer(nn.Module):
    decoder: Incomplete
    d_model: Incomplete
    nhead: Incomplete
    def __init__(self, d_model: int = 512, nhead: int = 8, num_decoder_layers: int = 6, dim_feedforward: int = 2048, dropout: float = 0.1, activation: str = 'relu', normalize_before: bool = False, return_intermediate_dec: bool = False) -> None: ...
    def forward(self, src, mask, query_embed, pos_embed, task_token: Incomplete | None = None): ...

class OneFormerTransformerDecoder(nn.Module):
    """
    Transformer decoder
    """
    config: Incomplete
    dropout: Incomplete
    num_heads: Incomplete
    is_training: Incomplete
    use_task_norm: Incomplete
    use_auxiliary_loss: Incomplete
    query_transformer: Incomplete
    decoder_norm: Incomplete
    num_feature_levels: int
    layers: Incomplete
    query_input_projection: Incomplete
    class_embed: Incomplete
    mask_embed: Incomplete
    def __init__(self, in_channels: int, config: OneFormerConfig) -> None: ...
    def forward(self, task_token: Incomplete | None = None, multi_stage_features: Incomplete | None = None, multi_stage_positional_embeddings: Incomplete | None = None, mask_features: Incomplete | None = None, query_features: Incomplete | None = None, query_embeddings: Incomplete | None = None, query_embedder: Incomplete | None = None, size_list: Incomplete | None = None, output_attentions: Incomplete | None = None): ...
    def forward_prediction_heads(self, output, mask_features, attention_mask_target_size): ...

class OneFormerTransformerModule(nn.Module):
    """
    The OneFormer's transformer module.
    """
    num_feature_levels: int
    position_embedder: Incomplete
    queries_embedder: Incomplete
    input_projections: Incomplete
    decoder: Incomplete
    level_embed: Incomplete
    def __init__(self, in_features: int, config: OneFormerConfig) -> None: ...
    def forward(self, multi_scale_features: List[Tensor], mask_features: Tensor, task_token: Tensor, output_attentions: bool = False) -> OneFormerTransformerDecoderOutput: ...

class OneFormerSinePositionEmbedding(nn.Module):
    """
    This is a more standard version of the position embedding, very similar to the one used by the Attention is all you
    need paper, generalized to work on images.
    """
    num_pos_feats: Incomplete
    temperature: Incomplete
    normalize: Incomplete
    scale: Incomplete
    def __init__(self, num_pos_feats: int = 64, temperature: int = 10000, normalize: bool = False, scale: Optional[float] = None) -> None: ...
    def forward(self, x: Tensor, mask: Optional[Tensor] = None) -> Tensor: ...

class PredictionBlock(nn.Module):
    layers: Incomplete
    def __init__(self, in_dim: int, out_dim: int, activation: nn.Module) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class OneFormerTextMapperAttention(nn.Module):
    num_heads: Incomplete
    scale: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    attn_drop: Incomplete
    proj: Incomplete
    proj_drop: Incomplete
    def __init__(self, dim, num_heads: int = 8, qkv_bias: bool = False, qk_scale: Incomplete | None = None, attn_drop: float = 0.0, proj_drop: float = 0.0) -> None: ...
    def forward(self, q, k, v): ...

class OneFormerTextTransformerDecoderLayer(nn.Module):
    self_attn: Incomplete
    cross_attn: Incomplete
    norm1: Incomplete
    norm2: Incomplete
    norm3: Incomplete
    dropout: Incomplete
    mlp: Incomplete
    def __init__(self, d_model, nhead, dropout: float = 0.1) -> None: ...
    def forward(self, hidden_state, mem): ...

class OneFormerTextContextDecoder(nn.Module):
    memory_proj: Incomplete
    text_proj: Incomplete
    decoder: Incomplete
    out_proj: Incomplete
    def __init__(self, transformer_width: int = 256, transformer_heads: int = 4, transformer_layers: int = 6, visual_dim: int = 1024, dropout: float = 0.1, **kwargs) -> None: ...
    def forward(self, text, visual): ...

class OneFormerTextMLP(nn.Module):
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, hidden_size: Optional[int] = None, intermediate_size: Optional[int] = None, output_size: Optional[int] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class OneFormerTextTransformerLayer(nn.Module):
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    attn_mask: Incomplete
    def __init__(self, width: int, heads: int, attn_mask: torch.Tensor) -> None: ...
    def forward(self, hidden_states: torch.Tensor, key_padding_mask: Optional[torch.Tensor] = None) -> torch.FloatTensor: ...

class OneFormerTextTransformer(nn.Module):
    width: Incomplete
    num_layers: Incomplete
    layers: Incomplete
    use_checkpoint: Incomplete
    def __init__(self, width: int, layers: int, heads: int, attn_mask: torch.Tensor = None, use_checkpoint: bool = False) -> None: ...
    def forward(self, hidden_states: torch.Tensor): ...

class OneFormerTextEncoder(nn.Module):
    context_length: Incomplete
    width: Incomplete
    transformer: Incomplete
    positional_embedding: Incomplete
    ln_final: Incomplete
    token_embedding: Incomplete
    def __init__(self, context_length: int, width: int, layers: int, vocab_size, use_checkpoint: bool = False) -> None: ...
    def build_attention_mask(self): ...
    def forward(self, text): ...

class OneFormerTextMapper(nn.Module):
    text_encoder: Incomplete
    text_projector: Incomplete
    prompt_ctx: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def forward(self, inputs: Tensor) -> Tensor: ...
    def encode_text(self, text): ...

class OneFormerTaskModel(nn.Module):
    task_mlp: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def forward(self, inputs: Tensor) -> Tensor: ...

ONEFORMER_START_DOCSTRING: str
ONEFORMER_INPUTS_DOCSTRING: str

class OneFormerPreTrainedModel(PreTrainedModel):
    config_class = OneFormerConfig
    base_model_prefix: str
    main_input_name: str

class OneFormerModel(OneFormerPreTrainedModel):
    main_input_name: Incomplete
    pixel_level_module: Incomplete
    transformer_module: Incomplete
    task_encoder: Incomplete
    is_training: Incomplete
    text_mapper: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def forward(self, pixel_values: Tensor, task_inputs: Tensor, text_inputs: Optional[Tensor] = None, pixel_mask: Optional[Tensor] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> OneFormerModelOutput:
        '''
        Returns:
            `OneFormerModelOutput`
        Example:

        ```python
        >>> import torch
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import OneFormerProcessor, OneFormerModel

        >>> # download texting image
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> # load processor for preprocessing the inputs
        >>> processor = OneFormerProcessor.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")
        >>> model = OneFormerModel.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")
        >>> inputs = processor(image, ["semantic"], return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)

        >>> mask_predictions = outputs.transformer_decoder_mask_predictions
        >>> class_predictions = outputs.transformer_decoder_class_predictions

        >>> f"👉 Mask Predictions Shape: {list(mask_predictions.shape)}, Class Predictions Shape: {list(class_predictions.shape)}"
        \'👉 Mask Predictions Shape: [1, 150, 128, 171], Class Predictions Shape: [1, 150, 151]\'
        ```'''

class OneFormerForUniversalSegmentation(OneFormerPreTrainedModel):
    main_input_name: Incomplete
    model: Incomplete
    matcher: Incomplete
    weight_dict: Incomplete
    criterion: Incomplete
    def __init__(self, config: OneFormerConfig) -> None: ...
    def get_loss_dict(self, masks_queries_logits: Tensor, class_queries_logits: Tensor, contrastive_queries_logits: Tensor, mask_labels: Tensor, class_labels: Tensor, text_queries: Tensor, auxiliary_predictions: Dict[str, Tensor], calculate_contrastive_loss: bool) -> Dict[str, Tensor]: ...
    def get_loss(self, loss_dict: Dict[str, Tensor]) -> Tensor: ...
    def forward(self, pixel_values: Tensor, task_inputs: Tensor, text_inputs: Optional[Tensor] = None, mask_labels: Optional[List[Tensor]] = None, class_labels: Optional[List[Tensor]] = None, pixel_mask: Optional[Tensor] = None, output_auxiliary_logits: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> OneFormerForUniversalSegmentationOutput:
        '''
        text_inputs (`List[torch.Tensor]`, *optional*):
            Tensor fof shape `(num_queries, sequence_length)` to be fed to a model
        mask_labels (`List[torch.Tensor]`, *optional*):
            List of mask labels of shape `(num_labels, height, width)` to be fed to a model
        class_labels (`List[torch.LongTensor]`, *optional*):
            list of target class labels of shape `(num_labels, height, width)` to be fed to a model. They identify the
            labels of `mask_labels`, e.g. the label of `mask_labels[i][j]` if `class_labels[i][j]`.

        Returns:
            `OneFormerUniversalSegmentationOutput`
        Example:

        Universal segmentation example:

        ```python
        >>> from transformers import OneFormerProcessor, OneFormerForUniversalSegmentation
        >>> from PIL import Image
        >>> import requests
        >>> import torch

        >>> # load OneFormer fine-tuned on ADE20k for universal segmentation
        >>> processor = OneFormerProcessor.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")
        >>> model = OneFormerForUniversalSegmentation.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")

        >>> url = (
        ...     "https://huggingface.co/datasets/hf-internal-testing/fixtures_ade20k/resolve/main/ADE_val_00000001.jpg"
        ... )
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> # Semantic Segmentation
        >>> inputs = processor(image, ["semantic"], return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        >>> # model predicts class_queries_logits of shape `(batch_size, num_queries)`
        >>> # and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
        >>> class_queries_logits = outputs.class_queries_logits
        >>> masks_queries_logits = outputs.masks_queries_logits

        >>> # you can pass them to processor for semantic postprocessing
        >>> predicted_semantic_map = processor.post_process_semantic_segmentation(
        ...     outputs, target_sizes=[image.size[::-1]]
        ... )[0]
        >>> f"👉 Semantic Predictions Shape: {list(predicted_semantic_map.shape)}"
        \'👉 Semantic Predictions Shape: [512, 683]\'

        >>> # Instance Segmentation
        >>> inputs = processor(image, ["instance"], return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        >>> # model predicts class_queries_logits of shape `(batch_size, num_queries)`
        >>> # and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
        >>> class_queries_logits = outputs.class_queries_logits
        >>> masks_queries_logits = outputs.masks_queries_logits

        >>> # you can pass them to processor for instance postprocessing
        >>> predicted_instance_map = processor.post_process_instance_segmentation(
        ...     outputs, target_sizes=[image.size[::-1]]
        ... )[0]["segmentation"]
        >>> f"👉 Instance Predictions Shape: {list(predicted_instance_map.shape)}"
        \'👉 Instance Predictions Shape: [512, 683]\'

        >>> # Panoptic Segmentation
        >>> inputs = processor(image, ["panoptic"], return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        >>> # model predicts class_queries_logits of shape `(batch_size, num_queries)`
        >>> # and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
        >>> class_queries_logits = outputs.class_queries_logits
        >>> masks_queries_logits = outputs.masks_queries_logits

        >>> # you can pass them to processor for panoptic postprocessing
        >>> predicted_panoptic_map = processor.post_process_panoptic_segmentation(
        ...     outputs, target_sizes=[image.size[::-1]]
        ... )[0]["segmentation"]
        >>> f"👉 Panoptic Predictions Shape: {list(predicted_panoptic_map.shape)}"
        \'👉 Panoptic Predictions Shape: [512, 683]\'
        ```
        '''
