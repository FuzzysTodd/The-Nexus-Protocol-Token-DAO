from _typeshed import Incomplete

logger: Incomplete

def conv1d_to_linear(model) -> None:
    """in-place
    This is for Dynamic Quantization, as Conv1D is not recognized by PyTorch, convert it to nn.Linear
    """

class QuantizeHelper:
    @staticmethod
    def quantize_torch_model(model, dtype=...):
        """
        Usage: model = quantize_model(model)

        TODO: mix of in-place and return, but results are different
        """
    @staticmethod
    def quantize_onnx_model(onnx_model_path, quantized_model_path, use_external_data_format: bool = False) -> None: ...
