from _typeshed import Incomplete
from nni.compression.pytorch.compressor import QuantForward as QuantForward, Quantizer as Quantizer
from nni.compression.pytorch.quantization.observers import default_histogram_observer as default_histogram_observer, default_weight_observer as default_weight_observer
from nni.compression.pytorch.utils.config_validation import QuantizerSchema as QuantizerSchema

logger: Incomplete

class ObserverQuantizer(Quantizer):
    """
    Observer quantizer is a framework of post-training quantization.
    It will insert observers into the place where the quantization will happen.
    During quantization calibration, each observer will record all the tensors it 'sees'.
    These tensors will be used to calculate the quantization statistics after calibration.

    The whole process can be divided into three steps:

    1. It will register observers to the place where quantization would happen (just like registering hooks).
    2. The observers would record tensors' statistics during calibration.
    3. Scale & zero point would be obtained after calibration.

    Note that the observer type, tensor dtype and quantization qscheme are hard coded for now. Their customization
    are under development and will be ready soon.

    Parameters
    ----------
    model : torch.nn.Module
        Model to be quantized.
    config_list : List[Dict]
        List of configurations for quantization. Supported keys:
            - quant_types : List[str]
                Type of quantization you want to apply, currently support 'weight', 'input', 'output'.
            - quant_bits : Union[int, Dict[str, int]]
                Bits length of quantization, key is the quantization type, value is the length, eg. {'weight': 8},
                when the type is int, all quantization types share same bits length.
            - op_types : List[str]
                Types of nn.module you want to apply quantization, eg. 'Conv2d'.
            - op_names : List[str]
                Names of nn.module you want to apply quantization, eg. 'conv1'.
            - exclude : bool
                Set True then the layers setting by op_types and op_names will be excluded from quantization.
    optimizer : torch.optim.Optimizer
        Optimizer is optional in `ObserverQuantizer`.

    Examples
    --------
        >>> from nni.algorithms.compression.pytorch.quantization import ObserverQuantizer
        >>> model = ...
        >>> config_list = [{'quant_types': ['weight', 'input'], 'quant_bits': {'weight': 8, 'input': 8}, 'op_types': ['Conv2d']}]
        >>> quantizer = ObserverQuantizer(model, config_list)
        >>> # define a calibration function
        >>> def calibration(model, calib_loader):
        >>>     model.eval()
        >>>     with torch.no_grad():
        >>>         for data, _ in calib_loader:
        >>>             model(data)
        >>> calibration(model, calib_loader)
        >>> quantizer.compress()

    For detailed example please refer to
    :githublink:`examples/model_compress/quantization/observer_quantizer.py <examples/model_compress/quantization/observer_quantizer.py>`.

    .. note::
        This quantizer is still under development for now. Some quantizer settings are hard-coded:

        - weight observer: per_tensor_symmetric, qint8
        - output observer: per_tensor_affine, quint8, reduce_range=True

        Other settings (such as quant_type and op_names) can be configured.

    Notes
    -----

    **About the compress API**

    Before the `compress` API is called, the model will only record tensors' statistics and no quantization process will be executed.
    After the `compress` API is called, the model will NOT record tensors' statistics any more. The quantization scale and zero point will
    be generated for each tensor and will be used to quantize each tensor during inference (we call it evaluation mode)

    **About calibration**

    Usually we pick up about 100 training/evaluation examples for calibration. If you found the accuracy is a bit low, try
    to reduce the number of calibration examples.
    """
    quant_grad: Incomplete
    device: Incomplete
    compressed: bool
    all_observers: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None) -> None: ...
    def validate_config(self, model, config_list): ...
    def record(self, wrapper, quant_type, tensor) -> None: ...
    def calculate_qparams(self, name, quant_type): ...
    def quantize_input(self, inputs, wrapper, **kwargs): ...
    def quantize_weight(self, wrapper, **kwargs) -> None: ...
    def quantize_output(self, output, wrapper, **kwargs): ...
    def compress(self) -> None:
        """
        Calculate quantization information of each tensor. Note that the inference of
        the compressed model will no longer update the corresponding. Instead, the quantization
        process will be simulated, which is used to test the accuracy of the quantization.
        """
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
