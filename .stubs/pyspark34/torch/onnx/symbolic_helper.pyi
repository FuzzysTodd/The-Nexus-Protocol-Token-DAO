import torch._C._onnx as _C_onnx
from _typeshed import Incomplete
from torch import _C
from torch.onnx._internal import jit_utils
from typing import Tuple

__all__ = ['args_have_same_dtype', 'cast_pytorch_to_onnx', 'check_training_mode', 'dequantize_helper', 'is_caffe2_aten_fallback', 'is_complex_value', 'parse_args', 'pytorch_name_to_type', 'quantize_helper', 'quantized_args', 'requantize_bias_helper', 'scalar_name_to_pytorch', 'scalar_type_to_onnx', 'scalar_type_to_pytorch_type']

def parse_args(*arg_descriptors: _ValueDescriptor):
    '''A decorator which converts args from torch._C.Value to built-in types.

    For example:

    ```
    @parse_args(\'v\', \'i\', \'fs\')
    foo(g, a, b, c):
        assert isinstance(a, torch._C.Value)
        assert isinstance(b, int)
        assert isinstance(c, list)
        assert isinstance(c[0], float)
    ```

    Args:
        arg_descriptors: list of str, where each element is
            a string that specifies the type to convert to. Valid descriptors:
            "v": no conversion, keep torch._C.Value.
            "i": int
            "is": list of int
            "f": float
            "fs": list of float
            "b": bool
            "s": str
            "t": torch.Tensor
            "none": the variable is unused
    '''
def quantized_args(*arg_q_descriptors: bool, scale: float | None = None, zero_point: int | None = None):
    """A decorator which extends support for quantized version of the base operator.
    Quantization is detected by examining the arguments that are annotated by
    `arg_q_descriptors`.

    If quantization is detected, the base operator symbolic function will be wrapped with
    argument de-quantization and output quantization.

    Otherwise, only the base symbolic function will be invoked.

    For example:

    ```
    @quantized_args(True, False)
    def foo(g, x, y):
        return x + y
    ```

    is equivalent to

    ```
    def q_foo(g, x, y):
        if is_quantized_tensor(x):
            x = dequantize(x)
            out = foo(g, x, y)
            return quantize(out)
        else:
            return foo(g, x, y)
    ```

    Args:
        arg_q_descriptors: A sequence of bool, where each element represents if the
          argument is QTensor for quantized version of this operator. It defaults
          to False for unspecified (variable length) arguments.
        scale: Quantized output scale. If None, derive from
          the first quantized input scale.
        zero_point: Quantized output zero point. If None,
          derive from the first quantized input zero point.
    """
def is_complex_value(x: _C.Value) -> bool: ...
def is_caffe2_aten_fallback() -> bool: ...
def check_training_mode(op_train_mode: int, op_name: str) -> None:
    """Warns the user if the model's training mode and the export mode do not agree."""
def dequantize_helper(g: jit_utils.GraphContext, qtensor: _C.Value, qdtype: _C_onnx.TensorProtoDataType | None = None) -> Tuple[_C.Value, _C.Value, _C.Value, _C.Value | None]:
    """Appends to graph `g` ONNX nodes that dequantizes `qtensor` into `tensor`.

    Args:
        g: Graph, the ONNX IR graph that is under construction.
        qtensor: torch._C.Value, either a tuple of (quantized_tensor, scale, zero_point)
            for per tensor quantization, or
            (quantized_tensor, scale, zero_point, axis) for per channel quantization,
            representing the quantized tensor.
        qdtype: torch.onnx.TensorProtoDataType default None, if not None, represents the
            data type of quantized tensor. It must be either
            torch.onnx.TensorProtoDataType.UINT8 or torch.onnx.TensorProtoDataType.INT8.
    """
def quantize_helper(g: jit_utils.GraphContext, tensor: _C.Value, scale: _C.Value, zero_point: _C.Value, axis: _C.Value | None = None) -> _C.Value:
    """Appends to graph `g` ONNX nodes that quantizes `tensor` based on `scale`, `zero_point` and `axis`.

    Args:
        g: Graph, the ONNX IR graph that is under construction.
        tensor: torch._C.Value, representing the tensor to be quantized.
        scale: torch._C.Value, quantized scale.
        zero_point: torch._C.Value, quantized zero point.
        axis: Optional[torch._C.Value] default None, if None, represents per tensor quantization.
            Otherwise, represents per channel quantization, along given axis.

    Returns:
        A TupleConstruct storing information of the quantized tensor.
    """
def requantize_bias_helper(g: jit_utils.GraphContext, bias, input_scale, weight_scale, axis: Incomplete | None = None):
    """In PyTorch, bias is float and is quantized to int32 implicitly inside the quantized ATen op kernel.
    In ONNX we need to make the quantization explicit because operators expect all of their inputs to be quantized.
    Since int32 is not a supported output type by ONNX operator `QuantizeLinear`, quantization is exported using
    regular operators.
    """
def args_have_same_dtype(args): ...

cast_pytorch_to_onnx: Incomplete
scalar_name_to_pytorch: Incomplete
scalar_type_to_pytorch_type: Incomplete
pytorch_name_to_type: Incomplete
scalar_type_to_onnx: Incomplete
