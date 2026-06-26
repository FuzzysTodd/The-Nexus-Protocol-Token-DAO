import torch
from . import default_layers as default_layers
from _typeshed import Incomplete
from nni.common.graph_utils import build_module_graph as build_module_graph
from nni.compression.pytorch.quantization.literal import BN_FOLD_OP as BN_FOLD_OP, BN_FOLD_TAG as BN_FOLD_TAG, QuantType as QuantType
from nni.compression.pytorch.quantization.observers import RecordingObserver as RecordingObserver

class LayerInfo:
    module: Incomplete
    name: Incomplete
    type: Incomplete
    def __init__(self, name, module) -> None: ...

class Compressor:
    """
    Abstract base PyTorch compressor
    """
    bound_model: Incomplete
    config_list: Incomplete
    optimizer: Incomplete
    modules_to_compress: Incomplete
    modules_wrapper: Incomplete
    is_wrapped: bool
    def __init__(self, model, config_list, optimizer: Incomplete | None = None) -> None:
        """
        Record necessary info in class members

        Parameters
        ----------
        model : pytorch model
            the model user wants to compress
        config_list : list
            the configurations that users specify for compression
        optimizer: pytorch optimizer
            optimizer used to train the model
        """
    def validate_config(self, model, config_list) -> None:
        """
        subclass can optionally implement this method to check if config_list if valid
        """
    def reset(self, checkpoint: Incomplete | None = None) -> None:
        """
        reset model state dict and model wrapper
        """
    def compress(self):
        """
        Compress the model with algorithm implemented by subclass.

        The model will be instrumented and user should never edit it after calling this method.
        `self.modules_to_compress` records all the to-be-compressed layers

        Returns
        -------
        torch.nn.Module
            model with specified modules compressed.
        """
    def set_wrappers_attribute(self, name, value) -> None:
        """
        To register attributes used in wrapped module's forward method.
        If the type of the value is Torch.tensor, then this value is registered as a buffer in wrapper,
        which will be saved by model.state_dict. Otherwise, this value is just a regular variable in wrapper.

        Parameters
        ----------
        name : str
            name of the variable
        value: any
            value of the variable
        """
    def get_modules_to_compress(self):
        """
        To obtain all the to-be-compressed modules.

        Returns
        -------
        list
            a list of the layers, each of which is a tuple (`layer`, `config`),
            `layer` is `LayerInfo`, `config` is a `dict`
        """
    def get_modules_wrapper(self):
        """
        To obtain all the wrapped modules.

        Returns
        -------
        list
            a list of the wrapped modules
        """
    def select_config(self, layer):
        """
        Find the configuration for `layer` by parsing `self.config_list`

        Parameters
        ----------
        layer : LayerInfo
            one layer

        Returns
        -------
        config or None
            the retrieved configuration for this layer, if None, this layer should
            not be compressed
        """
    def update_epoch(self, epoch) -> None:
        """
        If user want to update model every epoch, user can override this method.
        This method should be called at the beginning of each epoch

        Parameters
        ----------
        epoch : num
            the current epoch number
        """
    def add_activation_collector(self, collector): ...
    def remove_activation_collector(self, fwd_hook_id) -> None: ...
    def patch_optimizer(self, *tasks): ...
    def patch_optimizer_before(self, *tasks): ...

class PrunerModuleWrapper(torch.nn.Module):
    module: Incomplete
    name: Incomplete
    type: Incomplete
    config: Incomplete
    pruner: Incomplete
    def __init__(self, module, module_name, module_type, config, pruner) -> None:
        """
        Wrap a module to enable data parallel, forward method customization and buffer registeration.

        Parameters
        ----------
        module : pytorch module
            the module user wants to compress
        config : dict
            the configurations that users specify for compression
        module_name : str
            the name of the module to compress, wrapper module shares same name
        module_type : str
            the type of the module to compress
        pruner ： Pruner
            the pruner used to calculate mask
        """
    def forward(self, *inputs): ...

