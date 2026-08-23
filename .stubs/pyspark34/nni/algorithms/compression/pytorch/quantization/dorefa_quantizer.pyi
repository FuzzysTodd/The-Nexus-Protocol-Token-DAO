from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Quantizer as Quantizer
from nni.compression.pytorch.quantization.utils import get_bits_length as get_bits_length
from nni.compression.pytorch.utils.config_validation import QuantizerSchema as QuantizerSchema

logger: Incomplete

class DoReFaQuantizer(Quantizer):
    """
    Quantizer using the DoReFa scheme, as defined in:
    `DoReFa-Net: Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients <https://arxiv.org/abs/1606.06160>`__,
    authors Shuchang Zhou and Yuxin Wu provide an algorithm named DoReFa to quantize the weight, activation and gradients with training.

    Parameters
    ----------
    model : torch.nn.Module
        Model to be quantized.
    config_list : List[Dict]
        List of configurations for quantization. Supported keys for dict:
            - quant_types : List[str]
                Type of quantization you want to apply, currently support 'weight', 'input', 'output'.
            - quant_bits : Union[int, Dict[str, int]]
                Bits length of quantization, key is the quantization type, value is the length, eg. {'weight': 8},
                When the type is int, all quantization types share same bits length.
            - op_types : List[str]
                Types of nn.module you want to apply quantization, eg. 'Conv2d'.
            - op_names : List[str]
                Names of nn.module you want to apply quantization, eg. 'conv1'.
            - exclude : bool
                Set True then the layers setting by op_types and op_names will be excluded from quantization.
    optimizer : torch.optim.Optimizer
        Optimizer is required in `DoReFaQuantizer`, NNI will patch the optimizer and count the optimize step number.

    Examples
    --------
        >>> from nni.algorithms.compression.pytorch.quantization import DoReFaQuantizer
        >>> model = ...
        >>> config_list = [{'quant_types': ['weight', 'input'], 'quant_bits': {'weight': 8, 'input': 8}, 'op_types': ['Conv2d']}]
        >>> optimizer = ...
        >>> quantizer = DoReFaQuantizer(model, config_list, optimizer)
        >>> quantizer.compress()
        >>> # Training Process...

    For detailed example please refer to
    :githublink:`examples/model_compress/quantization/DoReFaQuantizer_torch_mnist.py
    <examples/model_compress/quantization/DoReFaQuantizer_torch_mnist.py>`.

    """
    def __init__(self, model, config_list, optimizer) -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list of dict
            List of configurations
        """
    def quantize_weight(self, wrapper, **kwargs): ...
    def quantize(self, input_ri, q_bits): ...
    def export_model(self, model_path, calibration_path: Incomplete | None = None, onnx_path: Incomplete | None = None, input_shape: Incomplete | None = None, device: Incomplete | None = None):
        """
        Export quantized model weights and calibration parameters(optional)

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
