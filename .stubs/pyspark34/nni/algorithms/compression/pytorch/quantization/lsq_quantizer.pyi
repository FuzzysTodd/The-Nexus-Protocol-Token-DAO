from _typeshed import Incomplete
from nni.compression.pytorch.compressor import BN_FOLD_TAG as BN_FOLD_TAG, QuantForward as QuantForward, Quantizer as Quantizer
from nni.compression.pytorch.quantization.utils import get_bits_length as get_bits_length

logger: Incomplete

class LsqQuantizer(Quantizer):
    """
    Quantizer defined in: `LEARNED STEP SIZE QUANTIZATION <https://arxiv.org/pdf/1902.08153.pdf>`__,
    authors Steven K. Esser and Jeffrey L. McKinstry provide an algorithm to train the scales with gradients.

    ..

        The authors introduce a novel means to estimate and scale the task loss gradient at each weight and activation
        layer's quantizer step size, such that it can be learned in conjunction with other network parameters.

    Parameters
    ----------
    model : torch.nn.Module
        The model to be quantized.
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
        Optimizer is required in `LsqQuantizer`, NNI will patch the optimizer and count the optimize step number.
    dummy_input : Tuple[torch.Tensor]
        Inputs to the model, which are used to get the graph of the module. The graph is used to find Conv-Bn patterns.
        And then the batch normalization folding would be enabled. If dummy_input is not given,
        the batch normalization folding would be disabled.

    Examples
    --------
        >>> from nni.algorithms.compression.pytorch.quantization import LsqQuantizer
        >>> model = ...
        >>> config_list = [{'quant_types': ['weight', 'input'], 'quant_bits': {'weight': 8, 'input': 8}, 'op_types': ['Conv2d']}]
        >>> optimizer = ...
        >>> dummy_input = torch.rand(...)
        >>> quantizer = LsqQuantizer(model, config_list, optimizer, dummy_input=dummy_input)
        >>> quantizer.compress()
        >>> # Training Process...

    For detailed example please refer to
    :githublink:`examples/model_compress/quantization/LSQ_torch_quantizer.py <examples/model_compress/quantization/LSQ_torch_quantizer.py>`.

    """
    quant_grad: Incomplete
    def __init__(self, model, config_list, optimizer, dummy_input: Incomplete | None = None) -> None: ...
    @staticmethod
    def grad_scale(x, scale):
        """
            Used to scale the gradient. Give tensor `x`, we have `y=grad_scale(x, scale)=x` in the forward pass,
            which means that this function will not change the value of `x`. In the backward pass, we have:

            .. math:

                \x0crac{\x07lpha_L}{\x07lpha_x}=\x0crac{\x07lpha_L}{\x07lpha_y}*\x0crac{\x07lpha_y}{\x07lpha_x}=sclae*\x0crac{\x07lpha_L}{\x07lpha_x}

            This means that the origin gradient of x is scaled by a factor of `scale`. Applying this function
            to a nn.Parameter will scale the gradient of it without changing its value.
        """
    @staticmethod
    def round_pass(x):
        """
            A simple way to achieve STE operation.
        """
    def quantize(self, x, scale, qmin, qmax): ...
    def quantize_weight(self, wrapper, **kwargs): ...
    def quantize_output(self, output, wrapper, **kwargs): ...
    def quantize_input(self, inputs, wrapper, **kwargs): ...
    def load_calibration_config(self, calibration_config) -> None: ...
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
    def step_with_optimizer(self) -> None:
        """
        override `compressor` `step` method, quantization only happens after certain number of steps
        """