class Pruner(Compressor):
    """
    Prune to an exact pruning level specification

    Attributes
    ----------
    mask_dict : dict
        Dictionary for saving masks, `key` should be layer name and
        `value` should be a tensor which has the same shape with layer's weight

    """
    def __init__(self, model, config_list, optimizer: Incomplete | None = None) -> None: ...
    def compress(self): ...
    def update_mask(self) -> None: ...
    def calc_mask(self, wrapper, **kwargs) -> None:
        """
        Pruners should overload this method to provide mask for weight tensors.
        The mask must have the same shape and type comparing to the weight.
        It will be applied with `mul()` operation on the weight.
        This method is effectively hooked to `forward()` method of the model.

        Parameters
        ----------
        wrapper : Module
            calculate mask for `wrapper.module`'s weight
        """
    def export_model(self, model_path, mask_path: Incomplete | None = None, onnx_path: Incomplete | None = None, input_shape: Incomplete | None = None, device: Incomplete | None = None, dummy_input: Incomplete | None = None, opset_version: Incomplete | None = None) -> None:
        """
        Export pruned model weights, masks and onnx model(optional)

        Parameters
        ----------
        model_path : str
            path to save pruned model state_dict
        mask_path : str
            (optional) path to save mask dict
        onnx_path : str
            (optional) path to save onnx model
        input_shape : list or tuple
            input shape to onnx model, used for creating a dummy input tensor for torch.onnx.export
            if the input has a complex structure (e.g., a tuple), please directly create the input and
            pass it to dummy_input instead
            note: this argument is deprecated and will be removed; please use dummy_input instead
        device : torch.device
            device of the model, where to place the dummy input tensor for exporting onnx file;
            the tensor is placed on cpu if ```device``` is None
            only useful when both onnx_path and input_shape are passed
            note: this argument is deprecated and will be removed; please use dummy_input instead
        dummy_input: torch.Tensor or tuple
            dummy input to the onnx model; used when input_shape is not enough to specify dummy input
            user should ensure that the dummy_input is on the same device as the model
        opset_version: int
            opset_version parameter for torch.onnx.export; only useful when onnx_path is not None
            if not passed, torch.onnx.export will use its default opset_version
        """
    def load_model_state_dict(self, model_state) -> None:
        """
        Load the state dict saved from unwrapped model.

        Parameters
        ----------
        model_state : dict
            state dict saved from unwrapped model
        """
    def get_pruned_weights(self, dim: int = 0) -> None:
        """
        Log the simulated prune sparsity.

        Parameters
        ----------
        dim : int
            the pruned dim.
        """

class QuantizerModuleWrapper(torch.nn.Module):
    module: Incomplete
    name: Incomplete
    type: Incomplete
    config: Incomplete
    quantizer: Incomplete
    bn_module: Incomplete
    def __init__(self, module, module_name, module_type, config, quantizer, bn_module: Incomplete | None = None) -> None:
        """
        Wrap a module to enable data parallel, forward method customization and buffer registeration.

        Parameters
        ----------
        module : pytorch module
            the module user wants to compress
        config : dict
            the configurations that users specify for compression
        module_name : str
            the name of the module to compress, wrapper module shares same name
        module_type : str
            the type of the module to compress
        quantizer ：quantizer
            the quantizer used to calculate mask
        bn_module : torch.nn.Module
            batch norm layer corresponding to current module, used for simulating batch normalization folding
        """
    def forward(self, *inputs): ...

class QuantizerIdentityWrapper(torch.nn.Module):
    module: Incomplete
    module_name: Incomplete
    def __init__(self, module, module_name) -> None:
        """
        Used to wrap modules that should be treated as torch.Identity

        Parameters
        ----------
        module : pytorch module
            the module to be wrapped
        module_name : str
            the name of the module to wrapped, wrapper module shares same name
        """
    def forward(self, x): ...

