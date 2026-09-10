import torch
from _typeshed import Incomplete

class LayernameModuleWrapper(torch.nn.Module):
    module: Incomplete
    module_bits: Incomplete
    def __init__(self, module, module_bits) -> None:
        """
        Parameters
        ----------
        module : torch.nn.Module
            Layer module of pytorch model
        module_bits : int
            Bits width setting for module
        """
    def forward(self, inputs): ...

def unwrapper(model_onnx, index2name, config):
    """
    Fill onnx config and remove wrapper node in onnx

    Parameters
    ----------
    model_onnx : onnx model
        Onnx model which is converted from pytorch model
    index2name : dict
        Dictionary of layer index and name
    config : dict
        Config recording name of layers and calibration parameters

    Returns
    -------
    onnx model
        Onnx model which is converted from pytorch model
    dict
        The configuration of onnx model layers and calibration parameters
    """
def torch_to_onnx(model, config, input_shape, model_path, input_names, output_names):
    """
    Convert torch model to onnx model and get layer bits config of onnx model.

    Parameters
    ----------
    model : pytorch model
        The model to speedup by quantization
    config : dict
        Config recording bits number and name of layers
    input_shape : tuple
        The input shape of model, shall pass it to torch.onnx.export
    model_path : str
        The path user want to store onnx model which is converted from pytorch model
    input_names : list
        Input name of onnx model providing for torch.onnx.export to generate onnx model
    output_name : list
        Output name of onnx model providing for torch.onnx.export to generate onnx model

    Returns
    -------
    onnx model
        Onnx model which is converted from pytorch model
    dict
        The configuration of onnx model layers and calibration parameters
    """
