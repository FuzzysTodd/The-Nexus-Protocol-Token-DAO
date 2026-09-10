from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Quantizer as Quantizer
from nni.compression.pytorch.utils.config_validation import QuantizerSchema as QuantizerSchema

logger: Incomplete

class NaiveQuantizer(Quantizer):
    """
    Quantize weight to 8 bits directly.

    Parameters
    ----------
    model : torch.nn.Module
        Model to be quantized.
    config_list : List[Dict]
        List of configurations for quantization. Supported keys:
            - quant_types : List[str]
                Type of quantization you want to apply, currently support 'weight'.
            - quant_bits : Union[int, Dict[str, int]]
                Bits length of quantization, key is the quantization type, value is the length, eg. {'weight': 8},
                when the type is int, all quantization types share same bits length.
            - op_types : List[str]
                Types of nn.module you want to apply quantization, eg. 'Conv2d'.
            - op_names : List[str]
                Names of nn.module you want to apply quantization, eg. 'conv1'.
            - exclude : bool
                Set True then the layers setting by op_types and op_names will be excluded from quantization.

    Examples
    --------
        >>> from nni.algorithms.compression.pytorch.quantization import NaiveQuantizer
        >>> model = ...
        >>> NaiveQuantizer(model).compress()
    """
    layer_scale: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None) -> None: ...
    def validate_config(self, model, config_list) -> None: ...
    def quantize_weight(self, wrapper, **kwargs): ...
