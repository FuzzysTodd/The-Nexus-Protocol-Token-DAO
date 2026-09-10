import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFSemanticSegmenterOutput as TFSemanticSegmenterOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_data2vec_vision import Data2VecVisionConfig as Data2VecVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from transformers.tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from typing import Dict, List, Optional, Tuple, Union

logger: Incomplete
TF_DATA2VEC_VISION_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFData2VecVisionModelOutputWithPooling(TFBaseModelOutputWithPooling):
    """
    Class for outputs of [`TFData2VecVisionModel`].

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`tf.Tensor` of shape `(batch_size, hidden_size)`):
            Average of the last layer hidden states of the patch tokens (excluding the *[CLS]* token) if
            *config.use_mean_pooling* is set to True. If set to False, then the final hidden state of the *[CLS]* token
            will be returned.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    last_hidden_state: tf.Tensor = ...
    pooler_output: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions) -> None: ...

class TFData2VecVisionDropPath(tf.keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    References:
        (1) github.com:rwightman/pytorch-image-models
    """
    drop_path: Incomplete
    def __init__(self, drop_path, **kwargs) -> None: ...
    def call(self, x, training: Incomplete | None = None): ...

class TFData2VecVisionEmbeddings(tf.keras.layers.Layer):
    """
    Construct the CLS token, position and patch embeddings. Optionally, also the mask token.

    """
    config: Incomplete
    patch_embeddings: Incomplete
    num_patches: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    cls_token: Incomplete
    mask_token: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, pixel_values: tf.Tensor, bool_masked_pos: Optional[tf.Tensor] = None) -> tf.Tensor: ...

class TFData2VecVisionPatchEmbeddings(tf.keras.layers.Layer):
    """
    Image to Patch Embedding.
    """
    config: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    patch_shape: Incomplete
    num_channels: Incomplete
    projection: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFData2VecVisionSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    relative_position_bias: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, relative_position_bias: Optional['TFData2VecVisionRelativePositionBias'] = None, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFData2VecVisionSelfOutput(tf.keras.layers.Layer):
    """
    The residual connection is defined in TFData2VecVisionLayer instead of here (as is the case with other models), due
    to the layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, gamma: Incomplete | None = None, training: bool = False) -> tf.Tensor: ...

class TFData2VecVisionAttention(tf.keras.layers.Layer):
    attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, relative_position_bias: Optional['TFData2VecVisionRelativePositionBias'] = None, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFData2VecVisionIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFData2VecVisionOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFData2VecVisionLayer(tf.keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    config: Incomplete
    attention: Incomplete
    intermediate: Incomplete
    data2vec_output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    drop_path: Incomplete
    init_values: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None, drop_path_rate: float = 0.0, **kwargs) -> None: ...
    lambda_1: Incomplete
    lambda_2: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, relative_position_bias: Optional['TFData2VecVisionRelativePositionBias'] = None, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFData2VecVisionRelativePositionBias(tf.keras.layers.Layer):
    config: Incomplete
    window_size: Incomplete
    num_relative_distance: Incomplete
    relative_position_index: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple, **kwargs) -> None: ...
    relative_position_bias_table: Incomplete
    def build(self, input_shape) -> None: ...
    def get_position_index(self): ...
    def call(self, inputs: Incomplete | None = None) -> tf.Tensor: ...

class TFData2VecVisionEncoder(tf.keras.layers.Layer):
    config: Incomplete
    relative_position_bias: Incomplete
    layer: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, TFBaseModelOutput]: ...

class TFData2VecVisionMainLayer(tf.keras.layers.Layer):
    config_class = Data2VecVisionConfig
    config: Incomplete
    add_pooling_layer: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: Data2VecVisionConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tuple, TFData2VecVisionModelOutputWithPooling]: ...

class TFData2VecVisionPooler(tf.keras.layers.Layer):
    layernorm: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFData2VecVisionPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = Data2VecVisionConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network. Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """

DATA2VEC_VISION_START_DOCSTRING: str
DATA2VEC_VISION_INPUTS_DOCSTRING: str

class TFData2VecVisionModel(TFData2VecVisionPreTrainedModel):
    config: Incomplete
    data2vec_vision: Incomplete
    def __init__(self, config: Data2VecVisionConfig, add_pooling_layer: bool = False, *inputs, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tuple, TFData2VecVisionModelOutputWithPooling]: ...
    def serving_output(self, output: TFData2VecVisionModelOutputWithPooling) -> TFData2VecVisionModelOutputWithPooling: ...

