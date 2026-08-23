import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFSemanticSegmenterOutput as TFSemanticSegmenterOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_segformer import SegformerConfig as SegformerConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_SEGFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFSegformerDropPath(tf.keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    References:
        (1) github.com:rwightman/pytorch-image-models
    """
    drop_path: Incomplete
    def __init__(self, drop_path, **kwargs) -> None: ...
    def call(self, x, training: Incomplete | None = None): ...

class TFSegformerOverlapPatchEmbeddings(tf.keras.layers.Layer):
    """Construct the overlapping patch embeddings."""
    padding: Incomplete
    proj: Incomplete
    layer_norm: Incomplete
    def __init__(self, patch_size, stride, hidden_size, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor) -> Tuple[tf.Tensor, int, int]: ...

class TFSegformerEfficientSelfAttention(tf.keras.layers.Layer):
    """SegFormer's efficient self-attention mechanism. Employs the sequence reduction process introduced in the [PvT
    paper](https://arxiv.org/abs/2102.12122)."""
    hidden_size: Incomplete
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    sr_ratio: Incomplete
    sr: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: SegformerConfig, hidden_size: int, num_attention_heads: int, sequence_reduction_ratio: int, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, height: int, width: int, output_attentions: bool = False, training: bool = False) -> Union[tf.Tensor, Tuple[tf.Tensor, tf.Tensor]]: ...

class TFSegformerSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: SegformerConfig, hidden_size: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFSegformerAttention(tf.keras.layers.Layer):
    self: Incomplete
    dense_output: Incomplete
    def __init__(self, config: SegformerConfig, hidden_size: int, num_attention_heads: int, sequence_reduction_ratio: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, height: int, width: int, output_attentions: bool = False) -> Union[tf.Tensor, Tuple[tf.Tensor, tf.Tensor]]: ...

class TFSegformerDWConv(tf.keras.layers.Layer):
    depthwise_convolution: Incomplete
    def __init__(self, dim: int = 768, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, height: int, width: int) -> tf.Tensor: ...

class TFSegformerMixFFN(tf.keras.layers.Layer):
    dense1: Incomplete
    depthwise_convolution: Incomplete
    intermediate_act_fn: Incomplete
    dense2: Incomplete
    dropout: Incomplete
    def __init__(self, config: SegformerConfig, in_features: int, hidden_features: int = None, out_features: int = None, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, height: int, width: int, training: bool = False) -> tf.Tensor: ...

class TFSegformerLayer(tf.keras.layers.Layer):
    """This corresponds to the Block class in the original implementation."""
    layer_norm_1: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layer_norm_2: Incomplete
    mlp: Incomplete
    def __init__(self, config, hidden_size: int, num_attention_heads: int, drop_path: float, sequence_reduction_ratio: int, mlp_ratio: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, height: int, width: int, output_attentions: bool = False, training: bool = False) -> Tuple: ...

class TFSegformerEncoder(tf.keras.layers.Layer):
    config: Incomplete
    embeddings: Incomplete
    block: Incomplete
    layer_norms: Incomplete
    def __init__(self, config: SegformerConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: bool = False) -> Union[Tuple, TFBaseModelOutput]: ...

class TFSegformerMainLayer(tf.keras.layers.Layer):
    config_class = SegformerConfig
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config: SegformerConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple, TFBaseModelOutput]: ...

class TFSegformerPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SegformerConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """

SEGFORMER_START_DOCSTRING: str
SEGFORMER_INPUTS_DOCSTRING: str

class TFSegformerModel(TFSegformerPreTrainedModel):
    config: Incomplete
    segformer: Incomplete
    def __init__(self, config: SegformerConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple, TFBaseModelOutput]: ...
    def serving_output(self, output: TFBaseModelOutput) -> TFBaseModelOutput: ...

class TFSegformerForImageClassification(TFSegformerPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    segformer: Incomplete
    classifier: Incomplete
    def __init__(self, config: SegformerConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TFSequenceClassifierOutput]: ...
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFSegformerMLP(tf.keras.layers.Layer):
    """
    Linear Embedding.
    """
    proj: Incomplete
    def __init__(self, config: SegformerConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFSegformerDecodeHead(TFSegformerPreTrainedModel):
    mlps: Incomplete
    linear_fuse: Incomplete
    batch_norm: Incomplete
    activation: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    config: Incomplete
    def __init__(self, config: SegformerConfig, **kwargs) -> None: ...
    def call(self, encoder_hidden_states, training: bool = False): ...

class TFSegformerForSemanticSegmentation(TFSegformerPreTrainedModel):
    segformer: Incomplete
    decode_head: Incomplete
    def __init__(self, config: SegformerConfig, **kwargs) -> None: ...
    def hf_compute_loss(self, logits, labels): ...
    def call(self, pixel_values: tf.Tensor, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TFSemanticSegmenterOutput]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a (per-pixel) classification loss is computed
            (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFSegformerForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
        >>> model = TFSegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs, training=False)
        >>> # logits are of shape (batch_size, num_labels, height/4, width/4)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 150, 128, 128]
        ```'''
    def serving_output(self, output: TFSemanticSegmenterOutput) -> TFSemanticSegmenterOutput: ...
