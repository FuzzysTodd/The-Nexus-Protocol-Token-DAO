from _typeshed import Incomplete
from nni.compression.pytorch.compressor import BN_FOLD_TAG as BN_FOLD_TAG, QuantGrad as QuantGrad, Quantizer as Quantizer
from nni.compression.pytorch.quantization.literal import PER_CHANNEL_QUANT_SCHEME as PER_CHANNEL_QUANT_SCHEME, QuantDtype as QuantDtype, QuantScheme as QuantScheme, QuantType as QuantType
from nni.compression.pytorch.quantization.settings import LayerQuantSetting as LayerQuantSetting
from nni.compression.pytorch.quantization.utils import calculate_qmin_qmax as calculate_qmin_qmax, get_min_max_value as get_min_max_value, get_quant_shape as get_quant_shape
from nni.compression.pytorch.utils.config_validation import QuantizerSchema as QuantizerSchema

logger: Incomplete

class QATGrad(QuantGrad):
    @staticmethod
    def quant_backward(tensor, grad_output, quant_type, scale, zero_point, qmin, qmax): ...

def update_quantization_param(bits, rmin, rmax, dtype, scheme):
    """
    calculate the `zero_point` and `scale`.

    Parameters
    ----------
    bits : int
        quantization bits length
    rmin : Tensor
        min value of real value
    rmax : Tensor
        max value of real value
    dtype : QuantDtype
        quantized data type
    scheme : QuantScheme
        quantization scheme to be used
    Returns
    -------
    float, float
    """
def update_ema(biased_ema, value, decay):
    """
    calculate biased stat and unbiased stat in each step using exponential moving average method

    Parameters
    ----------
    biased_ema : float
        previous stat value
    value : float
        current stat value
    decay : float
        the weight of previous stat value, larger means smoother curve

    Returns
    -------
    float, float
    """

class QAT_Quantizer(Quantizer):
    """
    Quantizer defined in:
    `Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference
    <http://openaccess.thecvf.com/content_cvpr_2018/papers/Jacob_Quantization_and_Training_CVPR_2018_paper.pdf>`__

    Authors Benoit Jacob and Skirmantas Kligys provide an algorithm to quantize the model with training.

    ..

        We propose an approach that simulates quantization effects in the forward pass of training.
        Backpropagation still happens as usual, and all weights and biases are stored in floating point
        so that they can be easily nudged by small amounts.
        The forward propagation pass however simulates quantized inference as it will happen in the inference engine,
        by implementing in floating-point arithmetic the rounding behavior of the quantization scheme:

        * Weights are quantized before they are convolved with the input. If batch normalization (see [17]) is used for the layer,
          the batch normalization parameters are “folded into” the weights before quantization.

        * Activations are quantized at points where they would be during inference,
          e.g. after the activation function is applied to a convolutional or fully connected layer’s output,
          or after a bypass connection adds or concatenates the outputs of several layers together such as in ResNets.

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
            - quant_start_step : int
                Disable quantization until model are run by certain number of steps, this allows the network to enter a more stable.
                State where output quantization ranges do not exclude a signiﬁcant fraction of values, default value is 0.
            - op_types : List[str]
                Types of nn.module you want to apply quantization, eg. 'Conv2d'.
            - op_names : List[str]
                Names of nn.module you want to apply quantization, eg. 'conv1'.
            - exclude : bool
                Set True then the layers setting by op_types and op_names will be excluded from quantization.
    optimizer : torch.optim.Optimizer
        Optimizer is required in `QAT_Quantizer`, NNI will patch the optimizer and count the optimize step number.
    dummy_input : Tuple[torch.Tensor]
        Inputs to the model, which are used to get the graph of the module. The graph is used to find Conv-Bn patterns.
        And then the batch normalization folding would be enabled. If dummy_input is not given,
        the batch normalization folding would be disabled.

    Examples
    --------
        >>> from nni.algorithms.compression.pytorch.quantization import QAT_Quantizer
        >>> model = ...
        >>> config_list = [{'quant_types': ['weight', 'input'], 'quant_bits': {'weight': 8, 'input': 8}, 'op_types': ['Conv2d']}]
        >>> optimizer = ...
        >>> dummy_input = torch.rand(...)
        >>> quantizer = QAT_Quantizer(model, config_list, optimizer, dummy_input=dummy_input)
        >>> quantizer.compress()
        >>> # Training Process...

    For detailed example please refer to
    :githublink:`examples/model_compress/quantization/QAT_torch_quantizer.py <examples/model_compress/quantization/QAT_torch_quantizer.py>`.

    Notes
    -----

    **Batch normalization folding**

    Batch normalization folding is supported in QAT quantizer. It can be easily enabled by passing an argument `dummy_input` to
    the quantizer, like:

    .. code-block:: python

        # assume your model takes an input of shape (1, 1, 28, 28)
        # and dummy_input must be on the same device as the model
        dummy_input = torch.randn(1, 1, 28, 28)

        # pass the dummy_input to the quantizer
        quantizer = QAT_Quantizer(model, config_list, optimizer, dummy_input=dummy_input)


    The quantizer will automatically detect Conv-BN patterns and simulate batch normalization folding process in the training
    graph. Note that when the quantization aware training process is finished, the folded weight/bias would be restored after calling
    `quantizer.export_model`.

    **Quantization dtype and scheme customization**

    Different backends on different devices use different quantization strategies (i.e. dtype (int or uint) and
    scheme (per-tensor or per-channel and symmetric or affine)). QAT quantizer supports customization of mainstream dtypes and schemes.
    There are two ways to set them. One way is setting them globally through a function named `set_quant_scheme_dtype` like:

    .. code-block:: python

        from nni.compression.pytorch.quantization.settings import set_quant_scheme_dtype

        # This will set all the quantization of 'input' in 'per_tensor_affine' and 'uint' manner
        set_quant_scheme_dtype('input', 'per_tensor_affine', 'uint)
        # This will set all the quantization of 'output' in 'per_tensor_symmetric' and 'int' manner
        set_quant_scheme_dtype('output', 'per_tensor_symmetric', 'int')
        # This will set all the quantization of 'weight' in 'per_channel_symmetric' and 'int' manner
        set_quant_scheme_dtype('weight', 'per_channel_symmetric', 'int')


    The other way is more detailed. You can customize the dtype and scheme in each quantization config list like:

    .. code-block:: python

        config_list = [{
            'quant_types': ['weight'],
            'quant_bits':  8,
            'op_types':['Conv2d', 'Linear'],
            'quant_dtype': 'int',
            'quant_scheme': 'per_channel_symmetric'
        }, {
            'quant_types': ['output'],
            'quant_bits': 8,
            'quant_start_step': 7000,
            'op_types':['ReLU6'],
            'quant_dtype': 'uint',
            'quant_scheme': 'per_tensor_affine'
        }]
    """
    quant_grad: Incomplete
    def __init__(self, model, config_list, optimizer, dummy_input: Incomplete | None = None) -> None: ...
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
    def quantize_input(self, inputs, wrapper, **kwargs): ...
    def quantize_output(self, output, wrapper, **kwargs): ...
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
