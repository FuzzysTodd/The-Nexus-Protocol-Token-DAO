from torch import Tensor as Tensor
from torch.masked import MaskedTensor as MaskedTensor, as_masked_tensor as as_masked_tensor, is_masked_tensor as is_masked_tensor
from torch.types import _dtype as DType
from typing import List, Tuple

DimOrDims = int | Tuple[int] | List[int] | None

def sum(input: Tensor | MaskedTensor, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def prod(input: Tensor | MaskedTensor, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def cumsum(input: Tensor, dim: int, *, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def cumprod(input: Tensor, dim: int, *, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def amax(input: Tensor | MaskedTensor, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}

{reduction_descr}

{reduction_identity_dtype}

{reduction_args}

{reduction_example}"""
def amin(input: Tensor | MaskedTensor, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}

{reduction_descr}

{reduction_identity_dtype}

{reduction_args}

{reduction_example}"""
def argmax(input: Tensor | MaskedTensor, dim: int = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}
{reduction_descr}
{reduction_identity_dtype}
{reduction_args}
{reduction_example}"""
def argmin(input: Tensor | MaskedTensor, dim: int = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}
{reduction_descr}
{reduction_identity_dtype}
{reduction_args}
{reduction_example}"""
def mean(input: Tensor | MaskedTensor, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}

{reduction_descr}

By definition, the identity value of a mean operation is the mean
value of the tensor. If all elements of the input tensor along given
dimension(s) :attr:`dim` are masked-out, the identity value of the
mean is undefined.  Due to this ambiguity, the elements of output
tensor with strided layout, that correspond to fully masked-out
elements, have ``nan`` values.

{reduction_args}

{reduction_example}"""
def median(input: Tensor | MaskedTensor, dim: int = -1, *, keepdim: bool = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}
{reduction_descr}
By definition, the identity value of a median operation is the median
value of the tensor. If all elements of the input tensor along given
dimension(s) :attr:`dim` are masked-out, the identity value of the
median is undefined.  Due to this ambiguity, the elements of output
tensor with strided layout, that correspond to fully masked-out
elements, have ``nan`` values.
{reduction_args}
{reduction_example}"""
def logsumexp(input: Tensor, dim: DimOrDims = None, *, keepdim: bool = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def logaddexp(input: Tensor | MaskedTensor, other: Tensor | MaskedTensor, *, dtype: DType | None = None, input_mask: Tensor | None = None, other_mask: Tensor | None = None) -> Tensor: ...
def norm(input: Tensor | MaskedTensor, ord: float | None = 2.0, dim: DimOrDims = None, *, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}

{reduction_descr}

The identity value of norm operation, which is used to start the
reduction, is ``{identity_float32}``, except for ``ord=-inf`` it is
``{identity_ord_ninf}``.

{reduction_args}

{reduction_example}"""
def var(input: Tensor | MaskedTensor, dim: DimOrDims = None, unbiased: bool | None = None, *, correction: int | None = None, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}
{reduction_descr}
The identity value of sample variance operation is undefined. The
elements of output tensor with strided layout, that correspond to
fully masked-out elements, have ``nan`` values.
{reduction_args}
{reduction_example}"""
def std(input: Tensor | MaskedTensor, dim: DimOrDims = None, unbiased: bool | None = None, *, correction: int | None = None, keepdim: bool | None = False, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor:
    """{reduction_signature}
{reduction_descr}
The identity value of sample standard deviation operation is undefined. The
elements of output tensor with strided layout, that correspond to
fully masked-out elements, have ``nan`` values.
{reduction_args}
{reduction_example}"""
def softmax(input: Tensor | MaskedTensor, dim: int, *, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def log_softmax(input: Tensor | MaskedTensor, dim: int, *, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def softmin(input: Tensor | MaskedTensor, dim: int, *, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
def normalize(input: Tensor | MaskedTensor, ord: float, dim: int, *, eps: float = 1e-12, dtype: DType | None = None, mask: Tensor | None = None) -> Tensor: ...