class Quantizer(Compressor):
    """
    Base quantizer for pytorch quantizer
    """
    identity_wrappers: Incomplete
    conv_bn_patterns: Incomplete
    all_shapes: Incomplete
    quant_grad: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None, dummy_input: Incomplete | None = None) -> None: ...
    def quantize_weight(self, wrapper, **kwargs) -> None:
        """
        quantize should overload this method to quantize weight.
        This method is effectively hooked to :meth:`forward` of the model.

        Parameters
        ----------
        wrapper : QuantizerModuleWrapper
            the wrapper for origin module
        """
    def quantize_output(self, output, wrapper, **kwargs) -> None:
        """
        quantize should overload this method to quantize output.
        This method is effectively hooked to :meth:`forward` of the model.

        Parameters
        ----------
        output : Tensor
            output that needs to be quantized
        wrapper : QuantizerModuleWrapper
            the wrapper for origin module
        """
    def quantize_input(self, inputs, wrapper, **kwargs) -> None:
        """
        quantize should overload this method to quantize input.
        This method is effectively hooked to :meth:`forward` of the model.

        Parameters
        ----------
        inputs : Tensor
            inputs that needs to be quantized
        wrapper : QuantizerModuleWrapper
            the wrapper for origin module
        """
    def fold_bn(self, *inputs, wrapper):
        """
        Simulate batch normalization folding in the training graph. Folded weight and bias are
        returned for the following operations.

        Parameters
        ----------
        inputs : tuple of torch.Tensor
            inputs for the module
        wrapper : QuantizerModuleWrapper
            the wrapper for origin module

        Returns
        -------
        Tuple of torch.Tensor
        """
    def export_model_save(self, model, model_path, calibration_config: Incomplete | None = None, calibration_path: Incomplete | None = None, onnx_path: Incomplete | None = None, input_shape: Incomplete | None = None, device: Incomplete | None = None) -> None:
        """
        This method helps save pytorch model, calibration config, onnx model in quantizer.

        Parameters
        ----------
        model : pytorch model
            pytorch model to be saved
        model_path : str
            path to save pytorch
        calibration_config: dict
            (optional) config of calibration parameters
        calibration_path : str
            (optional) path to save quantize parameters after calibration
        onnx_path : str
            (optional) path to save onnx model
        input_shape : list or tuple
            input shape to onnx model
        device : torch.device
            device of the model, used to place the dummy input tensor for exporting onnx file.
            the tensor is placed on cpu if ```device``` is None
        """
    def export_model(self, model_path, calibration_path: Incomplete | None = None, onnx_path: Incomplete | None = None, input_shape: Incomplete | None = None, device: Incomplete | None = None) -> None:
        """
        Export quantized model weights and calibration parameters

        Parameters
        ----------
        model_path : str
            path to save quantized model weight
        calibration_path : str
            (optional) path to save quantize parameters after calibration
        onnx_path : str
            (optional) path to save onnx model
        input_shape : list or tuple
            input shape to onnx model
        device : torch.device
            device of the model, used to place the dummy input tensor for exporting onnx file.
            the tensor is placed on cpu if ```device``` is None

        Returns
        -------
        Dict
        """
    def load_calibration_config(self, calibration_config) -> None:
        """
        This function aims to help quantizer set quantization parameters by
        loading from a calibration_config which is exported by other quantizer
        or itself. The main usage of this function is helping quantize aware training
        quantizer set appropriate initial parameters so that the training process will
        be much more flexible and converges quickly. What's more, it can also enable
        quantizer resume quantization model by loading parameters from config.

        Parameters
        ----------
        calibration_config : dict
            dict which saves quantization parameters, quantizer can export itself
            calibration config.
            eg, calibration_config = quantizer.export_model(model_path, calibration_path)
        """
    def find_conv_bn_patterns(self, model, dummy_input) -> None:
        """
        Find all Conv-BN patterns, used for batch normalization folding

        Parameters
        ----------
        model : torch.nn.Module
            model to be analyzed.
        dummy_input : tupel of torch.tensor
            inputs to the model, used for generating the torchscript
        """
    def record_shape(self, model, dummy_input):
        """
        Record input/output's shapes of each module to be quantized

        Parameters
        ----------
        model : torch.nn.Module
            model to be recorded.
        dummy_input : tupel of torch.tensor
            inputs to the model.
        """
    def step_with_optimizer(self) -> None: ...

class QuantGrad(torch.autograd.Function):
    """
    Base class for overriding backward function of quantization operation.
    """
    @classmethod
    def get_bits_length(cls, config, quant_type):
        """
        Get bits for quantize config

        Parameters
        ----------
        config : Dict
            the configuration for quantization
        quant_type : str
            quant type

        Returns
        -------
        int
            n-bits for quantization configuration
        """
    @staticmethod
    def quant_backward(tensor, grad_output, quant_type, scale, zero_point, qmin, qmax):
        """
        This method should be overrided by subclass to provide customized backward function,
        default implementation is Straight-Through Estimator

        Parameters
        ----------
        tensor : Tensor
            input of quantization operation
        grad_output : Tensor
            gradient of the output of quantization operation
        scale : Tensor
            the type of quantization, it can be `QuantType.INPUT`, `QuantType.WEIGHT`,
            `QuantType.OUTPUT`, you can define different behavior for different types.
        zero_point : Tensor
            zero_point for quantizing tensor
        qmin : Tensor
            quant_min for quantizing tensor
        qmax : Tensor
            quant_max for quantizng tensor

        Returns
        -------
        tensor
            gradient of the input of quantization operation
        """
    @staticmethod
    def forward(ctx, tensor, quant_type, wrapper, input_tensor: Incomplete | None = None, **kwargs): ...
    @classmethod
    def backward(cls, ctx, grad_output): ...

def quantize_helper(tensor, quant_type, wrapper, input_tensor: Incomplete | None = None, **kwargs): ...

class QuantForward(torch.nn.Module):
    """
    Base class for executing quantization operations. This is for quantization algorithms
    that do not need to customize gradient.
    """
    def forward(self, tensor, quant_type, wrapper, input_tensor: Incomplete | None = None, **kwargs): ...
