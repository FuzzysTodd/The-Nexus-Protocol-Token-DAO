import torch

__all__ = ['ReferenceQuantizedModule']

class ReferenceQuantizedModule(torch.nn.Module):
    def get_weight(self):
        """
        Fake quantize (quantize and dequantize) the weight with
        the quantization parameters for weight, this is used to
        simulate the numerics for the quantized weight in a quantized
        model
        """
    def get_quantized_weight(self): ...