class TFData2VecVisionForImageClassification(TFData2VecVisionPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    data2vec_vision: Incomplete
    classifier: Incomplete
    def __init__(self, config: Data2VecVisionConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, tuple]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFData2VecVisionConvModule(tf.keras.layers.Layer):
    """
    A convolutional block that bundles conv/norm/activation layers. This block simplifies the usage of convolution
    layers, which are commonly used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    conv: Incomplete
    bn: Incomplete
    activation: Incomplete
    def __init__(self, out_channels: int, kernel_size: Union[int, Tuple[int, int]], padding: str = 'valid', bias: bool = False, dilation: Union[int, Tuple[int, int]] = 1, **kwargs) -> None: ...
    def call(self, input: tf.Tensor) -> tf.Tensor: ...

class TFAdaptiveAvgPool1D(tf.keras.layers.Layer):
    output_dim: Incomplete
    mode: Incomplete
    map: Incomplete
    def __init__(self, output_dim, mode: str = 'dense', **kwargs) -> None: ...
    def build(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class TFAdaptiveAvgPool2D(tf.keras.layers.Layer):
    mode: Incomplete
    h_pool: Incomplete
    w_pool: Incomplete
    def __init__(self, output_shape, mode: str = 'dense', **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class TFData2VecVisionPyramidPoolingModule(tf.keras.layers.Layer):
    """
    Pyramid Pooling Module (PPM) used in PSPNet.

    Args:
        pool_scales (tuple[int]): Pooling scales used in Pooling Pyramid
            Module.
        channels (int): Channels after modules, before conv_seg.

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    pool_scales: Incomplete
    channels: Incomplete
    layer_list: Incomplete
    def __init__(self, pool_scales: Tuple[int, ...], channels: int, **kwargs) -> None: ...
    def call(self, x: tf.Tensor) -> List[tf.Tensor]: ...

class TFData2VecVisionUperHead(tf.keras.layers.Layer):
    """
    Unified Perceptual Parsing for Scene Understanding. This head is the implementation of
    [UPerNet](https://arxiv.org/abs/1807.10221).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    pool_scales: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    classifier: Incomplete
    psp_modules: Incomplete
    bottleneck: Incomplete
    lateral_convs: Incomplete
    fpn_convs: Incomplete
    fpn_bottleneck: Incomplete
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def psp_forward(self, inputs): ...
    def call(self, encoder_hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFData2VecVisionFCNHead(tf.keras.layers.Layer):
    """
    Fully Convolution Networks for Semantic Segmentation. This head is implemented from
    [FCNNet](https://arxiv.org/abs/1411.4038).

    Args:
        config (Data2VecVisionConfig): Configuration.
        kernel_size (int): The kernel size for convs in the head. Default: 3.
        dilation (int): The dilation rate for convs in the head. Default: 1.


    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    in_channels: Incomplete
    channels: Incomplete
    num_convs: Incomplete
    concat_input: Incomplete
    in_index: Incomplete
    convs: Incomplete
    conv_cat: Incomplete
    classifier: Incomplete
    def __init__(self, config: Data2VecVisionConfig, in_index: int = 2, kernel_size: int = 3, dilation: Union[int, Tuple[int, int]] = 1, **kwargs) -> None: ...
    def call(self, encoder_hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFData2VecVisionForSemanticSegmentation(TFData2VecVisionPreTrainedModel):
    num_labels: Incomplete
    data2vec_vision: Incomplete
    fpn1: Incomplete
    fpn2: Incomplete
    fpn3: Incomplete
    fpn4: Incomplete
    decode_head: Incomplete
    auxiliary_head: Incomplete
    def __init__(self, config: Data2VecVisionConfig, *inputs, **kwargs) -> None: ...
    def compute_loss(self, logits, auxiliary_logits, labels): ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, TFSemanticSegmenterOutput]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFData2VecVisionForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/data2vec-vision-base")
        >>> model = TFData2VecVisionForSemanticSegmentation.from_pretrained("facebook/data2vec-vision-base")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFSemanticSegmenterOutput) -> TFSemanticSegmenterOutput: ...
