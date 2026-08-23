import abc
from .utils import Constant as Constant
from _typeshed import Incomplete
from abc import abstractmethod
from torch import nn

class AvgPool(nn.Module, metaclass=abc.ABCMeta):
    """
    AvgPool Module.
    """
    def __init__(self) -> None: ...
    @abstractmethod
    def forward(self, input_tensor): ...

class GlobalAvgPool1d(AvgPool):
    """
    GlobalAvgPool1d Module.
    """
    def forward(self, input_tensor): ...

class GlobalAvgPool2d(AvgPool):
    """
    GlobalAvgPool2d Module.
    """
    def forward(self, input_tensor): ...

class GlobalAvgPool3d(AvgPool):
    """
    GlobalAvgPool3d Module.
    """
    def forward(self, input_tensor): ...

class StubLayer:
    """
    StubLayer Module. Base Module.
    """
    input: Incomplete
    output: Incomplete
    weights: Incomplete
    def __init__(self, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    def build(self, shape) -> None:
        """
        build shape.
        """
    def set_weights(self, weights) -> None:
        """
        set weights.
        """
    def import_weights(self, torch_layer) -> None:
        """
        import weights.
        """
    def import_weights_keras(self, keras_layer) -> None:
        """
        import weights from keras layer.
        """
    def export_weights(self, torch_layer) -> None:
        """
        export weights.
        """
    def export_weights_keras(self, keras_layer) -> None:
        """
        export weights to keras layer.
        """
    def get_weights(self):
        """
        get weights.
        """
    def size(self):
        """
        size().
        """
    @property
    def output_shape(self):
        """
        output shape.
        """
    def to_real_layer(self) -> None:
        """
        to real layer.
        """

class StubWeightBiasLayer(StubLayer):
    """
    StubWeightBiasLayer Module to set the bias.
    """
    def import_weights(self, torch_layer) -> None: ...
    def import_weights_keras(self, keras_layer) -> None: ...
    def export_weights(self, torch_layer) -> None: ...
    def export_weights_keras(self, keras_layer) -> None: ...

class StubBatchNormalization(StubWeightBiasLayer, metaclass=abc.ABCMeta):
    """
    StubBatchNormalization Module. Batch Norm.
    """
    num_features: Incomplete
    def __init__(self, num_features, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    def import_weights(self, torch_layer) -> None: ...
    def export_weights(self, torch_layer) -> None: ...
    def size(self): ...
    @abstractmethod
    def to_real_layer(self): ...

class StubBatchNormalization1d(StubBatchNormalization):
    """
    StubBatchNormalization1d Module.
    """
    def to_real_layer(self): ...

class StubBatchNormalization2d(StubBatchNormalization):
    """
    StubBatchNormalization2d Module.
    """
    def to_real_layer(self): ...

class StubBatchNormalization3d(StubBatchNormalization):
    """
    StubBatchNormalization3d Module.
    """
    def to_real_layer(self): ...

class StubDense(StubWeightBiasLayer):
    """
    StubDense Module. Linear.
    """
    input_units: Incomplete
    units: Incomplete
    def __init__(self, input_units, units, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    @property
    def output_shape(self): ...
    def import_weights_keras(self, keras_layer) -> None: ...
    def export_weights_keras(self, keras_layer) -> None: ...
    def size(self): ...
    def to_real_layer(self): ...

class StubConv(StubWeightBiasLayer, metaclass=abc.ABCMeta):
    """
    StubConv Module. Conv.
    """
    input_channel: Incomplete
    filters: Incomplete
    kernel_size: Incomplete
    stride: Incomplete
    padding: Incomplete
    def __init__(self, input_channel, filters, kernel_size, stride: int = 1, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    @property
    def output_shape(self): ...
    def import_weights_keras(self, keras_layer) -> None: ...
    def export_weights_keras(self, keras_layer) -> None: ...
    def size(self): ...
    @abstractmethod
    def to_real_layer(self): ...

class StubConv1d(StubConv):
    """
    StubConv1d Module.
    """
    def to_real_layer(self): ...

class StubConv2d(StubConv):
    """
    StubConv2d Module.
    """
    def to_real_layer(self): ...

class StubConv3d(StubConv):
    """
    StubConv3d Module.
    """
    def to_real_layer(self): ...

class StubAggregateLayer(StubLayer):
    """
    StubAggregateLayer Module.
    """
    def __init__(self, input_nodes: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...

class StubConcatenate(StubAggregateLayer):
    """StubConcatenate Module.
    """
    @property
    def output_shape(self): ...
    def to_real_layer(self): ...

class StubAdd(StubAggregateLayer):
    """
    StubAdd Module.
    """
    @property
    def output_shape(self): ...
    def to_real_layer(self): ...

class StubFlatten(StubLayer):
    """
    StubFlatten Module.
    """
    @property
    def output_shape(self): ...
    def to_real_layer(self): ...

class StubReLU(StubLayer):
    """
    StubReLU Module.
    """
    def to_real_layer(self): ...

class StubSoftmax(StubLayer):
    """
    StubSoftmax Module.
    """
    def to_real_layer(self): ...

class StubDropout(StubLayer, metaclass=abc.ABCMeta):
    """
    StubDropout Module.
    """
    rate: Incomplete
    def __init__(self, rate, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    @abstractmethod
    def to_real_layer(self): ...

class StubDropout1d(StubDropout):
    """
    StubDropout1d Module.
    """
    def to_real_layer(self): ...

class StubDropout2d(StubDropout):
    """
    StubDropout2d Module.
    """
    def to_real_layer(self): ...

class StubDropout3d(StubDropout):
    """
    StubDropout3d Module.
    """
    def to_real_layer(self): ...

class StubInput(StubLayer):
    """
    StubInput Module.
    """
    def __init__(self, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...

class StubPooling(StubLayer, metaclass=abc.ABCMeta):
    """
    StubPooling Module.
    """
    kernel_size: Incomplete
    stride: Incomplete
    padding: Incomplete
    def __init__(self, kernel_size: Incomplete | None = None, stride: Incomplete | None = None, padding: int = 0, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    @property
    def output_shape(self): ...
    @abstractmethod
    def to_real_layer(self): ...

class StubPooling1d(StubPooling):
    """
    StubPooling1d Module.
    """
    def to_real_layer(self): ...

class StubPooling2d(StubPooling):
    """
    StubPooling2d Module.
    """
    def to_real_layer(self): ...

class StubPooling3d(StubPooling):
    """
    StubPooling3d Module.
    """
    def to_real_layer(self): ...

class StubGlobalPooling(StubLayer, metaclass=abc.ABCMeta):
    """
    StubGlobalPooling Module.
    """
    def __init__(self, input_node: Incomplete | None = None, output_node: Incomplete | None = None) -> None: ...
    @property
    def output_shape(self): ...
    @abstractmethod
    def to_real_layer(self): ...

class StubGlobalPooling1d(StubGlobalPooling):
    """
    StubGlobalPooling1d Module.
    """
    def to_real_layer(self): ...

class StubGlobalPooling2d(StubGlobalPooling):
    """
    StubGlobalPooling2d Module.
    """
    def to_real_layer(self): ...

class StubGlobalPooling3d(StubGlobalPooling):
    """
    StubGlobalPooling3d Module.
    """
    def to_real_layer(self): ...

class TorchConcatenate(nn.Module):
    """
    TorchConcatenate Module.
    """
    def forward(self, input_list): ...

class TorchAdd(nn.Module):
    """
    TorchAdd Module.
    """
    def forward(self, input_list): ...

class TorchFlatten(nn.Module):
    """
    TorchFlatten Module.
    """
    def forward(self, input_tensor): ...

def keras_dropout(layer, rate):
    """
    Keras dropout layer.
    """
def to_real_keras_layer(layer):
    """
    Real keras layer.
    """
def is_layer(layer, layer_type):
    """
    Judge the layer type.

    Returns
    -------
    bool
        boolean -- True or False
    """
def layer_description_extractor(layer, node_to_id):
    """
    Get layer description.
    """
def layer_description_builder(layer_information, id_to_node):
    """build layer from description.
    """
def layer_width(layer):
    """
    Get layer width.
    """
def set_torch_weight_to_stub(torch_layer, stub_layer) -> None: ...
def set_keras_weight_to_stub(keras_layer, stub_layer) -> None: ...
def set_stub_weight_to_torch(stub_layer, torch_layer) -> None: ...
def set_stub_weight_to_keras(stub_layer, keras_layer) -> None: ...
def get_conv_class(n_dim): ...
def get_dropout_class(n_dim): ...
def get_global_avg_pooling_class(n_dim): ...
def get_pooling_class(n_dim): ...
def get_batch_norm_class(n_dim): ...
def get_n_dim(layer): ...
