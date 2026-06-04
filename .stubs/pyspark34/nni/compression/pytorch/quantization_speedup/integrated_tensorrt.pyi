from .backend import BaseModelSpeedup as BaseModelSpeedup
from _typeshed import Incomplete

TRT8: int
TRT7: int
TRT_LOGGER: Incomplete
logger: Incomplete

class CalibrateType:
    LEGACY: Incomplete
    ENTROPY: Incomplete
    ENTROPY2: Incomplete
    MINMAX: Incomplete

Precision_Dict: Incomplete

def valid_config(config: Incomplete | None = None) -> None:
    """
    This function validates the bits setting configuration
    """
def handle_gemm(network, layer_idx, config) -> None:
    """
    This function handles special gemm operation due to layer numbers of gemm changed during pytorch->onnx model convertion.

    Parameters
    ----------
    network : tensorrt.INetworkDefinition
        Represents a TensorRT Network from which the Builder can build an Engine
    layer_idx : int
        layer index of gemm
    config : dict
        Config recording bits number and name of layers
    """
def build_engine(model_file, config: Incomplete | None = None, extra_layer_bits: int = 32, strict_datatype: bool = False, calib: Incomplete | None = None):
    """
    This function builds an engine from an onnx model with calibration process.

    Parameters
    ----------
    model_file : str
        The path of onnx model
    config : dict
        Config recording bits number and name of layers
    extra_layer_bits : int
        Other layers which are not in config will be quantized to corresponding bits number
    strict_datatype : bool
        Whether constrain layer bits to the number given in config or not. If true, all the layer
        will be set to given bits strictly. Otherwise, these layers will be set automatically by
        tensorrt
    calib : numpy array
        The data using to calibrate quantization model

    Returns
    -------
    tensorrt.ICudaEngine
        An ICudaEngine for executing inference on a built network
    """

class ModelSpeedupTensorRT(BaseModelSpeedup):
    """
    Parameters
    ----------
    model : pytorch model
        The model to speedup by quantization.
    input_shape : tuple
        The input shape of model, shall pass it to torch.onnx.export.
    config : dict
        Config recording bits number and name of layers.
    onnx_path : str
        The path user want to store onnx model which is converted from pytorch model.
    extra_layer_bits : int
        Other layers which are not in config will be quantized to corresponding bits number.
    strict_datatype : bool
        Whether constrain layer bits to the number given in config or not. If true, all the layer
        will be set to given bits strictly. Otherwise, these layers will be set automatically by
        tensorrt.
    calibrate_type : tensorrt.tensorrt.CalibrationAlgoType
        The algorithm of calibrating. Please refer to https://docs.nvidia.com/deeplearning/
        tensorrt/api/python_api/infer/Int8/Calibrator.html for detail
    calibrate_data : numpy array
        The data using to calibrate quantization model
    calibration_cache : str
        The path user want to store calibrate cache file
    batchsize : int
        The batch size of calibration and inference
    input_names : list
        Input name of onnx model providing for torch.onnx.export to generate onnx model
    output_name : list
        Output name of onnx model providing for torch.onnx.export to generate onnx model
    """
    model: Incomplete
    onnx_path: Incomplete
    input_shape: Incomplete
    config: Incomplete
    extra_layer_bits: Incomplete
    strict_datatype: Incomplete
    calibrate_type: Incomplete
    calib_data_loader: Incomplete
    calibration_cache: Incomplete
    batchsize: Incomplete
    input_names: Incomplete
    output_names: Incomplete
    context: Incomplete
    onnx_config: Incomplete
    def __init__(self, model, input_shape, config: Incomplete | None = None, onnx_path: str = 'default_model.onnx', extra_layer_bits: int = 32, strict_datatype: bool = True, calibrate_type=..., calib_data_loader: Incomplete | None = None, calibration_cache: str = 'calibration.cache', batchsize: int = 1, input_names=['actual_input_1'], output_names=['output1']) -> None: ...
    def compress(self) -> None:
        """
        Get onnx config and build tensorrt engine.
        """
    def inference(self, test_data):
        """
        Do inference by tensorrt builded engine.

        Parameters
        ----------
        test_data : pytorch tensor
            Model input tensor
        """
    def export_quantized_model(self, path) -> None:
        """
        Export TensorRT quantized model engine which only can be loaded by TensorRT deserialize API.

        Parameters
        ----------
        path : str
            The path of export model
        """
    def load_quantized_model(self, path) -> None:
        """
        Load TensorRT quantized model engine from specific path.

        Parameters
        ----------
        path : str
            The path of export model
        """
