from _typeshed import Incomplete
from torch import Tensor as Tensor

class _CodeParser:
    template_params: Incomplete
    return_type: Incomplete
    function_name: Incomplete
    function_params: Incomplete
    function_body: Incomplete
    def __init__(self, code_string: str) -> None: ...

class _JittedFunction:
    code_string: Incomplete
    return_by_ref: Incomplete
    num_outputs: Incomplete
    kernel_name: Incomplete
    kwargs_dict: Incomplete
    is_cuda_available: Incomplete
    def __init__(self, code_string: str, return_by_ref: bool, num_outputs: int, **kwargs) -> None: ...
    def __call__(self, *tensors: Tensor, **kwargs): ...
